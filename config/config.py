from utils.log import LOGGING_CONFIG

uvicorn_config = {
    "app": "main:app",
    "host": "127.0.0.1",
    "port": 8080,
    "log_config": LOGGING_CONFIG,
    "debug": True,
}

fastapi_config = {
    "title": "HTMLRender",
}
