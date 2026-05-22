---
title: "Ollama"
type: entity
tags: [LLM, 本地部署, AI工具]
sources: [raw/01-articles/SpringAI.md]
last_updated: 2026-05-22
---

## 定义
Ollama 是一款用于本地化部署和管理大型语言模型的工具，支持多种开源模型（LLaMA、DeepSeek 等），提供简单的 API 接口，让用户能在自己电脑上运行 AI 模型。

## 关键信息
- 硬件配置：GPU ≥8GB 显存（7B/8B 模型），≥16GB（14B 模型），内存 ≥16GB（推荐 32GB）
- 模型存储：通过环境变量 OLLAMA_MODELS 指定安装路径
- 默认服务地址：http://localhost:11434
- 使用 Spring AI 集成：spring-ai-ollama-spring-boot-starter
- 支持 DeepSeek-R1 系列模型（1.5B/7B/14B 等版本）

## 关联连接
- [[SpringAI]] — Spring AI 集成
- [[DeepSeek]] — 支持的模型
- [[摘要-spring-ai]] — 来源
