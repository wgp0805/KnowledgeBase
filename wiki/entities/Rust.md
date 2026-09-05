---
title: "Rust"
type: entity
tags: [编程语言, 系统编程, 内存安全, 零成本抽象, 编译型]
sources: [raw/01-articles/SpringBoot3.2 + jdk21 + GraalVM上手体验.md]
last_updated: 2026-07-08
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

## 关联连接

- [[ActixWeb]]
- [[Golang]]
- [[Java]]
- [[GraalVM]]
- [[摘要-springboot3.2-graalvm上手]]
- [[marka]] — 使用 Rust 构建的 Markdown 编辑器
