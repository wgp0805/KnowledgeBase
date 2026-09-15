---
title: "DeepAgents"
type: entity
tags: [实体, 工具, Agent, LangChain, 框架]
sources: [raw/01-articles/为什么越来越多人用OpenWiki？.md]
last_updated: 2026-09-15
---

## 定义
[[LangChain]] 的 Agent 构建库/引擎，[[OpenWiki]] 的底层文档生成引擎即基于 Deep Agents 构建。它驱动「代码扫描 → 架构分析 → Wiki 生成」的 Agent 会话，负责读取代码库、识别模块划分与依赖关系、调用链路、集成点，并生成结构化 Markdown。

## 关键信息
- **在 OpenWiki 中的角色**：三层架构中的第二层（文档生成引擎），介于「代码仓库层（只读不改）」与「结构化知识层（openwiki/ 目录）」之间
- **工作模式**：**Agent 驱动 + 确定性工程** 的混合模式——不是「把代码丢给 LLM 让它自由发挥」，而是 Agent 会话负责理解与生成，确定性步骤（Git 上下文收集、Claims 校验、指针写入 `AGENTS.md`/`CLAUDE.md`）负责保证可复现与可溯源
- **与确定性工程的配合**：OpenWiki 用 Claims 机制约束 Deep Agents 的产出——每条事实性陈述必须关联一个 Claim，记录来源文件与行号；代码变更时 `--update` 只调和受影响的 Claims，使 Wiki 维护成本随代码量线性而非指数增长

## 关联连接
- [[摘要-openwiki-为什么越来越多人用]] — 来源
- [[OpenWiki]] — 主要使用方
- [[LangChain]] — 所属生态
- [[LLMWiki]] — OpenWiki 实现的理念
- [[Claims溯源]] — 约束 Deep Agents 产出的机制
- [[Agent]] — 核心概念
