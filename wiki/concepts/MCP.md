---
title: "MCP"
type: concept
tags: [AI, 协议, 外部服务]
sources: [raw/01-articles/40分钟学会Codex！"零基础"终级教程～【附完整文档】.md, raw/01-articles/全网最全！60分钟全面掌握Claude Code~【附完整文档】.md]
last_updated: 2026-05-19
---

## 定义
Model Context Protocol，解决 AI 与外部工具、外部服务连接的转接头协议，让 Agent 能访问外部数据源和工具。

## 关键信息
- MCP 服务占用 token 较多，难以同时存储很多
- 轻量外部工具正转向 Skill，重量的转向 CLI
- 使用时需配置 MCP 服务器地址和认证信息
- 典型应用：NotebookLM 知识库接入、Figma 设计稿读取
- Claude Code 率先发明 MCP，Codex 后续跟进支持

## 关联连接
- [[Agent]] — MCP 所属概念
- [[ClaudeCode]] — MCP 发明者
- [[Skill]] — 替代/互补方案
