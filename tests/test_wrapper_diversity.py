from __future__ import annotations

import random

from wq_agent.generator.llm import (
    LLMAlphaGenerator,
    build_proven_wrappers_section,
)


# --------------------------------------------------------------- sampled pool
def test_proven_wrappers_section_keeps_guidance_and_samples():
    sec = build_proven_wrappers_section(random.Random(0))
    # 仍保留标题与关键观察（教学内容不能丢）
    assert "实测高 Fitness Wrapper" in sec
    assert "关键观察" in sec
    # 至少包含一个 <signal> 占位的 wrapper 样例
    assert "<signal>" in sec


def test_proven_wrappers_section_varies_with_seed():
    a = build_proven_wrappers_section(random.Random(1))
    b = build_proven_wrappers_section(random.Random(2))
    # 不同 seed 抽到的样例集合应不同——这正是打破"每次都推同 3 个壳子"的关键
    assert a != b


# --------------------------------------------------- family saturation steer
def test_family_saturation_section_flags_overrepresented():
    dist = {
        "total_backtested": 20,
        "unique_skeletons": 5,
        "unique_outer2": 3,
        "top_outer2": [
            {"signature": "ts_decay_linear(rank", "count": 12, "avg_fitness": 0.4, "max_fitness": 1.1},
            {"signature": "group_neutralize(rank", "count": 5, "avg_fitness": 0.5, "max_fitness": 0.9},
            {"signature": "rank(ts_delta", "count": 3, "avg_fitness": 0.2, "max_fitness": 0.3},
        ],
    }
    sec = LLMAlphaGenerator._build_family_saturation_section(dist)
    assert sec  # 非空
    # 必须点名霸屏家族
    assert "ts_decay_linear(rank" in sec


def test_family_saturation_section_empty_when_sparse_or_diverse():
    # 数据太少 → 不打扰
    assert LLMAlphaGenerator._build_family_saturation_section(
        {"total_backtested": 4, "unique_outer2": 4, "top_outer2": []}
    ) == ""
    # 没有任何家族集中（都只占很小份额）→ 空
    dist = {
        "total_backtested": 30,
        "unique_outer2": 30,
        "top_outer2": [
            {"signature": f"op{i}(rank", "count": 1, "avg_fitness": 0.5, "max_fitness": 0.5}
            for i in range(30)
        ],
    }
    assert LLMAlphaGenerator._build_family_saturation_section(dist) == ""
    # None 安全
    assert LLMAlphaGenerator._build_family_saturation_section(None) == ""
