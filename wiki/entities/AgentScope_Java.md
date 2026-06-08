---
title: "AgentScope_Java"
type: entity
tags: [AI框架, 阿里, 通义, 生产级, 智能体]
sources: [raw/01-articles/JAVA中AI框架选型指南（2026）.md]
last_updated: 2026-06-08
---

## 定义
面向生产环境的智能体运行平台，阿里通义实验室出品。提供 ReAct 推理、Harness 工程化基础设施、多智能体编排与 MCP/A2A 协议支持。

## 关键信息
- GitHub: `agentscope-ai/agentscope-java` | Stars: 3,457
- 框架中立 | Java 17+

### 核心能力
- **Harness 工程化** — 长期运行、复杂任务的工程底座
- **多智能体** — 子 Agent 声明 + agent_spawn/agent_send
- **Middleware** — onAgent/onReasoning/onActing/onModelCall 五层钩子
- **沙箱执行** — 本地/Docker/E2B 一行切换，快照恢复
- **工具与 MCP** — 注解驱动工具注册，统一 MCP 接入
- **Workspace 抽象** — 工作区即 Agent 人格+记忆+领域知识
- **自学习闭环** — Agent 自起草 Skill → 审核 → 后台整理

### Skill 支持（原生，多后端）
通过 **SkillRepository** 提供原生 Skill 支持，遵循 Agent Skills 规范。

两大来源：
1. **技能市场** — Git 仓库 / Nacos / MySQL / classpath / 自定义后端
2. **工作区** — `workspace/skills/` 共享 / `<userId>/skills/` 按用户隔离

自学习闭环：Agent 从执行中总结经验，自动起草 Skill，成功模式以 Markdown 技能形式自动沉淀到 `workspace/skills/`，跨会话共享。

### Agent 支持（完善）
HarnessAgent 提供 Middleware + Toolkit 两个扩展通道；子智能体支持同步阻塞与后台委派；多 Agent 协作支持 Pipeline、Broadcast、Sequential 等模式；A2A + MCP 跨进程编排与工具集成。

## 关联连接
- [[AgentHarness]] — 工程化框架
- [[A2A]] — Agent 间通信
- [[MCP]] — 模型上下文协议
- [[Skill_Registry]] — 技能注册中心
- [[ReAct_Agent]] — Agent 模式
- [[摘要-java-ai框架选型指南-2026]] — 来源
