---
title: "logback vs log4j2 性能对比"
type: source
tags: [Logback, Log4j2, SLF4J, 日志框架, 性能对比, 异步日志]
sources: [raw/01-articles/logback VS log4j2：一倍左右的性能差异，是时候注意了！.md]
last_updated: 2026-07-08
---

## 核心摘要

该资料对 [[Logback]] 与 [[Log4j2]] 进行性能基准测试，结论是 [[Log4j2]] 性能约为 [[Logback]] 的两倍。文章同时阐述了日志框架的体系关系与选型建议。

### 日志框架体系

- [[SLF4J]] 是日志门面接口，具备高易用性和抽象性
- [[Logback]]、[[Log4j2]] 是 [[SLF4J]] 接口的具体实现
- 获取 Logger 两种方式：[[Lombok]] 的 `@Slf4j` 注解（推荐）或 `LoggerFactory.getLogger()`（推荐 `private static final`）

### 测试环境

- 硬件：AMD Ryzen 5 3600 6核 3.95GHz，32GB 内存
- JVM：semeru-11.0.20，参数 `-Xms1000m -Xmx1000m`
- 版本：log4j2 2.22.1，logback 1.4.14
- 线程数：1/8/32/128，统一预热后取三次平均值
- 日志长度：约 129 字符，统一格式输出到文件

### 性能结论

1. **[[Log4j2]] 全面优于 [[Logback]]，性能约为两倍**
2. 日志输出能力不会随线程数线性增长，约两倍 CPU 核数时性能达较高值
3. 打印方法名和行号会显著降低日志效率——单线程下去掉行号，log4j2 性能相差一倍多

### Spring Boot 中使用

- **Logback**：[[SpringBoot]] 默认集成，无需额外配置，配置文件 `logback.xml` 放于 `src/main/resource/`
- **Log4j2**：需排除 Spring 默认的 logback 依赖，引入 `log4j-core`/`log4j-api`/`log4j-slf4j2-impl`，配置文件 `log4j2.xml`

### 最佳实践

- 滚动日志策略，永远不让磁盘满（配置最大数量与最大大小）
- 统一日志格式（先打印方法名，再打印参数列表）
- 日志配置应遵循结构清晰、尽量简化原则，避免框架计算方法名/行号
- 全公司统一日志框架，便于后续 ETL 流程与日志收集分析

## 关联连接

- [[Logback]]
- [[Log4j2]]
- [[SLF4J]]
- [[日志框架]]
- [[Lombok]]
- [[SpringBoot]]
- [[Java]]
