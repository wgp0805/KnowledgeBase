---
title: "PiAgent"
type: entity
tags: [AI, Agent, 开源框架, pi-agent]
sources: [raw/01-articles/Pi-Agent 开源项目落地实战文档.md, raw/01-articles/Pi-Agent 智能体核心原理实战文档.md]
last_updated: 2026-08-04
---

## 定义
PiAgent（pi-agent）是一个 70K Star 的开源 Agent 框架，提供从 Demo 到生产环境落地的完整工程化能力，原生 TypeScript 版本，并提供 Python 复刻版。其核心价值在于封装了循环管控、上下文工程、工具调用容错等生产级稳定性与安全机制，让开发者无需从零踩坑。

> 注意：本实体指 70K Star 的开源 Agent 框架 pi-agent，与 [[PaiAgent]]（基于 DAG 工作流引擎、用 Qoder 搭建的 AI Agent 平台项目）是两个不同项目，勿混淆。
>
> 另注意：与 Mario Zechner 开发的 Pi（87.3k Stars 极简终端编码代理，系统提示词仅 ~1000 token）也是不同项目。Pi 侧重 token 极简主义和终端编码，pi-agent 侧重 Agent 工程化框架。详见 [[摘要-推荐一个节省token的AI编程神器]]。

## 关键信息

### Agent 本质公式
智能体底层原理：**Agent = 大模型 + 工具集 + 执行循环**。pi-agent 是对极简循环模型（200 行 read_file + write_file + while True）的工程增强版本。

### 三种使用方式
1. **学习参考**：通读源码，理解标准 Agent 工程架构，解决「Demo 能跑、上线崩溃」问题
2. **二次开发**：基于底层框架自定义工具、新增拦截钩子、改造上下文压缩策略
3. **直接落地**：不改动核心逻辑，仅配置提示词与工具列表，快速产出可上线 Agent

### 三大落地工程能力
1. **循环维护**：10 个全链路干预节点（Trace 生命周期钩子）管控无限循环、敏感内容、高危操作（详见 [[trace-turn]]）
2. **上下文工程**：工具输出截断机制 + 阈值驱动自动压缩，解决溢出与模型退化（详见 [[ContextEngineering]]）
3. **工具调用管理**：参数自动校验 + 调用前安全检查 + 调用后脱敏 + 错误回灌自愈（详见 [[error-feedback-self-healing]]）

## 关联连接
- [[Agent]] - 核心概念，pi-agent 是其工程化实现
- [[PaiAgent]] - 名字相近但不同的项目（DAG 工作流业务平台），需区分
- [[摘要-pi-agent-core-principles]] - 核心原理篇来源
- [[摘要-pi-agent-production-guide]] - 落地实战篇来源
- [[trace-turn]] - Trace/Turn 术语与 10 生命周期钩子
- [[ContextEngineering]] - 上下文工程能力
- [[error-feedback-self-healing]] - 工具错误自愈能力
- [[LoopEngineering]] - 循环工程方法论关联
