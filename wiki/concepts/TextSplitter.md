---
title: "TextSplitter"
type: concept
tags: [RAG, LangChain, 文本切分, 分块]
sources: [raw/01-articles/2026-08-07-LangChain — RAG 构建知识库（理论） - VipSoft.md]
last_updated: 2026-08-10
---

## 定义
Text Splitter（文本切分器）负责将长文档切分为合适大小的块（chunk），是影响 RAG 检索质量的关键环节。LLM 上下文窗口有限，切分大小直接决定检索精度：太大含过多无关信息精度下降，太小丢失上下文语义不完整。

## 关键信息

### 常见切分策略对比
| 策略 | 核心原理 | 优点 | 缺点 | 适用场景 |
| --- | --- | --- | --- | --- |
| 固定长度切分 | 按预设字符/token 数切 | 实现简单、速度快、可预测 | 易在句子中间硬截断，破坏语义 | 日志、代码等结构不敏感文本 |
| **递归切分**（推荐） | 按优先级分隔符（段落\n\n>句子。）逐级递归分割 | 尊重文档结构、语义完整、动态调整 | 无标准分隔符文本效果差 | 通用首选，报告/文章等规范文档 |
| 语义切分 | 嵌入模型算相邻句相似度，低于阈值切分 | 语义连贯性最好 | 计算成本高、依赖嵌入模型精度 | 学术论文、法律文件等高要求场景 |
| 结构感知切分 | 利用 Markdown/HTML 标题识别逻辑区块 | 天然符合文档组织逻辑 | 需格式良好的文档 | Markdown、网页等原生结构文档 |
| 滑动窗口切分 | 固定窗口高重叠率滑动 | 上下文连接紧密 | 冗余高、开销大 | 可与其它策略结合 |

### RecursiveCharacterTextSplitter（推荐）核心参数
| 参数 | 作用 | 默认值 |
| --- | --- | --- |
| chunk_size | 目标块大小（字符/token） | 4000 |
| chunk_overlap | 块间重叠长度，保留共同上下文 | 200 |
| separators | 分隔符优先级列表 | ["\n\n", "\n", " ", ""] |
| length_function | 长度计算方式（len 字符数 / tiktoken token数） | len |

### 切割流程
1. 用最高优先级分隔符分割 → 2. 块≤chunk_size 则保留、超大块降级用下一优先级分隔符再分割 → 3. 所有分隔符用完仍超大，则在空字符串（按字符）上按 chunk_size 硬截断

### 其他实现
- 固定长度：CharacterTextSplitter（按字符/字节），从_tiktoken_encoder 按 token 切分更精确
- 结构感知：MarkdownHeaderTextSplitter、RecursiveJsonSplitter、HTMLHeaderTextSplitter、from_language()
- **配合 MinerU 的建议**：优先按 Markdown 结构切分（语义完整且记住所处章节），超出目标 size 的块再用递归切分并保留 header

### 参数实践建议
- chunk_size：建议 200~1000（取决于文档类型和模型上下文）
- chunk_overlap：建议 chunk_size 的 10%~20%
- k（检索数量）：3~10（太少遗漏、太多噪声）

## 关联连接
- [[RAG]] — 检索质量的关键环节
- [[DocumentLoader]] — 切分前需要先加载
- [[Embeddings]] — 切分后的向量化步骤
- [[LangChain]] — 所属框架
- [[摘要-langchain-rag构建知识库-理论]] — 来源