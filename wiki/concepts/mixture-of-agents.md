---
title: "mixture-of-agents"
type: concept
tags: [AI, Agent, 多模型, 协作]
sources: [raw/01-articles/2026-07-21-Hermes Agent 完全指南：比 Claude Code 更自由的开源 AI Agent，从安装配置到多 Agent 协作 - 不吃紫菜.md]
last_updated: 2026-07-22
---

## 定义
Mixture-of-Agents（MoA）是一种多模型协作模式，采用参考模型 + 聚合器模式，多个参考模型独立推理后由聚合器综合得出最佳结果。在 Hermes Agent v0.18 中作为一等公民特性支持。

## 关键信息
- **参考模型**：多个 LLM 独立对同一问题进行推理
- **聚合器**：综合分析参考模型的输出，生成最终答案
- **优势**：综合多模型视角，减少单一模型的偏见和错误
- **适用场景**：需要高质量输出的复杂推理任务
- **可视化**：支持推理过程可视化，便于理解多模型协作逻辑

## 关联连接
- [[HermesAgent]] — 支持 MoA 的 Agent 系统
- [[multi-agent-collaboration]] — 多 Agent 协作
- [[摘要-hermes-agent-complete-guide]] — 来源
