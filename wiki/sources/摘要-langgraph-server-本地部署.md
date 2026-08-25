---
title: "摘要-langgraph-server-本地部署"
type: source
tags: [来源, LangGraph, 本地部署, llama.cpp, 离线Agent]
sources: [raw/01-articles/2026-08-24-LangGraph Server Agent 框架本地部署指南 - lyshark.md]
last_updated: 2026-08-25
---

## 核心摘要
lyshark 分享基于 LangGraph Server 搭建本地离线 AI Agent 的完整部署流程，适配 Windows 开发环境，全程无需调用公有大模型接口，实现纯本地化 AI 推理与工作流编排。核心区分：LangGraph 底层 Python 库 MIT 协议永久免费无额度限制；但 LangGraph Server 即便本地自托管 Lite 模式也受许可约束，每年最多 100 万次节点运行额度（工作流内部节点执行次数，非接口请求次数），超需购企业版。部署流程：pip 装 langgraph-cli[inmem] + langgraph-sdk → 克隆 new-langgraph-project 模板 → 配 .env 指向本地 llama.cpp → `langgraph dev` 启动内存开发服务（API 2024 端口 + Studio UI）→ llama-server 加载 GGUF 量化模型 → 编写 graph.py 工作流。SDK 支持 SSE 流式输出、同步调用、批量执行、会话记忆。

## 关键信息
- **协议与额度**：LangGraph Python 库 MIT 永久免费；LangGraph Server Lite 模式年 100 万次节点执行额度，超需企业版
- **核心依赖版本**：langchain 1.3.15、langgraph-api 0.12.6、langgraph-cli 0.4.31、langgraph-runtime-inmem 0.32.6、langgraph-sdk 0.4.2
- **部署六步**：
  1. pip install langgraph-cli[inmem] + langgraph-sdk（清华源加速）
  2. git clone new-langgraph-project 模板 + pip install -e .
  3. 配 .env（LANGSMITH_PROJECT + OPENAI_API_KEY=dummy + OPENAI_BASE_URL=http://127.0.0.1:11433/v1）
  4. set PYTHONUTF8=1 + set PYTHONIOENCODING=utf-8 + langgraph dev（dev 测试/build 部署）
  5. llama-server.exe -m qwen2.5-1.5b-instruct-q4_k_m.gguf --host 127.0.0.1 --port 11433 -c 4096 --jinja
  6. 编写 src/agent/graph.py（StateGraph + add_node + add_edge + compile）
- **服务端口**：API http://127.0.0.1:2024，Studio UI https://smith.langchain.com/studio/?baseUrl=http://127.0.0.1:2024
- **SDK 流式调用**：`client.runs.stream(None, "agent", input={...})`，事件类型 metadata/values
- **Windows 编码坑**：必须先 set PYTHONUTF8=1 和 PYTHONIOENCODING=utf-8 避免乱码
- **本地模型**：qwen2.5-1.5b-instruct-q4_k_m.gguf，llama.cpp 加载，--jinja 开启模板解析

## 关联连接
- [[LangGraph]] — LangChain 团队 Python AI Agent 编排框架
- [[LangChain]] — LangGraph 底层依赖
- [[llama.cpp]] — 本地 GGUF 量化模型推理引擎
- [[Qwen]] — 通义千问本地量化模型
