from botpy.message import Message, GroupMessage, C2CMessage

from fukbot.agent import BaseAgent


class Echo(BaseAgent):
    priority: int = 1
    name: str = "echo"
    description: str = "Echo plugin for Fukbot"
    help: str = "This plugin will echo the message back to you."
    usage: str = "send any message starts with /echo."
    alias: list[str] = ["echo", "/echo"]

    def match_group_at_message_create(self, message: GroupMessage) -> bool:
        """匹配群消息"""
        return message.content.strip().split()[0] in self.alias

    async def on_group_at_message_create(self, message: GroupMessage) -> None:
        """处理群消息"""
        await self.echo(message)

    def match_c2c_message_create(self, message: C2CMessage) -> bool:
        """匹配私聊消息"""
        return message.content.split()[0] in self.alias

    async def on_c2c_message_create(self, message: C2CMessage) -> None:
        """处理私聊消息"""
        await self.echo(message)

    async def echo(self, message: Message) -> None:
        """回声消息"""
        split_content = message.content.strip().split(" ", 1)
        if len(split_content) == 1:
            await message.reply(content=" ")
        else:
            await message.reply(content=split_content[1])
