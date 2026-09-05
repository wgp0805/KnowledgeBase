# Pi Agent 学习笔记 01 — Pi 定位与核心理念

> 学习日期：2026-08-07
> 所属阶段：阶段1 - 基础认知与环境搭建
> 学习来源：Pi 官方文档 + 导师讲解
> 掌握度：⭐⭐⭐⭐ (4/5)

---

## 1. Pi 的官方定位

> "Pi is a minimal terminal coding harness. It is designed to stay small at the core while being extended through TypeScript extensions, skills, prompt templates, themes, and pi packages."

中文理解：Pi 是一个**极简终端编程基座**（coding harness）。核心刻意保持很小，所有扩展能力都通过 TypeScript 扩展、Skills、提示词模板、主题和 Pi Packages 来加。

两个关键词：
- **minimal（极简）** — 核心尽量小
- **harness（基座/框架）** — 它不是一个"帮你写代码的 AI"，而是一个承载 AI 编程能力的架子

## 2. 什么是 "Coding Harness"？

### 成品 Agent vs Agent 基座

| 类型 | 代表 | 特点 |
|------|------|------|
| 成品 Agent | Claude Code, Codex | 买来就能用，功能完善，扩展能力有限 |
| Agent 基座 | Pi, Hermes | 提供底层框架，能力靠扩展加，高度可定制 |

### Pi 提供的
- 终端 TUI 界面
- 工具调用运行框架
- 事件系统
- Session 管理
- 扩展接口（最核心价值）

### Pi 不提供的（交给扩展）
- 具体的工具功能（可替换）
- 特定工作流
- UI 细节

**核心设计哲学：小内核，强扩展。**

## 3. Pi vs Hermes vs Claude Code 对比

| 维度 | Pi | Hermes | Claude Code |
|------|-----|--------|-------------|
| **核心定位** | 终端编程 Agent 基座 | 通用多平台 AI Agent 框架 | 成品编程 Agent |
| **扩展语言** | TypeScript + Markdown Skill | Markdown Skill + Python | Claude Code Skill |
| **扩展深度** | 最深（可改工具/事件/UI/Provider） | 深（工作流 + 插件系统） | 中等（Skill 为主） |
| **界面** | 终端 TUI | CLI/TUI/Desktop/Web/IM | 终端 |
| **使用场景** | 编程 + 深度定制 | 各种任务 | 编程 |
| **Skill 标准** | Agent Skills 标准 | Agent Skills 标准 | 自有格式 |

重要发现：Pi 和 Hermes 用的是同一套 Agent Skills 标准，Skill 可以相互迁移。

## 4. 扩展的三个层级

| 层级 | 方式 | 能改什么 | 深度 |
|------|------|---------|------|
| 最浅 | **Prompt / 配置** | 改系统提示、改设置 | 模型行为 |
| 中等 | **Skill** | 加工作流、加知识、加脚本调用 | 模型能力 |
| 最深 | **Extension / Plugin** | 加工具、拦截事件、改 UI、加 Provider | 基座行为 |

### Skill vs Extension 的关键区别

- **Skill**："告诉 Agent 一个新能力怎么用"，Agent 还是那个 Agent，运行逻辑没变。模型可能不遵守 Skill 里的规则。
- **Extension**："改 Agent 本身的运行方式"，在代码层面拦截和修改，模型绕不开。

### 举例：危险命令二次确认

| 方式 | 实现 | 可靠性 |
|------|------|--------|
| Skill | 写一条规则"执行 shell 前先问我" | 模型不一定遵守 |
| Extension | 在 tool_call 事件中检测危险命令直接拦截 | 100% 生效，模型绕不开 |

## 5. 为什么学 Pi 的扩展开发？

1. **理解 Agent 架构**：通过学 Pi 的扩展机制，理解一个 Agent 系统是怎么设计的
2. **知识可迁移**：架构思想可以迁移到 Hermes 和其他 Agent
3. **深度定制**：当你有特殊需求时（特定工作流、个性化工具链），Pi 的扩展体系能满足
4. **Skill 跨平台**：Agent Skills 标准让你写的 Skill 可以在多个 Agent 上用

## 6. 我的理解（练习输出）

Pi 是一个 agent 工具的最小核心，和其他 agent 工具一股脑的给到你不同，Pi 是把最基础的东西给你，你根据自己实际的情况编写扩展打造属于自己的 agent 工具。

如果只是普通的完成代码任务，选择合适的模型和合适的工具就行了，选择 pi 反倒不合适。如果对于 agent 工具有特殊的需求，想要在具体的工作实践中达到不同的效果，就要使用 pi+扩展。

Claude+Skill 实现的效果有限，如果是复杂的工作流和个性化的需求，还是去使用 pi 去实现比较好。

## 7. 相关资源

- [Pi 官方文档 Overview](https://pi.dev/docs/latest)
- [Agent Skills 标准](https://github.com/agent-skills/spec)
