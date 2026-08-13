---
title: "SpringAI_Alibaba"
type: entity
tags: [AI框架, 阿里, 多智能体, Java]
sources: [raw/09-archive/JAVA中AI框架选型指南（2026）.md, raw/01-articles/Spring AI 2.0 和 Spring AI Alibaba，哪个更好？.md]
last_updated: 2026-07-09
---

## 定义
阿里推出的独立 AI 框架项目（GitHub: `alibaba/spring-ai-alibaba`），专攻多智能体系统和工作流编排，深度集成 Spring AI 生态，核心运行在 Graph Runtime 上。

## 关键信息
- GitHub Stars: 10k+ | 1.0 GA 于 2026-05-13 | 版本: 1.1.2.0（2026-02）
- 框架依赖: Spring Boot | Java 17+
- 模型支持: 通义为主（多模型）
- 与 Spring Cloud Alibaba 无关（后者是微服务中间件）

### 定位与 Graph 引擎
- 定位：企业级编排运行时，类比 LangGraph；Spring AI 类比 JDBC（接入 AI），Alibaba 类比 Spring Cloud（编排多个 AI）
- Graph 引擎：低级别工作流和多代理协调框架，多智能体协作（ReAct Agent、Supervisor）、20+ 种标准组件（条件分支/并行处理/异常捕获）、流程快照（故障恢复）、记忆持久化（跨会话）、人工干预节点
- 1.1.2.0 新增：Agent Skills 支持、多智能体并行执行（AllOf/AnyOf 聚合策略）、异步工具执行与 returnDirect 增强

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
- [[摘要-spring-ai-2-vs-alibaba选型]] — Spring AI 2.0 vs Alibaba 选型
- [[LangGraph]] — 类比框架
- [[spring-ai-vs-langchain4j]] — 相关框架对比
