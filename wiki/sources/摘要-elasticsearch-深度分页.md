---
title: "摘要-elasticsearch-深度分页"
type: source
tags: [来源, Elasticsearch, 面试题, 深度分页, 分片]
sources: [raw/09-archive/面试官：什么是 Elasticsearch 的深度分页问题？如何解决？.md]
last_updated: 2026-09-16
---

## 核心摘要
犬小哈从面试视角深度剖析 Elasticsearch 深度分页问题：`from + size` 翻页越深，各分片与协调节点需加载、排序的数据量暴涨（翻到第 10 万页时每分片需处理百万级元数据、协调节点需归并 500 万条），默认 `index.max_result_window=10000` 拦截。四大解决方案对比：`from+size`（浅分页）、`scroll`（快照导出，7.10 起 deprecated）、`search_after`（游标实时翻页）、`PIT + search_after`（7.10+ 官方推荐，视图一致性）。强调 `search_after` 必须搭配唯一排序字段兜底、调大窗口是自欺欺人。

## 提炼要点
- **两阶段查询原理**：query 阶段各分片返回 `from+size` 条元数据，fetch 阶段协调节点归并排序后丢弃大部分数据——用户只要 10 条，ES 却算了 100 万条
- **`from+size` 开销公式**：协调节点开销 = `from + size` × 分片数，10000 是官方在"常见需求"与"集群安全"之间的保守经验值
- **`scroll` 三大坑**：快照非实时、上下文占堆内存（用完必须 `DELETE /_search/scroll`）、不能跳页；7.10 起仅建议旧集群 reindex 使用
- **`search_after` 唯一性要求**：排序字段组合必须唯一确定一条文档，标准做法是业务字段 + `_id` 双键兜底
- **`PIT`（Point in Time）轻量视图**：不固化完整快照，只记录当前点的段状态，比 scroll 轻量且保证翻页过程视图一致
- **调大 `max_result_window` 不推荐**：本质是拆闸门，OOM 风险不变；真有硬跳页需求应走离线任务/secondary 查询/产品限制

## 记忆口诀
浅翻 from + size，导出用 scroll，实时深翻 search_after，要一致性加 PIT，调大窗口是自欺。

## 关联连接
- [[Elasticsearch]] — 本文主角
- [[深度分页]] — 核心概念
- [[SearchAfter]] — 游标实时翻页方案
- [[PIT]] — Point in Time 时间点视图
- [[Scroll]] — 快照式全量遍历
- [[NearRealTime]] — ES 近实时机制
- [[FST]] — 底层数据结构
- [[摘要-es-为什么快-面试深度]] — 相关面试深度系列
- [[摘要-es-事务支持面试题]] — 相关面试系列
- [[小哈]] — 作者