---
title: "摘要-虚拟线程vs传统线程池"
type: source
tags: [来源, Java, 并发, 虚拟线程, 性能]
sources: [raw/01-articles/10000 个并发任务，虚拟线程 1 秒 vs 传统线程池 50 秒，差距在哪？.md]
last_updated: 2026-08-17
---

## 核心摘要
小哈（犬小哈）通过 10000 个并发任务实测对比 Java 虚拟线程（Virtual Thread，JDK 21+）与传统线程池的性能差距：虚拟线程 1 秒完成，传统线程池 50 秒。**核心原理**：传统线程是 OS 线程（1:1 模型），每个线程占用 1MB 栈空间，创建/销毁/切换开销大；虚拟线程是用户态轻量级线程（M:N 模型），由 JVM 调度，栈空间按需分配（几 KB），创建/切换成本极低。**实测对比**：10000 个 HTTP 请求任务，传统线程池（200 线程）需排队执行，50 秒完成；虚拟线程直接创建 10000 个，1 秒完成。**适用场景**：虚拟线程适合 IO 密集型任务（HTTP 请求、数据库查询、文件读写），不适合 CPU 密集型任务（仍受 CPU 核数限制）。**注意事项**：(1) 不要池化虚拟线程——用完即弃，每次新建；(2) 避免使用 `synchronized` 块（会 pin 平台线程，JDK 21 已优化但仍有边界情况），改用 `ReentrantLock`；(3) 警惕 `ThreadLocal` 滥用——虚拟线程数量巨大，每个 ThreadLocal 都会占用内存；(4) 使用 `Executors.newVirtualThreadPerTaskExecutor()` 创建虚拟线程执行器。**Spring Boot 集成**：`spring.threads.virtual.enabled=true` 一键开启，Tomcat、TaskExecutor、@Async 自动使用虚拟线程。

## 关键信息
- **JDK 版本**：虚拟线程在 JDK 21 正式发布（JEP 444），JDK 21 LTS 首次可用
- **线程模型**：传统线程 1:1（OS 线程），虚拟线程 M:N（JVM 调度到平台线程上）
- **栈空间**：传统线程固定 1MB，虚拟线程按需分配（几 KB 起）
- **实测数据**：10000 并发 HTTP 请求，虚拟线程 1 秒 vs 传统线程池 50 秒
- **适用场景**：IO 密集型（HTTP/DB/文件），不适合 CPU 密集型
- **最佳实践**：用完即弃不池化、避免 `synchronized` 用 `ReentrantLock`、警惕 `ThreadLocal`、用 `newVirtualThreadPerTaskExecutor()`
- **Spring Boot**：`spring.threads.virtual.enabled=true` 一键开启

## 关联连接
- [[小哈]] — 来源作者
- [[虚拟线程]] — 核心概念
- [[Java]] — 技术栈
- [[SpringBoot]] — 集成框架
- [[摘要-异地多活架构]] — 同作者相关文章
- [[摘要-deepseek-v4-pro-正式版实测]] — 同作者相关文章（实测任务涉及虚拟线程）
