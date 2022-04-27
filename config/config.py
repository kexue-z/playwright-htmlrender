import json

LOGGING_CONFIG = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "default": {
            "class": "utils.log.LoguruHandler",
        },
    },
    "loggers": {
        "uvicorn.error": {"handlers": ["default"], "level": "INFO"},
        "uvicorn.access": {
            "handlers": ["default"],
            "level": "INFO",
        },
    },
}

uvicorn_config = {
    "host": "127.0.0.1",
    "port": 8080,
    "log_config": LOGGING_CONFIG,
    "debug": True,
    "log_level": "debug",
}

fastapi_config = {
    "title": "HTMLRender",
}

weather_config = json.load(open("config/weather.json"))
