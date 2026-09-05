---
title: "NginxPulse"
type: entity
tags: [日志分析, Nginx, 运维, 开源]
sources: [raw/01-articles/终于找到一个好用的 Nginx 日志分析工具了.md]
last_updated: 2026-08-11
---

## 定义
NginxPulse 是开源（MIT）的轻量级 Nginx 日志分析面板，用 Go + Vue3 + SQLite 实现，实时展示 PV/UV、IP 归属地、客户端/浏览器分布等访问数据，定位是比 ELK 轻量、比 GoAccess 直观的"中间选择"。

## 关键信息
- 作者/仓库：likaia/nginxpulse，目前 2.6k star
- 技术栈：Go + Gin（后端）、Vue3 + Vite + PrimeVue（前端）、SQLite（存储）
- 核心功能：实时 PV/UV、IP 归属地（ip2region 本地库 + ip-api）、客户端/浏览器解析、多站点、自定义日志格式
- IP 归属地策略：内存缓存 → 远程 API 批量 → 本地 ip2region 兜底，兼顾速度与准确率
- 部署：Docker 一行命令（8088 前端面板 / 8089 后端 API）；也支持单体二进制（amd64/arm64）
- 特色能力：SFTP/HTTP/S3 拉远端日志、Push Agent、通配符与 .gz 日志、Caddy 支持、ACCESS_KEYS 访问控制
- 配置要点：多站点用 `WEBSITES` 数组；排除内网 IP 用 `PV_EXCLUDE_IPS`；自定义格式用 `logFormat`/`logRegex`
- 在线演示：https://nginx-pulse.kaisir.cn/

## 关联连接
- [[摘要-nginxpulse]] — 来源摘要
- [[Nginx]] — 日志来源服务器
- [[Docker]] — 主要部署方式
- [[Vue3]] — 前端技术栈
