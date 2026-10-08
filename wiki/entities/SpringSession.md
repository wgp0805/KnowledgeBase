---
title: "SpringSession"
type: entity
tags: [Java, Spring, Session, 分布式, 开源框架]
sources: ["raw/01-articles/2026-10-04 - 面试难题：分布式 Session 实现难点，这篇就够！.md"]
last_updated: 2026-10-08
---

## 定义
Spring Session 是 Spring 家族解决分布式 Session 问题的框架：把 HttpSession 存储透明地切换到外部共享介质（典型为 Redis），业务代码沿用 `request.getSession()` 不变，Session 数据自动写入 Redis 实现多节点共享。

## 关键信息
- **依赖组合**：`spring-boot-starter-data-redis` + `commons-pool2`（对象池）+ `spring-session-data-redis`
- **配置要点**：Redis host/port/database、connect-timeout、lettuce 连接池（max-active/max-wait/max-idle/min-idle）
- **代码体验**：登录时 `request.getSession().setAttribute(ticket, user)` 后 Session 即存入 Redis，视图层照常 `session.getAttribute(ticket)`——对业务透明，区别于手工 `RedisTemplate.opsForValue().set("user:"+ticket, user)` 的方案
- **适用场景**：多 Tomcat/微服务 + Nginx 负载均衡下避免用户频繁重新登录，属四种方案（复制/前端存储/粘滞/后端集中存储）中的"后端集中存储"落地方式

## 关联连接
- [[摘要-分布式session实现难点]] — 来源
- [[分布式会话]] — 解决的问题概念
- [[Redis]] — 默认共享存储
- [[Session]] — 被管理的对象
