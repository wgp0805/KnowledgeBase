---
title: "Embeddings"
type: concept
tags: [RAG, 向量化, 语义检索, Embedding]
sources: [raw/01-articles/2026-08-07-LangChain — RAG 构建知识库（理论） - VipSoft.md]
last_updated: 2026-08-10
---

## 定义
Embeddings（向量化）是将文本转换为高维向量的过程。语义相似的文本在向量空间中距离更近，这是语义检索（相似度搜索）的基础，是 RAG 知识库构建流水线的核心环节之一。

## 关键信息

### 常见开源向量模型
| 模型 | 参数量 | 维度 | 最大长度 | 核心特点 |
| --- | --- | --- | --- | --- |
| Qwen3-Embedding-0.6B | 0.6B | 1024 | 32K | MTEB 多语言 64.34，支持 MRL 维度压缩，多语言强 |
| jina-code-embeddings-0.5B | 0.5B | 896 | 32K | 代码检索 SOTA，MTEB Code 78.72%，15+ 编程语言 |
| BGE-M3 | 0.56B | 1024 | 8K | 稠密+稀疏+多向量混合检索，MIT 协议 |
| all-MiniLM-L6-v2 | 0.08B | 384 | 512 | 纯英文、推理快 50% |

### LangChain 支持的 Embedding 平台
| 模型类 | 提供方 |
| --- | --- |
| OpenAIEmbeddings | OpenAI |
| DashScopeEmbeddings | 阿里云百炼（text-embedding-v3/v4） |
| HuggingFaceEmbeddings | 本地开源模型 |
| OllamaEmbeddings | 本地开源模型（如 qwen3-embedding:0.6b） |

### 使用方法
- 关键在模型选择而不是工具（Ollama 只是工具，真正决定效果的是部署的模型）
- OllamaEmbeddings 示例：`OllamaEmbeddings(model="qwen3-embedding:0.6b", dimensions=1024)`，可选维度压缩节省存储
- 相似度衡量：余弦相似度（值越大越相似）
- 实测对比（"我要躺平/我爱工作/拒绝加班"）：text-embedding-v3 的相似度区分度（0.52/0.92/0.61）略优于 qwen3-embedding:0.6b

## 关联连接
- [[RAG]] — 向量化的应用场景
- [[TextSplitter]] — 向量化前的切分步骤
- [[VectorStore]] — 向量化后的存储环节
- [[LangChain]] — 所属框架
- [[Ollama]] — 本地 Embedding 平台
- [[DashScope]] — 阿里云百炼 Embedding
- [[Qwen]] — qwen3-embedding 模型底座
- [[摘要-langchain-rag构建知识库-理论]] — 来源