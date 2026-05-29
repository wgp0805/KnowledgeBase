---
title: "Elasticsearch"
type: entity
tags: [搜索引擎, 全文检索, 分布式, 大数据]
sources: [raw/01-articles/从 0 到 1 学习 elasticsearch ，这一篇就够了！(建议收藏).md]
last_updated: 2026-05-19
---

## 定义

Elasticsearch（简称 ES）是一个基于 Apache Lucene 的开源分布式全文检索引擎，提供近实时的存储、检索和分析能力。通过简单的 RESTful API 隐藏 Lucene 的复杂性，使全文搜索变得简单。由 Shay Banon 于 2010 年首次公开发布。

## 关键信息

### 历史
- Shay Banon 最初为妻子构建食谱搜索引擎，基于 Lucene 开发 Compass
- 之后重写 Compass 为独立服务，命名为 Elasticsearch
- 第一个公开版本发布于 2010 年 2 月

### 核心特性
- **分布式**：可扩展到上百台服务器，处理 PB 级数据
- **近实时**：数据索引后几乎立即可搜索
- **RESTful API**：通过 HTTP 接口操作，隐藏 Lucene 复杂性
- **开箱即用**：比 Solr 更简单易用
- **自身带分布式协调管理**：不依赖 Zookeeper

### ES vs Solr
| 对比项 | Elasticsearch | Solr |
|--------|--------------|------|
| 易用性 | 开箱即用，简单 | 安装略复杂 |
| 分布式 | 自身带分布式协调 | 依赖 Zookeeper |
| 数据格式 | 仅 JSON | JSON、XML、CSV 等 |
| 扩展功能 | 第三方插件提供（如 Kibana） | 官方内置更多功能 |
| 索引速度 | 建立索引快（实时查询相对慢） | 查询快，更新索引慢 |
| 适用场景 | 新兴实时搜索应用 | 传统搜索应用（电商等） |

### 安装要点
- 不允许 root 用户启动，需创建专用用户
- 需要调整系统参数：`max file descriptors`、`max number of threads`、`vm.max_map_count`
- 目录结构：bin（可执行文件）、config（配置文件）、jdk（内置 JDK）、data（索引目录）、logs（日志）、plugins（插件）

### ES 核心概念类比
| 关系型数据库 | Elasticsearch |
|-------------|---------------|
| 数据库 | 索引（Index） |
| 表 | 类型（Type，7.x 已弃用） |
| 行 | 文档（Document） |
| 列 | 字段（Field） |

### 常用组件
- **elasticsearch-head**：浏览器端数据展示插件
- **Kibana**：官方可视化分析平台，推荐用于数据查询
- **IK Analyzer**：中文分词插件，支持自定义词库

## 关联连接
- [[Lucene]] — 底层全文检索引擎库
- [[Kibana]] — ES 可视化平台
- [[Solr]] — 同类搜索引擎
- [[inverted-index]] — 倒排索引核心数据结构
- [[full-text-search]] — 全文搜索引擎概念
- [[analyzer]] — 分词器与文本分析
- [[摘要-elasticsearch-quick-start]] — 来源
- [[elasticsearch-disadvantages]] — ES 缺点分析
