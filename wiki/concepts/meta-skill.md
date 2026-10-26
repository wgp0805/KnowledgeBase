---
title: "meta-skill"
type: concept
tags: [AI, Agent, 元技能, 技能扩展]
sources: [raw/09-archive/skill-creator使用与优化指南.pdf, "raw/09-archive/2026-10-23-腾讯司内实践：手把手教你如何用 Skill 与 AI 协作.md"]
last_updated: 2026-10-26
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

### OpenClaw.NET MetaSKILL（声明式 DAG 编排）
OpenClaw.NET 的 MetaSKILL 是一种基于 YAML 声明式 DAG 的元技能编排引擎，与 Claude Code 的 skill-creator 元技能不同，它专注于工作流编排而非技能生成：

- **设计范式**：声明即编排（Declaration-as-Orchestration）
- **核心原语**：7 种步骤类型（llm_chat、agent、fan_out、skill_exec、user_input、route 等）
- **安全体系**：三步门禁（tool_allowlist + capabilities + MetaSkill.Enabled）+ 4 层超时保护
- **审计能力**：持久化审计记录 + CLI replay/reconstruct
- **双运行时**：AgentRuntime + MafAgentRuntime
- **与 Claude Code Workflows 的关系**：覆盖编排光谱两端，Workflows 灵活适合探索，MetaSKILL 安全适合生产

### 场景族生成器（Balance 三生成器，2026-10-23）
Balance Li 的 Learning/Design/Build 三生成器（[[BalanceSkillCreators]]，已上线腾讯司内市场）是 meta-skill 的新形态样本——与 skill-creator"对话式创建任意单个技能"不同，它们是**面向高频工作场景族**的生成器：

- **每类场景一个生成器**：Learning（系统学习）、Design（产品设计）、Build（构建与验证），同一套方法适配不同任务（学 SQL 和学英语的目标、内容、练习方式都不同）
- **生成专属子 Skill**：先澄清用户需求（主题/目标/基础/时间/偏好），再生成含项目背景、流程与保存规则的子 Skill（示例 learn_rag_review），子 Skill 按项目进展引导下一步并把进度与重要决定保存到项目文件
- **人工选择、不自动串联**：三生成器可配合使用，但需按任务选择、不会自动依次运行（与 Skill 体系中"User-invoked 之间互不调用"的铁律同向）
- **方法论落点**：这把 meta-skill 从"单次生成工具"推进为"方法固化 + 按需实例化"的生成器工厂模式，其 Learning 生成器落实为 [[学习闭环五步法]]

## 关联连接
- [[SkillCreator]] — skill-creator 元技能工具
- [[Skill]] — 技能概念体系
- [[ClaudeCode]] — 元技能所属平台
- [[摘要-skill-creator-guide]] — 来源摘要
- [[OpenClaw]] — MetaSKILL 所属项目
- [[dynamic-workflow]] — 动态工作流概念（代码编排）
- [[摘要-Claude-Code-Workflows-vs-MetaSKILL]] — 来源
- [[BalanceSkillCreators]] — 场景族生成器实体（腾讯司内实践）
- [[摘要-腾讯skill协作balance-li]] — 来源（生成器工厂模式）
