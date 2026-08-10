---
title: "DashScope"
type: entity
tags: [阿里云, 模型API, 通义, AI]
sources: [raw/01-articles/JAVA中AI框架选型指南（2026）.md, raw/01-articles/2026-07-19-【RAG扫盲系列·3】从零开始构建你的RAG项目第二弹：API 调用大模型问答 - Alkaid2077.md]
last_updated: 2026-07-20
---

## 定义
阿里云的通义大模型 API 平台（DashScope API），为 Spring AI Alibaba 和 AgentScope-Java 等框架提供底层模型调用能力。

## 关键信息
- 提供通义系列模型的 API 调用接口
- Spring AI Alibaba 通过 DashScopeApi 构建 ChatModel
- 支持文本生成、图像生成、语音合成等多种模型能力
- 需申请阿里云百炼 API Key 使用
- 提供 OpenAI API 兼容模式，可直接使用 langchain_openai.ChatOpenAI 等 OpenAI SDK，仅需修改 base_url 为 `https://dashscope.aliyuncs.com/compatible-mode/v1`
- RAG 场景中可配合 FAISS 向量库和 LangChain 实现完整问答链
- **Embedding 服务**：提供 text-embedding-v3、text-embedding-v4 文本向量化模型，LangChain 用 DashScopeEmbeddings 接入；实测 text-embedding-v3 相似度区分度略优于 qwen3-embedding:0.6b（见 [[Embeddings]]）

## 关联连接
- [[SpringAI_Alibaba]] — 依赖 DashScope 的框架
- [[AgentScope_Java]] — 支持 DashScope 的框架
- [[Embeddings]] — 向量化模型服务
- [[RAG]] — 知识库构建场景
- [[摘要-java-ai框架选型指南-2026]] — 来源
- [[摘要-rag-api-call]] — RAG API 调用实践
- [[摘要-langchain-rag构建知识库-理论]] — Embedding 服务来源
- [[RAG]] — 检索增强生成
- [[Qwen]] — 通义千问模型
