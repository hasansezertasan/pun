"""Configurations for the project."""

from __future__ import annotations

from functools import cache
from pathlib import Path
from typing import ClassVar

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict

from pun.__metadata__ import PROJECT_NAME
from pun.core.dirs import ROOT_FOLDER_PATH


class Settings(BaseSettings):
    """Application settings using pydantic-settings.

    Settings can be configured via environment variables or .env file.
    All settings are prefixed with the project name.
    """

    model_config: ClassVar[SettingsConfigDict] = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        # Dashes are normalized to underscores so the prefix is a valid shell
        # variable name (e.g. ``my-project`` -> ``MY_PROJECT_``).
        env_prefix=f"{PROJECT_NAME.upper().replace('-', '_')}_",
        case_sensitive=False,
        extra="ignore",
    )

    # Example settings - replace or extend these with your project's own.
    # ``log_level`` is consumed by ``core/logging_setup.py``; ``debug`` and
    # ``config_dir`` are illustrative placeholders not yet wired into anything.
    debug: bool = Field(default=False, description="Enable debug mode")
    log_level: str = Field(default="INFO", description="Logging level")
    config_dir: Path = Field(
        default=ROOT_FOLDER_PATH, description="Configuration directory"
    )


@cache
def get_settings() -> Settings:
    """Return the cached settings singleton.

    Cached so all callers share one instance; tests can reset or override it
    via ``get_settings.cache_clear()`` instead of patching an import-time value.

    Returns:
        Settings: The cached settings instance.
    """
    return Settings()


__all__ = ["Settings", "get_settings"]
