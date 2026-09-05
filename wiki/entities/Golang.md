---
title: "Golang"
type: entity
tags: [编程语言, 编译型, Google, 云原生, 并发]
sources: [raw/01-articles/SpringBoot3.2 + jdk21 + GraalVM上手体验.md]
last_updated: 2026-07-08
---

## 定义

Golang（Go）是 Google 开发的编译型编程语言，以简洁语法、内置并发（goroutine）和极低的内存占用著称，是云原生领域的主流语言。

## 关键信息

- **内存占用**：标准库 net/http 空闲约 10MB；使用 Gin 等 Web 框架也不超过 20MB
- **启动性能**：秒启动，无需预热
- **吞吐表现**：标准库 HTTP 服务可达约 7248 req/s（`ab -c 50 -n 10000`）
- **编译特性**：编译速度快，生成单一二进制文件，便于部署
- **并发模型**：goroutine + channel，轻量级并发原语
- **对比 [[Java]]**：在内存占用与启动速度上具有显著优势；与 [[GraalVM]] Native Image 性能相当
- **生态**：标准库强大，Web 框架有 Gin、Echo、Fiber 等

## 关联连接

- [[Rust]]
- [[Java]]
- [[GraalVM]]
- [[SpringBoot]]
- [[摘要-springboot3.2-graalvm上手]]
