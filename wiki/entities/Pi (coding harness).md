---
title: "Pi (coding harness)"
type: entity
tags: [AI, Agent, 编程工具, pi-dev, Agent基座]
sources: [raw/01-articles/pi-agent-study-01-pi-overview.md, raw/01-articles/pi-study-02-architecture.md]
last_updated: 2026-08-09
---

## 定义

Pi（pi.dev）是 Earendil Inc. 出品的**极简终端编程 Agent 基座**（minimal terminal coding harness）。核心刻意保持很小，所有扩展能力都通过 TypeScript 扩展、Skills、提示词模板、主题和 Pi Packages 来添加。

> ⚠️ 注意区分：本页面的 Pi 指 `pi.dev` 的终端编程基座，与 [[PiAgent]]（70K Star 的开源 Agent 框架）是**完全不同的两个项目**，勿混淆。

## 关键信息

### 核心设计哲学
**小内核，强扩展（minimal core, strong extension）**

Pi 只提供最基础的运行框架：
- 终端 TUI 界面
- 工具调用运行框架
- 事件系统
- Session 管理
- 扩展接口（核心价值）

具体功能和工作流全部交给扩展来实现。

### 四层扩展系统
| 层 | 形态 | 能力边界 |
|---|---|---|
| Skill | Markdown（SKILL.md） | 按需投喂工作流给模型；不能跑代码、不能拦事件 |
| Prompt Template | Markdown | 把常用 prompt 变成 `/foo` 命令 |
| Extension | TypeScript 模块 | 注册工具、拦 Agent loop、画 TUI、做 RPC |
| Package | npm/git 包 | 把前三层打包发布共享 |

详见 [[Pi 扩展生态与开发指南]]。

### 与其他 Agent 的对比

| 维度 | Pi (pi.dev) | Hermes | Claude Code |
|---|---|---|---|
| 定位 | 终端编程 Agent 基座 | 通用多平台 Agent 框架 | 成品编程 Agent |
| 扩展深度 | 最深（可改工具/事件/UI/Provider） | 深（工作流+插件系统） | 中等（Skill 为主） |
| Skill 标准 | Agent Skills 标准 | Agent Skills 标准 | 自有格式 |
| 界面 | 终端 TUI | CLI/TUI/Desktop/Web/IM | 终端 |

### 技术细节
- 安装：`npm install -g --ignore-scripts @earendil-works/pi-coding-agent`
- 扩展语言：TypeScript（jiti 加载免编译）
- 扩展位置：`~/.pi/agent/extensions/`（全局）或 `.pi/extensions/`（项目级）
- 热重载：`/reload` 命令

## 架构分层

Pi 采用「核心层 + 扩展层」的双层架构，通过 ExtensionContext 连接。

### 核心层四件套
1. **[[LLM Loop]]**：运行循环（思考→工具调用→观察→再思考），Agent 的心脏
2. **工具系统**：工具注册、调度、安全检查、结果处理
3. **Session 管理**：对话持久化、分支导航、上下文压缩
4. **TUI 界面**：终端 UI，Ink（React for Terminal）组件化

### 扩展层四层模型
| 层级 | 形态 | 能力边界 |
|------|------|---------|
| L1 Prompt Template | Markdown | 改提示词，不改变行为 |
| L2 Skill | Markdown + 脚本 | 投喂知识和工作流，依赖模型执行 |
| L3 Extension | TypeScript | 注册工具/拦截事件/自定义UI，代码级能力 |
| L4 Package | npm/git 包 | 打包分发单元，不增加新能力维度 |

详见 [[Agent扩展层级]]

### ExtensionContext（扩展上下文）
连接核心与扩展的桥梁，扩展通过它与核心交互：
- **读取 API**：cwd、mode、hasUI、getContextUsage、getSystemPrompt
- **操作 API**：registerTool、registerCommand、sendMessage、exec、setModel、compact
- **事件系统**：tool_call、tool_result、model_request、model_response、session_loaded 等
- **UI API**：confirm、select、input、notify、custom（自定义组件）

### 扩展加载流程
发现 → jiti加载 → 执行注册 → 就绪，支持 `/reload` 热重载

## 关联连接
- [[AgentHarness]] — Harness 概念，Pi 是典型实现
- [[Agent扩展层级]] — 三层/四层扩展模型
- [[LLM Loop]] — Agent 运行循环，Pi 核心组件之一
- [[Agent]] — Agent 核心概念
- [[PiAgent]] — ⚠️ 另一个同名项目（开源 Agent 框架），注意区分
- [[Hermes]] — 同类 Agent 基座，设计理念相似
- [[摘要-pi-agent-study-01-pi-overview]] — 学习笔记 01：定位与核心理念
- [[摘要-pi-study-02-architecture]] — 学习笔记 02：整体架构
