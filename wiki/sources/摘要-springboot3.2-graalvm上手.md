---
title: "SpringBoot 3.2 + GraalVM 上手体验"
type: source
tags: [SpringBoot, GraalVM, Native Image, AOT, JDK21, 性能对比, Golang, Rust]
sources: [raw/01-articles/SpringBoot3.2 + jdk21 + GraalVM上手体验.md]
last_updated: 2026-07-08
---

## 核心摘要

该资料实测 [[SpringBoot]] 3.2 + JDK 21 + [[GraalVM]] Native Image（AOT 编译）的性能表现，并与 [[Golang]]、[[Rust]] 进行横向对比。测试场景为一个返回固定数据的 `/customers` REST 接口，压测工具为 `ab -c 50 -n 10000`。

### Native Image（二进制部署）

- **启动**：秒启动，性能启动即巅峰（无需 JVM 预热）
- **内存**：压测约 70MB，空闲约 20MB
- **吞吐**：7076 req/s，单请求均值 7.066ms
- **局限**：编译为二进制后无法使用 jconsole、arthas 等监控工具

### Jar 部署（传统 JVM）

- **体积**：jar 包 19MB
- **内存**：压测约 200MB，空闲约 160MB
- **吞吐**：557.72 req/s，单请求均值 89.651ms
- **特点**：性能需 JVM 预热后才能达到巅峰

### 对比 Golang（标准库 net/http）

- **内存**：约 10MB（使用 Gin 框架也不超过 20MB）
- **吞吐**：7247.68 req/s，单请求均值 6.899ms
- **特点**：内存占用极低，启动快，性能与 Native Image 相当

### 对比 Rust（[[ActixWeb]] 框架）

- **内存**：空闲约 3MB，压测约 6MB
- **吞吐**：9163.48 req/s，单请求均值 5.456ms
- **特点**：性能最高，内存最低；但编译时间极长（零成本抽象的代价）

### 性能对比汇总

| 维度 | GraalVM Native | Jar (JVM) | Golang | Rust (Actix) |
|------|---------------|-----------|--------|--------------|
| 吞吐(req/s) | 7076 | 558 | 7248 | 9163 |
| 空闲内存 | ~20MB | ~160MB | ~10MB | ~3MB |
| 压测内存 | ~70MB | ~200MB | ~10MB | ~6MB |
| 启动预热 | 无需 | 需要 | 无需 | 无需 |

### 结论

[[AOT编译]] 已相对成熟，解决了 [[JVM]] 启动慢、需要预热、内存占用大等问题，Java 在云原生环境下取得了显著进步。美中不足是 GraalVM Native Image 编译速度极慢（约 15 分钟）。

## 关联连接

- [[SpringBoot]]
- [[GraalVM]]
- [[AOT编译]]
- [[JIT编译]]
- [[HotSpot]]
- [[JVM]]
- [[Java]]
- [[Golang]]
- [[Rust]]
- [[ActixWeb]]
