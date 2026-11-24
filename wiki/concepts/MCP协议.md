---
title: "MCP协议"
type: concept
tags: [概念, 协议, Agent, 工具接入]
sources: [raw/09-archive/2026-09-20 - 万字详解 10 道 AI Agent 高频面试题.md, raw/09-archive/REA 保姆级教程：DeepSeek Harness 实操.md, "raw/09-archive/2026-11-22 - 夯爆了，Spring AI 2.1 正式发布 ！.md"]
last_updated: 2026-11-24
---

## 定义
MCP（Model Context Protocol，模型上下文协议）是 Anthropic 提出的开放协议，用于标准化 Agent 与外部工具/数据源的连接方式，解决"每个 Agent 都要为每个工具写适配器"的碎片化问题。

## 关键信息
- **核心思想**：把工具接入标准化，一次实现到处复用
- **与 Function Calling 关系**：正交关系，工具形态/接入协议/路由策略是三个独立维度
  - Function Calling 是模型调用工具的方式（工具形态）
  - MCP 是工具接入的协议（接入协议）
  - 路由策略决定用哪个工具（路由策略）
- **应用**：Claude Code、Codex 等主流 Agent 均支持 MCP 连接外部服务
- **规模案例**：[[REA]] 6.4.0 把 170 个逆向工具全部打包为 MCP 工具（见 [[摘要-rea保姆级教程-deepseek-harness实操]]）

## 不同 Harness 的 MCP 配置方式差异（2026-10-14）
同一 MCP 服务器在不同 Agent Harness 下的接入形态不同，**MCP 协议本身是标准的，配置文件格式是各家私有的**：
- **Codex / Claude Code**：读 `mcpServers` JSON 配置
- **DeepSeek Harness**：不读 JSON，用 [[Cordis]] 的 YAML 补丁文件 `~/.dsh/cordis.patch.yml`，`insert` 一段 `@deepseek-ai/dsh-mcp-client` 插件配置，`transport: stdio` 表示 Harness 自己用 npx 启动服务器进程

## MCP 2026-07-28 无状态版本（来源：[[摘要-spring-ai-2-1发布]]）
这一次是协议层的大改：**没有握手、没有会话**，每个请求自带协议版本与客户端能力。

- **服务端收益**：不再持有会话状态，水平扩展变简单（任意实例都能处理任意请求，不需要粘性路由）
- **客户端收益**：客户端不持有会话、创建成本低，因此默认可以**每个 ChatClient 请求一个客户端**（`PER_REQUEST`），按用户身份隔离调用变得自然
- **迁移成本极低**：[[SpringAI]] 2.1 中服务端只需 `spring.ai.mcp.server.protocol=MODERN` 一行，原有 `@McpTool`、`@McpResource` 注解不用改
- **新旧可共存**：客户端可同时连老协议服务与 `protocol: MODERN` 的新服务，同一个工具提供者会把两边工具一起交给模型
- **理解要点**：无状态不等于无能力——它把"连接期上下文"从服务端挪到了每次请求的报文里，代价是请求变大，换来的是可扩展性

## 关联连接
- [[摘要-10道ai-agent高频面试题]] — 来源
- [[摘要-rea保姆级教程-deepseek-harness实操]] — 来源（DSH MCP 接入差异 + REA 170 工具案例）
- [[MCP]] — 相关实体
- [[FunctionCalling]] — 正交关系
- [[工具路由]] — 独立维度
- [[Agent]] — 应用场景
- [[DeepSeekHarness]] — YAML 补丁接入的代表 Harness
- [[REA]] — 大规模 MCP 工具化案例
- [[Cordis]] — DSH 补丁机制底座
- [[SpringAI]] — 2.1 支持 MODERN 协议的服务端与客户端
- [[摘要-spring-ai-2-1发布]] — 来源（2026-07-28 无状态协议落地）