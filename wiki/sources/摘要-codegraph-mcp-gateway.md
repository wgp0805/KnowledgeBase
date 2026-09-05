---
title: "摘要-codegraph-mcp-gateway"
type: source
tags: [来源, MCP, CodeGraph, Docker, 代码知识库]
sources: [raw/01-articles/2026-07-16-企业级落地方案：Docker 部署 CodeGraph 多项目统一 MCP 网关，附源码 - AI-Frontiers.md]
last_updated: 2026-07-17
---

## 核心摘要

本文介绍企业级 CodeGraph 多项目统一 MCP 网关的 Docker 部署方案。通过将一个父级目录下的多个项目批量构建 CodeGraph 知识库，并使用一个 Docker 容器、一个对外端口提供远程 MCP 访问，解决多项目切换检索语义信息时端口管理混乱的问题。方案采用 mcp-remote 桥接（stdio → HTTP）方式，更适合生产环境，支持在线构建镜像后离线部署。

## 关键信息

- **项目地址**：https://github.com/dora-wang-x/codegraph-mcp-gateway
- **核心组件**：CodeGraph CLI（代码语义分析）、supergateway（stdio→HTTP 桥接）、Docker 容器化
- **部署架构**：服务端项目集合目录 → Docker 挂载 → 批量初始化 → 统一网关入口
- **访问方式**：http://远程机器:8000/project-a/mcp、http://远程机器:8000/project-b/mcp
- **配置要点**：`.env` 文件配置 `HOST_PROJECTS_PATH`（项目路径）和 `HOST_PORT`（对外端口）
- **客户端支持**：OpenClaud 和 OpenCode 均支持 MCP 配置

## 关联连接

- [[MCP]] — 模型上下文协议
- [[Docker]] — 容器化部署技术
- [[CodeGraph]] — 代码语义分析工具（待创建）
- [[ClaudeCode]] — Anthropic AI 编程工具
- [[OpenCode]] — 开源 AI 编程助手
