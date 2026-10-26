---
title: "samply"
type: entity
tags: [工具, 性能分析, Profiler, 命令行, 开源]
sources: [raw/09-archive/2026-10-15-你的游戏本身就是 Harness ：如何让 AI Agent 读懂游戏并十倍加速迭代？ - leikooo.md]
last_updated: 2026-10-15
---

## 定义

samply 是一个免费、现代、**支持命令行的性能分析（profiler）工具**（GitHub: `mstange/samply`）。它被推荐为 AI 辅助游戏开发中"影响评估"环节的关键工具：可以轻松挂载到本地工程，并把性能捕获结果**直接 Dump 到终端**。

## 关键信息

- **为什么需要它**：传统的 Unity Profiler、Unreal Insights、JetBrains dotMemory 等可视化剖析工具是**专为人类肉眼设计的**，AI 极其讨厌这类不可交互的图形界面。AI 最擅长打交道的是结构化纯文本。
- **自治调优闭环**：Agent 本身熟读 samply 的源码与文档，能够自主执行采样 → 解析性能热点行号 → 修改优化代码 → 重新采样验证，实现**完全自治的性能调优内循环**。
- **通用原则**：如果性能分析工具能直接将采样快照输出为详尽的控制台文本报告，Agent 的迭代效率会呈指数级飙升（Unity 也正在努力让自家分析器对 Agent 更可读）。

## 关联连接

- [[纯文本性能分析]] — 所属方法论
- [[摘要-你的游戏本身就是Harness]] — 来源
- [[odiff]] — 同一工作流中负责视觉验收的命令行工具
- [[Agent迭代飞轮]] — samply 支撑"影响评估"最后一环
- [[KyleKukshtel]] — 推荐者
