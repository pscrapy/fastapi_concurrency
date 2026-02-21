from pydantic import Field
from pydantic_settings import (
    BaseSettings, 
    SettingsConfigDict
)


class ToyServerSettings(BaseSettings):
    server_port: int = Field("SERVER_PORT")
    server_host: str = Field("SERVER_HOST")

    uvicorn_workers: int = Field("UVICORN_WORKERS")
    uvicorn_concurrency_limit: int = Field("UVICORN_CONCURRENCY_LIMIT")
    uvicorn_backlog: int = Field("UVICORN_BACKLOG")

    fastapi_workers: int = Field("FASTAPI_WORKERS")

    gunicorn_workers: int = Field("GUNICORN_WORKERS")
    gunicorn_worker_connections: int = Field("GUNICORN_WORKER_CONNECTIONS")
    gunicorn_backlog: int = Field("GUNICORN_BACKLOG")

    model_config = SettingsConfigDict(env_file='config.env')

settings = ToyServerSettings()
