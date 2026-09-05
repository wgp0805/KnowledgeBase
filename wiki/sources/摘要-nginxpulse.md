---
title: "摘要-nginxpulse"
type: source
tags: [Nginx, 日志分析, 运维工具]
sources: [raw/01-articles/终于找到一个好用的 Nginx 日志分析工具了.md]
last_updated: 2026-08-11
---

## 核心摘要
介绍开源项目 **NginxPulse**——一个轻量级的 Nginx 日志分析面板，定位介于纯命令行的 GoAccess 和重量级的 ELK 之间的"中间选择"。技术栈为 Go + Gin 后端、Vue3 + Vite + PrimeVue 前端、SQLite 存储，足够轻量。核心功能包括实时 PV/UV 统计、IP 归属地查询（国内用 ip2region 本地库、国外走 ip-api，先查内存缓存再远程批量查、失败本地兜底）、客户端/浏览器解析、多站点支持与自定义日志格式。支持 Docker 一键部署（前端 8088 / 后端 8089）、多站点 WEBSITES 数组配置、通配符与 .gz 压缩日志直接解析，以及 SFTP/HTTP/S3 拉取远端日志、Push Agent、Caddy 日志类型、访问密钥（ACCESS_KEYS + X-NginxPulse-Key 请求头）等实用功能。目前 2.6k star，MIT 协议，GitHub: likaia/nginxpulse。

## 关键信息
- 一句话定位：轻量级 Nginx 日志分析面板，无需 ELK 的重量级、比 GoAccess 更直观
- 技术栈：Go + Gin / Vue3 + Vite + PrimeVue / SQLite
- IP 归属地三级策略：内存缓存 → 远程 API 批量查 → 本地 ip2region 兜底（速度与准确率兼顾）
- Docker 部署：`docker run` 一行命令，`-p 8088:8088`（前端面板）`-p 8089:8089`（后端 API）
- 多站点：`WEBSITES` 传 JSON 数组；日志按天切割支持通配符 `access-*.log`；.gz 压缩日志可直接解析
- 远端日志：SFTP / HTTP / S3/OSS 三种拉取方式；内网或边缘节点可用 Push Agent 主动推送
- 自定义格式：`logFormat`（log_format 语法）或 `logRegex`（正则命名分组）两种方式；Caddy 用户配置 `logType: "caddy"` 按 JSON 解析
- 访问控制：`ACCESS_KEYS='["your-secret-key"]'` 配合 X-NginxPulse-Key 请求头
- 常见坑：日志明细为空多半是权限问题（chmod -R 777）；PV/UV 为 0 是因为默认排除内网 IP（`PV_EXCLUDE_IPS='[]'` 可关闭）
- 单体部署：`./scripts/build_single.sh` 生成内置前端的单个二进制，支持 amd64/arm64

## 关联连接
- [[NginxPulse]] — 项目实体
- [[Nginx]] — 分析对象（Web 服务器）
- [[Docker]] — 部署方式
- [[Vue3]] — 前端技术栈
