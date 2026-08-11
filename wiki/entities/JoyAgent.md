---
title: "JoyAgent"
type: entity
tags: [AI, Agent, 京东云, 开源]
sources: [raw/01-articles/京东员工：实习生、应届生结合JoyCoder写的代码一坨屎，我Code Review的时候真是一口老血吐屏幕上，这种情况怎么办啊？（附Agent面试题）.md]
last_updated: 2026-08-11
---

## 定义
JoyAgent 是京东云推出的 AI Agent 平台，其开源版本 JoyAgent-JDGenie 支持 ReAct 与 Plan-and-Execute 两种执行模式，面向供应链智能体、智能客服等电商场景，具备子 Agent 编排与高并发 DAG 执行能力。

## 关键信息
- 京东云 AI Agent 平台，开源项目为 JoyAgent-JDGenie
- 支持 ReAct（思考→行动→观察循环）与 Plan-and-Execute（先规划 DAG 再执行）两种模式
- 子 Agent 能力：Report、Search、Code、File 等独立子 Agent
- 架构特色：多 Agent 上下文支持、高并发 DAG 调度、跨任务工作流记忆
- 核心场景：将京东"自营零售数据 + 仓储物流网络 + 供应链履约系统"演进为可自主决策的供应链智能体
- 智能客服应用：混合方案，高频标准流程走工作流，复杂场景走 Agent 动态决策

## 关联连接
- [[京东]] — 所属公司
- [[JoyCoder]] — 同系 AI 编程工具
- [[ReAct_Agent]] — ReAct 模式
- [[Research-Plan-Execute-Review-Ship]] — Plan-and-Execute 范式
- [[智能客服Agent设计]] — 应用场景
- [[摘要-京东-agent面试题]] — 来源