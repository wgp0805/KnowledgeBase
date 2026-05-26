---
title: "VibeEngineering"
type: concept
tags: [AI编程, 编程范式, Agent调度, 工程实践]
sources: [raw/01-articles/连 Karpathy 都开始恐慌：AI 正在重新定义「程序员」｜ 硅基时间.md]
last_updated: 2026-05-26
---

## 定义

**Vibe Engineering** 是由 Simon Willison 提出的 AI 辅助编程模式，核心理念是：**对每一行代码负责，但在规划、架构、调试、文档每个环节都重度调度 Agent**。这是 Vibe Coding 的对立面，是从"被替代"到"被放大"的分水岭。

## 关键信息

- **提出者**：Simon Willison（Django 联合创始人）
- **核心理念**：要用 AI 构建，也要保持人类的责任
- **程序员角色**：从"写代码的人"转变为"Director（导演）"——给 Agent 派任务、审产出
- **关键能力**：
  - 设计与品味（taste）
  - 判断力（discernment）
  - 清晰的沟通
  - 产出让人类愿意读的东西
- **实践模式**：
  - **Best of N**：给 Codex 一个任务，它并行尝试 4 种方案，工程师挑选最顺眼的继续
  - **7 小时 500 行**：大部分时间花在测试和验证上，最后只产出 500 行高质量 diff
  - **代码审查**：所有 PR 由 Codex 审核，拦下过会冲进生产环境的复杂 bug

## OpenAI 内部实践数据

- 工程师对 Codex 采用率超过 92%
- 所有内部 PR 都由 Codex 审核
- 用 Codex 的工程师产出的合并 PR 比不用的人多 70%
- Kotlin 重写 Rust 任务单次成功率超过 75%

## 防止认知卸载的三个做法

1. **代码可以不写，但必须读得懂** —— 读是新的写
2. **看到不懂的就追问到底** —— 判断力在"追问 AI"中练出来
3. **不脱离一线** —— OpenAI HR 负责人主动退一步当四个月实习生

## 关联连接

- [[VibeCoding]] — 与之对应的错误模式
- [[cognitive-offloading]] — Vibe Engineering 要解决的问题
- [[SimonWillison]] — 概念提出者
- [[RomainHuet]] — OpenAI 内部分享者
- [[AaronFriel]] — OpenAI 内部分享者
- [[Codex]] — Vibe Engineering 的核心工具
- [[OpenAI]] — 内部实践来源
- [[摘要-vibe-engineering-era]] — 来源
- [[AICoding]] — AI 辅助编程范式
