---
title: "摘要-ip地址存储数据类型"
type: source
tags: [来源, MySQL, 数据库设计, 面试]
sources: [raw/01-articles/2026-10-30 - 面试官：如果要存ip地址，用什么数据类型比较好.md]
last_updated: 2026-11-02
---

## 核心摘要

「小哈学Java」回答面试题「存 IP 地址用什么数据类型」，原载 CSDN（作者 Mikan）。结论：**存 IPv4 应使用 32 位无符号整数（UNSIGNED INT）而不是字符串**。

依据：

- IPv4 最小需要 7 个字符、最大 15 个字符，用 `VARCHAR(15)` 存即可，但 MySQL 存变长字符串需要额外 1 字节保存长度；无符号整数只需要 4 字节
- 节省空间：数据存储空间 + 索引存储空间都省
- 便于范围查询（`BETWEEN...AND`），且效率更高

转换函数：

- MySQL：`INET_ATON`（字符串→整数）、`INET_NTOA`（整数→字符串）；IPv6 用 `VARBINARY` + `INET6_ATON` / `INET6_NTOA`
- 应用层：文章给出 Java 实现 `IpLongUtils.ip2Long()` / `long2Ip()`，用移位与掩码完成双向转换

缺点：不便于阅读、需要手动转换。

文中另提到可以用 4 个字段分别存 IPv4 各部分，但存储空间和查询效率都不高（特定场景适用）。

## 关联连接
- [[IP地址存储]] — 上位概念
- [[MySQL]] — 提供转换函数的数据库
- [[UNSIGNED INT]] — 推荐的存储类型
- [[小哈]] — 文章作者
