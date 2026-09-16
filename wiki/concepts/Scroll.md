---
title: "Scroll"
type: concept
tags: [概念, Elasticsearch, 分页, 快照, 导出]
sources: [raw/01-articles/面试官：什么是 Elasticsearch 的深度分页问题？如何解决？.md]
last_updated: 2026-09-16
---

## 定义
Elasticsearch 的快照式全量遍历方案。思路：第一次查询时把结果集固化成快照，之后拿着游标 `scroll_id` 接着取，省去每次重算的过程。适合离线批量导出、全量扫描场景。

## 关键信息

### 使用流程
1. **发起 scroll 查询**：
```
POST /order/_search?scroll=1m
{
  "size": 1000,
  "query": { "match_all": {} }
}
```
2. **拿 scroll_id 继续拉**：
```
POST /_search/scroll
{
  "scroll": "1m",
  "scroll_id": "FGluY2x1ZGVfY29udGV4dF91dWlk..."
}
```
3. **用完主动清理**：
```
DELETE /_search/scroll
{
  "scroll_id": "..."
}
```

### 原理
- 首次查询时在集群里创建 **search context（搜索上下文）**
- 之后每次翻页都基于这个上下文继续，不用再从 from 0 开始算
- `scroll=1m` 表示快照保留 1 分钟

### 三大坑
1. **非实时**：快照生成后，这段时间里的新增、修改、删除对它不可见——不适合用户侧分页
2. **吃资源**：每个 scroll 会话在节点上维护一个搜索上下文，开着不关白白消耗堆内存。**用完必须主动 `DELETE /_search/scroll` 清理**
3. **不能跳页**：只能顺序往后拉，想直接翻到第 500 页？没门

### 版本演进（重要面试加分项）
- **ES 7.10 起，官方已把 scroll 标记为 deprecated（不推荐）**
- 现在只建议从 7.10 之前的旧集群 reindex 数据这类场景使用
- 新的深分页推荐 [[PIT]] + [[SearchAfter]]

### scroll vs search_after 核心区别
| 维度 | Scroll | SearchAfter |
|------|--------|-------------|
| 模型 | 快照模型，上下文固化结果集 | 无状态游标模型 |
| 实时性 | 非实时 | 实时 |
| 一致性 | 翻页过程数据一致 | 不保证一致性 |
| 适合场景 | 离线导出 | 实时深度翻页 |
| 资源占用 | 高（维护上下文） | 无状态 |

## 关联连接
- [[深度分页]] — 所属概念
- [[SearchAfter]] — 对比方案
- [[PIT]] — 7.10+ 推荐组合
- [[Elasticsearch]] — 主角
- [[摘要-elasticsearch-深度分页]] — 来源