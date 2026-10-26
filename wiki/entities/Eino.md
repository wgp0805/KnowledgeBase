---
title: "Eino"
type: entity
tags: [实体, Go语言, AI框架, Agent, 字节跳动]
sources: [raw/09-archive/为什么越来越多人用Eino？.md]
last_updated: 2026-10-22
---

## 定义
Eino 是字节跳动 [[CloudWeGo]] 团队开源的 **Go 语言大模型应用开发框架**，定位清晰：**让 Go 开发者用 Go 的方式构建生产级 AI 应用和 Agent，不需要绕道 Python**。它把 AI 应用开发的那套工程抽象（编排、流式处理、类型安全、并发管理、运行时稳定性）用 Go 的工程哲学重新实现了一遍，而非"Go 版 LangChain"的翻译。

## 关键信息
- **解决的痛点**：调 API 不难，难的是**编排**——判断意图、调用工具、把结果塞回模型继续推理、处理流式输出、管理多轮上下文、出错重试或切换备用模型。Python 有 [[LangChain]]、[[LlamaIndex]]，Go 生态长期没有对等物
- **四层架构**：
  - **组件层** —— ChatModel、Tool、Retriever、ChatTemplate 抽象，每个组件有自己的输入输出类型与流式范式；官方提供 OpenAI、Claude、Gemini、Ollama、Elasticsearch 等实现
  - **编排层** —— 用有向图 Graph 连组件，节点是组件实例、边是数据流通道；承担类型检查、流式处理、并发管理
  - **Agent 开发套件 ADK** —— 核心 ChatModelAgent 内置 [[ReAct]] 循环；DeepAgent 用于复杂任务拆解与委派
  - **运行时能力** —— 流式处理、类型检查、Callback 切面、中断恢复
- **类型安全**：`graph.AddEdge` 时编译期检查上下游类型是否匹配，不匹配直接编译失败。典型反例是把 ChatModel 节点输出（`*schema.Message`）连到期望 `[]*schema.Document` 的 Retriever 节点——"这不是多一点代码的问题，这是少一次线上事故的问题"
- **流式处理四种自动适配**：自动拼接（下游只接受非流）、自动装箱（下游要流上游给非流）、自动合并（多流汇聚到一个节点）、自动复制（一个流分发给多个下游避免竞争）。开发者只需声明自己需要什么，不必考虑"上游给的是流还是非流"
- **Agentic Runtime（v0.9）**：
  - **Cancel** —— 从外部主动终止正在运行的 Agent，支持安全点取消与 checkpoint 持久化
  - **Model Retry** —— 重试决策可读取模型输出、拒绝不满足条件的输出、修改下一次输入
  - **Model Failover** —— 主模型调用失败后切换备用模型，支持优先复用上一次成功的模型
  - **Middleware** —— 在 ReAct 循环的生命周期点位注入行为（上下文压缩、工具搜索、文件系统操作）
  - **中断与恢复** —— 任意节点中断、精确恢复，Agent 执行到某节点时暂停等人工输入，然后从断点继续；否则跑了十分钟的 Agent 因一次人工确认就要全部重来
- **Graph vs Agent**：Graph 是确定性编排（明确知道每一步做什么），Agent 是自主决策（模型自己决定下一步）；Eino 同时支持，且 Graph 可包装成 Tool 给 Agent 用，实现"确定性流程 + 自主决策"的混合
- **与 LangChain 对比**：Go/Python；编译期检查/运行时检查；Goroutine 单机 2000+ 连接 vs Thread/Async 200+ 连接时延迟显著；内存启动约 30MB vs 约 200MB；显式 Graph vs Chain 模式易写成面条代码；无缝对接 Hertz/Kitex/Gorm vs 需额外集成；流式处理框架全自动 vs 部分自动
- **优点**：Go 原生不绕道 Python；类型安全；流式自动适配；Agent 运行时能力完善；高并发低资源；字节跳动内部验证
- **缺点**：生态还在成长（组件数量与第三方集成与 Python 生态有差距）；API 仍在演进（v0.9 部分 API 标记"不推荐使用"）；Go 开发者 AI 经验相对少；不适合完全不懂 Go 的团队
- **适用场景**：Go 微服务接入 AI 能力、高并发 AI 网关/Agent 服务、需要类型安全的生产级应用、复杂 Agent 工作流、确定性流程编排 —— 均强烈推荐；Java/Python 技术栈团队（选 Spring AI / LangChain）与需大量第三方集成的场景需评估
- **安装**：`go get github.com/cloudwego/eino@latest`
- **官方地址**：https://github.com/cloudwego/eino ，文档 https://www.cloudwego.io/docs/eino/

## 关联连接
- [[CloudWeGo]] — 开源团队与生态
- [[字节跳动]] — 母公司
- [[LangChain]] / [[LlamaIndex]] / [[LangGraph]] — Python 生态对照
- [[GoogleADK]] — 借鉴的设计思路
- [[ReAct]] — ChatModelAgent 内置循环
- [[GraphWorkflow]] — 确定性编排路线
- [[AgentRuntime]] — Agentic Runtime 能力
- [[Middleware]] — ReAct 循环中的中间件注入
- [[Golang]] — 宿主语言
- [[摘要-为什么越来越多人用eino]] — 来源
