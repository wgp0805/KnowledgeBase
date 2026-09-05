---
title: "mvnd（Maven Daemon）完全教程"
type: synthesis
tags: [Maven, 构建工具, mvnd, 性能优化, Java]
sources: []
last_updated: 2026-08-04
---

# mvnd（Maven Daemon）完全教程

## 核心理念

**mvnd**（Maven Daemon）是 Apache Maven 团队官方推出的守护进程化构建工具。核心思想是：让 Maven 构建跑在一个**长期运行的后台 JVM 进程**中，而不是每次构建都启动一个新 JVM。

传统 `mvn` 每次执行都要重新启动 JVM、加载插件 classloader、JIT 编译热点代码，构建结束后全部丢弃。而 `mvnd` 让这些工作**只做一次，后续复用**，实现 2-10 倍的加速效果。

## 架构原理

```
┌──────────────────────────────────────────────┐
│              终端 (Terminal)                   │
│              mvnd clean install               │
└──────────────┬───────────────────────┬────────┘
               │                       │
               ▼                       ▼
     ┌─────────────────┐   ┌─────────────────────┐
     │  mvnd Client     │   │  mvnd Client         │
     │ (GraalVM 原生编译)  │   │ (轻量级，启动毫秒级)   │
     └────────┬─────────┘   └──────────┬──────────┘
              │                         │
              │  ┌───────────────────────────┐
              │  │  Daemon 注册表             │
              │  │  (管理空闲/忙碌的 daemon)   │
              │  └───────────┬───────────────┘
              │              │
              ▼              ▼
     ┌───────────────────────────────┐
     │  长期运行的 Daemon JVM         │
     │  · 缓存插件 classloader        │
     │  · 缓存 JIT 编译后的代码        │
     │  · 缓存依赖的 JAR 包解析结果     │
     │  · 自动并行构建（CPU-1 个线程）  │
     └───────────────────────────────┘
```

### 关键设计点

| 特性 | 说明 |
|------|------|
| **客户端原生编译** | 客户端用 GraalVM 编译为原生可执行文件，启动毫秒级 |
| **内嵌 Maven** | 发行包自带 Maven，无需额外安装 |
| **多 daemon 并行** | 无空闲 daemon 时可并行拉起多个，互不干扰 |
| **SNAPSHOT 排除缓存** | 快照版本插件不在 classloader 缓存中，避免脏缓存 |
| **自动并行构建** | 默认 `CPU核心数 - 1` 个线程并行构建模块 |

## 安装方法

### SDKMAN!（推荐）
```bash
sdk install mvnd
mvnd --version
```

### Homebrew（macOS / Linux）
```bash
# 稳定版 1.x（Maven 3.9.x）
brew install mvndaemon/homebrew-mvnd/mvnd@1

# 预览版 2.x（Maven 4.0.x）
brew install mvndaemon/homebrew-mvnd/mvnd
```

