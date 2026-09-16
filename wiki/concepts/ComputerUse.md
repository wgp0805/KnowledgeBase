---
title: "ComputerUse"
type: concept
tags: ["Codex", "Computer-Use", "OpenAI", "AGI"]
sources:
  - raw/01-articles/2026-09-15-OpenAI 总裁最新采访：现在所有人对 AI 的预测，大概率都是错的.md
last_updated: 2026-09-15
---

## 定义
Computer Use 是让 AI Agent 直接操作电脑界面（用鼠标、键盘、截图的方式来完成任务），就像一个真实的人坐在电脑前操作一样的能力。是 GPT-6 Astra 时代的核心跃升点，也是 Greg Brockman 判断"AGI 时代已经到来"的关键依据。

## 关键信息

### Astra 时代 Computer Use 的意义
- **Agent 能否用的两点**：模型够不够聪明去使用工具 + 能不能访问到需要的上下文
- **传统做法**（建 API/MCP server/CLI 接口）本质是给 AI 打补丁——把软件改造成 AI 勉强能用的格式，又麻烦又别扭，而且会引入额外的安全风险（多一层接口多一层可能被攻击的面）
- **Computer Use 完全不同**：让 AI 直接用人类界面操作软件，不需要任何特殊 API、不需要重新设计任何系统
- **方向上的根本转变**：以前是人类改变自己去适应软件，然后我们又在改造软件去适应 AI，但现在 AI 终于可以直接用人类用的那套界面了
- **不依赖任何中间层**：从长远看这条路会走得更远

### 2015-11 OpenAI 内部会议
OpenAI 早在 2015 年 11 月的一次内部会议上就讨论过这个想法——**"如果强化学习的环境是屏幕像素加上键鼠输入，那是不是任何可以在电脑上做的事都能成为训练任务？"** 当时有过早期尝试，但一直到现在才真正实现。

### 与 Codex 内置 Computer Use 的关系
- **Codex 的 Computer Use**：Codex 2026 大版本更新引入，让 Agent 直接操作 IntelliJ IDEA、Chrome 浏览器等桌面应用
- **Astra 的 Computer Use**：GPT-6 Astra 更广泛的能力——不只是 IDE 和浏览器，而是任何可以在电脑上做的事
- Codex 的 Computer Use 是 Astra 通用 Computer Use 能力在 Codex 产品形态下的落地

### 与 MCP/CLI 接口对比
| 维度 | API/MCP/CLI | Computer Use |
|-----|------------|-------------|
| 依赖 | 需要为 AI 建接口 | 用人类现有界面 |
| 攻击面 | 多一层接口多一层攻击面 | 无额外接口 |
| 覆盖 | 只覆盖已建模的部分 | 任何可在电脑上做的事 |
| 改造成本 | 需重新设计系统 | 不需任何改造 |

## 关联连接
- [[GregBrockman]] — 提出 Computer Use 重要性的判据者
- [[OpenAI]] — 实现方
- [[GPT-6]] / [[Astra]] — 核心模型
- [[Codex]] — 落地产品
- [[AGI]] — Computer Use 是 AGI 时代的钥匙
- [[MCP]] — Computer Use 对照方案
- [[NavierStokes]] — Computer Use 支撑的高阶能力案例
- [[摘要-OpenAI总裁Brockman最新采访]] — 来源
- [[摘要-GPT-6-Astra改变技术栈]] — Astra 技术栈影响
- [[摘要-gpt6-astra实测体验]] — Astra 实测（前端能力）
- [[摘要-codex-obsidian-自生长知识库]] — 同赛道 Computer Use 实践
