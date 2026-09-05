---
title: "摘要-mysql-primary-key-strategy"
type: source
tags: [来源, 原始文件, MySQL, 主键, 索引]
sources: [raw/01-articles/用雪花 id 和 uuid 做 MySQL 主键，被领导怼了.md]
last_updated: 2026-07-16
---

## 核心摘要
通过性能测试对比自增 ID、UUID、雪花算法三种 MySQL 主键方案，揭示 UUID 在 InnoDB 聚簇索引中的性能陷阱：随机写入导致频繁页分裂和碎片。测试结果显示插入效率排名为 auto_key > random_key（雪花）> uuid，uuid 在百万级数据量下效率急剧下降。文章深入分析了 B+ 树索引结构差异，指出自增主键的顺序写入特性是性能优势的根本原因。

## 关联连接
- [[MySQL]] — 关系型数据库
- [[聚簇索引]] — InnoDB 默认索引结构
- [[页分裂]] — B+ 树节点分裂机制
- [[B+树]] — 数据库索引底层数据结构
- [[雪花算法]] — 分布式 ID 生成方案
- [[UUID]] — 通用唯一识别码
