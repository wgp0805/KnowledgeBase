---
title: "MRTR"
type: concept
tags: [概念, MCP, 协议, 异步]
sources:
  - raw/09-archive/2026-08-02-MCP 第五版 × OpenClaw.NET：从协议升级到生态编排 - 张善友.md
last_updated: 2026-08-03
---

## 定义
MRTR（Multi Round-Trip Requests，多轮往返请求）是 MCP 第五版引入的机制，替代旧协议中「服务端主动请求客户端」的能力（如要求用户确认删除）。在无状态架构下，通过多轮携带状态的请求实现交互式流程。

## 关键信息
- **流程**：
  1. 客户端发起工具调用
  2. 服务端返回 `input_required`
  3. 客户端收集用户确认/参数
  4. 客户端携带 `inputResponses` + `requestState` 重新发起原始请求
  5. **任意服务端实例**继续完成任务
- **与 Harness 的互补**：OpenClaw.NET Harness 引擎可将 `input_required` 状态持久化到任务存储，用户响应后重新调度任务到任意 Worker 实例，实现「连接断、流程在、状态不丢」
- **意义**：解决无状态协议下交互式多轮流程的连续性，连接可以断，流程不会丢

## 关联连接
- [[MCP]] — 所属协议
- [[OpenClawNET]] — 主要采用者
- [[AgentHarness]] — 中断-恢复机制
- [[摘要-mcp-v5-openclaw-net]] — 来源
