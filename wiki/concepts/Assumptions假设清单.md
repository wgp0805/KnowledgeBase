---
title: "Assumptions假设清单"
type: concept
tags: [Agent, 需求澄清, 兜底机制, Codex]
sources: [raw/01-articles/用户需求模糊时 Agent 怎么澄清？.md]
last_updated: 2026-10-15
---

## 定义

Assumptions（假设清单）是 Agent 在**无法获得用户回答**时必须输出的交付物小节：Codex 的提示词明确规定，当获取不到用户回答时不要停下来，而是直接按最稳妥的推荐选项继续往下执行，但必须在最终输出的 Assumptions 小节里，把刚才替用户做出的所有假设一条条写清楚，让用户事后看结果时能一眼核对。

它解决的是[[需求澄清]]在**无人值守场景**下的最后一环：既不让后台任务卡死，也不让 Agent 悄悄替用户做决定。

## 关键信息

### 适用场景
后台定时任务、Headless（无界面）模式、Sub-agent 中等——屏幕前根本没有人可以回答提问。

### 双层兜底机制
1. **工具层拦截**（防止后台进程没人回应而卡死）：
   - Codex `request_user_input`（请求用户输入工具）第一行检查当前是不是 root 线程，若是 Sub-agent 发起调用直接报错："request_user_input can only be used by the root thread"，**只允许主 Agent 提问**；
   - 在 `codex exec` 这类非交互模式下，连外部 MCP 服务端通过 **elicitation**（服务端中途反问机制）发来的追问请求也会被自动取消，源码直接返回 Cancel 动作；
   - Pi 的 `questionnaire` 工具执行时也会先检查当前模式是不是 TUI，不是就直接报错返回。
2. **提示词兜底**：无法获取用户回答时不停止，按最稳妥的推荐选项继续执行，并在最终输出的 Assumptions 小节逐条写清所有代做的假设。

### 与 HITL 的关系
工具层拦截让"需要人"的动作只能在人真的在场时发生；提示词兜底保证无人时仍能交付**可审计的结果**——不是沉默失败，也不是静默替用户决策，而是显式声明假设。

## 关联连接

- [[AskUserQuestion]] — 有人在场时的提问通道
- [[偏好与取舍]] — 被兜底代做的主要是这类决策
- [[DiscoverableFacts]] — 事实类信息本就不该问用户
- [[需求澄清]] — 所属方法论
- [[HITL]] — 人类在环机制的边界定义
- [[Codex]] — Assumptions 小节与线程限制的出处
- [[Pi]] — questionnaire 的 TUI 模式检查
- [[摘要-用户需求模糊时Agent怎么澄清]] — 来源
