---
title: "Tool Result Pruning"
type: concept
tags: [概念, Agent, 压缩, 技术]
sources: [raw/01-articles/2026-09-01-Agent上下文管理概述-1 - Big-Yellow-J.md]
last_updated: 2026-09-01
---

## 定义
OpenCode实现的工具结果剪枝策略，对旧的工具调用结果进行标记和压缩，而不是直接删除整个工具调用链。

## 关键信息
- OpenCode有两层压缩：Tool Result Pruning和Conversation Compaction
- 第一层对工具调用结果进行压缩，主要压掉Tool Result的output
- 采用工程化的启发式规则：近期工具输出优先保护，较老、已完成、非保护类型的工具输出在累计超过一定Token预算后从Active Context中驱逐
- 不调用LLM处理，而是直接标记compacted

## 关联连接
- [[摘要-Agent上下文管理概述]] — 来源文章
- [[Agent上下文管理]] — 核心概念
- [[上下文压缩]] — 关键技术
- [[OpenCode]] — 实现该策略的Agent
