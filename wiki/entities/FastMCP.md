---
title: "FastMCP"
type: entity
tags: [MCP, Python, AI工具, 框架]
sources: [raw/01-articles/为什么越来越多人用FastMCP？.md]
last_updated: 2026-08-20
---

## 定义
FastMCP 是建立在 MCP 协议之上的 Python 框架，用装饰器 + 类型提示把 MCP 协议复杂的底层细节封装成 Pythonic API，让开发者几行代码即可声明工具、资源、提示词。口号："用 Pythonic 的方式构建 MCP 应用"，从原型到生产一个框架全搞定。

## 关键信息
- **市场地位**：占所有语言 70% 的 MCP 服务器份额，日下载量百万级，GitHub 25.5k Star（vs 原生 SDK 405 Star，差距 60 倍），是 MCP 生态事实标准
- **官方认可**：2024 年 FastMCP 1.0 被正式并入官方 MCP Python SDK
- **三大支柱**：
  - **Servers**：把 Python 函数包装成符合 MCP 标准的工具、资源和提示词
  - **Clients**：支持完整协议，连接任何 MCP 服务器（本地/远程，编程/CLI）
  - **Apps**：给工具提供交互式 UI，直接在对话中渲染
- **核心 API**：
  - `@mcp.tool` — 声明工具函数，Schema/验证/文档自动生成
  - `@mcp.resource("uri")` — 注册资源（AI 随时可读的"知识卡片"）
  - `@mcp.dependency` — 依赖注入（数据库连接、配置等由框架统一管理）
  - `Context` — 上下文注入，工具函数通过 `ctx.deps` 获取依赖
- **工具 vs 资源**：工具是 AI 主动按需调用，资源是 AI 随时可读（内容相对稳定）
- **生产就绪**：内置最佳实践，自动处理传输协商、认证、协议生命周期
- **企业级方案**：Prefect Horizon 网关提供 SSO/RBAC/审计日志/可观测性
- **开源地址**：GitHub `PrefectHQ/fastmcp`，官方文档 gofastmcp.com，中文文档 fastmcp.cn

## 优缺点
**优点**：开发效率极高、市场占有率第一、官方认可、原型到生产全覆盖、三大支柱能力完整、Pythonic 设计
**缺点**：主要面向 Python 生态（Java/Go 需其他方案）、封装带来灵活性损失、学习曲线在 MCP 本身而非框架

## 适用场景
- 为 AI 应用接入外部工具（强烈推荐）
- 构建 MCP 服务器（强烈推荐，社区最大生态最全）
- 桌面 AI 客户端集成（Claude Desktop/Cursor 都支持 MCP）
- AI Agent 开发（MCP 是 Agent 调用工具的标准方式）
- 快速原型验证（10 行代码跑通 MCP 服务器）
- 非 Python 技术栈 / 需深度定制协议行为 → 需评估

## 关联连接
- [[MCP]] — FastMCP 建立的协议基础
- [[PrefectHorizon]] — FastMCP 企业级网关
- [[摘要-为什么越来越多人用FastMCP]] — 来源
- [[苏三]] — 解析文章作者
- [[ClaudeCode]] — MCP 发明者，FastMCP 服务器可接入
- [[LangChain4j]] — Java 生态 MCP 实现参考（非 Python 替代）
