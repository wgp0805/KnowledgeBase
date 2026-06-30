---
title: "multi-agent-collaboration"
type: concept
tags: [AI, Agent, 协作模式, 全栈开发]
sources: [raw/01-articles/Java开发栈Skills全面指南.md, raw/01-articles/LangChain4j 和 LangGraph4j，哪个更好？.md]
last_updated: 2026-06-30
---

## 定义
多 Agent 协作模式是一种将复杂全栈项目拆分为多个专业化 Agent 角色的开发流程，每个 Agent 配备专属 Skill 负责特定领域，通过任务编排实现高效并行开发。

## 关键信息

### 典型角色分配
| Agent 角色 | 职责 | 推荐 Skill |
| :---: | :--- | :--- |
| 数据库架构师 | 数据库设计、迁移规划 | database-designer + migration-architect |
| 后端开发者 | Spring Boot + MyBatis + Redis 实现 | spring-boot-engineer + 自定义 MyBatis Skill |
| 前端开发者 | Vue/React + UI 组件库开发 | Patterns.dev React/Vue Skills + web-design-guidelines |
| 安全工程师 | 安全漏洞扫描 | security-hardening |
| DevOps 工程师 | CI/CD、部署 | ci-cd-pipeline-builder |

### 标准全栈工作流
1. **数据库设计阶段**：database-designer + migration-architect
2. **后端开发阶段**：Spring Boot Skills + MyBatis/Redis Skills
3. **前端开发阶段**：Vue/React Skills + Tailwind/设计指 Skills
4. **API 集成阶段**：api-design-principles
5. **测试阶段**：tdd-mastery + 前端测试 Skills
6. **部署阶段**：ci-cd-pipeline-builder

### 核心价值
- **专业化**：每个 Agent 聚焦单一领域，Skill 深度更高
- **并行化**：多个 Agent 可同时工作，缩短开发周期
- **标准化**：整体流程统一编排，输出质量可预期

## 关联连接
- [[摘要-java-stack-skills-guide]] — 来源
- [[Agent]] — 基础概念
- [[ai-agent-skill]] — 技能封装机制
- [[Skill]] — Agent 技能定义
- [[ClaudeCode]] — 多 Agent 调度平台
- [[LangGraph4j]] — Java 多 Agent 工作流编排框架
- [[Agent工作流编排]] — 状态图与多 Agent 流程编排方法论
- [[摘要-langchain4j-langgraph4j-comparison]] — LangGraph4j 多 Agent 模式来源
