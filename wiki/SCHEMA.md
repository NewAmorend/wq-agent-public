# Quant Wiki Schema

每个页面是一个独立 markdown 文件，YAML frontmatter + 正文。正文中用 `页面名` 互链。

## Frontmatter 字段

```yaml
---
title: 动量因子家族                # 必填，人类可读标题
type: concept                     # 必填，枚举见下
tags: [momentum, ts_delta]        # 必填，至少 1 个。用于 grep + 共享标签图边
sources: [https://...]            # 可选，来源链接
created: 2026-05-22               # 必填，YYYY-MM-DD
fitness: 0.62                     # 仅 type=entry 必填
sharpe: 1.4                       # 仅 type=entry 必填
turnover: 0.42                    # 仅 type=entry 必填
returns: 0.07                     # 仅 type=entry 必填
alpha_id: 123                     # 仅 type=entry 必填
---
```

## type 枚举

| type | 用途 | 目录 |
| --- | --- | --- |
| `concept` | 因子家族、市场异象、统计原理 | `concepts/` |
| `entity` | 具体证券、行业、研究对象 | `entities/`（按需）；dataset 页当前也用此类型 |
| `operator` | 单个算子语义 + 踩坑 | `operators/` |
| `field` | 单个数据字段语义 + 用法 | `fields/` |
| `pattern` | 失败模式、风险症状、修复处方 | `patterns/` |
| `recipe` | 可复用 alpha 构造手册 | `recipes/` |
| `lesson` | 失败模式归纳（自动写） | `lessons/` |
| `entry` | 已验证的 alpha 档案（自动写） | `entries/` |

## 文件命名

- 人写：`concepts/momentum.md`、`operators/ts_decay_linear.md`、`fields/cashflow_op.md`、`patterns/high-turnover.md`、`recipes/quality-profitability.md`
- 自动：`entries/2026-05-22-alpha-123.md`、`lessons/2026-05-22-batch-7.md`

## 互链规则

正文里写 `[[ts_decay_linear]]` 会自动建一条 wikilink 边。目标如果不存在，索引时记入 `log.md` 的"断链"列表，不报错。

## 黑名单

下列内容**不应**写入 wiki，会拉低检索质量：

- 纯算子列表（去 `wq.client.get_operators()` 拉就行）
- 通用 markdown 排版示例
- 与量化无关的内容
- 长篇 LLM 输出（建议人工 / auto_record 提炼后再入）
- 未被 recipe / pattern / field 复用的低质量字段占位页
