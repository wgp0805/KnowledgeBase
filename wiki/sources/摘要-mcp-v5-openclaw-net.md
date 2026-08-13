---
title: "摘要-mcp-v5-openclaw-net"
type: source
tags: [来源, MCP, OpenClaw, Agent]
sources:
  - raw/09-archive/2026-08-02-MCP 第五版 × OpenClaw.NET：从协议升级到生态编排 - 张善友.md
last_updated: 2026-08-03
---

## 核心摘要
- 2026-07-28 MCP 协议发布第五版，最显著变化是**会话从协议层被彻底删除**——MCP 从有状态的双向协议变成无状态的请求-响应协议。远程 MCP Server 可像普通 HTTP 服务一样部署到 Serverless、边缘节点或 Kubernetes。
- 无状态化影响：`initialize/initialized` 握手简化为每请求自包含协议版本；移除 `Mcp-Session-Id` 粘性会话，支持轮询负载均衡；状态外置到数据库/缓存；HTTP+SSE 长连接改为 Streamable HTTP 请求-响应。
- **显式业务句柄**：跨调用状态（浏览器实例、购物车、审批流程）通过显式句柄传递（如 create_browser 返回 browser_id，后续调用传递 browser_id），状态属于业务而不属于连接。
- **MRTR（Multi Round-Trip Requests）**：替代服务端反向请求客户端的能力。客户端发起工具调用 → 服务端返回 input_required → 客户端收集确认/参数 → 携带 inputResponses+requestState 重新发起原始请求 → 任意服务端实例继续完成任务。
- **网关层路由**：网关可通过 `Mcp-Method` 和 `Mcp-Name` 请求头路由，无需解析 JSON body，降低网关 CPU 开销。
- **OpenClaw.NET PR #196**：向 csharp-sdk v2.0 升级，拥抱 Streamable HTTP、协议协商（server/discover）、MCP Apps 代理端点、Tasks 扩展、JSON Schema 2020-12。
- 架构定位：单个 MCP Server 像「跑在 Agent 里的迷你 SaaS」，OpenClaw.NET 成为这些 SaaS 的编排操作系统（Gateway 无状态路由 + MetaSkill DAG 编排 + TokenHub 计量审计 + Harness 异步恢复 + OpenSandbox 安全渲染 + DDI Registry 契约治理）。
- 五大融合优势：无状态 Gateway×有状态 Harness；MCP Apps×OpenSandbox；Tasks×Harness 异步引擎；显式句柄×MetaSkill Token 经济；JSON Schema 2020-12×DDI Registry。

## 关联连接
- [[MCP]] — 协议版本升级
- [[OpenClawNET]] — 本文主角
- [[OpenClaw]] — 关联项目
- [[MRTR]] — 新机制
- [[meta-skill]] — MetaSkill DAG 编排
- [[AgentHarness]] — Harness 引擎
- [[可观测性]] — 链路追踪
