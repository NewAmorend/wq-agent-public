from __future__ import annotations

import pytest

from wq_agent.config import Settings
from wq_agent.llm import DeepSeekProvider, KimiProvider, LLMFactory, OpenAIProvider


class _Resp:
    def __init__(self, status: int, data: dict | None = None, text: str = "error-body"):
        self.status_code = status
        self._data = data or {}
        self.text = text

    def json(self):
        return self._data


class _Client:
    def __init__(self, responses: list[_Resp]):
        self.responses = responses
        self.calls: list[dict] = []

    async def post(self, url, json=None):
        self.calls.append({"url": url, "json": json})
        idx = min(len(self.calls) - 1, len(self.responses) - 1)
        return self.responses[idx]

    async def aclose(self):
        pass


def _provider(*, wire_api: str = "responses", base_url: str = "http://127.0.0.1:8080"):
    return OpenAIProvider(
        api_key="test-key",
        base_url=base_url,
        model="gpt-test",
        wire_api=wire_api,
        reasoning_effort="xhigh",
        store=False,
        max_tokens=123,
    )


def test_factory_creates_openai_provider():
    settings = Settings(
        LLM_PROVIDER="openai",
        OPENAI_API_KEY="test-key",
        OPENAI_BASE_URL="http://127.0.0.1:8080",
        OPENAI_MODEL="gpt-anything",
        OPENAI_WIRE_API="responses",
    )

    provider = LLMFactory.from_settings(settings)

    assert isinstance(provider, OpenAIProvider)
    assert provider.default_model == "gpt-anything"
    assert provider.wire_api == "responses"


def test_factory_uses_provider_defaults_and_valid_global_model_override():
    kimi = LLMFactory.from_settings(
        Settings(
            LLM_PROVIDER="kimi",
            LLM_MODEL="kimi-k2.6",
            LLM_MAX_TOKENS=777,
            KIMI_API_KEY="test-key",
            KIMI_BASE_URL="",
            KIMI_MODEL="",
        )
    )

    assert isinstance(kimi, KimiProvider)
    assert kimi.base_url == "https://ark.cn-beijing.volces.com/api/coding/v3/chat/completions"
    assert kimi.default_model == "kimi-k2.6"
    assert kimi.default_max_tokens == 777

    deepseek = LLMFactory.from_settings(
        Settings(
            LLM_PROVIDER="deepseek",
            LLM_MAX_TOKENS=888,
            DEEPSEEK_API_KEY="test-key",
            DEEPSEEK_BASE_URL="",
            DEEPSEEK_MODEL="",
        )
    )

    assert isinstance(deepseek, DeepSeekProvider)
    assert deepseek.base_url == "https://api.deepseek.com/v1/chat/completions"
    assert deepseek.default_model == "deepseek-chat"
    assert deepseek.default_max_tokens == 888


def test_factory_rejects_global_model_that_does_not_match_provider():
    with pytest.raises(ValueError, match="LLM_MODEL"):
        LLMFactory.from_settings(
            Settings(
                LLM_PROVIDER="deepseek",
                LLM_MODEL="gpt-5.4",
                DEEPSEEK_API_KEY="test-key",
            )
        )

    provider = LLMFactory.from_settings(
        Settings(
            LLM_PROVIDER="deepseek",
            LLM_MODEL="",
            DEEPSEEK_MODEL="deepseek-custom",
            DEEPSEEK_API_KEY="test-key",
        )
    )
    assert isinstance(provider, DeepSeekProvider)
    assert provider.default_model == "deepseek-custom"


def test_openai_provider_rejects_missing_or_placeholder_api_key():
    with pytest.raises(ValueError, match="OPENAI_API_KEY"):
        OpenAIProvider(api_key="", base_url="https://api.openai.com/v1")

    with pytest.raises(ValueError, match="OPENAI_API_KEY"):
        OpenAIProvider(api_key="your_openai_or_proxy_key", base_url="https://api.openai.com/v1")

    with pytest.raises(ValueError, match="OPENAI_API_KEY"):
        OpenAIProvider(api_key="change_me", base_url="https://api.openai.com/v1")


def test_openai_provider_rejects_remote_insecure_http_but_allows_localhost():
    with pytest.raises(ValueError, match="insecure HTTP"):
        OpenAIProvider(api_key="test-key", base_url="http://example.com:8080")

    provider = OpenAIProvider(api_key="test-key", base_url="http://127.0.0.1:8080")
    assert provider.base_url == "http://127.0.0.1:8080"


def test_kimi_and_deepseek_reject_placeholder_keys_and_remote_http():
    with pytest.raises(ValueError, match="KIMI_API_KEY"):
        KimiProvider(api_key="placeholder")

    with pytest.raises(ValueError, match="DEEPSEEK_API_KEY"):
        DeepSeekProvider(api_key="todo-fill-me")

    with pytest.raises(ValueError, match="KIMI_BASE_URL"):
        KimiProvider(api_key="test-key", base_url="http://example.com/chat")

    with pytest.raises(ValueError, match="DEEPSEEK_BASE_URL"):
        DeepSeekProvider(api_key="test-key", base_url="http://example.com/chat")

    assert KimiProvider(api_key="test-key", base_url="http://127.0.0.1:8080/chat").base_url
    assert DeepSeekProvider(api_key="test-key", base_url="http://localhost:8080/chat").base_url


