---
title: "IP地址存储"
type: concept
tags: [数据库设计, MySQL, 面试, 性能优化]
sources: [raw/01-articles/2026-10-30 - 面试官：如果要存ip地址，用什么数据类型比较好.md]
last_updated: 2026-11-02
---

## 定义

存 IP 地址用什么数据类型的工程决策：IPv4 推荐用 32 位无符号整数（UNSIGNED INT）而非字符串，IPv6 推荐用 VARBINARY。

## 关键信息

### IPv4：UNSIGNED INT vs VARCHAR(15)

| 维度 | VARCHAR(15) | UNSIGNED INT |
|------|-------------|--------------|
| 空间 | 7-15 字符 + 1 字节长度 = 8-16 字节 | 固定 4 字节 |
| 索引 | 占更多索引空间 | 更省索引空间 |
| 范围查询 | 字符串比较，效率低 | `BETWEEN...AND` 高效 |
| 可读性 | 直接可读 | 需要转换 |

### 转换函数

- MySQL：`INET_ATON`（字符串→整数）、`INET_NTOA`（整数→字符串）
- IPv6：`VARBINARY` + `INET6_ATON` / `INET6_NTOA`
- Java 层：移位与掩码实现双向转换（`ip2Long` / `long2Ip`）

### 其他方案

用 4 个字段分别存 IPv4 各部分——存储空间和查询效率都不如整数方案（特定场景可能适用）。

### 出处

《高性能 MySQL》第 3 版 4.1.7 节建议使用 32 位无符号整数存储 IPv4。

## 关联连接
- [[MySQL]] — 提供转换函数的数据库
- [[UNSIGNED]] — 整数类型关键字（待建）
- [[索引优化]] — 索引空间的考虑
- [[小哈]] — 文章作者
