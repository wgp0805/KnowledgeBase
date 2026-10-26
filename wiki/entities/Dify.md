---
title: "Dify"
type: entity
tags: [AI平台, LLMOps, 开源, RAG, Agent]
sources: [raw/09-archive/竟然还有小伙伴不知道这个AI学习路线！！.md, raw/01-articles/2026-10-05-小白也能上手的 LoRA 微调：五步走通训练到落地.md, raw/09-archive/xxl-job已正式接入AI.md]
last_updated: 2026-10-13
---

## 定义
Dify 是开源的 LLMOps（大模型运营）平台，支持通过可视化界面搭建知识库和 Agent，集成文档上传、向量化检索、大模型接入等功能，适合产品经理和运营人员零代码构建 AI 应用。

## 关键信息
- 核心能力：文档上传 → 向量化建库 → 接入 API Key → 开聊
- 支持接入多种大模型：[[DeepSeek]]、[[Kimi]]、[[Qwen]] 等
- 开源，界面友好，像"搭积木"一样搭建 AI 应用
- 与 [[Coze]] 同为推荐的入门级工具，但 Dify 更偏 RAG/知识库场景
- **自训模型接入（2026-10-05，详见 [[摘要-lora微调五步教程]]）**：模型供应商选 **OpenAI-API-compatible**，填 Base URL / API Key / model_id 三项即可把自训 LoRA 模型（[[LlamaFactory]] 起的兼容服务）接进应用对话测试；model_id 必须与 API 服务一致，连接失败先查服务是否启动、配置对不对、网络端口通不通
- **被 XXL-JOB 定时触发（2026-10-13，详见 [[摘要-xxl-job接入ai]]）**：`difyWorkflowJobHandler` 可在调度中心按 Cron 触发 Dify 工作流，`inputs`/`user` 从任务参数动态传入。`baseUrl` 与 `apiKey` 早期需放在执行器侧文件，后续版本优化为任务参数动态配置，支持多 Dify 应用集成——开箱即用，是 XXL-JOB AI 执行器最推荐的场景之一

## 关联连接
- [[摘要-ai大模型学习路线]] — 来源
- [[摘要-lora微调五步教程]] — 来源（自训 LoRA 模型接入）
- [[LlamaFactory]] — 产生自训模型的框架
- [[LoRA]] — 接入的微调方法
- [[Coze]] — 同类竞品
- [[RAG]] — 核心应用场景
- [[Agent]] — Agent 搭建能力
- [[Chroma]] — 向量数据库（同类技术栈）
- [[XXL-JOB]] — 通过 AI 执行器定时触发 Dify 工作流
- [[AI执行器]] — 触发机制
