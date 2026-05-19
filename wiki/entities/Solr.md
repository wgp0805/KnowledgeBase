---
title: "Solr"
type: entity
tags: [搜索引擎, 全文检索, Apache, Java]
sources: [raw/01-articles/从 0 到 1 学习 elasticsearch ，这一篇就够了！(建议收藏).md]
last_updated: 2026-05-19
---

## 定义

Solr 是 Apache 旗下的顶级开源项目，基于 Lucene 的全文搜索服务器。采用 Java 开发，可独立运行在 Jetty、Tomcat 等 Servlet 容器中，提供了比 Lucene 更丰富的查询语言。曾是排名第一的搜索引擎类应用，2016 年被 Elasticsearch 超越。

## 关键信息

- 支持更多格式数据：JSON、XML、CSV
- 依赖 Zookeeper 进行分布式管理
- 查询快，但更新索引（插入/删除）慢
- 拥有更大的用户和贡献者社区，比较成熟
- 适合电商等查询多、更新少的传统搜索应用场景

## 关联连接
- [[Elasticsearch]] — 主要竞争对手
- [[Lucene]] — 底层基础库
- [[摘要-elasticsearch-quick-start]] — 来源
