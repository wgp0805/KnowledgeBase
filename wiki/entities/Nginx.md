---
title: "Nginx"
type: entity
tags: [Web服务器, 反向代理]
sources: [raw/09-archive/nginx配置.md, raw/09-archive/服务器部署纯静态网站.md, raw/09-archive/hexo博客部署到自己的服务器.md, raw/01-articles/2026-08-24 - 拒绝再买服务器！我用 Docker + FRP 实现内网穿透，舒服~.md]
last_updated: 2026-09-09
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

### access.log 分析（来源：[[摘要-日志分析命令组合拳]]）
Nginx 访问日志是格式规范的列式数据，最适合用 [[awk]] 直接生成简报：

- **找访问量最高的 IP**（第一列为 IP）：awk '{print $1}' access.log | sort | uniq -c | sort -nr | head -n 10。服务突然报警 CPU 飙升、怀疑遭 CC 攻击或爬虫抓取时，这是最快的第一步
- **找响应最慢的接口**（响应时间在最后一列）：awk '$NF > 1.000 {print $7, $NF}' access.log，$NF 代表最后一列

## 关联连接
- [[SpringBoot]] — 后端代理目标
- [[Linux]] — 运行环境
- [[FRP]] — 内网穿透场景中内网常见服务
- [[摘要-docker-frp-内网穿透]] — 来源（内网穿透场景）
- [[摘要-日志分析命令组合拳]] — 来源（access.log 分析）
- [[日志分析]] — 场景化排查方法论
- [[awk]] — access.log 列处理工具
