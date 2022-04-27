from fastapi import FastAPI

from htmlrender.config import fastapi_config, uvicorn_config

app = FastAPI(**fastapi_config)

host = uvicorn_config["host"]
port = uvicorn_config["port"]

from .router import *
