---
title: "子Agent编排"
type: concept
tags: [AI概念, 多智能体, 任务委派]
sources: [raw/09-archive/AgentScopeJava2.0正式发布了！.md, raw/09-archive/AgentScope入门指南.md]
last_updated: 2026-07-22
---

## 定义
子Agent编排是 AgentScope Java 2.0 的多智能体协作机制，一个智能体（主 Agent）可以"委派"任务给另一个智能体（子 Agent），并在子 Agent 完成任务后接收结果。这种模式比静态的 Pipeline 更灵活，因为子 Agent 可以在运行时动态创建和销毁，任务的委派链也是动态决定的。

## 关键信息
- **声明式子Agent配置** — 在 workspace/subagents/<id>.md 中定义子 Agent 的名称、描述和提示词
- **动态创建** — 主 Agent 通过内置的 agent_spawn 工具动态创建子 Agent
- **两种委派模式**：
  - 同步委派 — 设置 timeout_seconds > 0，主 Agent 等待子 Agent 完成后再继续
  - 后台委派 — 设置 timeout_seconds = 0，子 Agent 异步执行，完成后自动反向通知
- **历史演进** — 1.x 中的 Pipeline 和 MsgHub 模块已在 2.0 中移除，取而代之的是更强大的子 Agent 系统

### 两种定义方式
1. **文件驱动**：在 `workspace/subagents/*.md` 中声明 `id`/`description`/`sysPrompt`，主 Agent 全凭 `description` 决定是否 spawn
2. **Java API 补强**：用 `SubagentDeclaration.builder().name().description().inlineAgentsBody()` 在代码中定义，支持注入 toolkit

### orchestrator + workers 模式
2.0 核心理念：主 Agent 扮演"主持人"，子 Agent 扮演"参与者"。主 Agent 负责接收用户任务、拆解委派、汇总结果。整个编排过程由 LLM 自主决定，不需要开发者写死 Pipeline。

### 实战示例
旅行助手场景（用户问"明天从北京飞杭州，落地后去西湖，要带伞吗？"）：
- 主 Agent 自主决定先查天气还是航班
- 三个 SubAgent（weather/flight/attraction）可并行启动
- 通过文件驱动定义，Java 端可补强真实 API 工具

## 关联连接
- [[AgentScope_Java]] — 所属框架
- [[HarnessAgent]] — 支持子 Agent 的 Agent
- [[Workspace]] — 子 Agent 声明位置
- [[摘要-AgentScopeJava2.0发布]] — 来源
- [[摘要-AgentScope入门指南]] — 来源（苏三入门实战指南）
