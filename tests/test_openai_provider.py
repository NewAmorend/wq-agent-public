from __future__ import annotations

import pytest

from wq_agent.config import Settings
from wq_agent.llm import LLMFactory, OpenAIProvider


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


def test_openai_provider_rejects_missing_or_placeholder_api_key():
    with pytest.raises(ValueError, match="OPENAI_API_KEY"):
        OpenAIProvider(api_key="", base_url="https://api.openai.com/v1")

    with pytest.raises(ValueError, match="OPENAI_API_KEY"):
        OpenAIProvider(api_key="your_openai_or_proxy_key", base_url="https://api.openai.com/v1")


def test_openai_provider_rejects_remote_insecure_http_but_allows_localhost():
    with pytest.raises(ValueError, match="insecure HTTP"):
        OpenAIProvider(api_key="test-key", base_url="http://example.com:8080")

    provider = OpenAIProvider(api_key="test-key", base_url="http://127.0.0.1:8080")
    assert provider.base_url == "http://127.0.0.1:8080"


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
