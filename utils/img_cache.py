import os
import shutil
from pathlib import Path

from .log import logger

cache_path = Path("./.cache/img")


def create_cache():
    logger.info("Creating cache")
    os.makedirs(cache_path, exist_ok=True)


def delete_cache():
    logger.info("Deleting Cache")
    try:
        shutil.rmtree(cache_path)
    except FileNotFoundError:
        logger.info("Cache not found, skipping")
