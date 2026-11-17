---
title: "ELK日志系统"
type: concept
tags: [日志, Elasticsearch, Logstash, Kibana, Filebeat, 可观测性]
sources: [raw/09-archive/2026-09-09-从零搭建ELK日志采集系统：Filebeat + Logstash + ES + Kibana 保姆级教程 - 佛祖让我来巡山.md, raw/09-archive/2026-11-16 - SpringBoot集成Hera，让日志查看从“找罪证”变“查答案”！.md]
last_updated: 2026-11-17
---

# ELK日志系统

## 核心定义
Elasticsearch + Logstash + Kibana 组合的日志采集分析系统，提供从分布式日志采集、解析过滤、存储搜索到可视化的完整链路。

## 关键要点
- 架构：Filebeat（采集）→ Logstash（过滤/解析）→ Elasticsearch（存储/搜索）→ Kibana（可视化）
- 核心价值：分布式日志统一采集、全文检索、实时监控
- Filebeat 替代早期 Logstash 采集端，降低资源消耗

## 详细说明

### 架构分层
1. **采集层（Filebeat）**：轻量级日志采集器，部署在各应用节点，支持多输入源、背压机制
2. **处理层（Logstash）**：强大的管道处理能力，支持 Grok 解析、字段过滤、字段增强
3. **存储层（Elasticsearch）**：分布式搜索引擎，支持全文检索、聚合分析
4. **展示层（Kibana）**：可视化仪表盘、日志查询、告警配置

### 核心价值
- **统一采集**：解决分布式系统日志分散问题
- **全文检索**：基于倒排索引实现毫秒级日志搜索
- **实时监控**：通过 Kibana 仪表盘实时展示系统状态
- **告警能力**：配合 Watcher 或 Kibana Alerting 实现异常告警

### 演进趋势
- ELK → EFK（Filebeat/Kafka 替代 Logstash）
- 引入 Kafka 作为缓冲层，解耦采集与处理
- 向可观测性平台演进，整合 Metrics、Logs、Traces

### 与 Hera 的对照（2026-11-16，详见 [[Hera]]）
ELK 强在"采集-解析-存储-检索"的通用链路，但缺乏**业务维度**聚合能力——查"某用户的下单日志"需要拼接用户 ID/订单号等多个条件。Hera 一类业务日志平台在 Agent 采集期注入业务标签（businessType/env/userId），实现按业务字段直筛、traceId 全链路串联与按业务重要性分级存储（核心进 ES、归档进 HDFS）。两者可互补：ELK 做通用日志底座，Hera 做业务视角的检索与链路溯源。

## 关联连接
- [[Elasticsearch]]
- [[Logstash]]
- [[Kibana]]
- [[Filebeat]]
- [[Hera]] — 业务日志平台对照（业务标签聚合 + 分级存储）
- [[摘要-elk日志系统搭建教程]] — Docker Compose 四件套搭建教程来源
- [[摘要-springboot集成hera日志平台]] — 对照来源（Hera 五层架构与集成）
