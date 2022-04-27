from htmlrender.main import app
from htmlrender.utils.log import logger
from htmlrender.utils.browser import get_browser, shutdown_browser
from htmlrender.utils.img_cache import create_cache, delete_cache


@app.on_event("startup")
async def startup():
    global browser
    browser = await get_browser()
    logger.success("Browser Started")
    create_cache()


@app.on_event("shutdown")
async def shutdown():
    await shutdown_browser()
    delete_cache()
    logger.debug("Browser Shutdown")
    logger.success("Browser Stoped")


from .root import root
from .md2pic import md2pic
