---
title: "Skill"
type: concept
tags: [AI, Agent, 技能扩展]
sources: [raw/01-articles/40分钟学会Codex！"零基础"终级教程～【附完整文档】.md, raw/01-articles/全网最全！60分钟全面掌握Claude Code~【附完整文档】.md, raw/01-articles/6条Claude Code实践中的经验与思考.md]
last_updated: 2026-05-19
---

## 定义
Agent 的技能包，是人为沉淀的可复用方法、流程和工具组合，相当于 Agent 做某类具体任务的行动指南/操作手册。

## 关键信息

### 四类 Skill
1. **领域知识型**：专业领域的最佳实践和知识
2. **工作流型**：标准化的操作流程
3. **工具组合型**：多工具协同使用的模式
4. **最佳实践型**：编码规范、设计模式等

### Thariq 的 9 类分类法（Anthropic 内部经验）
1. **知识/参考类**：告诉 Claude 如何正确使用内部库、CLI 或 SDK
2. **验证类**：描述如何测试或验证代码是否正确
3. **数据访问类**：连接数据和监控系统
4. **自动化工作流类**：把重复操作压缩成一条命令
5. **脚手架类**：为代码库的特定模块生成框架样板
6. **代码审查类**：执行代码质量检查
7. **部署类**：拉取、推送、部署代码
8. **调试类**：接收症状，走多工具调查流程，输出结构化排查报告
9. **运维类**：执行例行维护和操作流程

### 设计理念
- 渐进式披露：只发元信息（名称+何时调用），Agent 按需读取完整内容
- 不占满上下文，比写进 CLAUDE.md/agents.md 更灵活
- 安装方式：放入对应 skills 文件夹

### 为什么重要
- 大模型不可能把所有领域最佳实践塞进训练数据
- Skill 把专业知识变成 Agent 按需调用的"外接大脑"
- 工业标准化规避模型幻觉，优秀 Skill 集成大量开发者经验
- 能用 Skill 尽量用，比自己用模糊语言描述效果好得多

### 创建方式
1. 直接跟 Agent 讨论打磨
2. 先跑通流程再沉淀成 Skill（推荐）
3. 用 skill creator 工具辅助创建

## 关联连接
- [[Agent]] — Skill 所属概念
- [[ClaudeCode]] — Skill 发明者
- [[Codex]] — Skill 支持
- [[SkillCreator]] — 元技能创建工具
- [[meta-skill]] — 元技能概念
- [[Thariq]] — 9 类分类法提出者
- [[AICoding]] — AI 编程实践
- [[摘要-anthropic-engineer-skills]] — 9 类分类法来源
- [[spring-skill-usage-guide]] — Spring Skill 使用时机与组合策略
