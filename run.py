import sys

import uvicorn

from htmlrender.config import uvicorn_config
from htmlrender.utils.log import logger

if __name__ == "__main__":
    logger.success("Starting...")
    logger.debug("Starting...")

    uvicorn.run(app="htmlrender.main:app", **uvicorn_config)
