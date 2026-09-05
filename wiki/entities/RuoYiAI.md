---
title: "RuoYiAI"
type: entity
tags: [Java, AI, 开源, RuoYi, SpringAI, Langchain4j]
sources: [raw/01-articles/RuoYi 全栈 AI 平台开源了（若依）。.md]
last_updated: 2026-08-13
---

## 定义
RuoYi AI 是基于 [[RuoYi-Vue-Plus]] 扩展的开源全栈 AI 平台，用 Java 开发者熟悉的 Spring Boot 技术栈整合 RAG / Agent / 工作流等 AI 能力，定位为企业级 AI 应用落地参考与 Java AI 开发学习项目。作者 [[沉默王二]]。

## 关键信息
- **技术栈**：Java 17、Spring Boot 3.4、[[SpringAI]]、[[LangChain4j]]、Vue 3、Vben Admin、Milvus、Redis
- **核心能力**：本地 RAG 知识库、多模型接入、AI 流程编排、数字人、知识图谱、Agent Skills、自然语言生图
- **RAG 实现**：Langchain4j + BGE-large-zh-v1.5 中文向量模型，纯 Java 方案
- **平台集成**：FastGPT / 扣子 / DIFY 三平台统一接口 + 负载均衡
- **v3.0.0 分支**：新增 AI 流程编排、自然语言生成图表、Agent Skills
- **定位**：不追求单点极致（工作流不如 Dify、RAG 不如派聪明），胜在整合度与 Java 栈亲和力

## 关联连接
- [[摘要-ruoyi-ai平台]] — 来源摘要
- [[沉默王二]] — 作者
- [[SpringAI]] — 核心框架
- [[LangChain4j]] — RAG 框架
- [[RAG]] — 检索增强
- [[Skill]] — Agent Skills
- [[RuoYi-Vue-Plus]] — 上游基座
