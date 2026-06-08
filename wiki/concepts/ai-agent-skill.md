---
title: "AI Agent Skill"
type: concept
tags: [AI, Agent, 技能封装, Claude Code]
sources: [raw/01-articles/ClaudeCode写SpringBoot代码竟然这么野？这4个Skill让我彻底服了！.md, raw/01-articles/Java开发栈Skills全面指南.md, raw/01-articles/JAVA中AI框架选型指南（2026）.md]
last_updated: 2026-06-08
---

## 定义
AI Agent Skill 是一种可扩展的技能包机制，允许为 AI Agent（如 Claude Code）注入领域专业知识、工作流、工具组合和最佳实践，从而提升 AI 在特定领域的专业能力。

## 关键信息

### 四种类型
1. **领域知识**：特定领域的专业知识和规范
2. **工作流**：标准化的工作流程和步骤
3. **工具组合**：多个工具的协同使用方式
4. **最佳实践**：经过验证的最佳实践方案

### 核心价值
- **上限决定论**：AI 工具的上限完全取决于装了什么 Skill
- **专业化转型**：搭载专属 Skill 后，AI 从"代码搬运工"升级为"资深架构师"
- **标准化输出**：确保生成的代码符合行业规范和最佳实践

### Spring 生态 Skill 实例
- [[dr-jskill]]：企业级项目脚手架技能
- [[agent-skill-java-spring-framework]]：Spring 最新规范约束技能
- [[sivalabs-agent-skills]]：企业级业务技能库
- [[spring-testing-skills]]：智能化测试技能

### 应用场景
- 企业级项目生成
- 编码规范约束
- 业务逻辑封装
- 自动化测试生成
- 代码重构优化

### 多 Agent 协作开发模式
复杂全栈项目可拆分多个专业化 Agent 角色，每个配备专属 Skill：

| Agent 角色 | 职责 | 推荐 Skill |
| :---: | :--- | :--- |
| 数据库架构师 | 数据库设计、迁移规划 | database-designer + migration-architect |
| 后端开发者 | Spring Boot + MyBatis + Redis | spring-boot-engineer + 自定义 Skill |
| 前端开发者 | Vue/React + UI 组件库 | Patterns.dev Skills + web-design-guidelines |
| 安全工程师 | 安全漏洞扫描 | security-hardening |
| DevOps 工程师 | CI/CD、部署 | ci-cd-pipeline-builder |

### 自定义 Skill 开发
可以为项目编写自定义 Skill，例如：
- **MyBatis-Plus Skill**：封装 Mapper 规范、Service 层、分页配置、LambdaQueryWrapper
- **Redis 项目 Skill**：封装 Key 命名规范、Spring Data Redis + Lettuce 配置、Redisson 分布式锁

## 关联连接
- [[ClaudeCode]] — 支持 Skill 的 AI 工具
- [[Agent]] — 核心概念
- [[SpringBoot]] — 应用框架领域
- [[dr-jskill]] — 实例
- [[agent-skill-java-spring-framework]] — 实例
- [[sivalabs-agent-skills]] — 实例
- [[spring-testing-skills]] — 实例
- [[multi-agent-collaboration]] — 多 Agent 协作模式
- [[Skill]] — 技能扩展机制
- [[Summary-java-stack-skills-guide]] — 来源
- [[摘要-claude-code-springboot-skills]] — 来源
- [[摘要-java-ai框架选型指南-2026]] — 来源

### Java AI 框架对比简表
| 框架 | 原生 Skill | SKILL.md | Skill 后端 | 特色 |
|:---:|:---:|:---:|:---:|:---|
| Solon AI | ✅ | ✅ | 本地/Remote | 20个预置技能、CliSkill/RestApiSkill/ToolGatewaySkill/Text2SqlSkill |
| LangChain4j | ✅ | ✅ | 文件系统 | Tool Mode / Shell Mode 双模式 |
| Spring AI Alibaba | ✅ | ✅ | 文件系统 | SkillRegistry + SkillsAgentHook |
| AgentScope-Java | ✅ | ✅ | Git/Nacos/MySQL/文件 | 自学习闭环、多后端切换 |
| Spring AI | ❌ | — | 仅 Tool Callback | — |
