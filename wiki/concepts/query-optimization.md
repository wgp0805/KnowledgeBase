---
title: "query-optimization"
type: concept
tags: [数据库, MySQL, SQL优化]
sources: [raw/01-articles/mysql关键字explain解析.md, raw/01-articles/mysql查询cpu占用过高的方法.md]
last_updated: 2026-05-19
---

## 定义
SQL 查询优化是通过分析执行计划、优化索引和改写 SQL 语句来提升数据库查询性能的过程。

## 关键信息
- EXPLAIN 执行计划关键列：type（ALL/range/ref/const）、key（使用索引）、rows（扫描行数）、Extra（Using index/Using filesort/Using temporary）
- 优化目标：尽可能使用索引、减少扫描行数、避免文件排序和临时表
- 常见优化：覆盖索引、复合索引最左前缀原则、避免 SELECT *、避免隐式类型转换、避免函数包裹索引列
- CPU 过高排查：通过线程 ID 关联查找耗时 SQL

## 关联连接
- [[MySQL]] — 数据库
- [[Oracle]] — 数据库
