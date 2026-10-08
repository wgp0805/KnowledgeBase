---
title: "摘要-分布式session实现难点"
type: source
tags: [来源, 原始文件, 分布式Session, Java, Redis, 面试]
sources: ["raw/01-articles/2026-10-04 - 面试难题：分布式 Session 实现难点，这篇就够！.md"]
last_updated: 2026-10-08
---

## 核心摘要
单机 Tomcat 项目无 Session 共享问题，但部署多个微服务并用 Nginx 默认轮询负载均衡时，用户在 Tomcat1 登录、下一次请求被分到 Tomcat2，Tomcat2 的 Session 里没有用户信息，导致频繁重新登录。四种解决方案对比：①Session 复制——免改代码只改 Tomcat 配置，但同步传输占内网带宽、多台同步性能指数级下降、占内存无法有效水平扩展；②前端存储（Cookie）——不占服务器内存，但有安全风险、数据大小受 cookie 限制、占外网带宽；③Session 粘滞（Sticky）——免改代码、服务端可水平扩展，但新增机器重新 Hash 导致重新登录、应用重启也需重新登录；④后端集中存储——安全、易水平扩展，但增加复杂度且需改代码。Java 落地两条实现路径：Spring Session + Redis（引 spring-boot-starter-data-redis、commons-pool2、spring-session-data-redis 依赖并配 Redis 连接池，登录后 request.getSession() 自动写入 Redis，业务代码几乎无感）；或直接用 RedisTemplate 手工存取（UUID 生成 ticket 写入 `user:{ticket}` 键、Cookie 下发 userTicket，读取时按 ticket 从 Redis 取用户信息）。

## 关联连接
- [[分布式会话]] — 核心概念
- [[SpringSession]] — 首选实现框架
- [[Redis]] — 集中存储介质
- [[Session]] — 问题根源对象
