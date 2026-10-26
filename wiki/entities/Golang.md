---
title: "Golang"
type: entity
tags: [编程语言, 编译型, Google, 云原生, 并发]
sources: [raw/09-archive/SpringBoot3.2 + jdk21 + GraalVM上手体验.md, raw/09-archive/2026-09-27-并发编程（五）：Atomic——语言层的原子性、可见性与有序性 - ThinkerQAQ.md]
last_updated: 2026-09-28
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
- **Atomic 的内存模型保证**（来源：[[摘要-atomic语言层三性质]]）：`sync/atomic` 的 `atomic.Int64.Add` 是原子更新；Go Memory Model 规定"若原子操作 B 观察到 A 的效果，则 A synchronized-before B"，且所有 Atomic 操作表现得像处在某个顺序一致序列（sequentially consistent order）；happens-before 是 `sequenced-before` 与 `synchronized-before` 的传递闭包，因此 Atomic 更新前的普通写对观察到该更新的 Goroutine 可见且有序
- **与 Java/Python 对照**：Java 由 `AtomicInteger` + JLS §17.4 给出同样三性质；Python 应用层没有对称的通用整数 Atomic API

## 关联连接

- [[Rust]]
- [[Java]]
- [[GraalVM]]
- [[SpringBoot]]
- [[原子性-可见性-有序性]] — 语言层三性质对照
- [[AtomicInteger]] — Java 侧对照
- [[摘要-springboot3.2-graalvm上手]]
- [[摘要-atomic语言层三性质]] — Atomic 内存模型来源
