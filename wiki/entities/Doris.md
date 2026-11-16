---
title: "Doris"
type: entity
tags: [数据库, OLAP, 数据仓库, Apache, 实时分析]
sources: [raw/09-archive/2026-11-14 - SpringBoot+Doris Stream Load 海量数据实时更新方案！.md]
last_updated: 2026-11-16
---

## 定义
Apache Doris 是开源的 MPP 架构实时分析型数据库（OLAP），FE（Frontend，`8030` 端口 HTTP 接口）负责元数据与查询调度、BE（Backend）负责存储与计算，主打海量数据的实时导入与亚秒级查询，常作为业务库（[[MySQL]]/[[PostgreSQL]] 等 OLTP 侧）之上的分析层。

## 关键信息

### Stream Load 导入方式（2026-11-14 实战方案，详见 [[摘要-doris-streamload海量数据实时更新]]）
Stream Load 是 Doris 通过 HTTP PUT 同步导入数据的原生方式，URL 形如 `http://doris-fe:8030/api/{db}/{table}/_stream_load`，Basic 认证，支持 JSON（`strip_outer_array:true`）与 CSV（自定义 `column_separator` 如 `\x01`）两种格式：

- **注解式字段映射**：自定义 `@DorisField` 注解（`value` 重命名字段 / `order` 控制列顺序 / `ignore` 忽略字段）+ 反射工具类按注解过滤排序，自动完成实体到 Doris 字段映射并保持顺序一致；Date 类型必须格式化为 `yyyy-MM-dd HH:mm:ss` 否则入库为空值；配 ConcurrentHashMap 缓存字段反射结果避免重复开销
- **高性能加载**：`DorisStreamLoadProperties` 可配批次大小（10 万条）、并行度（8 线程固定池 + CompletableFuture 分批并行）、GZIP 压缩传输、指数退避重试（1s→2s→4s…，默认最多 3 次）；HttpClient 按并行度池化（maxPerRoute/maxTotal）
- **结果监控**：LoadResponse 返回 TxnId、Label、Status、成功/过滤/未选中行数、LoadTimeMs 及各阶段耗时明细，非 Success 即抛错触发重试
- **生产调优**：批次大小按集群性能调；并行度取 CPU 核数 ×2；大数据量场景加大 socket 超时；集群侧 `streaming_load_max_mb`、`max_running_txn_num_per_db` 放宽
- **效果**：作者声称相比 JDBC 批量更新性能提升 20-50 倍，适合海量数据实时更新场景

## 关联连接
- [[SpringBoot]] — 实战接入框架
- [[MySQL]] / [[PostgreSQL]] — 上游 OLTP 业务库（分析层与业务层组合）
- [[小哈]] — 实战文章作者
- [[摘要-doris-streamload海量数据实时更新]] — 来源
