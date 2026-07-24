---
title: "Agent 与 RAG 通信方式对比"
type: synthesis
tags: [RAG, Agent, MCP, FunctionCalling, 通信方式, 选型]
sources: []
last_updated: 2026-07-23
---

# Agent 与 RAG 通信方式对比

## 问题
当知识库规模变大（几百+文件）需要搭建真正的 RAG 系统时，Agent 与 RAG 之间的通信是否只能依赖 MCP？有无其他解决办法。

## 结论
**不是只有 MCP。** [[知识库-skill-solutions]] 方案四已明确指出 RAG 系统"通过 MCP 或 Tool 连接"。综合本库资料，Agent 访问 RAG 至少有四种主流路径，区别在于集成方式（进程内 / 跨进程）与通用性（标准化协议 / 私有调用）。

## 四种通信方式

### 方式一：Function Calling / @Tool（进程内集成，最底层）
[[FunctionCalling]] 是 Agent 调用工具的底层机制，MCP 本身也基于此模式工作。在 LangChain4j / Spring AI 中，用 `@Tool` 注解把"检索向量库"的方法直接暴露给 Agent：

```java
@Tool(description = "从知识库检索相关文档片段")
public String searchKnowledge(String query) {
    return vectorStore.similaritySearch(query);  // 直接调向量库
}
```

- **特点**：Agent 与 RAG 在同一进程，代码直接调向量库，无外部协议开销
- [[RAG]] 概念页中 LangChain4j 的 `ContentRetriever` 即此模式--把检索能力直接组装进 AI Service
- [[FunctionCalling]] 指出：Tools 是被动能力单元，"什么时候调、调几次"由上层 Agent 决定
- **适用**：用 Java 框架自己开发 Agent 的场景

### 方式二：MCP（标准化跨进程协议）
[[MCP]] 是"AI 与外部服务的转接头协议"，解决 Agent 如何连上别人写好的服务。

- 三种传输方式：`stdio`（本地进程）、`sse` / `ws`（远程 HTTP）
- **特点**：跨工具通用，[[ClaudeCode]] / [[Codex]] / [[OpenCode]] 均支持；但 [[MCP]] 占用 token 较多
- [[摘要-codegraph-mcp-gateway]] 是把代码知识库包装成 MCP 网关供多 Agent 调用的典型实践
- **适用**：使用现成 Agent 工具（如 Claude Code），让其访问自建 RAG 服务

### 方式三：直接 HTTP / REST API（RAG 作为独立服务）
[[摘要-RAG-KAG双引擎知识库系统]] 中的系统提供"近 200 个 API 端点"，[[摘要-rag-api-call]] 也展示了 RAG 可独立成一条问答链服务。

- **特点**：RAG 就是普通后端服务，Agent 用普通 HTTP 请求调用，拿 JSON 结果
- **适用**：RAG 已独立部署，Agent 是另一个独立系统（微服务架构）

### 方式四：Skill（轻量文件检索，非真 RAG）
[[知识库-skill-solutions]] 方案一推荐用 Skill + Grep/Read 检索。它不是真正的语义 RAG，但能解决 80% 问题，复杂度最低。

- **适用**：知识库尚未大到必须向量化的阶段，作为 RAG 的前置替代

## 选型对比

| 维度 | Function Calling / @Tool | MCP | HTTP API | Skill |
| --- | --- | --- | --- | --- |
| 集成位置 | 进程内 | 跨进程 | 跨系统 | Agent 内 |
| 通用性 | 框架内 | 跨工具标准 | 任意 HTTP 客户端 | 特定 Agent |
| 协议开销 | 无 | 有（占 token） | 有（网络） | 无 |
| 典型框架 | [[LangChain4j]] / [[SpringAI]] | [[ClaudeCode]] / [[Codex]] | [[FastAPI]] / Spring Cloud | [[ClaudeCode]] |
| 适用场景 | 自研 Java Agent | 现成 Agent 工具 | RAG 独立后端服务 | 小规模知识库 |

## 决策建议
1. **自己开发 Agent**（Spring AI / LangChain4j）→ 用 @Tool / ContentRetriever，进程内集成最省事
2. **用现成 Agent 工具**（Claude Code 等）→ 用 MCP，标准化跨工具
3. **RAG 已是独立后端** → 直接 HTTP API
4. **知识库还不大** → 先用 Skill，别急着上 RAG

一句话总结：**MCP 是"标准化插头"，Tool 是"焊死在电路板上的元件"，HTTP API 是"普通网线"**。三者本质都是让 Agent 拿到 RAG 检索结果，区别只在集成方式与通用性。

## 关联连接
- [[MCP]] - 标准化跨进程协议
- [[FunctionCalling]] - 工具调用底层机制
- [[RAG]] - 检索增强生成
- [[Agent]] - Agent 核心概念与扩展能力
- [[Skill]] - 轻量技能扩展
- [[知识库-skill-solutions]] - 知识库优先检索四种方案（方案四提出 MCP/Tool 连接）
- [[摘要-RAG-KAG双引擎知识库系统]] - RAG 独立服务 + API 端点实例
- [[摘要-rag-api-call]] - RAG 问答链独立服务化
- [[摘要-codegraph-mcp-gateway]] - MCP 网关包装知识库实践
- [[LangChain4j]] - ContentRetriever 进程内集成
- [[SpringAI]] - @Tool 注解机制
