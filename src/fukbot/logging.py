# 自定义日志文件路径
import os
import logging
from logging.handlers import TimedRotatingFileHandler
from botpy.logging import configure_logging, get_logger as _get_logger

if not os.path.exists("logs"):
    os.mkdir("logs")

custom_handler = {
    "handler": TimedRotatingFileHandler,
    "format": "%(asctime)s\t[%(levelname)s]\t(%(filename)s:%(lineno)s)%(funcName)s\t%(message)s",
    "level": logging.DEBUG,
    "when": "D",
    "backupCount": 7,
    "encoding": "utf-8",
    "filename": os.path.join("logs", "%(name)s.log"),  # 日志文件存储在 logs 文件夹下
}

# 配置日志
configure_logging(ext_handlers=[custom_handler])

# 获取 logger
get_logger = _get_logger
# logger = get_logger("MyBot")
