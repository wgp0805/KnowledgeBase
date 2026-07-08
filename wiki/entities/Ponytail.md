---
title: "Ponytail"
type: entity
tags: [AI编程, 减法思维, 开源工具, Agent技能]
sources: [raw/01-articles/20.9k Star 的开源项目，让你的 AI 少写点废代码.md]
last_updated: 2026-07-08
---

## 定义

Ponytail 是一个开源的 AI Agent 技能项目，核心理念是"最好的代码，是你根本不用写的代码"。它面向 [[ClaudeCode]]、[[Codex]]、GitHub Copilot CLI、[[Gemini]] CLI、[[OpenCode]] 等 AI 编程工具，安装后给 AI 注入一套"懒但不敷衍"的开发规则——先判断需求是否真的存在，再看标准库、平台原生能力、已有依赖，最后才写最少可用代码。它把那个"经验丰富、话不多、出手就删代码"的资深程序员塞进 AI 编程助手里。

## 关键信息

- **GitHub Star**: 20.9k+
- **核心理念**: 最好的代码，是你根本不用写的代码
- **GitHub**: <https://github.com/DietrichGebert/ponytail>
- **支持平台**: [[ClaudeCode]]、[[Codex]]、GitHub Copilot CLI、[[Gemini]] CLI、[[OpenCode]]
- **技术形态**: AI Agent 技能（[[ai-agent-skill]]），含 Node 生命周期 Hook
- **前置依赖**: 建议环境能正常访问 Node.js（用于生命周期 Hook）；Node 不在 PATH 时核心规则仍可用，自动激活能力可能不完整

### 核心机制

- **减法思维**: 能不写就不写，能用标准库就别造轮子，浏览器原生支持就别上依赖，一行能解决就别写五十行
- **`ponytail-review`**: 专门检查 [[过度工程化]]，直接告诉你哪里能删、用什么替代、能减少多少行（不长篇大论）

### 强度模式

| 命令 | 说明 |
| --- | --- |
| `/ponytail lite` | 更温和 |
| `/ponytail full` | 默认模式 |
| `/ponytail ultra` | 适合代码库已被过度设计折磨过时 |

### 安装示例（Claude Code）

```
/plugin marketplace add DietrichGebert/ponytail
/plugin install ponytail@ponytail
```

Codex、GitHub Copilot CLI、Gemini CLI、[[OpenCode]] 均有对应安装方式，OpenCode 需在 `opencode.json` 中配置 plugin。

### 典型用例

- 日期选择：优先 `<input type="date">` 而非引入 flatpickr
- 邮箱校验：先判断场景，前端提示用最简单的包含 `@` 判断，真实账号验证提醒依赖邮件确认流程而非迷信正则
- Review 建议：单一实现的接口可删、日期格式化库换 `Intl.DateTimeFormat`、手写循环用标准库一行完成

## 关联连接

- [[摘要-ponytail-ai减代码]] — 来源
- [[过度工程化]] — 核心概念
- [[ClaudeCode]] — 支持平台
- [[Codex]] — 支持平台
- [[OpenCode]] — 支持平台
- [[Gemini]] — Gemini CLI 支持
- [[GitHub]] — 代码托管
- [[AICoding]] — AI 辅助编程范式
- [[ai-agent-skill]] — Agent 技能机制
- [[Skill]] — 技能扩展机制
- [[CLAUDEmd]] — 类似的规则注入思路
