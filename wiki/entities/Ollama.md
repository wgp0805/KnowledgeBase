---
title: "Ollama"
type: entity
tags: [LLM, 本地部署, AI工具]
sources: [raw/09-archive/SpringAI.md, raw/09-archive/Ollama+DeepSeek本地部署（新人必看）.md]
last_updated: 2026-06-09
---

## 定义
Ollama 是一款用于本地化部署和管理大型语言模型的工具，支持 DeepSeek、Llama、Mistral 等开源模型，提供简单 API 和 CLI 交互，让用户能在自己电脑上运行 AI 模型。相比云端 API，Ollama 更安全、可离线运行。

## 关键信息

### 安装
- **macOS**：下载后拖入 Applications 即可，运行后菜单栏显示小图标，无界面
- **Windows**：通过 `OllamaSetup.exe /dir=<自定义目录>` 命令行安装，避免装到 C 盘
- 验证运行：浏览器访问 `http://localhost:11434/`

### 环境变量
- `OLLAMA_HOST`：监听地址，设为 `0.0.0.0:11434` 允许其他设备调用
- `OLLAMA_MODELS`：模型下载路径，避免默认下载到 C 盘（Windows）

### 使用
- 拉取模型：`ollama run deepseek-r1:7b`（支持断点续传，下载中断后重跑会继续）
- CLI 交互：拉取完成后直接在终端输入文本提问
- 硬件配置：GPU ≥8GB 显存（7B/8B 模型），≥16GB（14B 模型），内存 ≥16GB（推荐 32GB）
- 默认服务地址：http://localhost:11434
- Spring AI 集成：spring-ai-ollama-spring-boot-starter

### Embeddings（RAG 向量化）
- Ollama 也是 Embedding 模型的本地部署工具，关键在基于它部署的模型
- LangChain 集成：`OllamaEmbeddings(model="qwen3-embedding:0.6b", dimensions=1024)`，可选维度压缩节省存储
- qwen3-embedding:0.6b 是小模型中效果较好的一个，HuggingFace/Ollama 均支持部署（见 [[Embeddings]]）

## 关联连接
- [[SpringAI]] — Spring AI 集成
- [[DeepSeek]] — 支持的模型
- [[Embeddings]] — 向量化模型部署
- [[RAG]] — 知识库构建场景
- [[摘要-spring-ai]] — 来源
- [[摘要-Ollama+DeepSeek本地部署]] — 来源
- [[摘要-langchain-rag构建知识库-理论]] — Embeddings 来源
