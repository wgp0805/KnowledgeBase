---
title: "Elasticsearch"
type: entity
tags: [搜索引擎, 全文检索, 分布式, 大数据]
sources:
  - raw/09-archive/从 0 到 1 学习 elasticsearch ，这一篇就够了！(建议收藏).md
  - raw/09-archive/Elasticsearch 8.10安装（新人必看）.md
  - raw/09-archive/Elasticsearch 全景指南：从入门到原理深度解析.md
  - raw/01-articles/拼多多二面：为什么要使用 ElasticSearch？和传统关系数据库 MySQL 有什么不同？.md
  - raw/01-articles/2026-08-31 - 面试官：ElasticSearch 为什么快？.md
last_updated: 2026-09-01
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

### ES 不是银弹（面试反问场景）
- **强事务场景别用**：无真正 ACID，跨文档无法回滚（账户扣款、订单状态流转）
- **频繁更新场景别用**：segment 不可变，更新是"标记删除 + 新写入"，写放大严重（库存类字段）
- **多表关联查询别用**：`join` 能力弱（nested/parent-child 性能坑）
- **内存成本**：JVM 堆 + 文件缓存都要预留足，小数据量上 ES 纯属找事

### 为什么快（面试深度解析，四层叠加）
ES 快是"一堆优化叠出来的"，没有单点魔法，按"数据结构 → 存储 → 架构 → 写入"四层拆解：

**① 数据结构层**
- **倒排索引**：从"关键词 → 文档列表"，避开全表扫描。写入时多干活（分词、建索引），查询时少干活
- **FST + Term Index**：词典查询拆三层——Term Index（内存里的"目录页"，用 FST 只存前缀，体积极小）→ Term Dictionary（磁盘上的有序词典）→ Posting List。FST 三大特点：前缀共享（cat/catalog/catalogue 共用 cat）、查询 O(len)（只跟查询词长度有关）、内存占用小
- **Posting List 压缩**：文档 ID 先 delta 编码，再 Frame of Reference 压缩成块，配跳表（Skip List）支持快速跳块；Roaring Bitmap 用于 filter 缓存的 DocIdSet 求交并集
- **BKD-Tree**：数值类型和地理位置用空间多维索引，范围查询效率高

**② 存储层**
- **Segment 不可变**：读取无锁（天生线程安全）、压缩率高（可用激进压缩）、吃满 Page Cache（热数据几乎全驻内存）
- **Doc Values 列式存储**：排序聚合直接读列式存储，不用回源解析原文

**③ 架构层**
- **分片并行查询**：scatter-gather 模式，协调节点广播到所有分片并行执行，数据量翻倍加机器即可
- **缓存体系**：Page Cache 扛大头 + Shard Request Cache（分片级聚合结果）+ Query Cache（过滤查询位图）

**④ 写入侧（近实时 NRT）**
- **refresh**（默认 1s）：Buffer 生成新 Segment 进文件系统缓存，可搜索但未落盘 → 这就是"近实时"的由来
- **flush**（默认 30 分钟或 Translog 512MB）：Segment 真正 fsync 到磁盘，清空 Translog
- **force merge**：多个小 Segment 合并成大的，查询提速但吃资源，建议低峰期做

### 面试高频追问
- **ES 是实时的吗？** 不是，是近实时。写入到可搜索默认有 1 秒 refresh 间隔。强一致场景（秒杀扣库存）别用 ES
- **ES 为什么深分页慢？** `from + size` 每个分片都要取 `from + size` 条到协调节点排序。生产用 `search_after`，导出用 Scroll
- **refresh/flush/force merge 分别干什么？** refresh=Buffer 生成 Segment 进缓存（可搜索）；flush=Segment 落盘清 Translog；force merge=合并小 Segment
- **Segment 不可变，更新删除怎么办？** 打标记（.del 文件记录删除文档号），查询时过滤，物理删除等 Segment 合并

### 记忆口诀
**结构看三层：目录（Term Index/FST）→ 词典（Term Dictionary）→ 倒排列表（Posting List）；存储两板斧：不可变 Segment + 列式 Doc Values；架构一手牌：分片并行加缓存；写入近实时：1 秒 refresh 见。**

### 生产架构：MySQL + ES 黄金搭档
- **MySQL 是唯一数据源（Source of Truth）**，写操作先进 MySQL 保证事务完整
- 通过 **Canal 监听 Binlog**（或 Flink CDC）→ MQ → 消费写入 ES，业务与同步解耦
- 搜索请求全部打到 ES，MySQL 只服务正常业务读写
- MQ 削峰 + 失败重试保证最终一致性
- 实战案例：5000 万商品 + 多条件筛选 + 关键词搜索，搜索响应稳定百毫秒内

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
- [[摘要-拼多多二面-es-vs-mysql]] — 来源（面试视角 ES vs MySQL）
- [[摘要-es-为什么快-面试深度]] — 来源（面试深度解析为什么快）
- [[FST]] — 有限状态转换器，Term Index 核心
- [[TermIndex]] — 词典的"目录页"
- [[DocValues]] — 列式存储，排序聚合加速
- [[Segment]] — Lucene 不可变存储单元
- [[BM25]] — 相关性评分算法
- [[InvertedIndex]] — 倒排索引概念页
- [[NearRealTime]] — 近实时机制概念页
- [[BPlusTree]] — 对比数据结构（MySQL 索引底层）
- [[Canal]] — MySQL → ES 同步工具
- [[elasticsearch-disadvantages]] — ES 缺点分析
