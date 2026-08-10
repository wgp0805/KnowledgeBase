---
title: "RAG"
type: concept
tags: [AI, RAG, 检索增强, 知识库, 面试]
sources: [raw/01-articles/LangChain4j 来了，Java AI智能体开发再次起飞。。。.md, raw/01-articles/腾讯面试官："为什么 Claude Code 不用 RAG 检索代码，而是 grep？"我："因为...我也不知道"，他沉默了。.md, raw/01-articles/SpringAI.md, raw/01-articles/字节面试官：什么是 RAG？为什么需要 RAG？-2026-06-02 15_08_07.md, raw/01-articles/LangChain4j 和 LangGraph4j，哪个更好？.md]
last_updated: 2026-06-30
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

### 进阶版 RAG 流水线化
进阶版 RAG 支持查询转换器、查询路由、内容聚合器、内容注入器等特性，将整个 RAG 流程流水线化（RAG Pipeline），实现更灵活的检索增强策略。

### 关键实践
- RAG 关键不在框架，而在切分策略（段落完整性、块大小、重叠设置）
- 换向量库的影响往往不如调切分策略大

### Spring AI RAG 实现
Spring AI 通过 VectorStore + QuestionAnswerAdvisor 实现 RAG：
- VectorStore 存储文档向量，支持 SimpleVectorStore（内存）等实现
- 文档加载：TextReader 读取文本文件，TokenTextSplitter 切分段落
- QuestionAnswerAdvisor 自动检索相关文档并拼入 Prompt
- Spring AI Alibaba 集成 DashScope 通义模型实现 RAG

### LangChain 知识库构建组件（理论）
LangChain 实现 RAG 的两大阶段与五大组件：
- **知识库构建**：DocumentLoader 加载 → TextSplitter 切分 → Embeddings 向量化 → 存入 VectorStore
- **检索生成**：用户提问 → Embeddings 向量化 → VectorStore 检索 → 拼接上下文 → LLM 生成回答
- 五大组件：[[DocumentLoader]]、[[TextSplitter]]、[[Embeddings]]、[[VectorStore]]、[[Retriever]]（详见各概念页）
- 关键参数建议：chunk_size 200~1000、chunk_overlap 为 chunk_size 的 10%~20%、k 检索 3~10

## 代码搜索场景的局限性

### 为什么 Claude Code 放弃了 RAG
1. **语义相似度不适用于代码**：代码需要精确匹配，非"大概对"的语义匹配。`createD1HttpClient` 与 `buildD1HttpClient` 语义近但功能不同
2. **索引同步成本高**：代码持续变化，需增量更新、文件监听、冲突处理；grep 天然实时
3. **安全隐私**：Embedding 模型需本地算力或远程 API，代码内容敏感不适合外发

### 实证对比
- Anthropic 首席工程师 Boris Cherny：早期用 Voyage Embedding RAG，后 Agentic Search "outperformed everything, by a lot"
- 亚马逊论文（2025.12）："Keyword search is all you need"，关键词搜索 Agent 达 RAG 90%+ 性能
- Cursor 采用混合检索（grep + 向量），结论"两者配合效果最好"

## 为什么需要 RAG（面试视角）

大模型有四大绕不开的硬伤，RAG 逐一解决：

| 硬伤 | 具体表现 | RAG 如何解决 |
|------|---------|-------------|
| 幻觉问题 | 一本正经地胡说八道，编造不存在的事实 | 基于检索到的真实文档生成回答，有据可依 |
| 知识截止 | 训练数据有截止日期，不知道最新信息 | 知识库可随时更新，突破时间限制 |
| 领域知识不足 | 对企业内部文档、专业知识了解有限 | 接入企业私有数据，补齐领域短板 |
| 无法溯源 | 不知道回答的依据是什么，无法验证 | 可追溯引用来源，提供文档出处 |

记忆口诀："外挂知识库，带着资料考试"。

## RAG 核心流程详解

### 离线阶段（知识库构建）
1. **文档解析**：各种格式文档解析成纯文本
2. **切分（Chunk）**：切成合适大小的片段，切分策略直接影响检索效果
3. **向量化（Embedding）**：用 Embedding 模型编码成向量
4. **入库**：存入向量数据库

### 在线阶段（查询与生成）
1. **问题编码**：用户提问编码成向量
2. **相似度检索**：在向量库中找最相关的几段文本
3. **重排序（Rerank）**：用 Cross-Encoder 对初步检索结果精排，显著提升准确率
4. **组装 Prompt**：把检索文本塞进 Prompt
5. **生成回答**：大模型基于上下文生成最终回答

### RAG vs 微调 vs 长上下文选型

| 维度 | RAG | 微调（Fine-tuning） | 长上下文（Long Context） |
|------|-----|------|---------|
| 核心作用 | 注入外部知识 | 改变模型行为风格 | 扩大单次输入窗口 |
| 知识更新 | 随时更新知识库 | 需重新训练 | 更新输入内容即可 |
| 成本 | 低 | 中高（算力 + 数据） | 按 Token 计费，量大时成本高 |
| 幻觉控制 | 较好，有检索约束 | 一般 | 取决于上下文中的信息量 |
| 适用场景 | 知识密集型问答、企业知识库 | 特定格式输出、风格定制 | 全文分析、长文档摘要 |

选型口诀："知识用 RAG，能力用微调"。三者不是互斥的，实际项目经常组合使用。

### RAG 优化策略
1. **优化 Chunk 策略**：语义切分替代固定长度切分
2. **加 Rerank 重排序**：Cross-Encoder 精排
3. **Hybrid Search**：稠密向量 + 稀疏关键词检索融合
4. **Query 改写**：把口语化问题改写成更适合检索的 Query
5. **升级 Embedding 模型**

## 前沿演进

- [[AgenticRAG]] — 从被动检索到主动决策的智能体化 RAG
- [[GraphRAG]] — 结合知识图谱的图检索增强
- [[ContextEngineering]] — 从"检索增强"到"上下文工程"的认知升级

## 关联连接
- [[LangChain4j]] — RAG 框架实现
- [[ChatMemory]] — 对话记忆
- [[AgenticSearch]] — 替代 RAG 的代码搜索范式
- [[ClaudeCode]] — 放弃 RAG 改用 Agentic Search 的产品
- [[AgenticRAG]] — 智能体化 RAG 前沿趋势
- [[GraphRAG]] — 图检索增强生成
- [[ContextEngineering]] — 上下文工程
- [[DocumentLoader]] — 文档加载组件
- [[TextSplitter]] — 文本切分组件
- [[Embeddings]] — 向量化组件
- [[VectorStore]] — 向量库组件
- [[Retriever]] — 检索器组件
- [[Chroma]] — 向量数据库
- [[混合检索]] — KNN + BM25 混合检索
- [[LoRA]] — 微调方法
- [[Gemini]] — 长上下文模型代表
- [[MinerU]] — 推荐的 PDF 加载工具
- [[摘要-为什么Claude-Code不用RAG检索代码]] — 来源
- [[摘要-字节面试官什么是RAG为什么需要RAG]] — 来源
- [[摘要-langchain-rag构建知识库-理论]] — LangChain RAG 构建理论来源
- [[摘要-langchain4j-langgraph4j-comparison]] — LangChain4j 与 LangGraph4j 对比中的 RAG 能力来源
