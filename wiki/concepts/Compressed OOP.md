---
title: "Compressed OOP"
type: concept
tags: [JVM, Memory, JDK 27]
sources: [raw/01-articles/JDK27正式发布，人麻了!.md]
last_updated: 2026-09-17
---

## 定义
紧凑对象指针（Compressed OOP），JDK 27的JEP 534将对象头从96位压缩至64位。通过将Klass Pointer从64位压缩至32位（利用Metaspace典型不超过4GB的特性），实现内存占用的显著降低。

## 核心概念
- **对象头结构**：传统64位JVM对象头12字节（Mark Word 64位 + Klass Pointer 64位），压缩后总共8字节（Mark Word 64位 + Klass Pointer 32位 + 填充）
- **内存效益**：`new Object()` 从16字节降至12字节，堆占用直接降低**25%**
- **适用场景**：大规模Java应用，特别是创建大量小对象的场景
- **安全边界**：类元数据空间（Metaspace）通常不超过4GB，32位索引足以寻址
- **默认开启**：JDK 27中作为默认行为，无需显式配置

## 关联连接
- [[JDK27]] — 包含该特性的版本
- [[Object Head]] — 对象头概念
- [[Metaspace]] — 类元数据空间
- [[Heap Occupancy]] — 堆占用率