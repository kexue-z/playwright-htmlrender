from htmlrender.main import app
from fastapi.responses import RedirectResponse


@app.get("/")
async def root():
    """
    :说明: `root`
    > 转至文档首页

    :返回:
      - `重定向`: 重定向
    """
    return RedirectResponse("/docs")
