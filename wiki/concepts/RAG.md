---
title: "RAG"
type: concept
tags: [AI, RAG, 检索增强, 知识库]
sources: [raw/01-articles/LangChain4j 来了，Java AI智能体开发再次起飞。。。.md, raw/01-articles/腾讯面试官："为什么 Claude Code 不用 RAG 检索代码，而是 grep？"我："因为...我也不知道"，他沉默了。.md]
last_updated: 2026-05-20
---

## 定义
Retrieval-Augmented Generation（检索增强生成），把资料切块向量化存入向量库，提问时先检索相关片段再拼入 Prompt 给模型，解决模型无法知道私有/最新知识的问题。

## 关键信息

### LangChain4j RAG 架构
- **DocumentLoader**：从文件/URL/数据库加载原始文档
- **DocumentSplitter**：切块（按段落/句子/token）
- **EmbeddingModel**：文本转向量
- **EmbeddingStore**：向量库（Pinecone/Milvus/PgVector/Elasticsearch）
- **ContentRetriever**：组合以上，对外提供检索

### 两条流水线
1. **Indexing Pipeline（离线）**：原始数据→加载文档→切块→向量化→写入向量库
2. **Retrieval & Generation Pipeline（在线）**：用户问题→向量化→相似度检索→Top-K→拼入 Prompt→LLM→答案
3. 两条流水线共享同一个 Embedding 模型和向量库（一致性是关键）

### 关键实践
- RAG 关键不在框架，而在切分策略（段落完整性、块大小、重叠设置）
- 换向量库的影响往往不如调切分策略大

## 代码搜索场景的局限性

### 为什么 Claude Code 放弃了 RAG
1. **语义相似度不适用于代码**：代码需要精确匹配，非"大概对"的语义匹配。`createD1HttpClient` 与 `buildD1HttpClient` 语义近但功能不同
2. **索引同步成本高**：代码持续变化，需增量更新、文件监听、冲突处理；grep 天然实时
3. **安全隐私**：Embedding 模型需本地算力或远程 API，代码内容敏感不适合外发

### 实证对比
- Anthropic 首席工程师 Boris Cherny：早期用 Voyage Embedding RAG，后 Agentic Search "outperformed everything, by a lot"
- 亚马逊论文（2025.12）："Keyword search is all you need"，关键词搜索 Agent 达 RAG 90%+ 性能
- Cursor 采用混合检索（grep + 向量），结论"两者配合效果最好"

## 关联连接
- [[LangChain4j]] — RAG 框架实现
- [[ChatMemory]] — 对话记忆
- [[AgenticSearch]] — 替代 RAG 的代码搜索范式
- [[ClaudeCode]] — 放弃 RAG 改用 Agentic Search 的产品
- [[摘要-为什么Claude-Code不用RAG检索代码]] — 来源