@pytest.mark.asyncio
async def test_responses_payload_and_output_text_parsing():
    provider = _provider(wire_api="responses")
    client = _Client([_Resp(200, {"output_text": "alpha output"})])
    provider._client = client

    out = await provider.generate("make alpha", temperature=0.7, max_tokens=456)

    assert out == "alpha output"
    assert client.calls[0]["url"] == "http://127.0.0.1:8080/v1/responses"
    payload = client.calls[0]["json"]
    assert payload["model"] == "gpt-test"
    assert payload["input"] == [{"role": "user", "content": "make alpha"}]
    assert payload["temperature"] == 0.7
    assert payload["max_output_tokens"] == 456
    assert payload["store"] is False
    assert payload["reasoning"] == {"effort": "xhigh"}


@pytest.mark.asyncio
async def test_responses_fallback_text_output_parsing():
    provider = _provider(wire_api="responses")
    client = _Client(
        [
            _Resp(
                200,
                {
                    "output": [
                        {
                            "type": "message",
                            "content": [
                                {"type": "output_text", "text": "alpha one"},
                                {"type": "output_text", "text": "alpha two"},
                            ],
                        }
                    ]
                },
            )
        ]
    )
    provider._client = client

    out = await provider.generate("make alpha")

    assert out == "alpha one\nalpha two"


@pytest.mark.asyncio
async def test_chat_completions_payload_and_parsing():
    provider = _provider(wire_api="chat_completions", base_url="http://127.0.0.1:8080/v1")
    client = _Client(
        [_Resp(200, {"choices": [{"message": {"content": "chat alpha"}}]})]
    )
    provider._client = client

    out = await provider.generate("make alpha", temperature=0.2, max_tokens=99)

    assert out == "chat alpha"
    assert client.calls[0]["url"] == "http://127.0.0.1:8080/v1/chat/completions"
    payload = client.calls[0]["json"]
    assert payload["model"] == "gpt-test"
    assert payload["messages"] == [{"role": "user", "content": "make alpha"}]
    assert payload["temperature"] == 0.2
    assert payload["max_tokens"] == 99
    assert payload["store"] is False
    assert payload["stream"] is False
    assert "reasoning_effort" not in payload


@pytest.mark.asyncio
async def test_chat_completions_optional_token_and_reasoning_parameters():
    provider = OpenAIProvider(
        api_key="test-key",
        base_url="https://proxy.example",
        model="gpt-test",
        wire_api="chat_completions",
        reasoning_effort="xhigh",
        chat_token_param="max_completion_tokens",
        chat_reasoning_effort=True,
    )
    provider._client = _Client(
        [_Resp(200, {"choices": [{"message": {"content": "chat alpha"}}]})]
    )

    await provider.generate("make alpha", max_tokens=99)

    payload = provider._client.calls[0]["json"]
    assert payload["max_completion_tokens"] == 99
    assert "max_tokens" not in payload
    assert payload["reasoning_effort"] == "xhigh"


@pytest.mark.asyncio
async def test_deepseek_uses_configured_default_max_tokens():
    provider = DeepSeekProvider(
        api_key="test-key",
        base_url="https://deepseek.example/chat",
        model="deepseek-test",
        max_tokens=222,
    )
    provider._client = _Client(
        [_Resp(200, {"choices": [{"message": {"content": "deepseek alpha"}}]})]
    )

    out = await provider.generate("make alpha")

    assert out == "deepseek alpha"
    payload = provider._client.calls[0]["json"]
    assert payload["model"] == "deepseek-test"
    assert payload["max_tokens"] == 222


@pytest.mark.asyncio
async def test_auto_mode_falls_back_to_chat_completions_when_responses_is_unavailable():
    provider = _provider(wire_api="auto")
    client = _Client(
        [
            _Resp(404, text="missing responses endpoint"),
            _Resp(200, {"choices": [{"message": {"content": "chat fallback"}}]}),
        ]
    )
    provider._client = client

    out = await provider.generate("make alpha")

    assert out == "chat fallback"
    assert client.calls[0]["url"] == "http://127.0.0.1:8080/v1/responses"
    assert client.calls[1]["url"] == "http://127.0.0.1:8080/v1/chat/completions"


@pytest.mark.asyncio
async def test_auto_mode_does_not_fall_back_for_responses_configuration_errors():
    provider = _provider(wire_api="auto")
    client = _Client([_Resp(400, text="invalid reasoning effort")])
    provider._client = client

    with pytest.raises(Exception, match="invalid reasoning effort"):
        await provider.generate("make alpha")

    assert len(client.calls) == 1
