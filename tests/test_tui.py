from __future__ import annotations

from wq_agent.tui import WQAgentTui, _truncate


def test_tui_declares_core_bindings():
    actions = {binding[1] for binding in WQAgentTui.BINDINGS}
    assert {"generate", "run_batch", "refine", "backtest_pending", "refresh", "quit"} <= actions


def test_truncate_shortens_long_expressions():
    assert _truncate("rank(close)", 20) == "rank(close)"
    assert _truncate("abcdefghijklmnopqrstuvwxyz", 8) == "abcdefg..."
