from __future__ import annotations

from pathlib import Path

import pytest


_PAGES = {
    "concepts/momentum.md": """---
title: 动量
type: concept
tags: [momentum, ts_delta, trend]
created: 2026-05-22
---

动量因子捕捉过去 [[ts_delta]] 的延续。常配合 [[ts_decay_linear]] 平滑。
""",
    "concepts/reversal.md": """---
title: 反转
type: concept
tags: [reversal, ts_zscore, mean_reversion]
created: 2026-05-22
---

短期反转利用 [[ts_zscore]] 偏离做空头信号。
""",
    "operators/ts_decay_linear.md": """---
title: ts_decay_linear
type: operator
tags: [ts_decay_linear, smoothing, momentum]
created: 2026-05-22
---

线性加权移动平均，配合 [[动量]] 使用降低换手。
""",
    "operators/ts_delta.md": """---
title: ts_delta
type: operator
tags: [ts_delta, momentum, trend]
created: 2026-05-22
---

时间序列差分，是 [[动量]] 的最基本构件。
""",
    "dictionary/base.txt": "动量\n反转\nts_delta\nts_decay_linear\nts_zscore\n平滑\n",
    "dictionary/synonyms.yaml": "动量:\n  - momentum\n反转:\n  - reversal\n  - 均值回归\n",
}


@pytest.fixture
def wiki_root(tmp_path: Path) -> Path:
    root = tmp_path / "wiki"
    for rel, content in _PAGES.items():
        path = root / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")
    return root
