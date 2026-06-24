---
title: "Middleware"
type: concept
tags: [AI概念, 扩展机制, 钩子]
sources: [raw/01-articles/AgentScopeJava2.0正式发布了！.md]
last_updated: 2026-06-23
---

## 定义
Middleware 是 AgentScope Java 2.0 中的中间件扩展机制，全面取代了 1.x 的 Hook 接口。它提供了 5 个钩子位置，可以在 ReAct 循环的关键时机插入自定义逻辑。

## 关键信息
- **5个钩子位置**：
  - onAgent — Agent 初始化前，设置日志上下文、绑定租户信息、初始化链路追踪
  - onReasoning — LLM 推理前，在 Prompt 中注入当前工作区文件、做 Token 预算检查
  - onActing — 工具调用前，执行权限检查、参数校验、记录审计日志
  - onModelCall — 模型调用后，处理响应缓存、触发重试/降级策略
  - onSystemPrompt — 系统提示词构建时，动态追加时效性信息、替换占位符
- **设计优势**：
  - 职责单一性 — 每个 Middleware 只负责一件事，通过 priority 排序，互不干扰
  - 零主动调用 — 只要注册到框架中，就自动生效
  - 确定性 + 灵活性 — 保证核心循环可控，同时提供能力按需叠加
  - 可测试性 — 每个 Middleware 可以独立 Mock 测试

## 关联连接
- [[AgentScope_Java]] — 所属框架
- [[HarnessAgent]] — 使用 Middleware 的 Agent
- [[摘要-AgentScopeJava2.0发布]] — 来源
