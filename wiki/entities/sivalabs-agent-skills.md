---
title: "sivalabs-agent-skills"
type: entity
tags: [AI Skill, 业务技能封装, Spring AI, 企业级]
sources: [raw/01-articles/ClaudeCode写SpringBoot代码竟然这么野？这4个Skill让我彻底服了！.md]
last_updated: 2026-05-22
---

## 定义
Spring 社区布道师 Siva Prasad Reddy 出品的企业级技能库，提供统一的 Spring AI 技能封装规范，可将任意业务代码封装成 AI 可直接调用的原子技能。

## 关键信息

### 核心能力
- 统一的 AI 技能封装规范（AgentSkill 接口）
- 将业务代码封装成原子技能
- Claude 可通过自然语言直接调用接口
- 无需手动写控制器、接口路由

### 技能接口规范
```java
public interface AgentSkill {
    String skillName();
    String description();
    Object execute(Map<String, Object> params);
}
```

### 使用场景
- 手机号脱敏、数据格式化等原子操作
- 自然语言操控后端业务逻辑
- AI 驱动的后端开发

### 项目地址
https://github.com/sivaprasadreddy/sivalabs-agent-skills

## 关联连接
- [[ClaudeCode]] — 使用该技能的 AI 工具
- [[SpringBoot]] — 目标框架
- [[SpringAI]] — AI 集成框架
- [[dr-jskill]] — 配合使用的脚手架技能
- [[agent-skill-java-spring-framework]] — 配合使用的规范技能
- [[spring-testing-skills]] — 配合使用的测试技能
- [[摘要-claude-code-springboot-skills]] — 来源
