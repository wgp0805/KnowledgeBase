---
title: "摘要-spring-ai-2-1发布"
type: source
tags: [来源, SpringAI, Java, Agent, 发布]
sources: ["raw/09-archive/2026-11-22 - 夯爆了，Spring AI 2.1 正式发布 ！.md"]
last_updated: 2026-11-24
---

## 核心摘要
java1234（锋哥）2026-11-22 解读 Spring AI 2.1.0 GA：距 2.0 GA 仅五个月，含 430+ 次提交，重心从"能用"转向"能撑起生产级 Agent"。**构建基线是 Spring Boot 4.2**，必须一起升级，依赖用 `spring-ai-bom:2.1.0`。七块新能力：①[[MCP协议]] 2026-07-28 无状态版本（无握手无会话，每请求自带协议版本与客户端能力，服务端 `spring.ai.mcp.server.protocol=MODERN` 一行切换，`@McpTool` 注解不用改；客户端可新老混用，新协议默认 `PER_REQUEST` 客户端）；②[[DecisionModel]]（是非题/单选题/打分题 + 概率，`isYes(0.9)` 决定"多有把握才执行"，已有 OpenAi/Ollama/SystemOne 三个实现，并被 `DecisionDocumentReranker`、`DecisionToolIndex` 采用）；③消息模型改为**有序片段列表**（TextPart/ReasoningPart/ToolCallPart/ToolResultPart/MediaPart/UnknownPart，Anthropic thinking 签名可原样回传，老方法 `getText()`/`getToolCalls()` 降级为视图，老代码不改）；④Session API 取代 `ChatMemory`（只追加事件日志、轮次边界压缩、`conversation_search` 回溯、`JdbcSessionRepository` 支持 PG/MySQL/MariaDB/SQL Server/H2，故意不提供默认会话，Advisor 无状态所以多实例可接力）；⑤工具调用确认与上限（`@Tool(requiresConfirmation=true)`、`ToolCallDecisions` allow/deny、暂停与恢复都是普通请求因此无状态；默认单工具每轮 40 次、总共 150 次，`spring.ai.tools.limits.*` 可调）；⑥向量库支持"自带向量"（`upsert()` + 直接用算好的查询向量检索，覆盖 pgvector/Qdrant/Redis/ES/OpenSearch/Neo4j/MongoDB Atlas/Typesense/MariaDB/Chroma/Couchbase 共 11 种，`TokenTextSplitter` 终于支持分块重叠）；⑦安全修复 13 个 CVE，护栏拒绝统一为 `GuardrailRefusal` / `ContentFilteredException`。另外新增 `OpenAiResponsesChatModel` 对接 `/v1/responses`（GPT-5.4 起"工具调用+推理强度"组合必须走 Responses API，切一行 `spring.ai.openai.chat.api=responses`），`Generation` 统一带 `FinishReasonCategory`。

> 版本边界：`ChatMemory` 相关类已标记废弃，计划 3.0.0 移除；新项目直接上 Session。

## 关联连接
- [[SpringAI]] — 本篇主角（已增量合并 2.1 内容）
- [[SpringBoot]] — 4.2 是 2.1 的构建基线
- [[DecisionModel]] — 2.1 最实用的新 API
- [[ChatMemory]] — 被 Session API 取代的旧机制
- [[Session]] — 会话管理概念（Web Session，注意区分）
- [[MCP协议]] — 2026-07-28 无状态版本
- [[ToolCalling]] — 工具调用确认与上限
- [[HITL]] — 敏感操作先问人
- [[VectorStore]] — 自带向量 upsert/检索
- [[RAG]] / [[Chunk分块]] — TokenTextSplitter 分块重叠
- [[Ollama]] — 本地跑 d1-omni:600m 演示 DecisionModel
