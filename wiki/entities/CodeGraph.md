---
title: "CodeGraph"
type: entity
tags: [工具, 代码分析, MCP, 语义搜索]
sources: [raw/01-articles/2026-07-16-企业级落地方案：Docker 部署 CodeGraph 多项目统一 MCP 网关，附源码 - AI-Frontiers.md]
last_updated: 2026-07-17
---

## 定义

CodeGraph 是一款代码语义分析工具，能够为代码仓库构建知识库索引，支持通过 MCP 协议进行远程语义检索，帮助 AI 编程工具查找函数定义、类继承关系等语义信息。

## 关键信息

- **GitHub 仓库**：https://github.com/colbymchenry/codegraph
- **当前版本**：v1.4.0
- **运行模式**：原生仅支持 stdio 模式，不自带 HTTP/SSE/TCP 远程监听参数
- **安装方式**：提供 Linux x64 离线安装包，通过安装脚本部署
- **核心命令**：
  - `codegraph init <项目路径>` — 初始化代码知识库索引
  - `codegraph status <项目路径>` — 检查索引状态
  - `codegraph explore "查询内容" --path <项目路径>` — 测试查询
- **数据库**：索引存储在 `.codegraph/codegraph.db`
- **网关方案**：通过 mcp-remote 桥接（stdio → HTTP），配合 Docker 实现多项目统一访问

## 关联连接

- [[摘要-codegraph-mcp-gateway]] — 来源：Docker 部署多项目统一 MCP 网关方案
- [[MCP]] — 模型上下文协议
- [[Docker]] — 容器化部署
- [[ClaudeCode]] — 支持 MCP 的 AI 编程工具
- [[OpenCode]] — 支持 MCP 的 AI 编程助手
