---
title: "Lazy Constant"
type: concept
tags: [JVM, Performance, JDK 27]
sources: [raw/01-articles/JDK27正式发布，人麻了!.md]
last_updated: 2026-09-17
---

## 定义
惰性常量（Lazy Constant），JDK 27的JEP 531（第三预览），允许 defer（延迟）初始化 `static final` 常量，且JVM会将其当作真正的常量进行优化，性能等价于 `final` 字段。

## 核心概念
- **延迟初始化**：常量不在类加载时计算，而是在首次获取时计算
- **性能等价**：运行时性能等同于传统 `static final` 字段，无额外开销
- **解决的问题**：避免类加载时的昂贵计算，如从数据库加载配置、解析大文件、初始化ML模型
- **AI应用价值**：模型权重、tokenizer词表、向量索引等昂贵初始化数据可以按需加载
- **代码示例**：使用 `LazyConstant.of(() -> loadFromDatabase())` 包装昂贵计算

## 关联连接
- [[JDK27]] — 包含该特性（需--enable-preview）
- [[摘要-jdk27-正式发布-人麻了]] — 来源文章
- Static Final — 传统静态常量
- Database Loading — 数据库加载场景
- Model Weights — 模型权重加载
- AI Application — AI应用性能优化