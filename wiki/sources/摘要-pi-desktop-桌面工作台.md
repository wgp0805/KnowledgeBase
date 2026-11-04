---
title: "摘要-pi-desktop-桌面工作台"
type: source
tags: [来源, AI编程, 桌面端, Pi生态]
sources: [raw/09-archive/2026-10-31 - 又一个国产开源神器！社区版 Pi Agent 桌面工作台来了！.md]
last_updated: 2026-11-02
---

## 核心摘要

「程序员追风」介绍国产开源 AI 编程桌面端 **PI-Desktop**（GitHub `vastsa/PI-Desktop`，Early Preview），Windows / macOS / Linux 均可安装。它为 Coding Agent 提供独立的桌面工作区：本地项目、Agent 会话、模型配置、代码改动、插件都放在一个窗口里。软件本身**不自带大模型**，需接入自己已有的模型服务（云端、自建网关、兼容接口、本地模型均可）。Agent Runtime 来自开源 Pi 生态，PI-Desktop 负责桌面工作区、会话、权限、插件和多 Agent 编排。

三种执行方式：

- **Agent**：直接读项目、改文件、跑命令和测试，发现问题继续处理
- **Plan**：先研究仓库、给出实施计划，确认后再改（适合影响文件多或需求只有大概方向的场景）
- **Goal**：说清目标和验收条件，执行路线由 Agent 自己选

三者都受权限层约束，改文件、跑命令、调用工具、委派任务都会经过权限审批。

其他要点：

- 会话按项目保存，可置顶/归档/从旧会话开分支；`@` 选项目内文件，`/` 打开命令
- 项目有检查点，中断后尽量恢复现场（以实际恢复结果为准）
- Agent 执行记录（模型回复、工具调用、命令执行）与 Diff 可并排查看
- Subagent 承担独立后台任务，使用独立上下文，结果交回主 Agent；可指定哪些模型允许被 Subagent 调用
- Session Orchestrator：一个主 Session 协调多个 Worker Session 做长时间并行工作
- 插件生态：Token 统计、SSH 管理、Git Lens、浏览器自动化、终端、Markdown 笔记；Skills / MCP Server / 后台服务同样可接
- 数据默认存本机，API 凭据放操作系统钥匙串，官方声明没有遥测

注意事项：插件权限审批不等于完整操作系统沙箱，来源不明的插件不要轻易安装。多 Agent 只适合大仓库、可分开的工作项，小任务拆了反而难检查。

## 关联连接
- [[PI-Desktop]] — 被介绍的实体
- [[Pi (coding harness)]] — Agent Runtime 所属生态
- [[Subagent]] — 后台任务执行者
- [[MCP]] — 插件可接入的协议
- [[程序员追风]] — 文章作者
