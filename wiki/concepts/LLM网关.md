---
title: "LLM网关"
type: concept
tags: [AI, LLM, 网关, 多模型路由, 降级]
sources: [raw/01-articles/推荐一个牛逼的企业智能招聘系统.md]
last_updated: 2026-08-14
---

## 定义
LLM 网关（LLM Gateway）是统一管理多个大模型调用的中间层，负责模型路由、负载均衡、自动降级、Token 计费与监控，使业务代码与具体模型厂商解耦。

## 核心能力
- **多模型路由**：按 Agent 类型路由到不同模型（如视觉任务→qwen-vl-max，文本任务→qwen3-max，预测任务→deepseek-v4-flash）
- **多厂商主备**：Qwen / DeepSeek 双厂商，主备切换
- **自动降级**：主模型失败自动切换备模型
- **Token 计费**：每次调用真实记录 Token 消耗，喂给监控大盘
- **零代码切换**：切换模型、调整 Key 无需改动业务代码

## 架构位置
```
业务 Agent → LLM 网关（路由/降级/计费）→ 模型厂商 API
```

编排层（如 AgentScope）不直连大模型，通过适配器复用 LLM 网关的统一能力，实现编排层与模型层彻底解耦。

## 关联连接
- [[多智能体编排]] — 上游消费者
- [[AgentScope_Java]] — 编排层
- [[LangChain4j]] — 模型适配实现
- [[Qwen]] — 路由模型之一
- [[DeepSeek]] — 路由模型之一
- [[摘要-企业智能招聘系统]] — 来源
