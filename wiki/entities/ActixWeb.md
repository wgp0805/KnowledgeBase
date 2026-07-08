---
title: "ActixWeb"
type: entity
tags: [Rust, Web框架, 高性能, 异步, Actix]
sources: [raw/01-articles/SpringBoot3.2 + jdk21 + GraalVM上手体验.md]
last_updated: 2026-07-08
---

## 定义

Actix-web 是 [[Rust]] 生态的高性能异步 Web 框架，基于 Actix actor 框架构建，以极低的内存占用和极高的吞吐量著称。

## 关键信息

- **内存占用**：空闲约 3MB，压测时约 6MB——在所有主流 Web 框架中最低
- **吞吐表现**：约 9163 req/s（`ab -c 50 -n 10000`），性能领先
- **异步模型**：基于 Tokio 异步运行时，使用 async/await 语法
- **核心 API**：`HttpServer::new`、`App::new`、`#[get]` 宏路由、`Responder` trait
- **版本**：当前主流为 4.x
- **对比场景**：在与 [[SpringBoot]] + [[GraalVM]] Native Image、[[Golang]] 的横向对比中，内存与吞吐均最优

## 关联连接

- [[Rust]]
- [[Golang]]
- [[SpringBoot]]
- [[GraalVM]]
- [[摘要-springboot3.2-graalvm上手]]
