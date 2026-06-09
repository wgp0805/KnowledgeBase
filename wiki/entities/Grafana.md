---
title: "Grafana"
type: entity
tags: [监控, 可视化, 仪表盘]
sources: [raw/01-articles/全链路灰度发布：从"灰飞烟灭"到"稳如老狗"，我只用了这8步！！.md]
last_updated: 2026-06-09
---

## 定义
Grafana 是一个开源的指标分析和可视化平台，支持 Prometheus、InfluxDB、Elasticsearch 等多种数据源，提供丰富的仪表盘模板和告警能力。

## 关键信息
- 多数据源：支持 Prometheus、MySQL、ES 等
- 仪表盘模板：社区共享模板（如 Spring Boot 模板 ID 12856）
- 灰度场景：配合 Prometheus 监控灰度服务 vs 生产服务的性能对比（QPS、响应时间、错误率）

## 关联连接
- [[Prometheus]] — 指标数据源
- [[grayscale-release]] — 灰度发布监控可视化
