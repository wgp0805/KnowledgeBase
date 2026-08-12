---
title: "OpenClaw"
type: entity
tags: [实体, AI Agent, 开源项目]
sources: [raw/01-articles/小龙虾（OpenClaw）教程汇总.md, raw/01-articles/2026-08-02-MCP 第五版 × OpenClaw.NET：从协议升级到生态编排 - 张善友.md]
last_updated: 2026-08-03
---

## 定义
OpenClaw（小龙虾）是一个开源的 AI Agent 项目，由 Peter Steinberger 创建，允许用户通过终端与 AI 模型交互并执行复杂任务。

## 关键信息
- **创始人**：Peter Steinberger（"龙虾之父"，月烧 940 万 token）
- **核心特点**：
  - 终端 AI Agent，类似 Claude Code
  - 支持 Skill 扩展机制
  - 开源免费，社区活跃

### OpenClaw.NET MetaSKILL 编排引擎
OpenClaw.NET 提供基于 YAML 声明式 DAG 的 MetaSKILL 编排引擎，用于生产级 AI 工作流编排：

- **设计范式**：声明即编排（Declaration-as-Orchestration），编排逻辑是 YAML 声明的 DAG
- **运行环境**：OpenClaw.NET Gateway 服务器进程内
- **触发方式**：自然语言触发器匹配 + `meta_invoke` 工具
- **7 种步骤类型**：覆盖不同执行需求（llm_chat、agent、fan_out、skill_exec、user_input、route 等）
- **核心特性**：
  - `depends_on` 声明 DAG 依赖
  - `fan_out` 动态展开并行子步骤，wave-based 调度
  - `routes` / `when` 条件路由分支
  - `on_failure` 声明式失败替换步骤
  - `user_input` 人机交互暂停点（审批检查点）
  - `output_contract` 每步 JSON Schema 输出校验
  - `tool_allowlist` + `capabilities` + `MetaSkill.Enabled` 三步安全门禁
- **安全体系**：4 层超时保护（step / retry / session contract / agent loop）
- **审计能力**：持久化审计记录 + CLI replay/reconstruct
- **双运行时**：AgentRuntime + MafAgentRuntime
- **适用场景**：生产环境 CI/CD 工作流、需要人机交互审批、多人长期维护的重复任务
- **与 Claude Code Workflows 对比**：MetaSKILL 安全审计完善适合生产，Workflows 灵活度高适合探索

- **生态系统**：
  - 一站式部署平台：WorkBuddy、QoderWork、QClaw
  - 微信接入：ClawBot（腾讯官方插件）
  - 大量第三方 Skill
- **注意事项**：
  - Token 消耗较大
  - 需要从正规渠道安装，避免安全隐患

- **Pi Agent 作为运行时**：Pi Agent（Armin Ronacher 创建）是 OpenClaw 的 Agent 运行时。OpenClaw 不把 Pi 当子进程或 RPC 服务调用，而是直接嵌入 Pi SDK——会话状态、工具执行、消息历史都在 OpenClaw 进程内运行，无序列化/反序列化开销。详见 [[摘要-pi-agent-4工具极简主义]]。

## 关联连接
- [[摘要-OpenClaw小龙虾教程汇总]] — 来源
- [[PeterSteinberger]] — 创始人
- [[ArminRonacher]] — Pi Agent 创建者（Pi 是 OpenClaw 的 Agent 运行时）
- [[ClaudeCode]] — 类似 AI Agent
- [[Skill]] — 技能扩展机制
- [[WorkBuddy]] — 部署平台
- [[ClawBot]] — 微信接入插件
- [[meta-skill]] — 元技能概念
- [[dynamic-workflow]] — 动态工作流对比概念
- [[摘要-Claude-Code-Workflows-vs-MetaSKILL]] — 来源
- [[OpenClawNET]] — .NET 生态版本（MCP 编排层）
- [[MCP]] — 核心协议
- [[摘要-mcp-v5-openclaw-net]] — 来源（MCP 第五版 × OpenClaw.NET）
