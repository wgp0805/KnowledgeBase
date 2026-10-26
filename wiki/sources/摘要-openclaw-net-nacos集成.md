---
title: "摘要-openclaw-net-nacos集成"
type: source
tags: [来源, 原始文件, Nacos, OpenClaw, MCP, AI Agent]
sources: [raw/09-archive/2026-09-27-当 AI Agent 遇到 Nacos：OpenClaw.NET 集成入门 - 张善友.md]
last_updated: 2026-09-28
---

## 核心摘要

本文介绍 OpenClaw.NET 基于 Nacos 3.2.4 AI 管理中心与 MCP 协议的工具集成方案：Agent 要调用注册在 Nacos 里的外部 MCP Server（如天气服务），若让大模型自己摸索发现与调用，每轮消耗上万个 input token 且结果不稳定，OpenClaw.NET 则把"发现服务→确认版本→取工具列表与 schema→调用→失败处理→审计"做成一条**全程零 LLM 调用的确定性管线**。三层职责：Registry（Nacos AI 管理中心）决定"存在什么、谁可见"（元数据、端点、版本、工具开关 toolSpec.ToolsMeta），Router（NacosMcpRouter，.NET global tool，ONNX 本地向量检索）决定"如何被发现和连接"（search/add/use 三工具），OpenClaw 运行时决定"何时、以何身份、经何审批执行"。Agent 侧只需在 skill 文件声明 `capability_ref`（provider/binding/intent），"找哪个 Server、调哪个工具、参数怎么填"由管线完成。四个关键机制：协议防腐层（把 Router 的"散文信封"解析收敛到单一契约文件）、带世代（generation）的缓存（TTL 300s/容量 1024/FIFO，配置变更世代+1 旧键失效，过期返回 `capability_stale_binding`）、熔断（同目标连续失败 3 次熔断 30 秒、成功一次复位、被策略阻止的不计入）、失效事件（长轮询→SHA-256 比对→发布 CapabilityChange→缓存全量清空）。安全原则是"句柄不等于授权"：能力句柄只是句柄，每次执行都重新过 OpenClawToolExecutor 治理链（审批、hooks、审计、工具策略），注册表元数据不等于真实能力。

## 关联连接

- [[Nacos]] — AI 注册中心与配置变更来源
- [[OpenClawNET]] — 集成的运行时主体
- [[AI Registry]] — Nacos 侧的 AI 资源治理模块
- [[MCP]] — 工具协议
- [[张善友]] — 作者
- [[AgentRuntime]] — 能力解析与执行入口
- [[摘要-mcp-v5-openclaw-net]] — 同项目协议升级篇
