---
title: "Hikari"
type: entity
tags: [连接池, Java, 数据库]
sources: []
last_updated: 2026-05-29
---

## 定义
HikariCP 是目前性能最好的 Java 数据库连接池，Spring Boot 2.x+ 默认的数据库连接池实现，以极致的性能和可靠性著称。

## 关键信息
- Spring Boot 默认连接池（替代 Tomcat JDBC Pool）
- 核心优化：字节码级别优化、并发容器使用、减少锁竞争
- 配置项：maximumPoolSize、minimumIdle、connectionTimeout、idleTimeout
- 监控指标：通过 JMX 暴露连接池状态
- 与 Druid 对比：HikariCP 性能更好，Druid 功能更丰富（SQL 监控、防注入）

## 关联连接
- [[SpringBoot]] — 默认集成
- [[Druid]] — 竞品连接池
- [[MySQL]] — 常配合使用
