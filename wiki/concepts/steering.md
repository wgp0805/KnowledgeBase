---
title: "steering"
type: concept
tags: [AI Agent, 人机交互, 控制机制, Codex]
sources: [raw/09-archive/如何把Codex用到极致.md, "raw/01-articles/2026-10-05 - 用户中途取消，Agent 任务怎么停下来？.md"]
last_updated: 2026-10-08
---

## 定义
Steering（转向）是 AI Agent 运行过程中，用户可随时打断并纠正方向的控制机制，让 Agent 不必从头开始即可调整执行策略。

## 关键信息
- 任务跑到一半时，用户可打断 Agent 立刻纠偏
- 与传统"停止→重新写 prompt"不同，steering 是增量修正
- 与 [[queuing]] 互补：steering 是即时干预，queuing 是不打断当前任务排入下一步
- 核心哲学：人没有被踢出回路，Agent 不是替你拍板，而是把决策点提前暴露
- **与"取消"的分界（2026-10-05，详见 [[摘要-agent任务取消机制]]）**：用户不是想取消而是想补充要求时才走 steering——新消息先进队列，等当前这批工具执行完、下次调用模型之前再注入，因为 **tool_use 和 tool_result 之间不能夹别的消息**
- **两种队列实现**：Pi Agent 两条队列——steer（当前这轮工具执行完后注入）与 followUp（Agent 正常停下才执行，适合"做完这个再做那个"）；Claude Code 执行中补充输入会排队、等这批工具调用结束后在同一轮提交给模型，**Ctrl+Enter 则立即发送**（正在执行的 shell 转后台继续，模型还能看到已产生的输出）

## 关联连接
- [[摘要-把Codex用到极致]] — 来源
- [[摘要-agent任务取消机制]] — 来源（与取消的分界、两种队列实现）
- [[Agent任务取消]] — 用户真想停止时的机制
- [[Codex]] — 所属产品
- [[queuing]] — 互补的控制机制
- [[AgentLoop]] — 注入时机所依赖的执行循环
