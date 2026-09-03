---
title: "Qwen3.8-Flash"
type: concept
tags: [Qwen, 阿里云, 模型架构, 开源, 低成本]
sources: [raw/01-articles/2026-09-02-整个AI圈都在斩杀，Qwen却算了一笔长期账.md]
last_updated: 2026-09-03
---

## 定义
Qwen3.8-Flash 是阿里通义千问发布的轻量级高性能模型，采用为 Qwen4 准备的 Next 架构，125B 总参数但每步仅激活 6B，训练成本降至前代九分之一。

## 关键信息
- 架构：Next 架构（混合注意力 + 四通道信息读写 + 51B 外挂速查手册）
- 参数：125B 总参数，6B 激活参数
- 成本：每百万 Token 输入 0.8 元，输出 2.7 元（缓存命中 0.1 元）
- 性能：SWE-bench Pro 62.5 分（超 Opus4.6 9.1 分），AndroidWorld 超 Opus4.6 22.5 分
- 开源：Hugging Face + 魔搭同步放出权重，SGLang Day 0 支持
- 长文本：1M tokens 场景处理速度最快 8 倍提升
- 对比 Claude Opus 价格不到 3%，形成"斩杀线"

## 关联连接
- [[Qwen]] — 模型系列
- [[Next架构]] — 新架构
- [[MoE]] — 旧架构对比
- [[IntelligencePerDollar]] — 智能性价比
- [[开源生态]] — 分发策略
- [[阿里云]] — 运营实体
- [[摘要-qwen38-flash架构深度分析]] — 来源
