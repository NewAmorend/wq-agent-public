from __future__ import annotations

from ..config import Settings
from .anthropic import AnthropicProvider
from .base import BaseLLMProvider
from .openai import OpenAICompatibleProvider


PROTOCOL_PROVIDERS = ("openai_compatible", "anthropic")
LEGACY_PROVIDER_ALIASES = {
    "openai": "openai_compatible",
    "kimi": "openai_compatible",
    "deepseek": "openai_compatible",
}
LEGACY_BASE_URL_DEFAULTS = {
    "openai": "https://api.openai.com/v1",
    "kimi": "https://ark.cn-beijing.volces.com/api/coding/v3/chat/completions",
    "deepseek": "https://api.deepseek.com/v1/chat/completions",
}
LLM_PROVIDER_OPTIONS: dict[str, tuple[str, ...]] = {
    "openai_compatible": (),
    "anthropic": (),
    **{alias: () for alias in LEGACY_PROVIDER_ALIASES},
}


class LLMFactory:
    _providers: dict[str, type[BaseLLMProvider]] = {
        "openai_compatible": OpenAICompatibleProvider,
        "openai": OpenAICompatibleProvider,
        "anthropic": AnthropicProvider,
    }

    @classmethod
    def register(cls, name: str, provider_cls: type[BaseLLMProvider]) -> None:
        cls._providers[name] = provider_cls

    @classmethod
    def create(cls, name: str, **kwargs) -> BaseLLMProvider:
        provider_name = _normalize_provider_name(name)
        provider_cls = cls._providers.get(provider_name)
        if not provider_cls:
            raise ValueError(
                f"Unknown LLM provider: {name}. Available: {sorted(cls._providers.keys())}"
            )
        return provider_cls(**kwargs)

    @classmethod
    def from_settings(cls, settings) -> BaseLLMProvider:
        requested_provider = _first_text(
            settings.LLM_PROVIDER,
            _settings_default("LLM_PROVIDER"),
        ).lower()
        provider = _normalize_provider_name(requested_provider)
        max_tokens = _int_setting(settings, "LLM_MAX_TOKENS")
        if provider == "anthropic":
            return AnthropicProvider(
                api_key=_first_text(settings.LLM_API_KEY),
                base_url=_first_text(
                    _explicit_text(settings, "LLM_BASE_URL"),
                    "https://api.anthropic.com",
                ),
                model=_first_text(settings.LLM_MODEL, "claude-3-5-sonnet-latest"),
                max_tokens=max_tokens,
                allow_insecure_http=settings.LLM_ALLOW_INSECURE_HTTP,
                anthropic_version=_first_text(
                    settings.ANTHROPIC_VERSION,
                    _settings_default("ANTHROPIC_VERSION"),
                ),
            )
        if provider == "openai_compatible":
            return OpenAICompatibleProvider(
                api_key=_openai_compatible_setting(settings, requested_provider, "api_key"),
                base_url=_openai_compatible_setting(settings, requested_provider, "base_url"),
                model=_openai_compatible_setting(settings, requested_provider, "model"),
                wire_api=_first_text(settings.LLM_WIRE_API, settings.OPENAI_WIRE_API, "auto"),
                reasoning_effort=_first_text(
                    settings.LLM_REASONING_EFFORT,
                    settings.OPENAI_REASONING_EFFORT,
                ),
                store=settings.LLM_STORE or settings.OPENAI_STORE,
                max_tokens=max_tokens,
                allow_insecure_http=(
                    settings.LLM_ALLOW_INSECURE_HTTP or settings.OPENAI_ALLOW_INSECURE_HTTP
                ),
                chat_token_param=_first_text(
                    settings.LLM_CHAT_TOKEN_PARAM,
                    settings.OPENAI_CHAT_TOKEN_PARAM,
                    "max_tokens",
                ),
                chat_reasoning_effort=(
                    settings.LLM_CHAT_REASONING_EFFORT
                    or settings.OPENAI_CHAT_REASONING_EFFORT
                ),
            )
        raise ValueError(f"Unknown LLM provider in settings: {requested_provider}")


def _settings_default(key: str) -> str:
    field = Settings.model_fields[key]
    value = field.default
    if isinstance(value, bool):
        return "true" if value else "false"
    return "" if value is None else str(value)


def _first_text(*values) -> str:
    for value in values:
        text = "" if value is None else str(value).strip()
        if text:
            return text
    return ""


def _explicit_text(settings, key: str) -> str:
    if key not in getattr(settings, "model_fields_set", set()):
        return ""
    return _first_text(getattr(settings, key, ""))


def _int_setting(settings, key: str) -> int:
    value = _first_text(getattr(settings, key, ""), _settings_default(key))
    return int(value)


def _normalize_provider_name(provider: str) -> str:
    normalized = provider.strip().lower().replace("-", "_")
    return LEGACY_PROVIDER_ALIASES.get(normalized, normalized)


def _openai_compatible_setting(settings, requested_provider: str, field: str) -> str:
    if field == "api_key":
        fallback = {
            "openai": settings.OPENAI_API_KEY,
            "kimi": settings.KIMI_API_KEY,
            "deepseek": settings.DEEPSEEK_API_KEY,
        }.get(requested_provider, "")
        return _first_text(settings.LLM_API_KEY, fallback)
    if field == "base_url":
        if requested_provider == "openai_compatible":
            return _first_text(settings.LLM_BASE_URL, _settings_default("LLM_BASE_URL"))
        fallback = _legacy_text_or_default(
            {
                "openai": settings.OPENAI_BASE_URL,
                "kimi": settings.KIMI_BASE_URL,
                "deepseek": settings.DEEPSEEK_BASE_URL,
            }.get(requested_provider, ""),
            LEGACY_BASE_URL_DEFAULTS.get(requested_provider, ""),
        )
        return _first_text(fallback, settings.LLM_BASE_URL, _settings_default("LLM_BASE_URL"))
    if field == "model":
        if requested_provider == "openai_compatible":
            return _first_text(settings.LLM_MODEL, settings.OPENAI_MODEL)
        fallback = {
            "openai": settings.OPENAI_MODEL,
            "kimi": settings.KIMI_MODEL,
            "deepseek": settings.DEEPSEEK_MODEL,
        }.get(requested_provider, "")
        return _first_text(settings.LLM_MODEL, fallback, settings.OPENAI_MODEL)
    raise ValueError(f"Unknown OpenAI-compatible setting: {field}")


def _legacy_text_or_default(value: str, default: str) -> str:
    text = "" if value is None else str(value).strip()
    return text or default
