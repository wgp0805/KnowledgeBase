---
title: "Prometheus"
type: entity
tags: [监控, 时序数据库, 微服务]
sources: [raw/01-articles/全链路灰度发布：从"灰飞烟灭"到"稳如老狗"，我只用了这8步！！.md]
last_updated: 2026-06-09
---

## 定义
Prometheus 是一个开源的系统监控和告警工具包，最初由 SoundCloud 构建，后加入 CNCF。它采用拉取（Pull）模式采集指标，支持多维数据模型（指标名 + 标签）和 PromQL 查询语言。

## 关键信息
- 架构：Pull 架构定期从目标服务抓取指标
- 数据模型：时间序列数据，以 metric 和 label 标识
- 集成方式：服务端引入 `micrometer-registry-prometheus` 暴露 `/actuator/prometheus` 端点
- 灰度场景：监控灰度服务的 QPS、响应时间、错误率，与生产服务做对比

## 关联连接
- [[Grafana]] — 可视化仪表盘
- [[grayscale-release]] — 灰度发布监控
- [[SpringBoot]] — Actuator 集成
