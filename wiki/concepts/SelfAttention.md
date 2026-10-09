---
title: "SelfAttention"
type: concept
tags: [注意力机制, Transformer, LLM, 基础概念]
sources: []
last_updated: 2026-10-08
---

SelfAttention（自注意力）是 Transformer 的核心机制，为序列中每个 token 分配注意力权重，使模型捕捉上下文之间的依赖关系。在 [[粉色大象效应]] 的解释中，提示词里的负向禁止词因被自注意力高频关注反而成为生成目标，对应的解法是 [[剪枝优化]]。

## 关联连接
- [[粉色大象效应]] — 来源（死链修复）
- [[剪枝优化]] — 来源（死链修复）
- [[摘要-提示词粉色大象效应]] — 来源（死链修复）
