---
title: "agent-skill-java-spring-framework"
type: entity
tags: [AI Skill, Spring Framework, 编码规范, Spring 7]
sources: [raw/01-articles/ClaudeCode写SpringBoot代码竟然这么野？这4个Skill让我彻底服了！.md]
last_updated: 2026-05-22
---

## 定义
强制 Claude Code 遵循 Spring Framework 7 最新编码规范的技能，确保生成的代码使用最新技术栈，杜绝老旧 API。

## 关键信息

### 核心能力
- 摒弃 RestTemplate，统一使用 RestClient、JdbcClient
- 彻底淘汰 javax，全程 jakarta EE11 规范
- 适配 Java 25 结构化并发、虚拟线程新特性
- 自带 Spring Security 7、Keycloak、OAuth2 最新适配方案

### 规范约束
- 使用 Spring 官方推荐的 RestClient 替代 RestTemplate
- 使用 jakarta 包替代 javax 包
- 适配 Java 25 新特性

### 项目地址
https://github.com/AyrtonAldayr/agent-skill-java-spring-framework

## 关联连接
- [[ClaudeCode]] — 使用该技能的 AI 工具
- [[Spring]] — 目标框架
- [[SpringBoot]] — 目标框架
- [[RestClient]] — 推荐 HTTP 客户端
- [[dr-jskill]] — 配合使用的脚手架技能
- [[sivalabs-agent-skills]] — 配合使用的业务技能
- [[spring-testing-skills]] — 配合使用的测试技能
- [[摘要-claude-code-springboot-skills]] — 来源
