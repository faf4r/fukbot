import os

import botpy
from botpy.ext import cog_yaml

from fukbot import FukBot


config = cog_yaml.read(os.path.join(os.path.dirname(__file__), "config.yaml"))
intents = botpy.Intents().all()
bot = FukBot(intents=intents, timeout=60, is_sandbox=False, match_all=config["match_all"])
bot.run(appid=config["appid"], secret=config["secret"])
