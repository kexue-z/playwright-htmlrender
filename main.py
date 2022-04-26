import uvicorn
from fastapi import FastAPI

from utils.log import logger
from config.config import fastapi_config, uvicorn_config

app = FastAPI(**fastapi_config)


@app.get("/")
async def root():
    return {"message": "Hello World"}


if __name__ == "__main__":
    logger.success("Starting...")
    uvicorn.run(**uvicorn_config)
