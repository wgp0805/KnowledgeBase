---
title: "AI执行器"
type: concept
tags: [任务调度, AI, XXL-JOB, 集成]
sources: [raw/01-articles/xxl-job已正式接入AI.md]
last_updated: 2026-10-13
---

## 定义
AI 执行器是把 AI 调用封装成标准任务 Handler 的调度组件，让 AI 任务与普通任务共用同一套调度、重试、告警与日志。[[XXL-JOB]] 从 v3.1.0 引入 AI 执行器，内置多个基于 Bean 模式（`@XxlJob("handlerName")`）的 AI Handler，与 Spring AI、Ollama、Dify 打通；v3.4.0 又集成 [[OpenClaw]] 新增 `openClawJobHandler`。

## 关键信息
- **核心设计**：`prompt` 与 `input` 从**任务参数**动态获取而非硬编码——同一个 Handler 可以跑不同的 AI 任务，只需在调度中心配置不同任务参数
- **调度中心保持无感知**：只管"什么时候触发、触发哪个 Handler、传什么参数"；AI 执行器负责"怎么调 AI"
- **内置 Handler**：
  - `ollamaJobHandler` — 调用本地模型的标准化封装
  - `difyWorkflowJobHandler` — 触发 Dify 工作流；`baseUrl`/`apiKey` 已从执行器侧文件优化为任务参数动态配置，支持多 Dify 应用
  - `openClawJobHandler` — v3.4.0 新增
- **代价与边界**：AI 任务需单独部署 AI 执行器（普通执行器不能跑）、任务参数受数据库字段长度限制、**不支持流式输出**（同步等待，长文本生成耗时长）、内置 Handler 灵活性有限（复杂多轮对话与工具调用仍需自定义 Handler）
- **适用场景**：定时 AI 数据摘要/内容生成、定时触发 Dify 工作流、定时 AI 数据清洗；已在用 XXL-JOB 的项目可零额外基础设施接入

## 关联连接
- [[XXL-JOB]] — 载体框架
- [[Ollama]] — 本地模型后端
- [[Dify]] — 工作流后端
- [[OpenClaw]] — 集成对象
- [[SpringAI]] — 相关生态
- [[异步执行器]] — 相关概念
- [[摘要-xxl-job接入ai]] — 来源
