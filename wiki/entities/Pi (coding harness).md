---
title: "Pi (coding harness)"
type: entity
tags: [AI, Agent, 编程工具, pi-dev, Agent基座]
sources: [raw/09-archive/pi-agent-study-01-pi-overview.md, raw/09-archive/pi-study-02-architecture.md]
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

详见 Pi 扩展生态与开发指南。

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

### 并发写保护：模块级文件变更队列（2026-10-21，详见 [[摘要-多agent并发改文件冲突]]）

Pi **没有 worktree 隔离**（命令行参数表里没有 worktree 相关开关），多个 session **共享同一个工作目录**。它的并发安全靠**时间**而非空间：

- **文件变更队列**：内部实现为一个**模块级 Map**，同一个文件上的写入操作会串成 Promise 链，前一个做完才轮到下一个，不同文件之间可以并行
- **队列 key 的双重解析**：先做一次路径解析、再做一次真实路径解析——**两个软链接指向同一个文件时也会排进同一个队列**
- **edit 工具四步入队**：检查文件是否存在、读取当前内容、匹配 oldText、写回结果，**四步全部放在队列里面完成**；同一个进程里有十个并行 edit 也会老实排队

**三个漏洞**：
1. **bash 工具没有引用这个队列**——模型用 `sed` 改写文件、用重定向写文件、执行 prettier 格式化都不排队，甚至和同进程的 edit 也不互斥
2. **队列只在同一进程内共享**——两个终端各开一个 pi 指向同一个仓库，它们在内存里根本看不见对方，后写的那个仍会直接覆盖先写的，**没有任何提示**
3. **write 工具连读都不读**，建好父目录就把内容写进去，**无条件覆盖**；edit 工具的 oldText 校验是文本匹配的副产物而非版本校验——外部改动落在 oldText 内会报「找不到要替换的文本」，落在 oldText 外则匹配照常成功、双方基于不同基线各改各的、结果静默写回

> 对照：Claude Code 用 **worktree 空间隔离**，但它的四道检查（编辑目标路径 / 命令执行位置 / git 重定向 / 命令形态）**不跟踪 shell 实际写入了哪些文件**，用 `cp` 或重定向仍能写回主仓库。详见 [[Agent并发写冲突]] 与 [[Worktree]]。

## 关联连接
- [[AgentHarness]] — Harness 概念，Pi 是典型实现
- [[Agent扩展层级]] — 三层/四层扩展模型
- [[LLM Loop]] — Agent 运行循环，Pi 核心组件之一
- [[Agent]] — Agent 核心概念
- [[PiAgent]] — ⚠️ 另一个同名项目（开源 Agent 框架），注意区分
- [[Hermes]] — 同类 Agent 基座，设计理念相似
- [[Agent并发写冲突]] — 与 Claude Code worktree 的对照分析
- [[摘要-pi-agent-study-01-pi-overview]] — 学习笔记 01：定位与核心理念
- [[摘要-pi-study-02-architecture]] — 学习笔记 02：整体架构
- [[摘要-多agent并发改文件冲突]] — 来源（文件变更队列与漏洞）
