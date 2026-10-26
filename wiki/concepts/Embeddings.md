---
title: "Embeddings"
type: concept
tags: [RAG, 向量化, 语义检索, Embedding]
sources: [raw/01-articles/2026-08-07-LangChain — RAG 构建知识库（理论） - VipSoft.md, "raw/09-archive/2026-10-23-Spring AI Alibaba -- 文生图、文生音及向量化 - NE_STOP.md"]
last_updated: 2026-10-26
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

### Spring AI Java 侧用法（DashScope，2026-10-23 NE_STOP 教程）
注入 `EmbeddingModel` 后：`embeddingModel.call(new EmbeddingRequest(List.of(msg), DashScopeEmbeddingOptions.builder().withModel("text-embedding-v3").build()))` 返回 EmbeddingResponse（`getResult().getOutput()` 为 float 数组）；不传 Options 时走全局配置 `spring.ai.dashscope.embedding.options.model=text-embedding-v3`。嵌入原理：将文本、图形、视频转换为浮点数数组，核心目标是把语义编码进向量；text-embedding-v3 在 Java/Spring AI 生态可经 DashScope 直接使用。

## 知识冲突
- **维度与检索精度（2026-10-26 标注）**
  - 旧说法（本页）：Qwen3-Embedding 支持 MRL 维度压缩，1024 维可降维使用以省存储——隐含"维度并非越高越好"
  - 新说法（[[摘要-spring-ai-alibaba-文生图文生音向量化]]，2026-10-23）："向量数据库维度越高，查询精准度也越高，查询效果越好"
  - 两种说法并列保留（**状态：⏳ 待查**）；后一种过于绝对，忽略高维的存储/计算成本与 MRL 压缩实践，详见 [[向量数据库]]

## 关联连接
- [[RAG]] — 向量化的应用场景
- [[TextSplitter]] — 向量化前的切分步骤
- [[VectorStore]] — 向量化后的存储环节
- [[LangChain]] — 所属框架
- [[Ollama]] — 本地 Embedding 平台
- [[DashScope]] — 阿里云百炼 Embedding
- [[Qwen]] — qwen3-embedding 模型底座
- [[摘要-langchain-rag构建知识库-理论]] — 来源
- [[摘要-spring-ai-alibaba-文生图文生音向量化]] — 来源（Spring AI Java 侧用法）