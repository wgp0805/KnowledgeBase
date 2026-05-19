---
title: "elasticsearch-disadvantages"
type: synthesis
tags: [Elasticsearch, 搜索引擎, 缺点, 技术选型]
sources: [wiki/entities/Elasticsearch.md]
last_updated: 2026-05-19
---

# Elasticsearch 使用缺点分析

## 来自知识库的记载

根据 [[Elasticsearch]] 中 ES vs Solr 对比表：

- **数据格式单一**：仅支持 JSON 数据格式，不如 Solr 支持 JSON、XML、CSV 等灵活
- **功能依赖插件**：高级功能多依赖第三方插件（如 Kibana 提供可视化），官方内置功能不如 Solr 丰富
- **学习成本高**：社区相对 Solr 较小，版本更新快，学习使用成本较高
- **查询性能**：ES 索引快但实时查询速度相对 Solr 较慢（Solr 查询快，适用于电商等查询密集型场景）

## 通用知识补充

- **数据一致性**：ES 是近实时（NRT）系统，数据写入到可搜索存在秒级延迟，不适合强一致性场景
- **无事务支持**：没有跨文档的事务机制，无法像关系型数据库保证 ACID
- **内存消耗大**：JVM 堆内存管理复杂，GC 问题易导致集群不稳定，需要精细化调优
- **权限管理**：免费版仅提供基础安全，完整安全功能需白金版 license
- **脑裂风险**：集群配置不当（如 `discovery.zen.minimum_master_nodes` 设置错误）时易发生脑裂
- **深度分页**：`from + size` 深度分页越深性能越差，需用 `search_after` 或 `scroll` API 替代

## 关联连接
- [[Elasticsearch]] — 实体页面
- [[Solr]] — 竞品对比
