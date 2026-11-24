---
title: "摘要-nginx生产级配置实战"
type: source
tags: [来源, Nginx, 反向代理, 部署]
sources: ["raw/09-archive/2026-11-23 - Nginx 配置实战：从摸鱼到部署，手把手教你搞定生产级配置.md"]
last_updated: 2026-11-24
---

## 核心摘要
终码一生 2026-11-23 的 Nginx 生产配置速查（原文 juejin.cn/post/7510819038953930763），按四个真实场景给可直接抄的配置片段。①**反向代理 + 负载均衡**：`upstream` 列出 3 台后端，`least_conn` 最小连接数、`keepalive 32` 复用长连接减少握手、`proxy_next_upstream error timeout http_500` 失败自动重试；`location /api/` 转发并设 `X-Real-IP` / `X-Forwarded-For` / `Host`，配 connect/read/send 超时，价值是隐藏真实 IP、流量均摊。②**静态资源 + 动静分离**：`root /data/`、`autoindex off`、`expires 30d`、`gzip on` + `gzip_types`，并用 `valid_referers` 做图片防盗链（非法引用返回 403），让 Nginx 直接吐文件、后端只处理接口。③**限流防刷 + IP 黑白名单**：`limit_conn_zone`（单 IP 并发连接数，10m 共享内存）与 `limit_req_zone rate=5r/s`（令牌桶），登录接口 `limit_conn 10` + `limit_req burst=10 nodelay`，配合 `deny` 与白名单判断返回 403，防 CC 打崩与日志爆量。④**HTTPS**：`listen 443 ssl`、`ssl_protocols TLSv1.2 TLSv1.3`、`ssl_ciphers`、`ssl_prefer_server_ciphers on`、`rewrite ^(.*)$ https://$host$1 permanent` 强制跳转。

运维收尾：`yum/apt install nginx` 或 Windows 解压启动；`systemctl start/restart nginx`；改完配置必须先 `nginx -t` 校验再重启。作者强调配置不是一次性的，要按服务器压力与用户反馈动态调整限流阈值、及时拉黑恶意 IP。

## 关联连接
- [[Nginx]] — 本篇主角（已增量合并）
- [[反向代理]] — 场景一的概念底座
- [[负载均衡]] — upstream 策略与健康剔除
- [[限流]] — limit_req / limit_conn 令牌桶与并发控制
- [[IP限流]] — 单 IP 维度限流
- [[动静分离]] — 静态资源与接口分流
- [[DockerCompose生产配置]] — 部署形态对照
- [[SpringBoot]] — 被反代的典型后端
