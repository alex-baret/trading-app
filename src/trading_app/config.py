"""Configuration utilities for the trading app."""

from __future__ import annotations

import os

from pydantic import BaseModel, Field


class Settings(BaseModel):
    """Runtime settings loaded from environment variables."""

    broker_api_key: str = Field(default="", alias="BROKER_API_KEY")
    broker_api_secret: str = Field(default="", alias="BROKER_API_SECRET")
    broker_base_url: str = Field(default="https://paper-api.example-broker.com", alias="BROKER_BASE_URL")
    env: str = Field(default="development", alias="APP_ENV")
    paper_mode: bool = Field(default=True, alias="PAPER_MODE")

    @classmethod
    def from_env(cls) -> "Settings":
        env_map = {
            "BROKER_API_KEY": os.getenv("BROKER_API_KEY", ""),
            "BROKER_API_SECRET": os.getenv("BROKER_API_SECRET", ""),
            "BROKER_BASE_URL": os.getenv("BROKER_BASE_URL", "https://paper-api.example-broker.com"),
            "APP_ENV": os.getenv("APP_ENV", "development"),
            "PAPER_MODE": os.getenv("PAPER_MODE", "true").lower() in {"1", "true", "yes", "on"},
        }
        return cls.model_validate(env_map)
