---
title: "从零搭建ELK日志采集系统：Filebeat + Logstash + ES + Kibana 保姆级教程"
type: source
tags: [ELK, 日志采集, Docker, DevOps, 运维, Filebeat, Logstash, Elasticsearch, Kibana]
sources: [raw/01-articles/2026-09-09-从零搭建ELK日志采集系统：Filebeat + Logstash + ES + Kibana 保姆级教程 - 佛祖让我来巡山.md]
last_updated: 2026-09-14
---

# 摘要：从零搭建ELK日志采集系统

## 核心摘要
本文提供了一套基于 Docker Compose 一键部署 Filebeat + Logstash + Elasticsearch + Kibana 四件套的完整教程。架构轻量级（无需Kafka中间件），适合中小规模项目（日日志量 < 500GB），所有服务容器化运行，配置完整注释，复制修改路径即可启动。

## 关键要点
- 架构：Spring Boot应用 → 日志文件 → Filebeat（采集）→ Logstash（处理）→ Elasticsearch（存储检索）→ Kibana（可视化）
- 轻量级架构，无需Kafka中间件，适合日日志量 < 500GB的中小规模项目
- 前提条件：Docker 20.10+、至少4GB可用内存（推荐8GB）、Java应用日志输出到目录
- Filebeat通过multiline处理Java异常堆栈，保证完整异常作为一条事件
- Logstash支持JSON解析（推荐，配合logstash-logback-encoder）和Grok正则解析两种模式
- ES索引按天切分（app-logs-YYYY.MM.dd），便于管理
- 常见坑：Filebeat权限问题（user:root）、Logstash连ES（depends_on）、Kibana看不到日志（索引模式/时间选择器）
- 进阶优化：Logback输出JSON、调整pipeline.workers、配置ILM索引生命周期、添加Prometheus监控

## 详细内容

### 整体架构与数据流
```
Spring Boot应用 → 日志文件(/var/log/myapp/*.log)
  → Filebeat(tail读取, Beats协议:5044)
  → Logstash(解析/过滤, Bulk API:9200)
  → Elasticsearch(存储&检索)
  → Kibana:5601(可视化)
  → 开发者/运维
```

### 四组件职责
| 组件 | 角色 | 功能 |
|------|------|------|
| Filebeat | 采集器 | 监控日志文件变化，读取新行，发送给Logstash |
| Logstash | 处理器 | 接收日志，正则/JSON解析成结构化数据，输出到ES |
| Elasticsearch | 存储检索引擎 | 存储日志，建立倒排索引，支持全文检索 |
| Kibana | 可视化界面 | Web界面，搜索日志、制作图表 |

### 目录结构
```
elk-demo/
├── docker-compose.yml
├── filebeat/
│   └── filebeat.yml
├── logstash/
│   └── pipeline/
│       └── logstash.conf
└── elasticsearch/
    └── data/
```

### 关键配置要点

**Filebeat配置要点：**
- multiline处理Java异常堆栈：`pattern: '^\d{4}-\d{2}-\d{2}'`，不匹配时合并到上一行
- 自定义字段：app_name、env，fields_under_root设为true
- 内存队列：events 4096，flush.min_events 1024，flush.timeout 5s

**Logstash管道（input → filter → output）：**
- JSON模式（推荐）：配合logstash-logback-encoder，效率最高，无需Grok
- Grok模式：纯文本日志用正则解析
- 索引按天切分：`index => "app-logs-%{+YYYY.MM.dd}"`
- bulk_size 5000，bulk_timeout 60s

**Docker Compose关键配置：**
- ES：single-node模式，关闭xpack.security，JVM堆1GB
- Logstash：JVM内存限制512m
- Kibana：I18N_LOCALE=zh-CN
- Filebeat：user:root读取宿主机日志，挂载data目录保存registry

### 验证链路
1. 访问 `http://localhost:9200` 检查ES
2. `curl localhost:9200/_cat/indices?v` 检查索引
3. Kibana创建Index Pattern（app-logs-*，时间字段@timestamp）
4. Discover中搜索：`level:"ERROR"`、`app_name:"my-springboot-app"`、`message:"超时"`

### 常见问题
| 问题 | 原因 | 解决 |
|------|------|------|
| Filebeat无法读取日志 | 权限 | user:root 或 chmod o+r |
| Logstash连不上ES | 启动顺序 | depends_on + 重试机制 |
| Kibana看不到日志 | 索引模式/时间选择器 | 检查Index Pattern和时间范围 |
| 日志重复 | registry丢失 | 挂载data目录，勿删 |
| 磁盘不足 | 无保留策略 | 配置ILM自动删除过期索引 |

### 进阶优化建议
- 日志格式：Logback输出JSON，避免Grok解析，大幅提升性能
- Filebeat多行合并：根据日志格式调整multiline.pattern
- Logstash性能：调整pipeline.workers和pipeline.batch.size
- ES内存：至少分配2GB
- 索引生命周期：ILM自动转只读或删除超过7天的索引
- 监控告警：Prometheus + Grafana

## 关联连接
- [[ELKStack]]
- [[DockerCompose]]
- [[日志采集架构]]
- [[Elasticsearch]]
- [[Logstash]]
- [[Filebeat]]
- [[Kibana]]
- [[DevOps实践]]
