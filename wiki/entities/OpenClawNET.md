---
title: "OpenClawNET"
type: entity
tags: [实体, AI Agent, 开源项目, MCP]
sources:
  - raw/09-archive/2026-08-02-MCP 第五版 × OpenClaw.NET：从协议升级到生态编排 - 张善友.md
last_updated: 2026-08-03
---

## 定义
OpenClaw.NET 是 OpenClaw 的 .NET 生态版本，定位为「MCP 生态编排层」：当单个 MCP Server 变成「迷你 SaaS」时，OpenClaw.NET 成为这些 SaaS 之间的编排操作系统，通过 PR #196（csharp-sdk v2.0）全面拥抱 MCP 第五版协议。

## 关键信息
- **架构六层组件**：
  - **Gateway**：无状态路由与协议翻译（Mcp-Method/Mcp-Name 请求头路由、缓存语义、OTel 链路追踪、OAuth/OIDC 鉴权、限流审计、协议协商）
  - **MetaSkill**：工具编排与状态传递（显式句柄即 DAG 数据令牌）
  - **TokenHub**：计量与审计（每个句柄可追踪、计费、审计）
  - **Harness**：异步任务与中断恢复（MRTR 的 input_required 状态持久化，用户响应后重新调度到任意 Worker）
  - **OpenSandbox**：安全界面渲染（MCP Apps 沙箱 iframe 环境）
  - **DDI Registry**：契约治理（JSON Schema 2020-12 注册/版本化）
- **MCP 第五版适配要点（PR #196）**：
  - 协议协商优先 `server/discover`，404/-32601 回退 initialize
  - 支持 Streamable HTTP、每请求携带 Mcp-Method/Mcp-Name/Mcp-Protocol-Version 请求头
  - 实现 `/apps/mcp/{appId}` 代理端点（MCP Apps 正式扩展）
  - Tasks 扩展：任务句柄模型与 Harness 工作流实例 ID 同构
  - JSON Schema 2020-12：支持 $ref/oneOf/anyOf/allOf；工具缺失 inputSchema 时跳过而非崩溃；AllowRelaxedInputSchemaValidation 兼容开关
- **状态哲学**：无状态 Gateway × 有状态 Harness——获得 Serverless 弹性 + 有状态工作流可靠性

## 关联连接
- [[OpenClaw]] — 所属项目
- [[MCP]] — 核心协议
- [[MRTR]] — 协议新机制
- [[meta-skill]] — 编排引擎
- [[AgentHarness]] — 任务引擎
- [[摘要-Claude-Code-Workflows-vs-MetaSKILL]] — MetaSkill 编排对比
- [[摘要-mcp-v5-openclaw-net]] — 来源
