---
title: "AgentTodoList"
type: concept
tags: [概念, Agent, 任务管理, DeepSeekHarness]
sources: ["raw/09-archive/阿里面试官：“Agent 的 Todo List 有什么用？”.md"]
last_updated: 2026-10-26
---

## 定义

Agent 的任务清单机制：以单个 `todo_write` 工具承载任务管理，每次全量覆写整张清单，同时服务模型自身的目标刷新（防跑偏）与用户的进度可见（及时纠偏）。

## 关键信息

- **双重价值**：一是让模型把大目标拆成具体步骤，通过不断重写清单把目标刷新到上下文末尾，防止长程任务中初始目标被后来的工具结果淹没（上下文末尾注意力最强的复述原理，源自 Manus《Context Engineering for AI Agents》博客）；二是把推理进度展示给用户，让用户在 Agent 跑偏之前及时纠正。把它仅当作"给用户看的进度条"没有 get 到价值。
- **单一工具设计**：DeepSeek Harness 的 Todo 模块只向模型暴露一个 `todo_write` 工具（选型对比：新增/修改/删除/查询四工具 vs 单一 `todo_write` 全量覆写 vs 改写本地 Markdown 文件——DSH 选全量覆写）。理由：①省去模型跨轮次记忆任务编号的负担；②每次重写即把全局目标与当前进度复述到上下文末尾，防止中途忘掉。
- **三态状态机**：参数为 `todos` 数组，每项仅两个必填字段——`content`（任务描述）与 `status`（状态）；状态枚举只有 `pending`（待处理）/`in_progress`（进行中）/`completed`（已完成）三种；模型多传 `id` 或 `priority` 字段会被参数校验器当场报错拦截。
- **提示词约束**：工具描述规定"简单的单步任务直接跳过清单；复杂的多步任务动手前先列出清单；每完成一项必须立刻标记为 `completed`，不允许累积到最后批量交差"。
- **并行控制**：布尔配置项 `allowParallelInProgress` 设为 `false` 时，模型提交两个以上 `in_progress` 任务会被工具执行模块的校验函数直接抛异常、返回一条错误结果，逼迫模型当场修正参数并重新调用；校验逻辑还拦截空字符串与重复任务描述；开启并发 Sub-agent 和后台任务时该开关设为 `true`。防止"一口气把所有任务全标记成进行中"靠提示词 + 代码校验双管齐下，不能只押一边。
- **配套架构**：清单渲染走 [[会话投影]]——`todo/write` 事件不进模型消息流、不占上下文窗口、不破坏 Prefix Caching，详见该概念页。
- **压缩韧性**：长对话触发上下文压缩时，压缩模块内置固定 Checkpoint 摘要模板，强制把还没做完的任务写进 `Pending Jobs` 和 `Current Work` 章节，确保压缩后任务不丢；前端读会话投影则丝毫不受影响。
- **边界**：Plan 模式（只做规划）下系统提示词明令禁止调用 `todo_write`——Plan 模式负责动手前敲定方案，`todo_write` 跟踪的是方案获批后的执行进度；多 Agent 分工场景下全量覆写失效，需演进成按编号更新的任务工具。

## 关联连接

- [[摘要-dsh-todolist机制]] — 来源
- [[DeepSeekHarness]] — 源码解析的载体
- [[会话投影]] — 配套架构：清单事件与会话投影分离渲染
- [[AgentLoop]] — todo_write 是执行循环中的目标锚点与状态检查点
- [[LostInTheMiddle]] — "上下文末尾注意力最强"的原理（中间位置注意力衰减）
- [[EventSourcing]] — `todo/write` 事件日志的底层模式
- [[前缀缓存稳定布局]] — 事件不进消息流保护 Prefix Caching 命中率
- [[上下文压缩]] — 压缩时 Checkpoint 摘要模板承接未完成任务
- [[goals]] — 同属任务管理的带验证器长跑任务机制
- [[agent-view]] — Claude Code 侧同类"任务进度可视化"机制
- [[摘要-DeepSeek-Harness任务管理方法]] — 同实体不同侧面：任务管理方法论 vs 工具底层机制
- [[steering]] — 用户在 Agent 跑偏之前纠正
