---
title: "ToolCallConfirmation"
type: concept
tags: [概念, SpringAI, 工具调用, HITL, 安全]
sources: ["raw/09-archive/夯爆了，Spring AI 2.1 正式发布！.md"]
last_updated: 2026-11-27
---

## 定义

Tool Call Confirmation 是 [[SpringAI]] 2.1（RC1 引入）的**框架级工具调用确认机制**：模型要调用被标记为需要确认的工具时，**整个工具调用循环会在执行任何调用之前暂停**，把回复连同待确认调用列表返回给应用；应用逐条给出 allow / deny 决策后再恢复执行。

它解决的是「**模型调用工具，到底该不该无条件信任**」这个企业级 Agent 绕不开的问题——框架层缺少一道人工确认的闸门时，模型可能「参数都对、判断错了」（如把不该退的款退了）。

## 关键信息

### 此前只能自己 hack

2.1 之前要在工具调用前加确认，只能在 `ToolCallingManager` 外面包一层：拦截工具调用请求、暂停循环、等人工决策、再把结果塞回去。写起来不难，**写对很难**：

- 暂停时的状态存哪里？
- 服务重启了怎么办？
- 多实例部署时，决策请求打到另一台机器上，怎么找到暂停的上下文？

**大部分团队的做法是「不做了」**——高危工具要么直接禁用，要么在 Prompt 里写一句「请谨慎操作」祈祷模型听话。

### 用法

```java
@Tool(description = "Book a flight", requiresConfirmation = true)
String bookFlight(String flightNumber) {
    return bookingService.book(flightNumber);
}
```

模型要调用该工具时整段循环暂停，应用收集每个调用的 `ToolCallDecision`（allow，或 deny 并附带一条消息），再调 `ToolCallingManager.executeToolCalls(prompt, reply, decisions)` 执行回复里的调用，结果作为下一次请求发回。**被拒绝的调用会把消息返回给模型，而不是真正执行**。

### 关键设计：暂停不保留状态

循环在等待时不保留任何状态——**暂停是一次普通的响应返回，恢复是一次普通的请求发送**。只要应用保存了对话，服务重启也能恢复；多实例部署也不怕决策打到另一台机器。这与 [[HITL]] 传统实现（进程内拦截器挂起等待）的关键差别就在这里。

### 哪些调用需要确认

由 `ToolCallConfirmationPolicy` 决定：

- **默认策略**：读取工具元数据（即 `requiresConfirmation` 标记）
- **`forTools(...)`**：指定**你不拥有的工具**，如 [[MCP协议|MCP]] 服务端暴露的工具
- **lambda**：检查调用参数——例如只确认超过某个金额的转账

### 能力边界

Tool Call Confirmation 是 2.1 核心项目的一部分，有正式发布和支持。但「**跨多个 Agent 等待人工**」的确认流转属于 Spring AI Agent 的规划范围，不在 2.1 核心能力里；需要时得等后续版本或自己在上层编排。

## 关联连接
- [[SpringAI]] — 所属框架（2.1 RC1 引入）
- [[摘要-spring-ai-2-1-苏三解读]] — 来源（苏三视角完整展开）
- [[摘要-spring-ai-2-1发布]] — 来源（锋哥版特性清单）
- [[ToolCalling]] — 工具调用机制总概念
- [[HITL]] — 人机协同上位概念（含人工把关可靠性实测）
- [[审批设计]] — 审批信息要素与失败即拒绝
- [[MCP协议]] — `forTools(...)` 覆盖的外部工具来源
- [[AgentRuntime]] — 该能力支撑「Spring AI 成为 Agent 运行时」的定位
