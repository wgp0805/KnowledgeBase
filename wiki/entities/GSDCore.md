---
title: "GSDCore"
type: entity
tags: [AI编程, 规范驱动, 上下文工程, 开源工具, 工作流]
sources: [raw/01-articles/2.3k star 的新项目，用来指挥 Claude Code 和 Codex 干活！.md]
last_updated: 2026-07-08
---

## 定义

GSD Core 是一个开源的 AI 编码工作流项目，核心定位是为 AI 编程工具提供元提示、[[ContextEngineering|上下文工程]]和 [[规范驱动开发]] 能力。它不是新编辑器，也不替代 [[ClaudeCode]] 或 [[Cursor]]，而是给这些 AI 编码助手加上一层"项目管理大脑"——引导 AI 先理解项目、再拆解阶段、按计划执行、最后检查结果，让 AI 围绕项目上下文持续工作而非"想到哪改到哪"。

## 关键信息

- **GitHub Star**: 2.3k+
- **核心理念**: 给 AI 编码助手加上项目管理大脑，串联需求讨论、任务规划、代码执行和结果验证
- **GitHub**: <https://github.com/open-gsd/gsd-core>（注意是 `open-gsd/gsd-core`，勿与其他同名旧仓库混淆）
- **支持平台**: macOS、Windows、Linux
- **支持工具**: [[ClaudeCode]]、[[Codex]]、[[Gemini]] CLI、[[Cursor]]、Windsurf
- **前置依赖**: Node.js（通过 `npx` 安装）
- **技术形态**: 元提示 + [[ContextEngineering|上下文工程]] + [[规范驱动开发]]

### 安装

```bash
# 标准安装
npx @opengsd/gsd-core@latest

# 最小模式
npx @opengsd/gsd-core@latest --minimal
```

安装时引导选择接入的 AI 编码环境；完成后用 `/gsd-help`（Codex 中为 `$gsd-help`）查看可用能力。

### 核心工作流（GSD = Get Stuff Done）

| 阶段 | 命令 | 作用 |
| --- | --- | --- |
| 分析代码库 | `/gsd-map-codebase` | 理解现有代码结构 |
| 建立上下文 | `/gsd-new-project` | 创建或更新项目上下文 |
| 需求讨论 | `/gsd-discuss-phase <n>` | 理清功能需求与边界 |
| 生成计划 | `/gsd-plan-phase <n>` | 制定执行计划 |
| 执行 | `/gsd-execute-phase <n>` | 按计划写代码 |
| 验证 | `/gsd-verify-work <n>` | 检查本阶段工作 |

### 解决的痛点

AI 编码工具在需求复杂、上下文变长时容易"忘记前面的约定、改着改着把项目结构搞乱"。GSD Core 通过元提示和上下文工程减少上下文丢失、需求跑偏和无序改动，让 AI 编码从简单聊天生成变成更接近真实开发流程的项目交付。

## 关联连接

- [[摘要-gsd-core-ai工作流]] — 来源
- [[规范驱动开发]] — 上层方法论
- [[ContextEngineering]] — 上下文工程能力
- [[ClaudeCode]] — 支持平台
- [[Codex]] — 支持平台
- [[Cursor]] — 支持平台
- [[Gemini]] — Gemini CLI 支持
- [[GitHub]] — 代码托管
- [[AICoding]] — AI 辅助编程范式
- [[SpecKit]] — 同属规范驱动阵营的兄弟方案
- [[CLAUDEmd]] — 类似的元提示/规则注入思路
