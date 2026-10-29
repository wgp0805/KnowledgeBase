---
title: "Nginx"
type: entity
tags: [Web服务器, 反向代理]
sources: [raw/09-archive/nginx配置.md, raw/09-archive/服务器部署纯静态网站.md, raw/09-archive/hexo博客部署到自己的服务器.md, raw/09-archive/2026-08-24 - 拒绝再买服务器！我用 Docker + FRP 实现内网穿透，舒服~.md, raw/09-archive/2026-10-28 - Cloudflare正式开源Nginx替代品：Pingora.md]
last_updated: 2026-10-29
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

### 被替代的叙事：Pingora（来源：[[摘要-cloudflare开源pingora]]）
2022 年起 [[Cloudflare]] 已用 Rust 写的 [[Pingora]] 替换 Nginx 作为内部代理，2026-10 正式开源。这件事对 Nginx 的意义不是"技术过时"，而是暴露了它的**能力边界**：

- **边界一：可编程性**。Nginx 的扩展要靠 C 模块（高风险）或 [[OpenResty]] 的 Lua 层。Pingora 直接把代理逻辑写成 Rust 程序（filters + callbacks），把"配置代理"变成"编程代理"
- **边界二：内存安全**。Cloudflare 的动机是让"难以安全实现的功能"成为可能（类 Wireshark 的过滤语言、跑用户 JS、即时重写 HTML 响应），而不是单纯追求吞吐
- **反方意见**：[[OpenResty]] 作者 [[章亦春]] 认为这是新工程师"搞不定" Nginx 的重造轮子，用 Rust 写解释型网关是退步
- **现实结论**：Pingora 处于 pre-1.0、API 不稳定、仅支持 Unix，且只有 Cloudflare 一家超大规模验证。**绝大多数团队的 nginx.conf 仍然是性价比最高的选择**，不必因此迁移

## 关联连接
- [[Pingora]] — Cloudflare 的 Rust 替代品（2022 起生产使用，2026-10 开源）
- [[OpenResty]] — Nginx + Lua 的可编程扩展路线
- [[章亦春]] — OpenResty 作者，Pingora 批评者
- [[Cloudflare]] — 替代事件的发生方
- [[SpringBoot]] — 后端代理目标
- [[Linux]] — 运行环境
- [[FRP]] — 内网穿透场景中内网常见服务
- [[摘要-docker-frp-内网穿透]] — 来源（内网穿透场景）
- [[摘要-日志分析命令组合拳]] — 来源（access.log 分析）
- [[摘要-cloudflare开源pingora]] — 来源（被替代叙事）
- [[日志分析]] — 场景化排查方法论
- [[awk]] — access.log 列处理工具
