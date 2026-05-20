---
title: "meta-skill"
type: concept
tags: [AI, Agent, 元技能, 技能扩展]
sources: [raw/02-papers/skill-creator使用与优化指南.pdf]
last_updated: 2026-05-20
---

## 定义
元技能（Meta-Skill）是一种关于技能的技能——即专门用于创建、管理和优化其他 AI 技能的高层级抽象工具。它不直接解决某个具体领域问题，而是提供一套方法论和流程来生成领域技能。

## 关键信息

### Meta-Skill 的设计理念
- **技能生成技能**：通过自然语言描述需求，自动产出结构化的技能文件
- **生命周期管理**：覆盖技能的创建→优化→测试→迭代全流程
- **人机协作**：AI 负责框架生成，人类负责边界条件和业务逻辑把关

### skill-creator 的实现方式
- 使用预定义的模板和提示工程框架
- 通过多轮对话逐步细化技能需求
- 自动生成 SKILL.md 核心文件及配套资源
- 支持优化模式进行增量改进

### 与普通 Skill 的区别
- **普通 Skill**：解决特定领域的任务（如代码审查、文档生成）
- **Meta-Skill**：不直接解决业务问题，而是提供"制造技能的工具"
- **类比**：普通 Skill 是产品，Meta-Skill 是生产产品的机器

## 关联连接
- [[SkillCreator]] — skill-creator 元技能工具
- [[Skill]] — 技能概念体系
- [[ClaudeCode]] — 元技能所属平台
- [[摘要-skill-creator-guide]] — 来源摘要
