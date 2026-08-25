---
title: "llama.cpp"
type: entity
tags: [工具, 本地推理, GGUF, 量化模型, 开源]
sources: [raw/01-articles/2026-08-24-LangGraph Server Agent 框架本地部署指南 - lyshark.md]
last_updated: 2026-08-25
---

## 定义
llama.cpp 是本地 GGUF 量化模型推理引擎，支持在本地 CPU/GPU 上运行量化后的大语言模型，无需公网调用。通过 llama-server 可暴露 OpenAI 兼容 API，作为本地大模型服务供 LangGraph、应用等调用。

## 关键信息
- **核心组件**：llama-server.exe（服务端，暴露 HTTP API）
- **启动命令示例**：`llama-server.exe -m qwen2.5-1.5b-instruct-q4_k_m.gguf --host 127.0.0.1 --port 11433 -c 4096 --jinja`
- **关键参数**：
  - `-m`：指定 GGUF 量化模型文件
  - `--host/--port`：监听地址端口
  - `-c`：上下文长度（如 4096）
  - `--jinja`：开启 jinja 模板解析，保证消息交互格式正确
- **OpenAI 兼容**：暴露 `/v1` 接口，可被 LangGraph、ChatOpenAI 客户端等直接调用
- **配合 LangGraph**：.env 配置 `OPENAI_BASE_URL=http://127.0.0.1:11433/v1` + `OPENAI_API_KEY=dummy` 即可纯本地调用
- **适用场景**：本地离线 AI Agent、私有化部署、功能调试、轻量化 AI 场景

## 关联连接
- [[摘要-langgraph-server-本地部署]] — 来源
- [[LangGraph]] — 配合使用的编排框架
- [[Qwen]] — 常用量化模型
