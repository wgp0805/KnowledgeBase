---
title: "FastCode"
type: entity
tags: [开源工具, 代码库理解, AI编程]
sources: ["raw/01-articles/比 Claude Code 快4倍、消耗节省接近一半！港大开源的代码库理解神器.md"]
last_updated: 2026-07-20
---

## 定义

FastCode 是香港大学 HKUDS 团队开源的代码库理解与分析框架，采用"侦察优先（Scouting-First）"策略，先构建代码语义地图和结构关系图，再按需精准加载代码分析。

## 关键信息

- **核心方法**：侦察优先（Scouting-First），先建立索引再按需读取，而非传统做法满仓库翻文件
- **技术架构**：分层 AST 索引 + 混合检索（语义向量+BM25）+ 关系图谱（调用图/依赖图/继承图）+ 预算感知决策
- **性能表现**：比 Cursor 快约 3 倍，比 Claude Code 快约 4 倍；成本节省 44-55%；Token 效率最高达 10 倍
- **支持语言**：Python、JavaScript/TypeScript、Java、Go、Rust、C/C++、C#
- **接入方式**：Web 界面（端口 5000）、CLI、REST API、MCP 服务（接入 Cursor/Claude Code/Windsurf）、飞书机器人
- **环境要求**：Python 3.12+，Git

## 关联连接
- [[摘要-fastcode-hkuds-codebase-understanding]] — 来源
- [[HKUDS]] — 开发团队
- [[Cursor]] — 对比基准
- [[ClaudeCode]] — 对比基准
- [[MCP]] — 支持的接入协议
- [[Ripgrep]] — 同类代码搜索工具
- [[Scouting-First]] — 核心策略
