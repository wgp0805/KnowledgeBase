---
title: "Elasticsearch"
type: entity
tags: [搜索引擎, 全文检索, 分布式, 大数据]
sources:
  - raw/01-articles/从 0 到 1 学习 elasticsearch ，这一篇就够了！(建议收藏).md
  - raw/01-articles/Elasticsearch 8.10安装（新人必看）.md
  - raw/01-articles/Elasticsearch 全景指南：从入门到原理深度解析.md
last_updated: 2026-06-08
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

### 8.x 安全特性（默认启用）
从 ES 8.x 开始默认启用安全功能：
- **HTTPS**：所有通信默认使用 HTTPS，安装时自动生成自签名 TLS/SSL 证书
- **身份验证**：默认创建 elastic 用户并生成随机密码，首次启动时在控制台输出
- 密码可通过 `elasticsearch-reset-password -u elastic` 重置
- 开发环境可通过修改 `elasticsearch.yml` 设置 `xpack.security.enabled: false` 和 `xpack.http.ssl.enabled: false` 禁用

### 相关性评分（BM25）
ES 8.x 默认使用 **BM25 算法**（替代旧版 TF-IDF）：
- **词频 (TF)**：词在文档中出现越多分数越高（有饱和效应）
- **逆文档频率 (IDF)**：词越罕见区分度越高
- **字段长度归一化**：短文档中出现的词比长文档更有价值

### 近实时机制
ES 是近实时搜索引擎（默认约 1 秒延迟）：
- **写入** → In-Memory Buffer → **Refresh**（默认 1s）→ File System Cache（可搜索）→ **Flush** → Disk
- **Refresh**：内存 Buffer 刷到文件系统缓存，文档可搜索但未落盘
- **Translog**：保证数据持久性，断电不丢失

### 分布式架构（分片路由）
- **写入流程**：客户端 → 协调节点 → 根据 `hash(_routing) % num_shards` 路由到主分片 → 主分片写入后并行复制到副本 → 全部确认后返回
- **读取流程**：协调节点广播到所有分片（主/副均可）→ 各分片本地排序后返回 top N → 全局归并排序返回

### 常见问题
| 问题 | 原因 | 解决方案 |
|------|------|----------|
| 写入慢 | 单条写入、副本过多 | 使用 Bulk API 批量写入；写入时临时设 replicas=0 |
| 深分页慢 | from+size 需全局排序 | 使用 search_after 或 Scroll API |
| 集群 Yellow | 副本分片未分配 | 检查节点数 ≥ 副本数+1；磁盘水位线 |
| 集群 Red | 主分片未分配 | 检查节点存活；reroute 手动分配 |
| 搜索结果不准 | Mapping 类型错误 | text vs keyword 选错；中文未配置 IK |
| 字段冲突 | 动态 Mapping 自动推断 | 生产环境手动定义 Mapping，关闭 dynamic |

## 关联连接
- [[Lucene]] — 底层全文检索引擎库
- [[Kibana]] — ES 可视化平台
- [[Solr]] — 同类搜索引擎
- [[inverted-index]] — 倒排索引核心数据结构
- [[full-text-search]] — 全文搜索引擎概念
- [[analyzer]] — 分词器与文本分析
- [[摘要-elasticsearch-quick-start]] — 来源（基础入门）
- [[摘要-elasticsearch-8.10-install]] — 来源（8.10 安装与安全配置）
- [[摘要-elasticsearch-comprehensive-guide]] — 来源（全景原理深度解析）
- [[BM25]] — 相关性评分算法
- [[elasticsearch-disadvantages]] — ES 缺点分析
