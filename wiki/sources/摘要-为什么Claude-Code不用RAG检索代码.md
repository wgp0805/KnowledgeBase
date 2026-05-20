---
title: "摘要-为什么Claude-Code不用RAG检索代码"
type: source
tags: [Claude-Code, RAG, Agentic-Search, 代码搜索, ripgrep]
sources: [raw/01-articles/腾讯面试官："为什么 Claude Code 不用 RAG 检索代码，而是 grep？"我："因为...我也不知道"，他沉默了。.md]
last_updated: 2026-05-20
---

## 核心摘要
Claude Code 使用 Glob + Grep + Read 三工具组合（Agentic Search）进行代码搜索，而非 RAG。原因：代码场景下精确匹配比语义匹配更重要；索引同步成本高；代码安全隐私要求高。Anthropic 首席工程师 Boris Cherny 确认早期版本用过 Voyage Embedding 的 RAG，但 Agentic Search 全面碾压。亚马逊论文实锤关键词搜索可达 RAG 90% 以上性能。Cursor 的混合检索实践也佐证 grep 是不可或缺的基础能力。

## 关键论据

### RAG 检索代码的三大问题
1. **语义相似度不适用于代码**：`createD1HttpClient` 与 `buildD1HttpClient` 语义近但功能不同；`handleAuth` 与 `validateJwtToken` 语义远但有调用关系
2. **索引同步成本高**：代码持续变化，RAG 索引需增量更新、文件监听、冲突处理；grep 天然实时
3. **安全隐私**：RAG 需 Embedding 模型，本地消耗算力，远程泄露代码

### Agentic Search 优势
- 无需预处理，打开仓库直接搜
- LLM 自身充当 Reranker，理解+决策+行动，多轮迭代搜索
- 三个工具均 `isConcurrencySafe = true`，可并行执行

### ripgrep 性能
- Rust 编写，SIMD 指令集加速，中型仓库全文搜索约 200ms
- 默认递归搜索，自动跳过 .gitignore 和二进制文件
- Claude Code 封装保护：默认最多返回 250 行，超时部分结果"尽力返回"

### 亚马逊论文验证
- 论文标题："Keyword search is all you need"
- 关键词搜索 Agent 可达传统 RAG 90% 以上性能
- 代码命名约定本身携带足够语义信息

### Cursor 的混合检索
- 训练自有 Embedding 模型，用 Turbopuffer 做向量数据库
- 超过 1000 文件的大型仓库中，语义搜索提升代码留存率 2.6%
- 结论是"两者配合效果最好"，grep 是不可或缺基础

## 关联连接
- [[ClaudeCode]] — 使用 Agentic Search 的产品
- [[AgenticSearch]] — 核心搜索范式
- [[RAG]] — 被替代的检索方案
- [[Ripgrep]] — 底层搜索工具
- [[Cursor]] — 采用混合检索的对比产品
- [[BorisCherny]] — Anthropic 首席工程师
