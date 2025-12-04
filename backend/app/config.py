from pydantic_settings import BaseSettings
from typing import List, Optional
from pydantic import field_validator


class Settings(BaseSettings):
    api_host: str = "0.0.0.0"
    api_port: int = 8000
    api_reload: bool = True
    cors_origins: str = "http://localhost:5173,http://localhost:3000"
    
    # Database settings
    database_url: Optional[str] = None
    
    # Redis settings
    redis_url: Optional[str] = None
    
    @property
    def cors_origins_list(self) -> List[str]:
        """Parse CORS origins from comma-separated string to list"""
        return [origin.strip() for origin in self.cors_origins.split(',') if origin.strip()]
    
    class Config:
        env_file = ".env"
        case_sensitive = False


settings = Settings()
