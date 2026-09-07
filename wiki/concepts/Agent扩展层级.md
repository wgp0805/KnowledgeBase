---
title: "Agent扩展层级"
type: concept
tags: [AI, Agent, 扩展机制, 架构设计]
sources: [raw/01-articles/pi-agent-study-01-pi-overview.md, raw/01-articles/pi-study-02-architecture.md]
last_updated: 2026-08-09
---

## 定义

Agent 扩展层级是指对 AI Agent 系统进行能力扩展时的不同深度等级。不同层级修改的对象不同（模型行为 vs 基座行为），能力边界和可靠性也有本质差异。

## 关键信息

### 三层/四层扩展模型

**基础三层模型**：

| 层级 | 方式 | 修改对象 | 能力边界 | 可靠性 |
|------|------|---------|---------|--------|
| L1 最浅 | **Prompt / 配置** | 系统提示词、设置项 | 改变模型的行为倾向 | 低（模型可能不遵守） |
| L2 中等 | **Skill** | 注入工作流、知识、脚本 | 扩展模型的专业能力和工作流程 | 中（依赖模型理解并执行） |
| L3 最深 | **Extension / Plugin** | Agent 基座代码 | 注册工具、拦截事件、改 UI、加 Provider | 高（代码层面，模型绕不开） |

**Pi 的四层细分**（在基础三层上增加了 Prompt Template 和 Package 两层）：

| 层级 | Pi 中的形态 | 写起来要 | 能力边界 |
|------|------------|---------|---------|
| L1 | **Prompt Template** | 2 分钟 | 把常用 prompt 变成 `/foo` 命令 |
| L2 | **Skill** | 几分钟到几小时 | 按需投喂工作流 + 知识 + 脚本 |
| L3 | **Extension (TypeScript)** | 30 分钟到几天 | 注册工具、拦事件、画 TUI、做 RPC |
| L4 | **Package** | 1 小时 | 把前三层打包发布分享（分发单元） |

> 注：Package 是分发单元，不增加新的能力维度，所以本质上还是三层能力等级 + 一层分发。

### 核心区别：Skill vs Extension

这是最容易混淆也是最重要的区别：

- **Skill** = "告诉 Agent 一个新能力怎么用"
  - Agent 的运行逻辑没变，只是多了一份知识/流程
  - 模型可能选择不使用 Skill，也可能用错
  - 优点：简单、易写、跨平台（Agent Skills 标准）

- **Extension** = "改 Agent 本身的运行方式"
  - 在代码层面修改基座的行为
  - 模型无法绕过，100% 按代码执行
  - 优点：能力强、可靠；缺点：技术门槛高、每个基座写法不同

### 典型案例对比：危险命令二次确认

| 实现方式 | 原理 | 可靠性 |
|---------|------|--------|
| Prompt 提示 | 系统提示里写"危险命令前先问用户" | 低，模型可能忽略 |
| Skill 规则 | Skill 文档里规定"执行 shell 前必须确认" | 中，模型大概率遵守但不保证 |
| Extension 拦截 | 在 tool_call 事件钩子中检测并强制弹窗 | 高，模型绕不开，代码层面生效 |

### 各 Agent 系统的扩展能力对比

| 系统 | L1 Prompt | L2 Skill | L3 Extension |
|------|----------|----------|-------------|
| **Pi (pi.dev)** | ✅ | ✅（Agent Skills 标准） | ✅（TypeScript，深度最深） |
| **Hermes** | ✅ | ✅（Agent Skills 标准） | ✅（插件系统） |
| **Claude Code** | ✅ | ✅（自有格式） | ⚠️（有限） |
| **Codex** | ✅ | ✅ | ⚠️（有限） |

### 选型建议

- 只是想加知识或工作流 → 用 **Skill**（简单、可迁移）
- 需要可靠的工具/事件级控制 → 用 **Extension**
- 需要改 Agent 核心逻辑 → 直接改源码（或选一个高度可扩展的基座如 Pi）

## 关联连接
- [[Agent]] — Agent 核心概念
- [[AgentHarness]] — Agent 基座概念
- [[LLM Loop]] — Agent 运行循环，扩展通过事件钩子介入
- [[AI Agent Skill]] — Skill 详细概念
- [[Pi (coding harness)]] — 扩展能力最强的 Agent 基座之一
- [[Hermes]] — 另一个支持多层扩展的 Agent 基座
