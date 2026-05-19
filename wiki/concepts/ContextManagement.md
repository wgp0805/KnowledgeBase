---
title: "ContextManagement"
type: concept
tags: [AI, 上下文, 性能优化]
sources: [raw/01-articles/40分钟学会Codex！"零基础"终级教程～【附完整文档】.md, raw/01-articles/全网最全！60分钟全面掌握Claude Code~【附完整文档】.md]
last_updated: 2026-05-19
---

## 定义
管理 Agent 上下文窗口使用的策略和技术，确保模型在有限上下文空间内保持高效准确的输出。

## 关键信息

### 核心问题
- 模型上下文有限（1M token 听着大，有效比例仅 60%-80%）
- 上下文越多，模型能力下降（把握不住重点）
- 回答变慢、质量下降是上下文溢出的典型症状

### Claude Code 的管理手段
- `/compact`：主动压缩上下文，保留关键信息释放空间
- `/clear`：彻底清空重开对话
- `/context`：查看上下文占比和各组件 token 消耗
- 上下文 >60% 时建议手动 /compact

### Codex 的管理手段
- 可视化上下文余量圆圈
- 自动压缩（上下文快满时）
- 手动 `/压缩` 命令
- 状态栏持续显示上下文余量

### 最佳实践
- 结束某个任务后主动压缩
- 任务间适时 clear
- 描述越具体 token 越省（指令不足时 Agent 要花更多 token 探索）

## 关联连接
- [[Agent]] — 上下文管理所属概念
- [[ClaudeCode]] — 管理工具
- [[Codex]] — 管理工具
- [[AgentHarness]] — harness 核心组件
