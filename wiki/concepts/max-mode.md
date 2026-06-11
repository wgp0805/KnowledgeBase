---
title: "max-mode"
type: concept
tags: [AI Agent, 可靠性, 并行计算, MiMo Code]
sources: [raw/01-articles/小米版Claude Code正式发布，这次开源能给到夯.md]
last_updated: 2026-06-11
---

## 定义
Max Mode 是 AI Agent 中通过并行生成多个候选方案并由 judge 模型选出最优的可靠性提升机制。每轮决策时并行生成 N 个候选方案（默认 N=5），每个候选独立完成推理和工具调用规划但不实际执行，由同一模型作为 judge 对比选出最优方案执行。

## 关键信息
- **核心思路**：用算力换可靠性，在每一步投入额外计算换取更可靠的决策
- **采样策略**：默认使用 temperature=1 做 5 次独立采样，几乎不会产出相同结果
- **置信度信号**：多个候选指向同一方向时，表明该方向置信度高
- **性能提升**：在 SWE-Bench Pro 上相比单次采样提升 10-20%
- **成本代价**：约 4-5 倍 token 消耗
- **适用场景**：一步走错全盘皆输的长任务
- **配置**：当前为实验性功能，需在 `.mimocode/mimocode.json` 或 `~/.config/mimocode/mimocode.json` 中设置 `experimental.maxMode` 为 `true`

### 与 Goal 的维度差异
- [[max-mode]] 是并行维度，同一步花 N 倍算力选最优
- [[goals]] 是串行维度，在同一个任务上做更长的自我检查和执行
- 两者可以同时启用

## 关联连接
- [[MiMoCode]] — 所属产品
- [[goals]] — 串行维度的可靠性机制
- [[dynamic-workflow]] — 复杂任务的流程编排
- [[AgentHarness]] — Harness 计算主题
- [[摘要-mimo-code发布]] — 来源
