---
title: "摘要-superpowers-grill-me怎么选"
type: source
tags: [AI编程, Skill, grill-me, superpowers, 需求澄清]
sources: [raw/01-articles/面试官皱眉：你懂 Vibe Coding，那你说superpowers和grill-me怎么选？，我：小孩才做选择，我全都要！.md]
last_updated: 2026-08-05
---

## 核心摘要

本文回答了一个面试联想问题：AI 编程工具 **grill-me** 和 **superpowers** 应该怎么选？文章的核心观点是二者不是竞品，而是解决不同阶段的问题，应当配合使用。**grill-me** 定位为"编码前的需求澄清/设计追问"，让 AI 像面试官一样逐层追问，把需求/设计的每个分支都问清楚；**superpowers** 定位为"编码中的全流程开发方法论"。组合后的完整 AI 编程工作流是：grill-me（想清楚）→ superpowers brainstorming（补充细节）→ writing-plans（拆任务）→ tdd/subagent（执行）。

## 关键信息

### grill-me 是什么
- 出自 TypeScript 大神 **Matt Pocock**，是他开源的 `mattpocock/skills` 仓库中的一个 skill（GitHub 178k+ Star）
- 核心理念：在 AI 动手写代码之前，先像面试官一样追问用户，把需求/设计的每个分支都问清楚，直到关键决策点达成共识
- Skill 本体只有几行 prompt，关键在于最后一句 "provide your recommended answer"——每个问题都附上推荐答案，用户只需说"对"或纠正，对话效率极高

### grill-me vs superpowers 定位区别
| 工具 | 定位 | 介入时机 |
| --- | --- | --- |
| grill-me | 需求澄清 / 设计追问 | 编码前 |
| superpowers | 全流程开发方法论 | 编码中 |

### 与 superpowers brainstorming 的区别
- **grill-me**：轻量级压力测试，一问一答的面试式追问，快速收敛设计决策
- **superpowers brainstorming**：全流程头脑风暴，会生成视觉伴侣、架构图、数据模型等一整套产物

### 安装
```bash
npx skills@latest add mattpocock/skills
```
- 运行命令后可选择需要的 skill 安装，再选择安装到哪个 AI 代理编程工具（如 Claude Code），最后选择项目/全局范围，安装后输入 `/grill-me` 即可使用

### 效果对比
- 不用 grill-me：AI 可能直接做"全家桶"，80% 功能不需要，写两小时返工
- 用了 grill-me：14 轮追问、10 分钟对齐所有设计决策，AI 拿着明确共识去写代码，一次到位

### 组合工作流
```
grill-me（想清楚）→ superpowers brainstorming（补充细节）→ writing-plans（拆任务）→ tdd / subagent（执行）
```

## 关联连接
- [[GrillMe]] — 编码前的需求澄清 skill
- [[superpowers]] — 编码中的全流程方法论
- [[MattPocock]] — grill-me 作者，mattpocock/skills 创建者
- [[ClaudeCode]] — grill-me 的载体平台
- [[AICoding]] — AI 编码范式
- [[VibeCoding]] — 该文题眼
- [[TDD]] — 组合工作流中的执行环节
- [[brainstorming]] — superpowers 中与 grill-me 互补的 skill