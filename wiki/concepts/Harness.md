---
title: "Harness"
type: concept
tags: [概念, Agent, 架构, 框架]
sources:
  - raw/09-archive/DeepSeek员工：Harness开始内测，有plugin、skill、MCP、Agent开源项目者优先，并赠送API额度（附Agent面试题）.md
  - raw/09-archive/2026-08-15-DeepSeek Harness 教程：一切皆插件的开源 Agent 框架 - 掉落的果实.md
  - raw/09-archive/2026-09-07-对话OpenRouter CEO：Harness 正在取代超级 App，未来所有软件都只是 Agent 的后台工具.md
  - raw/09-archive/2026-10-13-这 6 本 GitHub 上的开源 AI 宝典，那是相当有真东西。.md
  - raw/09-archive/2026-10-15-你的游戏本身就是 Harness ：如何让 AI Agent 读懂游戏并十倍加速迭代？ - leikooo.md
last_updated: 2026-10-15
---

## 定义
Harness 是指 AI Agent 中模型之外的一切基础设施层，包括工具调用、记忆管理、上下文控制、桌面集成、MCP 协议、Skills 体系等。核心公式为 **Model + Harness = Agent**：模型负责推理，Harness 负责将模型的推理能力转化为可执行的工程化操作。

## 关键信息
- Harness 是未来五年 AI 工程化的核心主题，各大模型厂商都在争先恐后构建自己的 Harness
- 国内主要 Harness 产品：DeepSeek Harness（DSH）、阿里 Qoder、月之暗面 Kimi Code、智谱 Zcode
- 所有 Agent 本质上都是在做 Harness——让模型更好用、更匹配业务
- **Harness 最关键的能力**：上下文管理、Memory 管理、多 Agent 协作、提示词优化

### 核心组件
1. **工具调用系统**：工具注册表、Schema 校验、HITL 审批
2. **记忆管理系统**：短期记忆（会话级）、长期记忆（跨会话持久化）、项目记忆（规则文件）
3. **上下文控制**：窗口管理、摘要压缩、Token 预算控制
4. **MCP 协议**：外部服务集成
5. **Skills 体系**：可复用的行为模块
6. **多 Agent 协作**：Sub-agent 编排、任务分解

### DSH 四种运行模式（详见 [[摘要-deepseek-harness教程-掉落的果实]]）
1. **TUI 模式**：终端交互（默认），`dsh` 启动
2. **Headless 模式**：无界面自动化，`dsh --headless -p "任务"`，适合 CI/CD
3. **Web UI 模式**：`dsh --web`，浏览器访问，支持可视化调试
4. **SDK 模式**：作为库嵌入，`import { DSH } from '@deepseek/harness'`

### DSH 插件协议
- 定义 `name`、`version`、`tools`、`skills`、`hooks`
- 支持生命周期钩子：`onSessionStart`、`onToolCall`、`onSessionEnd`
- 脚手架：`dsh plugin create <name>`
- 配置文件：`dsh.config.json`

### Harness vs App（Alex Atallah / OpenRouter CEO 视角，2026-09-07）
- **Harness 不会随模型变强而消失**：将成为模型之上的可组合工作界面，也是没有自研模型的创业公司掌握用户关系的重要一层
- **区别在于可组合性**：一个 Harness 可以调用另一个 Harness，也可以在云端沙箱里启动另一个 Harness
- **Harness 通常建立在 Unix 环境上**：模型对 Unix 和 bash 命令训练充分，比围绕一组复杂 App 做编排更可靠更确定
- **让 Agent 操作普通 App** 会遇到登录/密码/虚拟浏览器/寻找 API/阅读文档等许多未知问题；进入 Harness 则更容易检查内部发生了什么
- **更多 Harness 会出现**：它是建立在模型之上的用户体验，让不拥有模型的开发者能够拥有用户关系
- 模型变强后，系统提示词里塞进的大量杂物反而可能拖累表现；Anthropic 曾展示删掉部分系统提示词内容后模型矛盾变少、表现更好

### 开源教材论断：Harness 才是竞争力（2026-10）
《深入理解 AI Agent：设计原理与工程实践》（4.9 万 Star 开源教材，详见 [[深入理解AIAgent]]）全书围绕 **Agent = LLM + 上下文 + 工具** 展开，核心立场是**模型之外的工程能力 Harness 才是竞争力所在**——上下文工程、记忆、Tool、多 Agent 协作等 Harness 能力被提升到与模型并列的位置（来源：[[摘要-github开源ai宝典6本]]）。

### 领域定制 Harness：你的游戏本身就是 Harness（2026-10-15，详见 [[摘要-你的游戏本身就是Harness]]）
通用 Harness 的致命短板是**无法与被改造对象的内核对话**——游戏对 Claude Code、Cursor 这类工具就是一个焊死的黑盒，模型只能看见编辑器里的文本，而游戏的真实运行状态大量存在于非代码资产中。Kyle Kukshtel 的结论是：让 LLM 胜任游戏开发本质上是**上下文工程问题**，解法是**把游戏本身做成 Harness**——用 [[确定性]]、[[FatStruct]]、[[命令模式]]、[[外部化数据管理]]、[[无头模拟内核]]、[[图像差分]]、[[纯文本性能分析]] 七条原则把游戏内部变得对模型处处透明、处处可寻址，最终串成 [[Agent迭代飞轮]]，把一次 Agent 迭代从数十分钟压到数秒。

这条论断与下方"Harness 才是竞争力"的主张同向：**模型之外的工程能力才是差异化所在**，只不过这里把 Harness 的外延从"围绕模型搭外壳"推进到了"改造被操作对象本身"。

## 关联连接
- [[DeepSeekHarness]] — DeepSeek 原生 Harness 实现
- [[PaiCLI]] — 开源终端 Agent Harness 实现
- [[ReAct_Agent]] — ReAct 推理循环是 Harness 的核心模式
- [[摘要-deepseek-harness内测]] — 来源
- [[摘要-deepseek-harness教程-掉落的果实]] — 来源（DSH 完整教程）
- [[摘要-对话OpenRouter-CEO-Harness取代超级App]] — 来源（Harness vs App 视角）
- [[ClaudeCode]] — Claude 的 Harness 实现
- [[Codex]] — Codex 的 Harness 实现
- [[HITL]] — 人机协作审批机制
- [[context-compression]] — 上下文压缩策略
- [[Pi]] — 极简 Harness 实现（系统提示词仅 200 Token）
- [[AlexAtallah]] — Harness 不会消失论的提出者
- [[OpenRouter]] — CEO 对谈来源平台
- [[HarnessEngineering]] — Harness 工程实践
- [[harness-architecture-comparison]] — Harness 架构分类与 Agent 选型综合对比
- [[深入理解AIAgent]] — 4.9 万 Star 开源教材（Agent = LLM + 上下文 + 工具）
- [[摘要-github开源ai宝典6本]] — 教材推荐来源
- [[摘要-你的游戏本身就是Harness]] — 来源（领域定制 Harness：游戏即 Harness）
- [[Agent迭代飞轮]] — 七条游戏工程原则串联后的闭环
- [[KyleKukshtel]] — 该论断提出者
- [[上下文污染]] — 通用 Harness 在领域场景失效的根因之一