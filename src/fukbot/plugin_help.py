from botpy.message import Message

from .agent import BaseAgent


class HelpPlugin(BaseAgent):
    """
    内置帮助插件，由Fukbot额外管理，输出对其它plugins的帮助信息。
    """

    priority: int = 0
    name: str = "help"
    description: str = "帮助插件"
    help: str = "显示所有插件的帮助信息"
    usage: str = "/help [plugin_name]"
    alias: list[str] = ["help", "/help", "帮助"]

    def __init__(self) -> None:
        super().__init__()
        self.plugins: list[BaseAgent] = []

    def match_group_at_message_create(self, message: Message) -> bool:
        """匹配群消息"""
        return message.content.strip().split()[0] in self.alias

    async def on_group_at_message_create(self, message: Message) -> Message:
        """处理群消息"""
        args = message.content.strip().split(" ", 1)
        if len(args) == 1:
            content = self.get_all_help()
        else:
            plugin_name = args[1]
            content = self.get_plugin_help(plugin_name)
        return await message.reply(content=content)

    def get_all_help(self) -> str:
        """获取所有插件的帮助信息"""
        help_text = "可用插件列表：\n"
        for plugin in self.plugins:
            help_text += f"{plugin.alias[0]}: {plugin.help}\n"
        return help_text.strip()

    def get_plugin_help(self, plugin_name: str) -> str:
        """获取指定插件的帮助信息"""
        for plugin in self.plugins:
            if plugin.name == plugin_name or plugin_name in plugin.alias:
                return f"Plugin <{plugin.name}>\ndescription: {plugin.description}\nusage: {plugin.usage}"
        return f"未找到插件: {plugin_name}"
