---
title: "LeeRobinson"
type: entity
tags: [人物, 工程师, Agent, PersonalAgent, 分享者]
sources:
  - raw/01-articles/2026-10-21-斯坦福新课直接讲 personal agent，Grok Bot 工程师分享如何打造出 always-on agent.md
last_updated: 2026-10-21
---

## 定义

Lee Robinson，Grok Bot 团队工程师，曾在 Cursor、现于 SpaceX。在斯坦福 CS146S 课程上做了一场关于 always-on agent 工程实现的分享，系统讲解了服务器、沙箱、记忆、动态工具发现、prompt caching、durable workflow 等生产级设计。

## 关键信息

### 分享的核心观点
- **开发者与 AI 的关系四阶段**：复制粘贴 → 模型能改文件跑命令 → 编程 Agent 有专门应用但人仍是瓶颈（每条命令都要审）→ **Agent 有自己的电脑、自己的记忆，能在工作中学新技能，你去睡觉了它还在干**
- **一切皆电脑**：不要为每一个能力发明一套新机制，而是把一切都落到文件、命令和一台真正的电脑上
- **delete the product（把产品删掉）**：认定今天的模型是它们这辈子最差的时候，六个月后可能要把界面整个重做；策略是为下一代模型而建，尽量少建、让界面足够简单，让模型自己去想、去做
- **auto review 比人更安全**：人要面对几百条 shell 命令会疲劳；做盲测多数时候是模型审得更好
- **能力阶梯**：先试最便宜最可靠的办法，一级一级往上爬，全失败才打扰用户

### 团队实践原则
- 推服务端更新比推 App Store 更新快得多；重计算放服务器；**所有东西都存服务器上，随时可以重建那台机器**
- 记忆分四层：核心事实 / 按日期的对话日志 / 半小时级草稿 / 其余放文件按需查
- 压缩本身「所有的压缩都会丢信息，怎么压得好，可能值好几篇博士论文」

### 被引用的外部观点
引用 OpenRouter 的 Alex 在 X 上的说法：现在每个应用看起来都一样（侧边栏、agent、对话框），但这就像 2005 年大家都在做一个服务器、一个数据库、一个增删改查的界面——**每个新产品都要有 agent 的一面，要么集成它，要么变成一份给别的 agent 使用的「无头数据」**。

## 关联连接

- [[GrokBot]] — 正在做的产品
- [[SpaceX]] — 现任公司
- [[Cursor]] — 曾任公司
- [[Firecracker]] — 承载 agent 的虚拟机
- [[Temporal]] — 采用的 durable workflow 实现
- [[DurableWorkflow]] — 提炼概念
- [[能力阶梯]] — 提炼概念
- [[ThinClientThickServer]] — 提炼概念
- [[动态工具发现]] — 提炼概念
- [[常驻智能体]] — 所属概念
- [[摘要-always-on-agent-斯坦福分享]] — 来源
