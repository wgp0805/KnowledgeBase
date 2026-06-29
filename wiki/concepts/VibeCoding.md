---
title: "VibeCoding"
type: concept
tags: [AI编程, 编程范式, 认知卸载, 开发流程]
sources: [raw/01-articles/连 Karpathy 都开始恐慌：AI 正在重新定义「程序员」｜ 硅基时间.md, https://v.douyin.com/U8iw9gPpXE0/]
last_updated: 2026-06-29
---

## 定义

**Vibe Coding** 是由 Andrej Karpathy 提出的 AI 辅助编程模式，指让 AI 模型随意编写代码，程序员不做深度审查，只是"祈祷测试能过"。这种模式下程序员处于"甩手掌柜"状态，容易导致**认知卸载**和编程能力退化。

## 关键信息

- **提出者**：Andrej Karpathy（OpenAI 联合创始人）
- **核心特征**：让模型随便写，然后祈祷测试能过
- **典型表现**：
  - 不深入理解代码逻辑
  - 依赖 AI 盲目试错
  - 把理解、调试等核心任务卸载给 AI
- **后果**：认知卸载，编程肌肉萎缩，最终**被替代**
- **对照组数据**：Anthropic 研究显示，AI 辅助组成绩比纯手写组低 17%，最依赖 AI 的人成绩最低

## 实战工作流（敲代码的小虾米）

抖音创作者 [[敲代码的小虾米]] 提出了一套系统化的 Vibe Coding 实战流程，强调在让 AI 写代码之前必须先"立好地基和规矩"：

### 前置四步（上篇）

1. **立项和功能清单** — 明确项目要做什么，拆分成具体功能，确保需求清晰。建议先与 AI（如 DeepSeek）讨论需求，让 AI 提问来帮助梳理思路。
2. **选技术栈** — 选择适合项目且 AI 熟悉的技术栈，避免过度选型，优先选择 AI 训练数据中常见的框架。
3. **搭项目架构** — 搭建项目骨架和目录结构，确定通用规则和代码规范。
4. **写 Agent 宪法** — 编写 AI Agent 的行为准则（Constitution），制定 AI 做事的具体规则，确保 AI 按既定规则行事不越界。这是 Vibe Coding 中最重要的纪律保障。

### 下篇要点

- **立真源** — 确立真实的数据源和依赖
- **落文档** — 将架构和规则落实到文档
- **敲代码** — 在充分准备后让 AI 生成代码

### 工具链建议

- **DeepSeek** — 用于需求讨论和初版需求文档生成
- **ChatGPT / Claude** — 用于完善需求文档和架构
- **Codex / Claude Code** — 用于将文档转化为详细项目文档和代码生成
- **Git** — 作为 Vibe Coding 中最实用的安全防线

### 核心理念

> 底稿要自己写，AI 写的要么曲解你的意思，要么乱来。
> 多跟 AI 沟通，把它当成协作伙伴而非黑盒工具。

## 与 Vibe Engineering 的对比

| 维度 | Vibe Coding | Vibe Engineering |
|------|-------------|------------------|
| 核心特征 | 让模型随便写，祈祷测试能过 | 对每一行代码负责，重度调度 Agent |
| 程序员角色 | 甩手掌柜 | Director（导演） |
| 结局 | 被替代——认知卸载，肌肉萎缩 | 被放大——成为 Director |
| 认知状态 | 卸载认知 | 加固认知 |

## 关联连接

- [[VibeEngineering]] — 与之对应的正确模式
- [[cognitive-offloading]] — Vibe Coding 导致的后果
- [[AndrejKarpathy]] — 概念提出者
- [[SimonWillison]] — 提出 Vibe Engineering 与之对应
- [[敲代码的小虾米]] — 实战工作流提出者
- [[Codex]] — 实战工具链中的 AI Agent
- [[ClaudeCode]] — 实战工具链中的 AI 编码工具
- [[DeepSeek]] — 实战工具链中的需求讨论工具
- [[Git]] — Vibe Coding 安全防线
- [[摘要-vibe-engineering-era]] — 来源
- [[摘要-vibe-coding-实战篇总结-上]] — 实战工作流来源
- [[AICoding]] — AI 辅助编程范式
