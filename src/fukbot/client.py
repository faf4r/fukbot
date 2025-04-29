from types import MethodType
from typing import Self, Callable, Coroutine, Any
from importlib import import_module
import inspect

import botpy
from botpy.message import Message

from fukbot.logging import get_logger
from fukbot.ext import post_group_file, post_c2c_file
from fukbot.flags import on_func_names
from fukbot.agent import BaseAgent
from fukbot.plugin_help import HelpPlugin
from plugins import plugin_list


class FukBot(botpy.Client):  # type: ignore[misc]
    """基于botpy的QQ机器人框架"""

    def __init__(
        self,
        match_all: bool = False,
        logger_name: str | None = None,
        *args: Any,
        **kwargs: Any,
    ) -> None:
        super().__init__(*args, **kwargs)
        self.match_all = match_all
        self.logger = get_logger(logger_name if logger_name else "FukBot")

    async def on_ready(self) -> None:
        # 注册动态方法
        self.register_methods()
        # 加载插件
        self.load_plugins()
        # 插件init
        await self.init_plugins()

        # 绑定plugin_help插件
        self.load_plugin_help()

        # 绑定on_message事件
        self.bind_on_message()
        self.logger.info(f"{self.robot.name} is on ready!")

    def register_methods(self) -> None:
        """动态绑定方法到API实例，提供文件上传的最新支持"""
        self.api.post_group_b64file = MethodType(post_group_file, self.api)
        self.api.post_c2c_b64file = MethodType(post_c2c_file, self.api)

    def load_plugins(self) -> None:
        """加载插件"""
        self.plugins: list[BaseAgent] = []
        for plugin_name in plugin_list:
            try:
                self.load_plugin(plugin_name)
                self.logger.info(f"Loaded plugin: <{plugin_name}>")
            except Exception as e:
                self.logger.error(f"Failed to load plugin <{plugin_name}>: {e}")
        self.plugins.sort()

    def load_plugin(self, plugin_name: str) -> None:
        """加载单个插件"""
        module = import_module(plugin_name)
        plugin_class = getattr(module, "Agent", None)
        if plugin_class is None:
            raise ImportError(f"Plugin <{plugin_name}> does not implement an Agent class.")
        plugin_instance = plugin_class()
        self.plugins.append(plugin_instance)

    async def init_plugins(self) -> None:
        for plugin in self.plugins:
            if hasattr(plugin, "init"):
                await plugin.init(self)
                self.logger.info(f"<{plugin.name}> init success!")

    def load_plugin_help(self) -> None:
        """加载帮助插件"""
        help_plugin = HelpPlugin()
        help_plugin.plugins = self.plugins
        self.plugins.append(help_plugin)
        self.logger.info("Loaded plugin: <help>")

    def bind_on_message(self) -> None:
        """绑定消息事件"""
        for name in on_func_names:
            match_name = "match_" + name[3:]  # 变量不能直接使用，on_message里调用的时候是最后一次的结果

            def create_on_message(
                name: str, match_name: str
            ) -> Callable[[Self, Message], Coroutine[Any, Any, None]]:  # 通过闭包传递参数
                async def on_message(self: Self, message: Message) -> None:
                    self.logger.debug(message)
                    self.logger.info(f"Received message: {message.content}")
                    for plugin in self.plugins:
                        match_message = getattr(plugin, match_name, None)
                        handler = getattr(plugin, name, None)
                        if not match_message or not handler:
                            self.logger.warning(f"Plugin <{plugin.name}> does not implement {match_name} or {name}.")
                            continue
                        if inspect.iscoroutinefunction(match_message):
                            match_result = await match_message(message)  # 不需要self
                        else:
                            match_result = match_message(message)  # 不需要self
                        if match_result:
                            try:
                                self.logger.info(f"Plugin <{plugin.name}> match message!")
                                if inspect.iscoroutinefunction(handler):
                                    await handler(message)
                                else:
                                    handler(message)  # 不需要self
                            except Exception as e:
                                self.logger.error(f"Plugin <{plugin.name}> error: {e}")
                            finally:
                                if not self.match_all:  # TODO: 是否考虑多插件一起await
                                    break

                return on_message

            on_message: Callable[..., Any] = create_on_message(name, match_name)
            setattr(self, name, MethodType(on_message, self))
