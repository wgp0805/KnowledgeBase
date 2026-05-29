---
title: "Druid"
type: entity
tags: [连接池, Java, 数据库, 监控]
sources: []
last_updated: 2026-05-29
---

## 定义
Druid 是阿里巴巴开源的 Java 数据库连接池，内置强大的监控功能（SQL 执行统计、慢查询检测、防火墙），是国内使用最广泛的连接池之一。

## 关键信息
- SQL 监控：实时统计 SQL 执行次数、耗时、慢查询
- SQL 防火墙：防 SQL 注入攻击
- 内置 Web 监控页面：可视化查看连接池和 SQL 状态
- 配置：通过 druid-spring-boot-starter 整合
- 与 HikariCP 对比：Druid 功能更丰富，HikariCP 性能更好

## 关联连接
- [[Hikari]] — 竞品连接池（性能优先）
- [[SpringBoot]] — 整合框架
- [[MySQL]] — 常配合使用
