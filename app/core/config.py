from pydantic import BaseSettings

class Settings(BaseSettings):
    database_url: str
    app_host: str = "0.0.0.0"
    app_port: int = 8000

    class Config:
        env_file = ".env"

settings = Settings()
