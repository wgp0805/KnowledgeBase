---
title: "UUID"
type: concept
tags: [概念, 分布式ID, 主键]
sources:
  - raw/09-archive/用雪花 id 和 uuid 做 MySQL 主键，被领导怼了.md
last_updated: 2026-08-03
---

## 定义
UUID（Universally Unique Identifier，通用唯一识别码）是一种全局唯一标识符标准，用 128 位数字生成，无需中心化协调即可保证唯一性。

## 关键信息
- **优点**：全局唯一、无需中心节点、跨系统合并安全
- **做 MySQL 主键的劣势**：生成值随机，插入 InnoDB 聚簇索引时无法顺序追加，导致频繁 [[页分裂]] 和碎片
- **性能测试结论**（百万级数据）：插入效率 `auto_key > random_key（雪花）> uuid`，uuid 效率急剧下降
- **其他用途**：Token 生成（如 `UUID.randomUUID().toString().replace("-","")`）、CAS 票据 ID 等
- **不推荐做主键**：见 [[摘要-mysql-primary-key-strategy]]

## 关联连接
- [[雪花算法]] — 同类分布式 ID 方案
- [[聚簇索引]] — 受影响的数据结构
- [[页分裂]] — 随机主键的性能陷阱
- [[摘要-mysql-primary-key-strategy]] — 性能对比来源
