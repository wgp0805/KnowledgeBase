---
title: "Nginx"
type: entity
tags: [Web服务器, 反向代理]
sources: [raw/01-articles/nginx配置.md, raw/01-articles/服务器部署纯静态网站.md, raw/01-articles/hexo博客部署到自己的服务器.md]
last_updated: 2026-05-19
---

## 定义
Nginx 是一个高性能的 HTTP 和反向代理 Web 服务器，以高并发、低内存消耗著称，广泛用于静态资源服务、反向代理、负载均衡和 SSL 终端。

## 关键信息
- location 匹配规则：= 精确匹配、^~ 前缀匹配、~ 正则匹配（区分大小写）、~* 正则匹配（不区分大小写）
- proxy_pass 路径处理：加 / 截取匹配路径，不加 / 拼接完整路径
- root vs alias：root 不替换匹配路径，alias 替换匹配路径
- 反向代理配置：proxy_set_header、proxy_pass、proxy_redirect
- 静态资源服务：root + try_files 配置 SPA 前端路由
- rewrite 重写规则使用正则和标志（last/break/redirect/permanent）

## 关联连接
- [[SpringBoot]] — 后端代理目标
- [[Linux]] — 运行环境
