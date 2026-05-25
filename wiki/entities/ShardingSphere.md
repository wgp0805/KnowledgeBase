---
title: "ShardingSphere"
type: entity
tags: [数据库, 中间件, 分库分表, Java]
sources: [raw/01-articles/从40分钟到1秒：我用分库分表彻底解决了上亿数据的大表性能问题！！.md]
last_updated: 2026-05-25
---

## 定义

Apache ShardingSphere 是一套开源的分布式数据库中间件解决方案，包含 Sharding-JDBC（JAR包嵌入模式）和 Sharding-Proxy（代理模式）两个产品。Java 项目首选 Sharding-JDBC，以 JAR 包形式嵌入应用，无额外网络开销，性能优异。

## 关键信息

- **核心功能**：数据分片、读写分离、分布式事务、数据加密
- **分片策略**：支持按 user_id 哈希分库、按时间范围分表等
- **配置方式**：Spring Boot application.yml 配置 actual-data-nodes、database-strategy、table-strategy
- **路由机制**：自动将 SQL 路由到正确的库和表，业务代码无需修改
- **版本**：5.5.0（Spring Boot 3.x）

## 配置示例

```yaml
spring:
  shardingsphere:
    datasource:
      names: db0,db1
    rules:
      sharding:
        tables:
          orders:
            actual-data-nodes: db$->{0..1}.orders_$->{202401..202412}
            database-strategy:
              standard:
                sharding-column: user_id
                sharding-algorithm-name: db-by-userid
```

## 关联连接
- [[摘要-sharding-database-table]] — 来源
- [[MySQL]] — 底层数据库
- [[consistent-hashing]] — 一致性哈希算法
- [[SpringBoot]] — 集成框架
