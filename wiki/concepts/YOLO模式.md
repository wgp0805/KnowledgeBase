---
title: "YOLO模式"
type: concept
tags: [AI, Agent, 安全, 权限管理]
sources: [raw/01-articles/【Pi Agent】 源码剖析：4 个工具的极简主义——为什么更少反而更好.md]
last_updated: 2026-08-12
---

## 定义
YOLO 模式（You Only Live Once）是 AI Agent 的一种安全策略——无限制执行，无权限弹窗确认。Pi Agent 默认以 YOLO 模式运行，其创建者 Armin Ronacher 认为权限弹窗是"安全剧场"，开发者终究会点"全部允许"，不如一开始就不弹。

## 核心论点
1. **弹窗是心理安慰**：如果 Agent 有读写文件 + 执行命令的权限，弹窗只是心理安慰，不提供真正的安全保障
2. **效率优先**：开发者为了效率终究会点"全部允许"，弹窗反而打断工作流
3. **诚实面对现实**：不如一开始就不弹，把安全选择权交给开发者
4. **容器隔离更可靠**：如果需要沙箱，在 Docker 容器中运行 Agent，容器隔离比应用层权限系统更可靠

## 与其他安全策略对比
- **Claude Code**：权限确认弹窗 + 沙箱（安全优先）
- **Cursor**：频繁弹窗确认
- **Pi Agent**：YOLO 模式，无弹窗，建议容器隔离
- **双 LLM 模式**（Simon Willison）：一个 LLM 执行，另一个审查——Pi 认为这只是再加一层剧场

## 关联连接
- [[安全剧场]] — YOLO 模式的理论基础
- [[ArminRonacher]] — YOLO 模式的提出者
- [[摘要-pi-agent-4工具极简主义]] — 来源文章
- [[guardrails]] — 对比概念：AI Agent 安全护栏体系
- [[auto-mode]] — Claude Code 的类似概念（无需确认直接执行）
