---
title: "Checkpoint"
type: concept
tags: [AI, Agent, 状态持久化, LangGraph]
sources: ["raw/01-articles/从链式调用到图式自治：LangChain与LangGraph核心差异与落地选型全解析 - 一天不进步，就是退步.md"]
last_updated: 2026-07-13
---

## 定义

Checkpoint 是 LangGraph 等 Agent 编排框架中的状态持久化机制，在工作流每个节点执行后保存当前状态快照，支持中断恢复、时间旅行回溯和多轮调试。

## 关键信息

- **核心作用**：将 Agent 工作流的中间状态序列化存储，实现"暂停-恢复"能力
- **存储介质**：内存（SQLite/PostgreSQL）或文件系统
- **关键能力**：
  - 中断恢复：工作流中断后从最后 checkpoint 继续
  - 时间旅行：回溯到任意历史节点重新执行
  - 人机协作：在 checkpoint 处暂停等待人工审批
- **适用场景**：长时间运行的 Agent 任务、需要人工干预的工作流、调试与审计

## 关联连接
- [[LangGraph]] — Checkpoint 所属框架
- [[Agent工作流编排]] — 工作流状态管理
- [[摘要-LangChain与LangGraph对比]] — 来源
