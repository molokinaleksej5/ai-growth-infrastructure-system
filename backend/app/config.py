from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    database_url: str
    redis_url: str = "redis://redis:6379/0"
    openai_api_key: str | None = None
    claude_api_key: str | None = None
    gemini_api_key: str | None = None
    deepseek_api_key: str | None = None
    default_ai_provider: str = "openai"
    telegram_bot_token: str | None = None
    telegram_admin_chat_id: str | None = None
    google_places_api_key: str | None = None
    class Config:
        env_file = ".env"
        extra = "ignore"
settings = Settings()
