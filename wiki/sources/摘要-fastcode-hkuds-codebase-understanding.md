---
title: "摘要-fastcode-hkuds-codebase-understanding"
type: source
tags: [来源, 代码库理解, AI编程, FastCode]
sources: ["raw/01-articles/比 Claude Code 快4倍、消耗节省接近一半！港大开源的代码库理解神器.md"]
last_updated: 2026-07-20
---

## 核心摘要

香港大学 HKUDS 团队开源的 FastCode，是一个面向代码库理解与分析的开源框架。核心思路是"侦察优先（Scouting-First）"——先构建代码的语义地图和结构关系图，再按需精准定位加载代码分析，而非像传统做法满仓库翻文件。

性能对比 Cursor 快约 3 倍、比 Claude Code 快约 4 倍，成本节省 44-55%，Token 效率最高达 10 倍节省。技术架构包括分层 AST 索引、混合检索（语义向量+BM25）、调用/依赖/继承关系图谱、预算感知决策。支持 MCP 协议接入 Cursor/Claude Code/Windsurf，也提供 Web 界面、CLI、REST API 和飞书机器人等多种使用方式。

## 关联连接
- [[FastCode]] — 香港大学开源的代码库理解框架
- [[HKUDS]] — 香港大学数据科学团队
- [[Cursor]] — AI 代码编辑器，FastCode 对比基准
- [[ClaudeCode]] — Anthropic 终端 AI Agent，FastCode 对比基准
- [[MCP]] — Model Context Protocol，FastCode 支持的接入协议
