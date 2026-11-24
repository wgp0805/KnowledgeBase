---
title: "UptimeKuma"
type: entity
tags: [工具, Docker, 监控, 自托管]
sources: ["raw/09-archive/2026-11-20 - 8 个让你直呼卧槽的 Docker 神器，让你的服务器瞬间开挂！.md"]
last_updated: 2026-11-24
---

## 定义
Uptime Kuma（镜像 `louislam/uptime-kuma`）是开源的自托管服务监控工具，实时监控网站与服务的可用性并推送告警。

## 关键信息
- 实时监控：HTTP(s)、TCP、Ping、DNS、关键词、心跳等多种探针
- 通知渠道：邮件、Telegram、Slack、Webhook 等数十种
- 卖点是"好看 + 配置简单"，适合个人或小团队监控自己的服务与站点
- 最小启动：`-p 3001:3001 -v uptime-kuma:/app/data louislam/uptime-kuma:1`，`restart: always`
- 常与 [[Homer]] / [[Dockge]] 一起作为自托管面板组的门面
- 边界：轻量可用性监控，不替代 [[Prometheus]] + Grafana 那套指标/链路可观测体系

## 关联连接
- [[Docker]] — 分发方式
- [[Prometheus]] — 指标监控对照（可观测性体系）
- [[Dockge]] — 同为面板型自托管工具
- [[Netdata]] — 主机级监控对照
- [[摘要-8个docker神器]] — 来源
