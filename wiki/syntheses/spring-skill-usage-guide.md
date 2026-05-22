---
title: "spring-skill-usage-guide"
type: synthesis
tags: [Spring Boot, AI Skill, Claude Code, 最佳实践]
sources: [摘要-claude-code-springboot-skills]
last_updated: 2026-05-22
---

# Spring Skill 使用时机指南

## 4个 Spring Skill 使用时机

### 1. [[dr-jskill]] — 项目启动阶段

**时机**：创建新项目时一次性使用

**作用**：生成对标 [[JHipster]] 的生产级 [[SpringBoot]] 完整项目骨架，集成 PostgreSQL、Docker、监控、多前端架构

**触发指令**：
> 基于dr-jskill规范，创建一个生产级SpringBoot4后台项目，集成PostgreSQL、Docker、监控链路、Vue前端

---

### 2. [[agent-skill-java-spring-framework]] — 日常编码全程

**时机**：写任何 [[Spring]] 代码时持续生效

**作用**：强制 AI 遵循 Spring 7 / Boot 4 最新规范，杜绝老旧 API（如 RestTemplate、javax 包）

**核心约束**：
- RestClient 替代 RestTemplate
- jakarta 替代 javax
- 适配 Java 25 虚拟线程、结构化并发

---

### 3. [[sivalabs-agent-skills]] — 业务封装阶段

**时机**：需要将业务逻辑封装成 AI 可调用的原子技能时

**作用**：提供统一的 AgentSkill 接口规范，让 [[ClaudeCode]] 通过自然语言直接调用后端业务

**适用场景**：手机号脱敏、数据格式化、业务规则校验等原子操作

---

### 4. [[spring-testing-skills]] — 测试阶段

**时机**：业务代码完成后，生成测试用例时

**作用**：自动生成 @WebMvcTest / @DataJpaTest / @WebFluxTest 全套测试，覆盖正常、异常、边界场景

---

## 最佳组合策略

| 阶段 | 使用的 Skill | 产出 |
|------|-------------|------|
| 项目初始化 | [[dr-jskill]] | 完整项目骨架 |
| 业务开发 | [[agent-skill-java-spring-framework]] | 规范代码 |
| 技能封装 | [[sivalabs-agent-skills]] | AI 可调用接口 |
| 测试覆盖 | [[spring-testing-skills]] | 全套测试用例 |
| 代码重构 | 四者联动 | 校验+事务+异常+规范全方位优化 |

## 关联连接
- [[dr-jskill]] — 企业级项目脚手架技能
- [[agent-skill-java-spring-framework]] — Spring 最新规范约束技能
- [[sivalabs-agent-skills]] — 企业级业务技能库
- [[spring-testing-skills]] — 智能化测试技能
- [[ClaudeCode]] — 使用这些技能的 AI 工具
- [[ai-agent-skill]] — 技能扩展机制
- [[摘要-claude-code-springboot-skills]] — 来源
