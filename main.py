import io

import uvicorn
from fastapi import FastAPI
from fastapi.responses import Response, StreamingResponse

from utils.api import md_to_pic, capture_page
from utils.log import logger
from config.config import fastapi_config, uvicorn_config
from utils.browser import get_browser, shutdown_browser

app = FastAPI(**fastapi_config)


@app.on_event("startup")
async def startup():
    global browser
    browser = await get_browser()
    logger.success("Browser Started")


@app.on_event("shutdown")
async def shutdown():
    await shutdown_browser()
    logger.success("Browser Stoped")


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/web/")
async def web(
    url: str,
):
    img = await capture_page(url)
    return StreamingResponse(img, status_code=200, media_type="images/png")


@app.get("/md/")
async def md(md: str):
    img = await md_to_pic(md)
    return StreamingResponse(io.BytesIO(img), status_code=200, media_type="images/png")


if __name__ == "__main__":
    logger.success("Starting...")
    uvicorn.run(**uvicorn_config)
