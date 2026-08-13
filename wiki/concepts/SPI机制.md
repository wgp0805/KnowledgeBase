---
title: "SPI机制"
type: concept
tags: [Java, 类加载, 服务发现, 双亲委派破坏]
sources: [raw/09-archive/面试官：什么是双亲委派模型？怎么破坏？.md]
last_updated: 2026-07-08
---

## 定义
SPI（Service Provider Interface）是 [[Java]] 的服务发现机制，允许接口定义在核心库中而实现类由第三方提供。它是破坏 [[双亲委派模型]]的经典案例，通过**线程上下文类加载器**（Thread Context ClassLoader）绕过父加载器无法向下委派的限制。

## 关键信息
- **核心矛盾**：接口在 `rt.jar` 中由 Bootstrap ClassLoader 加载，但实现类是第三方 jar 包在 classpath 下，只能由 Application ClassLoader 加载。Bootstrap ClassLoader 是最顶层加载器，看不到 classpath 下的类，而双亲委派是单向的只能往上走
- **解决方案**：通过 `Thread.currentThread().getContextClassLoader()` 获取线程上下文类加载器（通常是 Application ClassLoader），用它加载驱动实现类
- **典型应用**：JNDI、JDBC（如 `DriverManager` 加载 `com.mysql.cj.jdbc.Driver`）
- **本质**：接口让父加载器加载，实现类通过线程上下文类加载器"偷偷"拿到子加载器来加载，绕过双亲委派限制
- **设计评价**：在当时架构下算是一种优雅的妥协（hack 式设计）

## 关联连接
- [[摘要-双亲委派模型]] — 来源
- [[双亲委派模型]] — 被破坏的机制
- [[类加载器]] — 涉及的组件
- [[JVM]] — 运行环境
- [[Java]] — 所属语言
- [[MySQL]] — JDBC 驱动实现典型场景
