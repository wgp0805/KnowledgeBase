---
title: "摘要-dsh-todolist机制"
type: source
tags: [来源, 原始文件]
sources: ["raw/09-archive/阿里面试官：“Agent 的 Todo List 有什么用？”.md"]
last_updated: 2026-10-26
---

## 核心摘要

文章以面试问答形式拆解 Agent Todo List 的设计原理，核心素材是 DeepSeek Harness 的 Todo 源码。论点一：Todo List 不只是给用户看的进度条，它同时解决两个问题——通过不断重写清单把目标刷新到上下文末尾防止模型执行跑偏（依据 Manus《Context Engineering for AI Agents》的复述强化注意力原理），以及让用户在 Agent 跑偏之前及时纠正。论点二：底层只暴露一个 `todo_write` 工具、每次全量覆写整张清单，状态枚举仅三种，参数校验器拦截多余字段。论点三：提示词与代码校验双管齐下控制并行任务数（`allowParallelInProgress` 开关）。论点四：清单数据通过事件溯源日志与会话投影分离渲染，事件不进模型消息流、不占上下文窗口、不破坏 Prefix Caching，压缩时用 Checkpoint 摘要模板保住未完成任务。论点五：Plan 模式明令禁止调用 `todo_write`，多 Agent 分工时需演进成按编号更新的任务工具。

## 关联连接

- [[DeepSeekHarness]] — 核心实体，文章所有源码细节的载体
- [[AgentTodoList]] — 本篇提炼的核心概念
- [[会话投影]] — 本篇提炼的架构模式（模型上下文与前端视图分离）
- [[AgentLoop]] — todo_write 是执行循环中的目标锚点
- [[摘要-DeepSeek-Harness任务管理方法]] — 同实体不同侧面：任务管理方法论 vs Todo 工具机制
- [[LostInTheMiddle]] — "上下文末尾注意力最强"的原理页
- [[EventSourcing]] — `todo/write` 事件 + `todos` 会话投影的底层架构模式
- [[前缀缓存稳定布局]] — 事件不进消息流正是为了保护 Prefix Caching 命中率
- [[上下文压缩]] — Checkpoint 摘要模板保留未完成任务
- [[沉默王二]] — 文章作者
