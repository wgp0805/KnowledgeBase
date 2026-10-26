---
title: "PIT"
type: concept
tags: [概念, Elasticsearch, 分页, 一致性, 时间点]
sources: [raw/09-archive/面试官：什么是 Elasticsearch 的深度分页问题？如何解决？.md]
last_updated: 2026-09-16
---

## 定义
PIT 全称 **Point in Time**（时间点快照），ES 7.10 引入的轻量级视图机制。用于配合 `search_after` 解决翻页过程中数据变化导致的一致性隐患——先创建一个轻量级视图，之后所有分页查询都基于这个视图，不固化完整快照但保证数据视图一致。

## 关键信息

### 为什么需要 PIT
`search_after` 有个小隐患：翻页过程中数据变了怎么办？比如翻到第 3 页时有人删了第 2 页的几条数据，第 4 页就可能漏数据。PIT 通过创建时间点视图解决这一问题。

### 使用流程
1. **创建 PIT 视图**：
```
POST /order/_pit?keep_alive=1m
```
返回一个 `pit id`（形如 `46ToAwMDaWR5ZHVja2VyWc2VjX2g...`）

2. **后续查询带 pit 参数**：
```
POST /_search
{
  "size": 10,
  "pit": {
    "id": "46ToAwMDaWR5ZHVja2VyWc2VjX2g...",
    "keep_alive": "1m"
  },
  "sort": [
    { "create_time": "desc" },
    { "_id": "asc" }
  ]
}
```

3. **后续使用方式与 search_after 完全一致**：把每页最后一条的排序值传给下一页的 `search_after`

### 与 Scroll 对比
| 维度 | PIT | Scroll |
|------|-----|--------|
| 快照类型 | 轻量级视图，只记录段状态 | 固化完整快照 |
| 资源占用 | 低 | 高（维护搜索上下文） |
| 版本引入 | ES 7.10 | 更早，7.10 起 deprecated |
| 官方推荐 | ✅ 深分页推荐 | ❌ 仅旧集群 reindex |

### ES 7.10+ 官方推荐的深分页组合拳
**PIT + search_after** ——面试说到这一层，基本稳了。

### 关键参数
- `keep_alive`：视图保留时长（如 `1m` = 1 分钟），超时后视图自动清理

## 关联连接
- [[SearchAfter]] — 组合使用
- [[深度分页]] — 所属概念
- [[Scroll]] — 对比方案（更重）
- [[Elasticsearch]] — 主角
- [[摘要-elasticsearch-深度分页]] — 来源