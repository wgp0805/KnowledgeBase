---
title: "GrillMe"
type: entity
tags: [Skill, 需求澄清, AI编程, mattpocock]
sources: [raw/01-articles/面试官皱眉：你懂 Vibe Coding，那你说superpowers和grill-me怎么选？，我：小孩才做选择，我全都要！.md]
last_updated: 2026-08-05
---

## 定义

**Grill-me** 是 Matt Pocock 开源的 `mattpocock/skills` 仓库中的一个 AI 编程 skill，定位是**编码前的需求澄清与设计追问工具**。它让 AI 像严格的面试官一样，对用户的计划进行结构化拆解、逐层追问每个设计分支，直到所有关键决策点都达成共识，从而避免"需求没对齐就开干"导致的返工。

## 关键信息

### 核心理念
- **介入时机**：编码之前（"动手前想清楚"）
- **工作方式**：一问一答的面试式压力测试，快速收敛设计决策
- **核心技巧**：每个问题都附上推荐答案（"provide your recommended answer"），用户只需回答"对"或纠正，对话效率极高

### Skill 本体（仅几行 prompt）
```yaml
name: grill-me
description: Interview the user relentlessly about a plan or design until reaching shared understanding, resolving each branch of the decision tree. Use when user wants to stress-test a plan, get grilled on their design, or mentions "grill me".
```
```text
Interview me relentlessly about every aspect of this plan until
we reach a shared understanding. Walk down each branch of the design
tree resolving dependencies between decisions one by one.

If a question can be answered by exploring the codebase, explore
the codebase instead.

For each question, provide your recommended answer.
```

### 适用场景
- 写 PRD 之前，先梳理清楚到底要做什么
- 让 AI 实现功能之前，先对齐设计决策
- 确定数据模型 / API 形状之前，先压力测试
- 多个设计决策相互依赖时，逐个解耦

### 安装与使用
```bash
npx skills@latest add mattpocock/skills
```
- 选择 grill-me skill → 选择安装载体（如 Claude Code）→ 选择项目/全局范围
- 使用：输入 `/grill-me 我想开发一个 Markdown 编辑器。` 即触发追问

### 效果
- 实测以 Markdown 编辑器为例：14 轮追问、约 10 分钟对齐所有设计决策
- 相比不用 grill-me（AI 直接做"全家桶"返工），使用后一次到位

### 与 superpowers 的关系
- **grill-me**（轻量压力测试）≠ **superpowers brainstorming**（全流程头脑风暴，生成视觉伴侣/架构图/数据模型等完整产物）
- 两者可串联：先用 grill-me 快速收敛核心决策，再用 superpowers 展开详细设计

## 知识冲突（已记录-待决策）
> **状态**：两种说法并存，用户选取规划起点时需注意作者最新推荐。如需统一，可将本文推荐降级为"备选 skill"。
- [[MattPocock]] 页面（2026-07 来源）记载作者已把 `/grill-me` 从默认推荐位移除，转而推荐 `/domain-model` 作为规划起点；2026-08 本文仍将 grill-me 作为编码前需求澄清的首选 skill 进行推荐。两者不矛盾——前者讲作者对自家 skill 编排的调整，后者讲 grill-me 相对 [[Superpowers]] 的定位差异，但用户在选取规划起点时需注意作者的最新推荐。

## 关联连接
- [[摘要-superpowers-grill-me怎么选]] — 来源
- [[MattPocock]] — 作者
- [[Superpowers]] — 编码中的互补工具
- [[ClaudeCode]] — 常用载体平台
- [[AICoding]] — AI 编码范式
- [[brainstorming]] — superpowers 中的同类但更重量的 skill
- [[TDD]] — 组合工作流中的执行环节