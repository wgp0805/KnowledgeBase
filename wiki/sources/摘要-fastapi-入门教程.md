---
title: "摘要-fastapi-入门教程"
type: source
tags: [来源, 原始文件, Python, Web框架, API]
sources: [raw/01-articles/FastAPI 入门教程.md]
last_updated: 2026-06-29
---

## 核心摘要
苏三《FastAPI 入门教程》从 Java 开发者视角系统讲解 Python 高性能 Web 框架 FastAPI。FastAPI 由 Sebastián Ramírez 在 2018 年创建，GitHub 80K+ Star，定位"三高"——高开发效率、高运行性能、高类型安全。本质区别是基于 **ASGI 异步规范**（vs Flask/Django 的 WSGI 同步规范），通过 **Starlette + Pydantic + Uvicorn** 三引擎驱动："星型架构"包含路由系统、依赖注入、数据验证。性能：TechEmpower JSON 序列化达到 Django 的 8 倍，接近 Go Gin 水平。FastAPI 的最大亮点是 **写代码=写文档**——基于 Python 类型注解自动生成 Swagger UI 和 ReDoc 双份交互式文档。适用场景：AI 模型部署、微服务、数据 API、快速原型；不适合：CPU 密集型计算、大型企业全栈、Java 技术栈团队。一个真实对比实验：FastAPI 开发只用 2 天（Spring Boot 还在战 Maven），压测 1000 并发 FastAPI 响应 45ms/吞吐 2400 优于 Spring Boot 80ms/1800，但**长期运维 Spring Boot 生态更成熟**。

## 关联连接
- [[FastAPI]] — 核心实体
- [[Pydantic]] — 数据验证引擎
- [[Uvicorn]] — ASGI 服务器
- [[ASGI]] — 异步规范
- [[SpringBoot]] — 对比框架
- [[AIService]] — 主要应用场景
- [[async-await]] — 异步编程基础
