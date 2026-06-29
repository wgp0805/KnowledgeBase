---
title: "摘要-Spring-Cloud-Gateway-War-Tomcat"
type: source
tags: [来源, Spring Cloud Gateway, Tomcat, War, WebFlux]
sources: [raw/01-articles/2026-06-26-Spring Cloud Gateway 打 War 包部署外置 Tomcat 全攻略：原理、实现与踩坑实录 - 码猿手.md]
last_updated: 2026-06-29
---

## 核心摘要
本文完整记录了让标准 Spring Cloud Gateway（WebFlux 版）以 War 包形式部署到外置 Tomcat 的改造方案。核心思路是自定义 WebApplicationInitializer，用 SpringApplication.run() 启动上下文，同时通过空壳 WebServer 排除内嵌 Netty 冲突。文章深入剖析了请求处理全链路（从 ServletHttpHandlerAdapter 到 DispatcherHandler），并指出该方案存在底层 IO 模型冲突（Netty 非阻塞 vs Tomcat 阻塞）、高阶特性兼容 Bug、生命周期缺陷等致命短板，QPS 下降 50% 以上，结论是"理论可行但生产不推荐"，建议改用原生 jar 包或 spring-cloud-starter-gateway-mvc。

## 关联连接
- [[SpringCloudGateway]] — 改造目标组件
- [[Tomcat]] — 外置 Servlet 容器
- [[SpringBoot]] — 基础框架
- [[Servlet]] — Servlet 规范适配
- [[microservices]] — 微服务架构
- [[grayscale-release]] — 灰度路由兼容性问题
