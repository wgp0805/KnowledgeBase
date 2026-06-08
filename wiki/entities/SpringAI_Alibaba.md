---
title: "SpringAI_Alibaba"
type: entity
tags: [AI框架, 阿里, 多智能体, Java]
sources: [raw/01-articles/JAVA中AI框架选型指南（2026）.md]
last_updated: 2026-06-08
---

## 定义
阿里推出的独立 AI 框架项目（GitHub: `alibaba/spring-ai-alibaba`），专攻多智能体系统和工作流编排，深度集成 Spring AI 生态，核心运行在 Graph Runtime 上。

## 关键信息
- GitHub Stars: 9,871 | 版本: 1.1.2.0
- 框架依赖: Spring Boot | Java 17+
- 模型支持: 通义为主（多模型）
- 与 Spring Cloud Alibaba 无关（后者是微服务中间件）

### Agent 支持（完善）
- **单 Agent（ReactAgent）**：ReAct 范式，思考→行动→观察循环
- **多 Agent 工作流**：SequentialAgent（链式）、ParallelAgent（并行）、LlmRoutingAgent（LLM 路由分发）、LoopAgent（循环迭代）
- **Graph Core**：DAG 工作流 + 条件路由 + 状态管理 + PlantUML/Mermaid 可视化
- **A2A（Agent-to-Agent）**：通过 Nacos 实现分布式 Agent 间通信

### Skill 支持（原生）
通过 **SkillRegistry + SkillsAgentHook** 提供原生 Skill 支持，遵循 Agent Skills 规范：
- SkillRegistry：技能注册中心，管理所有 Skill 的元信息
- SkillsAgentHook：Agent 钩子，自动注入 `read_skill` 工具和技能列表到 System Prompt
- FileSystemSkillRegistry：从本地文件系统加载 Skill 目录
- 渐进式披露：先注入技能列表（name, description, skillPath），按需加载完整 SKILL.md

### RAG 支持
内置 RAG 支持，集成 DashScope 通义模型实现检索增强生成。

## 关联连接
- [[SpringAI]] — 兼容的 Spring AI 生态
- [[DashScope]] — 底层模型 API
- [[ReAct_Agent]] — Agent 模式
- [[A2A]] — Agent 间通信协议
- [[Skill_Registry]] — 技能注册中心
- [[摘要-java-ai框架选型指南-2026]] — 来源
