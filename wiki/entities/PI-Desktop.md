---
title: "PI-Desktop"
type: entity
tags: [开源项目, AI编程, 桌面端, Pi生态, 多Agent]
sources: [raw/09-archive/2026-10-31 - 又一个国产开源神器！社区版 Pi Agent 桌面工作台来了！.md]
last_updated: 2026-11-02
---

## 定义

PI-Desktop（GitHub `vastsa/PI-Desktop`）是国产开源的 AI 编程桌面工作台，Early Preview 阶段，支持 Windows / macOS / Linux。为 Coding Agent 提供独立桌面工作区：会话按项目保存、模型自接、代码改动可检查、插件可扩展。Agent Runtime 来自开源 Pi 生态，PI-Desktop 负责桌面工作区、会话、权限、插件和多 Agent 编排。**不自带大模型**，需接入自己已有的模型服务。

## 关键信息

### 三种执行方式

| 方式 | 说明 | 适用场景 |
|------|------|----------|
| **Agent** | 直接读项目、改文件、跑命令和测试 | 日常改代码 |
| **Plan** | 先研究仓库，给实施计划，确认后再改 | 影响文件多、需求只有大概方向 |
| **Goal** | 说清目标和验收条件，执行路线由 Agent 选 | 结果明确，中间步骤不想逐项交代 |

三者均受权限层约束（改文件、跑命令、调用工具、委派任务都会经过权限审批）。

### 核心功能

- **会话按项目保存**：置顶、归档、从旧会话开分支或搜索内容；`@` 选项目内文件，`/` 打开命令
- **项目检查点**：中断后尽量恢复任务现场（以实际恢复结果为准）
- **Agent 执行记录回看**：模型回复、工具调用、命令执行记录 + Diff 并排查看；长会话右侧有缩略导航
- **Subagent**：独立后台任务，独立上下文，结果交回主 Agent；可指定哪些模型允许被调用
- **Session Orchestrator**：一个主 Session 协调多个 Worker Session 做长时间并行工作
- **多会话导入**：可从本机其他 Coding Agent 工具导入历史会话
- **插件系统**：Token 统计、SSH 管理、Git Lens、浏览器自动化；Skills / MCP Server / 后台服务均可接入；插件间可传递消息

### 数据与隐私

- 项目、会话、设置、日志默认存本机
- API 凭据放在操作系统钥匙串里
- 模型请求不强制经过 PI-Desktop 云端中转，官方声明无遥测

### 安装

下载 Releases 安装包（Mac Apple Silicon/Intel、Windows x64、Linux x64/ARM64）即可，无需 Node.js/pnpm/Rust 环境。

### 评价与限制

- 优点：会话留存与修改审查做得到位；模型可换；插件已有实际可用的
- 限制：多 Agent 只适合大仓库、可分开的工作项，小任务拆开反而难检查；插件生态仍薄弱；Early Preview 阶段部分接口和行为会变
- 注意：插件权限审批不等于完整操作系统沙箱，来源不明的插件别乱装

## 关联连接
- [[摘要-pi-desktop-桌面工作台]] — 来源
- [[Pi (coding harness)]] — Agent Runtime 所属生态
- [[Orca]] — 同类多模型桌面工作台
- [[DeepSeekHarness]] — 另一套 Harness + 桌面客户端路线
- [[Subagent]] — 后台任务执行概念
- [[MCP]] — 插件可接入的协议
- [[程序员追风]] — 文章作者
