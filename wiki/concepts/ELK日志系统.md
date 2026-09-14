---
title: "ELK日志系统"
type: concept
tags: [日志, Elasticsearch, Logstash, Kibana, Filebeat, 可观测性]
last_updated: 2026-09-14
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

## 关联连接
- [[Elasticsearch]]
- [[Logstash]]
- [[Kibana]]
- [[Filebeat]]
