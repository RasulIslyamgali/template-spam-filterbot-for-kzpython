from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file='.env', extra='ignore')

    TG_BOT_API_TOKEN: str
    DEFAULT_BAN_DAYS: int = 10


settings = Settings()
