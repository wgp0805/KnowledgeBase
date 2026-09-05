---
title: "MoE (Mixture of Experts)"
type: concept
tags: ["MoE", "模型架构", "DeepSeek"]
last_updated: 2026-09-01
---

# MoE (Mixture of Experts)

MoE（混合专家架构）：多个专家网络中路由激活部分专家，降低计算量同时保持模型容量。DeepSeek 模型采用 MoE 架构，配合灰度曝光等工程策略。

### 与 Next 架构对比
MoE 是"长在一棵树上，改来改去只能修修边幅"，Next 架构是"把树给换了"。MoE 通过部分专家激活降低计算量，Next 架构通过混合注意力+四通道读写+外挂速查手册三大技术动作，训练成本降至九分之一。

## 关联连接
[[DeepSeek-V4]], [[灰度曝光]], [[沉默王二]], [[Qwen3.8-Flash]], [[Next架构]], [[摘要-qwen38-flash架构深度分析]]
