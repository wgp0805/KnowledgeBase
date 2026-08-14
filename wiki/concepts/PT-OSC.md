---
title: "PT-OSC"
type: concept
tags: [MySQL, DDL, Percona, 在线变更, 触发器]
sources: [raw/01-articles/千万级的大表如何新增字段？.md]
last_updated: 2026-08-14
---

## 定义
PT-OSC（pt-online-schema-change）是 Percona Toolkit 提供的 MySQL 在线表结构变更工具，通过创建影子表 + 触发器同步增量数据的方式，实现大表 DDL 期间不长时间锁表。

## 工作原理
1. 创建与原表结构相同的新表（影子表）并应用 DDL 变更
2. 按主键分块将原表数据拷贝到影子表
3. 在原表上创建 INSERT/UPDATE/DELETE 三个触发器，将变更同步到影子表
4. 数据拷贝完成后，毫秒级原子 RENAME 切换表名
5. 删除旧表

## 关键信息
- **锁表时间**：仅 cut-over 阶段毫秒级锁
- **数据一致性**：最终一致
- **痛点**：
  - 触发器加重主库 CPU 和锁竞争，高并发时性能下降 30%+
  - 无法暂停，失败需重头开始
  - 外键约束支持复杂

## 命令示例
```bash
pt-online-schema-change \
  --alter "ADD COLUMN age INT" \
  D=test,t=user --execute
```

## 适用场景
- 无外键/触发器的常规表
- 兼容低版本 MySQL

## 关联连接
- [[MySQL]] — 所属数据库
- [[OnlineDDL]] — 原生方案对比
- [[GhOst]] — 无触发器替代方案
- [[摘要-千万级大表新增字段方案]] — 来源
