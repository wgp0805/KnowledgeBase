---
title: "AgentScope_Java"
type: entity
tags: [AI框架, 阿里, 通义, 生产级, 智能体, 分布式, 多租户]
sources: [raw/01-articles/JAVA中AI框架选型指南（2026）.md, raw/01-articles/AgentScopeJava2.0正式发布了！.md]
last_updated: 2026-06-23
---

## 定义
面向生产环境的智能体运行平台，阿里通义实验室出品。提供 ReAct 推理、Harness 工程化基础设施、多智能体编排与 MCP/A2A 协议支持。2.0 版本聚焦企业级生产场景，以"稳定运行、安全控制、灵活接入"为核心。

## 关键信息
- GitHub: `agentscope-ai/agentscope-java` | Stars: 3,457
- 框架中立 | Java 17+
- 最新版本：AgentScope Java 2.0 RC2（2026年6月发布）

### 1.0 核心能力
- **Harness 工程化** — 长期运行、复杂任务的工程底座
- **多智能体** — 子 Agent 声明 + agent_spawn/agent_send
- **Middleware** — onAgent/onReasoning/onActing/onModelCall 五层钩子
- **沙箱执行** — 本地/Docker/E2B 一行切换，快照恢复
- **工具与 MCP** — 注解驱动工具注册，统一 MCP 接入
- **Workspace 抽象** — 工作区即 Agent 人格+记忆+领域知识
- **自学习闭环** — Agent 自起草 Skill → 审核 → 后台整理

### 2.0 核心升级
- **分布式部署** — 会话状态、沙箱快照、工作区抽象全部可外置到 Redis/MySQL/OSS，K8s 环境下任意副本无状态恢复
- **多租户隔离** — RuntimeContext 穿透到工作区路径、存储命名空间和沙箱环境，框架层强制约束数据隔离
- **权限体系** — 允许/拒绝/确认三级管控，工具调用安全边界清晰
- **模型容错** — 自动重试 + 备用模型，长链路任务不中断
- **事件流** — 类型化事件流覆盖整个执行生命周期，每一步都可观察、可干预
- **Workspace 文件驱动** — AGENTS.md、MEMORY.md、subagents/*.md 都是普通文件，配置即代码
- **子Agent编排** — 声明式配置 + 动态委派，支持同步和后台两种模式

### Skill 支持（原生，多后端）
通过 **SkillRepository** 提供原生 Skill 支持，遵循 Agent Skills 规范。

两大来源：
1. **技能市场** — Git 仓库 / Nacos / MySQL / classpath / 自定义后端
2. **工作区** — `workspace/skills/` 共享 / `<userId>/skills/` 按用户隔离

自学习闭环：Agent 从执行中总结经验，自动起草 Skill，成功模式以 Markdown 技能形式自动沉淀到 `workspace/skills/`，跨会话共享。

### Agent 支持（完善）
HarnessAgent 提供 Middleware + Toolkit 两个扩展通道；子智能体支持同步阻塞与后台委派；多 Agent 协作支持 Pipeline、Broadcast、Sequential 等模式；A2A + MCP 跨进程编排与工具集成。

### 与 Spring AI Alibaba 的关系
Spring AI Alibaba 是阿里巴巴基于 Spring AI 打造的企业级 AI 应用开发框架，专为 Spring 技术栈设计。从发展趋势来看，Spring AI Alibaba 在后续版本中会将内核逐步升级为 AgentScope，两者生态打通后 Java 开发者将获得统一的体验。

## 关联连接
- [[AgentHarness]] — 工程化框架
- [[A2A]] — Agent 间通信
- [[MCP]] — 模型上下文协议
- [[Skill_Registry]] — 技能注册中心
- [[ReAct_Agent]] — Agent 模式
- [[ReActAgent]] — 核心推理循环 Agent
- [[HarnessAgent]] — 推荐入口 Agent
- [[Middleware]] — 中间件扩展机制
- [[分布式部署]] — 企业级部署能力
- [[多租户隔离]] — 企业级安全能力
- [[Workspace]] — 文件驱动架构
- [[事件流]] — 流式响应能力
- [[子Agent编排]] — 动态任务委派能力
- [[摘要-java-ai框架选型指南-2026]] — 来源
- [[摘要-AgentScopeJava2.0发布]] — 来源
- [[react-loop-explanation]] — ReAct 循环详解
- [[react-vs-plan-execute]] — ReAct vs Plan-and-Execute 对比分析
