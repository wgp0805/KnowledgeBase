---
title: "摘要-codegraph-deep-dive"
type: source
tags: [来源, CodeGraph, 代码分析, MCP]
sources: ["raw/09-archive/CodeGraph为什么突然这么火？.md"]
last_updated: 2026-07-20
---

## 核心摘要

[[苏三]]全面介绍 [[CodeGraph]]——一个本地优先的代码智能工具，专为 AI 编程助手设计。核心思想是预先构建代码知识图谱（基于 tree-sitter 解析 AST，提取函数/类/方法为节点、调用/继承/引用为边，存入本地 SQLite+FTS5），让 AI 直接查图而非反复 grep/Read。

官方测试数据：工具调用减少 71%，Token 消耗降低 57%，任务速度提升 46%，综合成本降低 35%。安装后通过 `codegraph init -i` 初始化，自动为 Claude Code/Cursor/Codex CLI/opencode/Hermes Agent 等配置 MCP 服务器。提供 10 个 MCP 工具（codegraph_context/trace/search/callers/callees/impact 等），支持增量同步。

## 关联连接
- [[CodeGraph]] — 核心实体
- [[TreeSitter]] — 底层 AST 解析引擎
- [[苏三]] — 文章作者
- [[MCP]] — 接入协议
- [[ClaudeCode]] — 兼容的 AI 编程工具
- [[OpenCode]] — 兼容的 AI 编程助手
- [[Cursor]] — 兼容的 AI 代码编辑器
- [[Docker]] — 已有网关部署方案
