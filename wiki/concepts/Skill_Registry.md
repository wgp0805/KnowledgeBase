---
title: "Skill Registry"
type: concept
tags: [AI, Agent, 技能管理, 注册中心]
sources: [raw/09-archive/JAVA中AI框架选型指南（2026）.md]
last_updated: 2026-06-08
---

## 定义
技能注册中心，管理和维护 AI Agent 技能（Skill）的生命周期——注册、发现、加载、更新。是 AI 框架中 Skill 系统的核心基础设施。

## 关键信息

### 各框架的实现
- **Spring AI Alibaba**（SkillRegistry）：管理所有 Skill 的元信息，配合 SkillsAgentHook 自动注入 `read_skill` 工具和技能列表到 System Prompt
- **Solon AI**（SkillRegistry）：支持优先级排序、按需动态加载、分布式 Remote Skills
- **AgentScope-Java**（SkillRepository）：多后端实现——Git 仓库、Nacos、MySQL、classpath、工作区文件

### 核心功能
- 渐进式披露：先注入技能列表（元信息），按需加载完整 SKILL.md
- 多后端支持：文件系统、Git、数据库、配置中心
- 与 Agent 深度绑定：通过 hooks 或 tools 自动注入 Agent

## 关联连接
- [[Skill]] — 被管理的对象
- [[SpringAI_Alibaba]] — SkillRegistry 实现
- [[SolonAI]] — SkillRegistry 实现
- [[AgentScope_Java]] — SkillRepository 实现
- [[渐进式披露]] — 底层设计原则
- [[摘要-java-ai框架选型指南-2026]] — 来源
