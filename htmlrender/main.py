from fastapi import FastAPI

from htmlrender.config import fastapi_config, uvicorn_config

app = FastAPI(**fastapi_config)

host = uvicorn_config["host"]
port = uvicorn_config["port"]

from .router import *

# @app.get("/web/")
# async def web(
#     url: str,
# ):
#     uid = await capture_page(url)
#     return {"img_url": f"http://{host}:{port}/img/{uid}.png"}


# @app.get("/md/")
# async def md(md: str):
#     uid = await md_to_pic(md)
#     return {"img_url": f"http://{host}:{port}/img/{uid}.png"}


# @app.get("/img/{filename:path}")
# async def read_file(filename):
#     async with await open_file(f".cache/img/{filename}", "rb") as f:
#         content = await f.read()
#     return StreamingResponse(
#         content=io.BytesIO(content), status_code=200, media_type="image/png"
#     )
