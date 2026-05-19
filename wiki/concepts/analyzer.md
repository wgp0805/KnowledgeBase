---
title: "analyzer"
type: concept
tags: [搜索引擎, 分词, 全文检索, 中文处理]
sources: [raw/01-articles/从 0 到 1 学习 elasticsearch ，这一篇就够了！(建议收藏).md]
last_updated: 2026-05-19
---

## 定义

分词器（Analyzer/Tokenizer）是搜索引擎将文本拆分为词条（Token）的组件。分词质量直接影响搜索结果的相关性。默认的中文分词会将每个字看作一个词，需使用专门的中文分词器（如 IK Analyzer）才能正确处理中文。

## 关键信息

### IK 分词器
IK 提供两种分词算法：
- **ik_smart**（最少切分/粗粒度）：优先匹配最长词，无重复数据
- **ik_max_word**（最细粒度划分）：穷尽语句中所有分词可能

### 自定义词库
IK Analyzer 支持通过自定义词典文件（.dic）扩展词库，将未收录的专有名词、人名等添加到词库中。

### 字段类型与分词
ES 中字段类型决定是否分词：
- **text** 类型：会被分析器分词后匹配查询
- **keyword** 类型：不会被分析器处理，作为完整字符串存储

### term vs match 查询
- **term**：不经过分词，直接查询精确值（适合 keyword 字段）
- **match**：使用分词器解析后查询（适合 text 字段）

## 关联连接
- [[Elasticsearch]] — 搜索引擎中的分词应用
- [[full-text-search]] — 全文搜索依赖分词技术
- [[inverted-index]] — 分词结果构建倒排索引
- [[摘要-elasticsearch-quick-start]] — 来源
