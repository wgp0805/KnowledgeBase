---
title: "AgenticSearch"
type: concept
tags: [AI, Agent, 代码搜索, Claude-Code]
sources: [raw/01-articles/腾讯面试官："为什么 Claude Code 不用 RAG 检索代码，而是 grep？"我："因为...我也不知道"，他沉默了。.md]
last_updated: 2026-05-20
---

## 定义
不预先构建任何索引，让 Agent 在执行任务的过程中，根据当前上下文和目标，动态决定搜什么、怎么搜、搜到之后下一步干什么的搜索范式。Anthropic 内部命名。

## 关键信息

### 核心工具链（Claude Code 实现）
1. **Glob**：按文件名模式匹配（如 `**/*.java`），结果按修改时间排序
2. **Grep**：文件内搜索，底层 ripgrep，支持正则、行号、并行搜索
3. **Read**：读取具体文件内容，支持指定行号范围

### 工作流程
1. Glob 看目录结构 → 2. Grep 搜关键词 → 3. Read 读取相关文件 → 4. LLM 判断后续策略（多轮迭代）

### 相比 RAG 的核心优势
- **零预处理**：无需构建索引，打开仓库即搜
- **确定性结果**：精确匹配，无误召回
- **LLM 即 Reranker**：Agent 理解搜索结果后动态调整策略，非简单重排序
- **多轮迭代**：顺藤摸瓜式搜索，RAG 一次检索做不到
- **并行安全**：三个工具均 `isConcurrencySafe = true`

### 实证支撑
- Boris Cherny（Anthropic 首席工程师）：Agentic Search "outperformed everything, by a lot"
- 亚马逊论文：关键词搜索 Agent 达传统 RAG 90%+ 性能
- Cursor：混合检索中 grep 为不可或缺基础

## 关联连接
- [[摘要-为什么Claude-Code不用RAG检索代码]] — 来源
- [[ClaudeCode]] — 采用此范式的产品
- [[RAG]] — 对比范式
- [[Ripgrep]] — 底层搜索引擎
- [[Agent]] — Agent 核心概念
