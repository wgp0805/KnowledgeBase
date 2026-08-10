---
title: "VectorStore"
type: concept
tags: [RAG, 向量数据库, 向量检索]
sources: [raw/01-articles/2026-08-07-LangChain — RAG 构建知识库（理论） - VipSoft.md]
last_updated: 2026-08-10
---

## 定义
Vector Store（向量库）用于存储和检索向量化后的文档。LangChain 提供了统一的 VectorStore 接口，使开发者能用统一方式调用任意向量库（add_documents / delete / similarity_search）。

## 关键信息

### 统一接口（三个核心方法）
- **add_documents**：添加文档到向量库（只需提供向量模型，框架自动向量化）
- **delete**：根据 id 集合批量删除文档
- **similarity_search**：基于相似度检索与用户问题相关的文档

### 常用向量库选型
| 向量库 | 特点 | 适用规模 |
| --- | --- | --- |
| InMemory | 内存态 | 开发调试 |
| **Chroma** | 支持持久化到磁盘 | 中小规模 |
| Milvus | 分布式 | 大规模 |

### search 方法检索类型
| search_type | 说明 |
| --- | --- |
| similarity | 相似度检索（等同 similarity_search） |
| similarity_score_threshold | 相似度分数阈值过滤（不返回得分） |
| mmr | 基于 MMR 算法筛选，提升多样性 |

- 核心参数：k（返回数量，默认 4）、score_threshold（最小关联阈值）、fetch_k（MMR 输入量，默认 20）、lambda_mult（MMR 多样性，1 最小 0 最大，默认 0.5）、filter（按 metadata 筛选）
- 获取得分：similarity_search_with_relevance_scores 返回文档+得分

## 关联连接
- [[RAG]] — 向量库是 RAG 存储层
- [[Embeddings]] — 向量化的数据进入向量库
- [[TextSplitter]] — 切分后的文档被向量化后入库
- [[Retriever]] — 向量库可通过 as_retriever 转为检索器
- [[Chroma]] — 常用实现（中小规模）
- [[FAISS]] — 向量相似度搜索库
- [[LangChain]] — 所属框架
- [[摘要-langchain-rag构建知识库-理论]] — 来源