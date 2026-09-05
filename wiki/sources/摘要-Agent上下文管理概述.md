---
title: "摘要-Agent上下文管理概述"
type: source
tags: [来源, Agent, 上下文管理, 技术]
sources: [raw/01-articles/2026-09-01-Agent上下文管理概述-1 - Big-Yellow-J.md]
last_updated: 2026-09-01
---

## 核心摘要
这篇文章系统性地分析了Agent运行过程中的上下文组织与压缩策略。介绍了Pi Agent、OpenCode、Manus等工业级Agent的上下文管理方案，包括静态+动态提示词的组织方式、Tool Result Pruning、结构化压缩、KV Cache压缩等技术。文章总结了Agent上下文管理的核心要点：上下文组织（静态内容+用户消息+Agent交互轨迹+工具结果）和上下文压缩（选择性保留工具结果、基于提示词的摘要、选择性丢弃或Token级压缩）。

## 关联连接
- [[Agent上下文管理]] — 文章探讨的核心概念
- [[上下文压缩]] — Agent上下文管理的关键技术
- [[Tool Result Pruning]] — OpenCode的工具结果剪枝策略
- [[结构化压缩]] — Pi Agent的压缩策略
- [[KV Cache压缩]] — 模型层的压缩技术
