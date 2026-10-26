---
title: "MattPocock"
type: entity
tags: [TypeScript, 教育, Skill, 开源]
sources: [raw/09-archive/Matt Pocock 那个 5 个月冲到 17 万 star 的 grill-me，作者自己却不用了，原因是这几个.md, raw/09-archive/面试官皱眉：你懂 Vibe Coding，那你说superpowers和grill-me怎么选？，我：小孩才做选择，我全都要！.md, raw/09-archive/强模型时代，删掉SuperpowersAI编程工作流到底该怎么选.md, raw/01-articles/2026-10-21:开源「提示语管理.skill」，就为快速选出最适合你的Prompt（附25个深度思考提示语）.md]
last_updated: 2026-10-21
---

## 定义

Matt Pocock 是 Total TypeScript 的作者，TypeScript 教育领域的知名人物，同时也是 `mattpocock/skills` 仓库的创建者——一个 5 个月冲到 17 万 star 的 AI 编码 skill 集合。他运营着 [aihero.dev](https://aihero.dev) 社区，newsletter 约有 6 万开发者订阅。

## 关键信息

### 代表作品
- **mattpocock/skills**：GitHub 17 万+ star 的 AI 编码 skill 仓库，设计哲学是"把 skill 当纪律，不当框架"
- **Total TypeScript**：TypeScript 教育课程品牌
- **aihero.dev**：AI 编码技能社区 & newsletter（6 万订阅者）

### 核心观点
- Skill 是"随时该被替换、被 hack、被组合的一次性纪律"，不是供起来的框架
- 反对 GSD、BMAD、Spec-Kit 等"接管流程"的重量级框架，认为它们让用户失去控制权
- 主张 User-invoked（编排层）与 Model-invoked（纪律层）的两层调用架构，编排层之间互不调用
- 自己撤下最火的 `/grill-me` skill 从默认推荐位，转而推荐 `/domain-model` 作为规划起点
- 但于 2026-08 的对比文章中仍未改动 grill-me 作为编码前需求澄清 skill 的核心价值（详见 [[GrillMe]]）

### 设计哲学
1. **小（Small）**：每个 skill 职责单一
2. **可改（Easy to adapt）**：允许用户修改定制
3. **可组合（Composable）**：skill 之间可自由组合
4. **跨模型（Work with any model）**：不绑定特定 AI 模型
5. **基于工程基础（Based on decades of engineering experience）**：引用 The Pragmatic Programmer、DDD（Eric Evans）、XP（Kent Beck）、软件设计哲学（Ousterhout）等经典

### ask-matt 路由（2026-10，被广泛模仿）
除 `grill-me` 外，仓库里还有一个 **`ask-matt` 路由** skill。它的价值在于：**你不需要知道仓库里有多少个 skill、也不需要记住哪个叫什么名字，只要跟它说「我现在遇到了什么情况」，它就会帮你挑出合适的 skill。**

作者实测：描述「我有个 AI 提示语合集网站 goodcase，里面放了 1000 多个视频，视频的存储优化的想法还比较模糊，不确定该怎么推进」，ask-matt 回答应该先用 `grilling` 把想法问清楚、每个分支问到底，再用 `to-spec` 收成规格书做成开发计划——**不光告诉你用哪个，还告诉你为什么不是另一个，以及跑完之后接哪个**。

> 这一形态后来被 [[Laoyeye]]（老爷爷提示语路由）复刻，成为「提示语存了一堆但从来不用」的标准解法，详见 [[提示语路由]]。

### 强模型时代的优势

[[摘要-强模型时代删掉Superpowers该怎么选]] 指出，在 GPT-5.6、Kimi K3、Fable-5 等强模型时代，Matt Skills 的轻量可组合特性使其成为大多数日常开发场景的优选：

- **避免流程税**：不强制全套流程，简单任务可直接用模型原生能力，按需调用 grill-with-docs / to-spec / to-tickets / implement
- **保留人的主导权**：开发者自掌流程控制权，需要时才启用对应模块
- **适配强模型**：利用模型原生规划/自测/评审能力，Skills 当工具零件按需调用而非强制流水线
- **典型用法**：需求模糊调用 `grill-with-docs`；要写规格调用 `to-spec`；简单改动直接让模型原生执行

详见 [[强模型时代工作流选型]]。

## 关联连接
- [[摘要-mattpocock-skills]] — 来源
- [[GrillMe]] — mattpocock/skills 中的经典需求澄清 skill
- [[Skill]] — Skill 概念体系
- [[AICoding]] — AI 编码范式
- [[GSDCore]] — GSD 框架（对比对象）
- [[SpecKit]] — Spec-Kit 框架（对比对象）
- [[TDD]] — 测试驱动开发实践
- [[摘要-强模型时代删掉Superpowers该怎么选]] — 来源（强模型时代定位）
- [[Laoyeye]] — 复刻其 ask-matt 路由形态的提示语路由 skill
- [[提示语路由]] — 该形态提炼出的概念
- [[流程税]] — Matt Skills 规避的成本概念
- [[强模型时代工作流选型]] — 选型方法论
- [[matt-skills-boundary-judgment]] — Matt Skills 适用边界与跳步判断实操