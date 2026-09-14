---
title: "Filebeat"
type: entity
tags: [ELK, 日志采集, Elastic, 数据管道]
last_updated: 2026-09-14
---

# Filebeat

## 身份定义
Filebeat 是 Elastic 开源的轻量级日志采集器，属于 Elastic Stack（ELK）生态的第一环。它负责监控指定的日志文件或路径，并将日志数据转发到 Logstash 或 Elasticsearch。

## 核心功能/特征
- 监控指定日志文件/路径，实时采集日志内容
- 支持将日志转发到 Logstash 进行处理，或直接写入 Elasticsearch
- 轻量级设计，资源占用低，适合部署在各类节点上
- 在 ELK 数据管道中承担第一环角色：Filebeat → Logstash → ES → Kibana

## 关联连接
- [[Elasticsearch]]
- [[Logstash]]
- [[Kibana]]
