from htmlrender.main import app
from htmlrender.config import uvicorn_config
from htmlrender.utils.api import md_to_pic

host = uvicorn_config["host"]
port = uvicorn_config["port"]


@app.get("/md2pic/")
async def md2pic(text: str) -> dict:
    """
    :说明: `md2pic`
    > markdown转图片

    :参数:
      * `text: str`: 纯文本消息

    :返回:
      - `dict`: 图片地址
    """
    uid = await md_to_pic(text)
    return {"img_url": f"http://{host}:{port}/img/{uid}.png"}
