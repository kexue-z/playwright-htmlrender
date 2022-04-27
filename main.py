import io

import uvicorn
from anyio import open_file
from fastapi import FastAPI
from fastapi.responses import RedirectResponse, StreamingResponse

from utils.api import md_to_pic, capture_page
from utils.log import logger
from config.config import fastapi_config, uvicorn_config
from utils.browser import get_browser, shutdown_browser

logger.debug(f"fastapi_config: {fastapi_config}")
app = FastAPI(**fastapi_config)

host = uvicorn_config["host"]
port = uvicorn_config["port"]


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
    return RedirectResponse("/docs")


@app.get("/web/")
async def web(
    url: str,
):
    uid = await capture_page(url)
    return {"img_url": f"{host}:{port}/img/{uid}.png"}


@app.get("/md/")
async def md(md: str):
    uid = await md_to_pic(md)
    return {"img_url": f"{host}:{port}/img/{uid}.png"}


@app.get("/img/{filename:path}")
async def read_file(filename):
    async with await open_file(f".cache/img/{filename}", "rb") as f:
        content = await f.read()
    return StreamingResponse(
        content=io.BytesIO(content), status_code=200, media_type="image/png"
    )


if __name__ == "__main__":
    logger.success("Starting...")
    logger.debug(f"uvicorn_config: {uvicorn_config}")
    uvicorn.run(**(uvicorn_config))
