import sys

import uvicorn

from htmlrender.config import uvicorn_config
from htmlrender.utils.log import logger, logger_id, default_filter, default_format

logger.remove(logger_id)
logger.add(
    sys.stdout,
    level="DEBUG",
    colorize=True,
    diagnose=False,
    filter=default_filter,
    format=default_format,
)
logger.debug("Logger Started")
print("Logger Started")
if __name__ == "__main__":
    logger.success("Starting...")
    logger.debug("Starting...")

    uvicorn.run(app="htmlrender.main:app", **uvicorn_config)
