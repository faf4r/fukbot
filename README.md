# FukBot

FukBot 是一个基于 [botpy](https://github.com/tencent-qq/botpy) 的简单框架，用于构建官方 QQ 机器人。

## Description
- 插件化开发：支持通过插件扩展功能，插件可以动态加载。
- 内置帮助插件：提供 /help 命令，显示所有插件的帮助信息。
- 消息处理：
  - 支持群聊消息（GroupMessage）和私聊消息（C2CMessage）。
  - 插件可以通过匹配消息内容来处理特定命令。
- 文件上传支持：支持通过 Base64 编码上传图片、视频等文件到群聊或私聊。
- 日志记录：使用自定义日志配置，支持按天滚动日志文件。

## Structure
```
.
├── .flake8                   # Flake8 配置文件
├── .gitignore                # Git 忽略文件
├── .pre-commit-config.yaml   # Pre-commit 配置
├── mypy.ini                  # mypy配置文件
├── poetry.lock               # Poetry 锁文件
├── pyproject.toml            # 项目配置文件
├── README.md                 # 项目说明
├── src/                      # 源代码目录
│   ├── bot.py                # 主程序入口
│   ├── config.yaml           # 配置文件
│   ├── fukbot/               # 核心框架代码
│   │   ├── __init__.py
│   │   ├── agent.py          # 插件基类
│   │   ├── client.py         # FukBot 客户端
│   │   ├── ext.py            # 扩展功能
│   │   ├── flags.py          # 消息事件标志
│   │   ├── logging.py        # 日志配置
│   │   ├── plugin_help.py    # 内置帮助插件
│   │   └── utils.py          # 工具函数
│   ├── plugins/              # 插件目录
│   │   ├── __init__.py
│   │   ├── echo/             # Echo 插件
│   │   │   ├── __init__.py
│   │   │   └── echo.py
│   │   └── ping/             # Ping 插件
│   │       ├── __init__.py
│   │       └── ping.py
├── tests/                    # 测试目录
```

## Usage
### install
1. 克隆项目到本地：
   ```bash
   git clone https://github.com/faf4r/fukbot.git
   cd fukbot
   ```
2. 安装依赖：
   ```bash
   poetry install
   ```
3. 配置机器人：
   修改`src/example.config.yaml`文件为`src/config.yaml`，填写`appid`和`secret`。
   修改`src/bot.py`文件，确定`intents`、`timeout`、`sandbox`等参数
4. 运行机器人：
```bash
poetry run python bot.py
```

## 插件开发
FukBot 支持插件化开发，插件需要继承`fukbot.agent.BaseAgent`并实现`priority`、`name`、`description`、`help`、`usage`、`alias`等类属性，最后创建`__init__.py`将插件导出名为`Agent`的类。具体实现可参考内置插件[`ping`](./src/plugins/ping/)和[`echo`](./src/plugins/echo/)。
以下是一个简单的插件示例：
```
from botpy.message import Message, GroupMessage
from fukbot.agent import BaseAgent

class MyPlugin(BaseAgent):
    priority = 1
    name = "my_plugin"
    description = "A custom plugin example"
    help = "This is a custom plugin."
    usage = "/myplugin"
    alias = ["myplugin", "/myplugin"]

    def match_group_at_message_create(self, message: GroupMessage) -> bool:
        return message.content.strip().split()[0] in self.alias

    async def on_group_at_message_create(self, message: GroupMessage) -> None:
        await message.reply(content="Hello from MyPlugin!")
```
将插件文件放入`src/plugins/`目录，并在`src/plugins/__init__.py`中添加插件。

## 测试
```bash
poetry run black src/
poetry run flake8
poetry run mypy
```