### 手动下载安装
1. 从 [Apache mvnd 下载页](https://downloads.apache.org/maven/mvnd/) 下载对应平台 ZIP
2. 解压到目标目录，将 `bin` 加入 `PATH`
3. 验证：`mvnd --version`

### Windows 注意
`VCRUNTIME140.dll was not found` → 安装 [VC++ Redistributable](https://aka.ms/vs/17/release/vc_redist.x64.exe)

### macOS 注意
```bash
xattr -r -d com.apple.quarantine mvnd-x.y.z-darwin-amd64
```

## 基本用法

`mvnd` 命令行参数与 `mvn` **完全兼容**，直接替换：

```bash
# 替换 mvn
mvnd clean install
mvnd clean test
mvnd clean package -DskipTests
mvnd clean install -P production
mvnd clean install -pl my-module -am

# mvnd 专属命令
mvnd --status    # 查看运行中的 daemon
mvnd --stop      # 停止所有 daemon
mvnd --help      # 查看帮助
```

## 配置详解

### 配置文件优先级（高→低）

1. `MVND_PROPERTIES_PATH` 环境变量或 `-Dmvnd.propertiesPath` 指定路径
2. `[项目根目录]/.mvn/mvnd.properties`（项目级）
3. `~/.m2/mvnd.properties`（用户级，最常用）
4. `[MVND_HOME]/conf/mvnd.properties`（系统级）

### 核心配置项（`~/.m2/mvnd.properties`）

```properties
# Java 家目录（默认从 JAVA_HOME 读取）
java.home=C:/Program Files/Java/jdk-21

# Daemon JVM 堆大小
mvnd.minHeapSize=256M
mvnd.maxHeapSize=4G

# 线程栈大小
mvnd.threadStackSize=1M

# 额外 JVM 参数
mvnd.jvmArgs=-XX:+UseZGC,-XX:MaxGCPauseMillis=100

# 空闲超时（默认 3 小时）
mvnd.idleTimeout=30 minutes

# 构建线程数（默认 CPU核心-1）
mvnd.threads=4

# 关闭输出缓冲，实时显示日志
mvnd.noBuffering=true

# 日志保留周期
mvnd.logPurgePeriod=7d

# Maven settings.xml 路径
maven.settings=D:/tools/maven/conf/settings.xml
```

### 场景化配置推荐

| 项目规模 | 最大堆 | 空闲超时 | 额外 JVM |
|----------|--------|----------|----------|
| 小型（<10 模块） | 1G | 10 min | 默认 |
| 中型（10-50 模块） | 4G | 30 min | `-XX:+UseZGC` |
| 大型（50+ 模块） | 8G | 1 hour | `-XX:+UseZGC,-XX:MaxGCPauseMillis=100` |

## 性能对比

| 场景 | mvn | mvnd | 提速 |
|------|-----|------|------|
| 首次构建（冷启动） | 启动 JVM | 启动 daemon | 差异不大 |
| 第二次构建（热启动） | 重新启动 JVM | 复用 daemon | **2-8 倍** |
| 第三次构建（JIT 优化） | 重新 JIT 编译 | JIT 已缓存 | **3-10 倍** |
| 增量构建 | 重新加载插件 | classloader 已缓存 | **5-15 倍** |

> 连续构建越多，加速效果越明显。

## 最佳实践与注意事项

### 适合场景
- 日常开发中反复编译/测试
- 多模块项目
- 本地开发环境

### 不适合场景
- CI 一次性构建（全新环境无缓存可复用）
- 低配机器（daemon 常驻内存，注意调小堆大小）
- SNAPSHOT 依赖频繁更新的项目（留意缓存问题）

### 常见问题

| 问题 | 解决 |
|------|------|
| daemon 内存占用过高 | 调小 `mvnd.maxHeapSize`，或 `mvnd --stop` |
| 构建结果异常（怀疑缓存问题） | `mvnd --stop` 重启 daemon |
| 想用回原版 mvn | 直接用 `mvn`，两者互不冲突 |
| 开发机下班后 daemon 仍占内存 | 设置 `mvnd.idleTimeout=30 minutes` |

## 总结

| 维度 | 评价 |
|------|------|
| 学习成本 | 极低，`mvn` 换成 `mvnd` 即可 |
| 加速效果 | 持续开发场景 2-10 倍 |
| 内存开销 | 常驻一个 JVM 进程（默认最大 2G） |
| 成熟度 | Apache 官方项目，生产可用 |
| 适合人群 | 所有使用 Maven 的 Java 开发者 |

## 关联连接

- [[Maven]] — 项目构建与依赖管理工具
- [[摘要-maven]] — Maven 完整教程摘要
- [[摘要-maven-4-重构]] — Maven 4 核心架构变化
- [[GraalVM]] — 多语言运行时，mvnd 客户端的原生编译基础
- [[JVM]] — Java 虚拟机