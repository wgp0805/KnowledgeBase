---
title: "AutoMemory"
type: concept
tags: [AI, 记忆, 自动化]
sources: [raw/01-articles/全网最全！60分钟全面掌握Claude Code~【附完整文档】.md, raw/01-articles/40分钟学会Codex！"零基础"终级教程～【附完整文档】.md]
last_updated: 2026-05-19
---

## 定义
Agent 的自动记忆机制，由后台 agent 在工作过程中自动记录用户习惯、反馈、项目信息等，按需注入到后续对话中。

## 关键信息

### Claude Code Auto Memory
- 需手动开启：`/memory` → 第一个选项
- 四种记忆类型：user（角色偏好）、feedback（反馈）、project（项目决策）、reference（外部资源索引）
- 存在项目目录下，只作用于当前项目
- 只读 memory.md 索引，遇到具体问题按索引读对应文件
- 可用自然语言删除记忆（"忘掉刚刚说的..."）

### Codex 自动记忆
- 实验性功能，需手动打开
- 在结束对话/任务/闲置后自动总结记忆
- 太短的对话不记、额度太低时不记
- 官方不建议手动修改自动记忆文件

### 优先级
Auto Memory 是第二优先级（CLAUDE.md/agents.md 是第一优先级），在工作过程中由 Agent 自己记录、按需注入。

## 关联连接
- [[ClaudeCode]] — Auto Memory 所属产品
- [[Codex]] — 对应自动记忆功能
- [[CLAUDEmd]] — 第一优先级记忆
- [[ContextManagement]] — 记忆与上下文的关系
