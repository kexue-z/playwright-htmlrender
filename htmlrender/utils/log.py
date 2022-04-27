import sys
import logging
from typing import Union

import loguru
from htmlrender.config import LOG_LEVEL

logger = loguru.logger


class Filter:
    def __init__(self) -> None:
        self.level: Union[int, str] = LOG_LEVEL

    def __call__(self, record):
        module_name: str = record["name"]

        record["name"] = module_name.split(".")[0]
        levelno = (
            logger.level(self.level).no if isinstance(self.level, str) else self.level
        )
        return record["level"].no >= levelno


class LoguruHandler(logging.Handler):  # pragma: no cover
    def emit(self, record):
        try:
            level = logger.level(record.levelname).name
        except ValueError:
            level = record.levelno

        frame, depth = logging.currentframe(), 2
        while frame and frame.f_code.co_filename == logging.__file__:
            frame = frame.f_back
            depth += 1

        logger.opt(depth=depth, exception=record.exc_info).log(
            level, record.getMessage()
        )


logger.remove()
default_filter: Filter = Filter()
"""默认日志等级过滤器"""
default_format: str = (
    "<g>{time:MM-DD HH:mm:ss}</g> "
    "[<lvl>{level}</lvl>] "
    "<c><u>{name}</u></c> | "
    # "<c>{function}:{line}</c> | "
    "{message}"
)
"""默认日志格式"""
logger_id = logger.add(
    sys.stdout,
    level="DEBUG",
    colorize=True,
    diagnose=True,
    filter=default_filter,
    format=default_format,
)
