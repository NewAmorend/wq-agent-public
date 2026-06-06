from __future__ import annotations

from .base import BaseLLMProvider
from .kimi import KimiProvider
from .deepseek import DeepSeekProvider
from .openai import OpenAIProvider


class LLMFactory:
    _providers: dict[str, type[BaseLLMProvider]] = {
        "kimi": KimiProvider,
        "deepseek": DeepSeekProvider,
        "openai": OpenAIProvider,
    }

    @classmethod
    def register(cls, name: str, provider_cls: type[BaseLLMProvider]) -> None:
        cls._providers[name] = provider_cls

    @classmethod
    def create(cls, name: str, **kwargs) -> BaseLLMProvider:
        provider_cls = cls._providers.get(name)
        if not provider_cls:
            raise ValueError(f"Unknown LLM provider: {name}. Available: {list(cls._providers.keys())}")
        return provider_cls(**kwargs)

    @classmethod
    def from_settings(cls, settings) -> BaseLLMProvider:
        provider = settings.LLM_PROVIDER.lower()
        model_override = settings.LLM_MODEL if settings.LLM_MODEL else None
        if provider == "kimi":
            return KimiProvider(
                api_key=settings.KIMI_API_KEY,
                base_url=settings.KIMI_BASE_URL,
                model=model_override or settings.KIMI_MODEL,
                max_tokens=settings.LLM_MAX_TOKENS,
            )
        elif provider == "deepseek":
            return DeepSeekProvider(
                api_key=settings.DEEPSEEK_API_KEY,
                base_url=settings.DEEPSEEK_BASE_URL,
            )
        elif provider == "openai":
            return OpenAIProvider(
                api_key=settings.OPENAI_API_KEY,
                base_url=settings.OPENAI_BASE_URL,
                model=model_override or settings.OPENAI_MODEL,
                wire_api=settings.OPENAI_WIRE_API,
                reasoning_effort=settings.OPENAI_REASONING_EFFORT,
                store=settings.OPENAI_STORE,
                max_tokens=settings.LLM_MAX_TOKENS,
                allow_insecure_http=settings.OPENAI_ALLOW_INSECURE_HTTP,
                chat_token_param=settings.OPENAI_CHAT_TOKEN_PARAM,
                chat_reasoning_effort=settings.OPENAI_CHAT_REASONING_EFFORT,
            )
        raise ValueError(f"Unknown LLM provider in settings: {provider}")
