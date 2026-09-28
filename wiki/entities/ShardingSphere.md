---
title: "ShardingSphere"
type: entity
tags: [数据库, 中间件, 分库分表, Java]
sources: [raw/09-archive/从40分钟到1秒：我用分库分表彻底解决了上亿数据的大表性能问题！！.md, raw/01-articles/2026-09-23 - 分库分表，可能真的要退出历史舞台了！.md]
last_updated: 2026-09-28
---

## 定义

Apache ShardingSphere 是一套开源的分布式数据库中间件解决方案，包含 Sharding-JDBC（JAR包嵌入模式）和 Sharding-Proxy（代理模式）两个产品。Java 项目首选 Sharding-JDBC，以 JAR 包形式嵌入应用，无额外网络开销，性能优异。

## 关键信息

- **核心功能**：数据分片、读写分离、分布式事务、数据加密
- **分片策略**：支持按 user_id 哈希分库、按时间范围分表等
- **配置方式**：Spring Boot application.yml 配置 actual-data-nodes、database-strategy、table-strategy
- **路由机制**：自动将 SQL 路由到正确的库和表，业务代码无需修改
- **版本**：5.5.0（Spring Boot 3.x）

### 中间件路线的架构定位（2026-09）
来自 [[摘要-分库分表vs-newsql对比]]：
- 在 Pavlo 的 NewSQL 分类中，ShardingSphere、Mycat、DRDS 属于第二类"中间件方案"，与 Spanner/TiDB 等新架构型相对
- 被称"伪分布式"的点：中间件层与底层 DB 重复做 SQL 解析与执行计划生成、存储引擎仍是面向磁盘的 B+Tree
- 架构风格是**妥协与平衡、面向应用型**：只做 SQL 解析/路由计算/SQL 重写，因此可支持多种数据库方言；因缺少底层数据分布与统计信息只能用规则优化（RBO），跨库 join 即使实现效率也低，通常交给应用处理
- 优势：技术门槛更低、对存量关系库生态复用最充分、定制化能力强

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
- [[摘要-分库分表vs-newsql对比]] — 中间件路线与 NewSQL 的对比来源
- [[newsql]] — 对照架构
- [[MySQL]] — 底层数据库
- [[consistent-hashing]] — 一致性哈希算法
- [[SpringBoot]] — 集成框架
