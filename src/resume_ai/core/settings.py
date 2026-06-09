from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")

    TEXT_MODEL: str
    STT_MODEL: str
    EMBED_MODEL: str

    QDRANT_URL: str = "localhost"
    QDRANT_PORT: int = 6333

    ROUTER_MESSAGES_TO_ANALYZE: int = 5
    TOTAL_MESSAGES_SUMMARY_TRIGGER: int = 20
    TOTAL_MESSAGES_AFTER_SUMMARY: int = 6

settings = Settings()