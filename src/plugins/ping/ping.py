from botpy.message import Message, GroupMessage, C2CMessage

from fukbot.agent import BaseAgent


class Agent(BaseAgent):
    priority: int = 1
    name: str = "ping"
    description: str = "Ping plugin for Fukbot"
    help: str = "This plugin will return pong!"
    usage: str = "send /ping to check server status."
    alias: list[str] = ["ping", "/ping"]

    def match_group_at_message_create(self, message: GroupMessage) -> bool:
        """匹配群消息"""
        return message.content.strip().split()[0] in self.alias

    async def on_group_at_message_create(self, message: GroupMessage) -> None:
        """处理群消息"""
        await self.ping(message)

    def match_c2c_message_create(self, message: C2CMessage) -> bool:
        """匹配私聊消息"""
        return message.content.split()[0] in self.alias

    async def on_c2c_message_create(self, message: C2CMessage) -> None:
        """处理私聊消息"""
        await self.ping(message)

    async def ping(self, message: Message) -> None:
        """Ping方法"""
        await message.reply(content="pong!")
