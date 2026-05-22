---
title: Building Diversified Portfolios that Outperform Out-of-Sample (HRP)
type: concept
tags: [paper, portfolio-construction, hrp, hierarchical-clustering]
sources: [https://jpm.pm-research.com/content/42/4/59]
created: 2026-05-22
authors: [Marcos Lopez de Prado]
year: 2016
paper_source: manual
---

# Building Diversified Portfolios that Outperform Out-of-Sample

**作者**：López de Prado　**年份**：2016 (JPM)　**书**：Advances in Financial Machine Learning, 2018

## 核心结论

提出 **Hierarchical Risk Parity (HRP)** 组合构建法：用层次聚类 + 二分递归 + 风险均分替代马克维茨二次优化。在样本外稳定优于 MV / IVP / RP，对协方差矩阵估计误差远更鲁棒。

## Key Takeaway

- MV 优化对协方差噪声极其敏感（"Markowitz 优化器是噪声放大器"）
- HRP 不需要矩阵求逆，奇异协方差仍能跑
- 适合作为多 alpha 信号 → 最终持仓的合成步骤

## 对 wq-agent 的启示

- LLM 生成的 alpha 池里，多数信号互相高度相关
- 把 top-N 高 fitness alpha 通过 HRP 而非等权合成，可能显著提升组合夏普
- WQ Brain 内不直接支持 HRP；可在导出 alpha 数据后离线做组合

## 相关

- 因子稳健性 [[2019-hou-mo-xue-zhang-which-factors]]
