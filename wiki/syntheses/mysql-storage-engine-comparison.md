---
title: "mysql-storage-engine-comparison"
type: synthesis
tags: [MySQL, 存储引擎, InnoDB, MyISAM, 数据库架构]
sources:
  - raw/02-papers/第05章_存储引擎.pdf
last_updated: 2026-05-22
---

# MySQL 存储引擎对比与底层架构

## 常用存储引擎

[[MySQL]] 常用的存储引擎包括 **InnoDB**（默认，MySQL 5.5+）、**MyISAM**（MySQL 5.5 前默认）、**Memory**（Heap）、**CSV**、**Archive** 等。

## InnoDB vs MyISAM 核心区别

| 维度 | InnoDB | MyISAM |
|------|--------|--------|
| 事务 | ✅ 支持 ACID（redo log + undo log） | ❌ 不支持 |
| 行级锁 | ✅ 支持（MVCC 实现） | ❌ 仅表级锁 |
| 外键 | ✅ 支持 | ❌ 不支持 |
| 聚簇索引 | ✅ 主键即聚簇索引 | ❌ 非聚簇（数据和索引分离） |
| 全文索引 | ✅（MySQL 5.6+） | ✅（原生支持） |
| 数据文件 | `.ibd`（表空间，含数据和索引） | `.MYD`（数据）+ `.MYI`（索引） |
| 缓存 | 缓冲池 Buffer Pool 缓存数据和索引 | Key Cache 仅缓存索引 |
| 崩溃恢复 | ✅ 支持（double write + crash recovery） | ❌ 需修复表 |
| 压缩 | ✅ 支持表级压缩 | ✅ 支持 |
| COUNT(*) | 全表扫描 | 直接从元数据读取 |

## 底层架构实现

### InnoDB 架构核心组件

- **Buffer Pool**：内存中的数据和索引缓存，以 page（16KB）为单位
- **redo log**：WAL（Write-Ahead Logging）机制，保证事务持久性
- **undo log**：事务回滚和 MVCC 快照读
- **Change Buffer**：辅助二级索引变更的缓冲区
- **Doublewrite Buffer**：防止部分页面写入失败
- **行格式**：Compact、Redundant、Dynamic、Compressed

### MyISAM 架构特点

- 数据和索引分离存储（`.MYD` + `.MYI`）
- 使用 Fixed / Dynamic / Compressed 行格式
- 不支持事务，无崩溃恢复能力
- 全表扫描时顺序读取 .MYD 文件

### Memory 引擎

数据全在内存，重启即丢，适合临时表。使用哈希索引，表级锁，每行固定长度。

## 关联连接
- [[MySQL]] — 关系型数据库
- [[摘要-mysql-course]] — MySQL 完整教程
- [[query-optimization]] — 查询优化
- [[transaction-management]] — 事务管理
- [[jvm-tuning]] — JVM 性能调优
