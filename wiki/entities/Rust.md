---
title: "Rust"
type: entity
tags: [编程语言, 系统编程, 内存安全, 零成本抽象, 编译型]
sources: [raw/09-archive/SpringBoot3.2 + jdk21 + GraalVM上手体验.md, raw/09-archive/2026-10-28 - Cloudflare正式开源Nginx替代品：Pingora.md]
last_updated: 2026-10-29
---

## 定义

Rust 是一门系统编程语言，以零成本抽象和内存安全（所有权机制）为核心特性，无需垃圾回收即可保证内存安全，性能极高。

## 关键信息

- **内存安全**：通过所有权（Ownership）和借用检查器在编译期保证内存安全，无需 GC
- **零成本抽象**：高层抽象不带来运行时开销，但代价是编译时间极长
- **Web 性能**：使用 [[ActixWeb]] 框架，空闲内存约 3MB，压测约 6MB，吞吐约 9163 req/s
- **编译时间**：编译速度慢是主要痛点（实际项目编译可达数分钟）
- **对比 [[Java]] / [[Golang]]**：性能最高、内存最低，但学习曲线陡峭、编译慢
- **生态**：Web 框架有 Actix-web、Axum、Rocket；包管理器为 cargo

### 基础设施案例：Pingora（来源：[[摘要-cloudflare开源pingora]]）
- [[Cloudflare]] 用 Rust 写了异步多线程代理框架 [[Pingora]]，2022 年起替代 [[Nginx]]，每秒处理超 4000 万请求
- 能提供的特性高度依赖 Rust 语言能力：**零停机优雅重启**、filters/callbacks 深度定制、可观测性集成
- 官方对 Rust 的定位值得注意：内存安全的价值不只是"防 Bug"，而是**为高风险的动态能力提供执行边界**——用类 Wireshark 的过滤语言写防火墙规则、让数百万用户跑任意 JavaScript、即时重写 HTML 响应
- 反面视角：[[章亦春]] 认为用 Rust 写解释型网关是退步（抽象层次之争，非性能之争）

## 关联连接

- [[ActixWeb]]
- [[Pingora]] — Rust 异步多线程代理框架（Cloudflare 生产案例）
- [[Nginx]] — Pingora 的替代对象
- [[Cloudflare]] — Pingora 出品方
- [[Golang]]
- [[Java]]
- [[GraalVM]]
- [[摘要-springboot3.2-graalvm上手]]
- [[marka]] — 使用 Rust 构建的 Markdown 编辑器
- [[摘要-cloudflare开源pingora]] — 来源（Pingora 案例）
