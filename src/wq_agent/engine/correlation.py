from __future__ import annotations


def parse_pnl_response(data: dict) -> tuple[list[str], list[float]]:
    """WQ PnL recordset（累计 PnL）→（日期, 每日收益）。

    假设 records 为 [[date, cumulative_pnl], ...]。容错：跳过缺值/格式错误的行。
    每日收益 = 累计 PnL 的逐日差分（首日丢弃）。
    """
    records = data.get("records") or []
    dates: list[str] = []
    cum: list[float] = []
    for rec in records:
        if not isinstance(rec, (list, tuple)) or len(rec) < 2:
            continue
        d, v = rec[0], rec[1]
        if v is None:
            continue
        try:
            cum.append(float(v))
        except (TypeError, ValueError):
            continue
        dates.append(str(d))
    daily = [cum[i] - cum[i - 1] for i in range(1, len(cum))]
    return dates[1:], daily
