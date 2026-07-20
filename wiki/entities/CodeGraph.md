---
title: "CodeGraph"
type: entity
tags: [工具, 代码分析, MCP, 语义搜索]
sources:
  - raw/01-articles/2026-07-16-企业级落地方案：Docker 部署 CodeGraph 多项目统一 MCP 网关，附源码 - AI-Frontiers.md
  - raw/01-articles/CodeGraph为什么突然这么火？.md
last_updated: 2026-07-20
---

## 定义

CodeGraph 是一个本地优先的代码智能工具，专为 AI 编程助手设计。核心思想是预先用 tree-sitter 解析代码构建知识图谱（函数/类/方法为节点，调用/继承/引用为边，存入本地 SQLite+FTS5），让 AI 直接查图而非反复 grep/Read。

## 关键信息

- **GitHub 仓库**：https://github.com/colbymchenry/codegraph
- **开发者**：colbymchenry
- **Star**：2万+（截至 2026-07-18，曾登 GitHub Trending 第二位）
- **协议**：MIT
- **当前版本**：v1.4.0
- **核心架构**：
  - **AST 解析层**：tree-sitter 解析源码，支持多语言增量解析
  - **图谱构建层**：提取节点（函数/类/方法/接口/路由/组件）+ 边（调用/导入/继承/引用/路由绑定）
  - **存储层**：本地 SQLite 数据库 + FTS5 全文检索
- **性能数据**（7 个真实代码库测试）：
  - 工具调用减少 71%
  - Token 消耗降低 57%
  - 任务执行速度提升 46%
  - 综合成本降低 35%
- **安装方式**：
  - 一键安装脚本（自带运行时，无需 Node.js）
  - npm 全局安装（`npm install -g @colbymchenry/codegraph`）
  - 交互式安装器（`codegraph install --yes`，自动检测已装 AI 代理并配置 MCP）
- **核心命令**：
  - `codegraph init -i` — 交互式初始化项目索引（创建 `.codegraph/` 目录）
  - `codegraph uninit` — 从项目中移除 CodeGraph
  - `codegraph index --force` — 强制重建索引
  - `codegraph sync` — 增量更新索引
  - `codegraph status` — 查看索引统计信息
  - `codegraph query <关键词>` — 按名称搜索符号
  - `codegraph callers <符号名>` — 查找谁调用了某函数
  - `codegraph callees <符号名>` — 查找某函数调用了谁
  - `codegraph impact <符号名> --depth 2` — 变更影响分析
  - `codegraph affected` — 查找受改动影响的测试文件
  - `codegraph serve --mcp` — 启动 MCP 服务器
- **MCP 工具（10 个）**：
  - `codegraph_context` — 一次获取入口点、相关符号和代码片段
  - `codegraph_trace` — 追踪两个符号间完整调用路径
  - `codegraph_search` — 按名称搜索符号
  - `codegraph_callers` — 找出函数调用方
  - `codegraph_callees` — 找出函数调用依赖
  - `codegraph_impact` — 分析修改影响范围
- **数据安全**：纯本地运行，代码不上传第三方服务器
- **自动增量同步**：文件监听器自动检测变化并增量更新索引
- **运行模式**：原生仅支持 stdio 模式，不自带 HTTP/SSE/TCP 远程监听参数
- **网关方案**：通过 mcp-remote 桥接（stdio → HTTP），配合 Docker 实现多项目统一访问

## 关联连接

- [[摘要-codegraph-deep-dive]] — 来源：CodeGraph 深度解析
- [[摘要-codegraph-mcp-gateway]] — 来源：Docker 部署多项目统一 MCP 网关方案
- [[TreeSitter]] — 底层 AST 解析引擎
- [[MCP]] — 模型上下文协议
- [[Docker]] — 容器化部署
- [[ClaudeCode]] — 支持 MCP 的 AI 编程工具
- [[OpenCode]] — 支持 MCP 的 AI 编程助手
- [[Cursor]] — 兼容的 AI 编辑器
- [[苏三]] — 文章作者
