from utils.log import LOGGING_CONFIG

uvicorn_config = {
    "app": "main:app",
    "host": "0.0.0.0",
    "port": 8080,
    "log_config": LOGGING_CONFIG,
}

fastapi_config = {
    "title": "HTMLRender",
}
