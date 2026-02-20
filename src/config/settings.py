from pydantic import Field
from pydantic_settings import (
    BaseSettings, 
    SettingsConfigDict
)


class ToyServerSettings(BaseSettings):
    server_port: int = Field("SERVER_PORT")
    server_host: str = Field("SERVER_HOST")

    model_config = SettingsConfigDict(env_file='config.env')

settings = ToyServerSettings()
