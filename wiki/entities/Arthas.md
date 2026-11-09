---
title: "Arthas"
type: entity
tags: [Java诊断, 阿里, 开源工具, AI运维]
sources: [raw/09-archive/面试官：你掌握哪些 Linux 常用命令？.md, raw/09-archive/2026-11-01 - 为什么越来越多人用Arthas 4 ？.md]
last_updated: 2026-11-02
---

## 定义
Arthas 是阿里巴巴开源的 Java 诊断工具，被推荐为线上排查神器，在面试中提及可加分。**Arthas 4**（2026 年大版本升级）是这个工具在 JDK 支持、性能分析与 AI 工作流三个方向上的全面演进。

## 关键信息

### 核心价值
Arthas 是 Java Agent，通过 attach 机制挂到正在运行的 JVM 上——**不需要重启、不需要改代码、不需要提前埋点**。它不是「又一个监控工具」，而是「能让你在线上运行的 JVM 里直接『做手术』的探针」。你不用改代码、不用重启、不用等下一个发版窗口，就能看清线程在干什么、方法被谁调用、返回值是什么、耗时花在哪。

### 命令体系
- **看全局**：`dashboard`（线程、内存、GC、系统负载）、`jvm`（JVM 参数和类加载统计）
- **看线程**：`thread`（线程栈）、`thread -n`（CPU 最高）、`thread -b`（死锁）
- **看方法**：`watch`（入参返回值）、`trace`（调用链路耗时）、`monitor`（周期统计）、`tt`（时间隧道）
- **看类**：`sc`（搜索已加载类）、`jad`（反编译）、`classloader`
- **热更新**：`jad` + `mc` + `redefine` 一条龙，改完方法体直接生效
- **性能分析**：`profiler`（火焰图）、`jfr`（JVM 飞行记录）

### Arthas 4 三大升级
1. **JDK 支持 8 到 25**：官方明确支持 JDK 17、21、25；Jackson、Fastjson2、OGNL、Netty 等依赖同步升级
2. **火焰图从「看 CPU」到「看墙钟时间」**：内置 async-profiler 升级到 4.4，4.0.2 起支持 `--wall` 参数看墙钟时间，解决「CPU 不高但接口慢」的问题（锁等待、网络 IO 阻塞、连接池耗尽时线程在等、不耗 CPU）；会话默认超时从 30 分钟放宽到 3 小时
3. **MCP Server 让 AI 跑诊断命令**：在 HTTP 服务上实现 MCP 端点（`arthas.mcpEndpoint=/mcp`、`arthas.httpPort=8563`），暴露 29 个诊断工具（`dashboard`/`thread`/`trace`/`jad`/`profiler` 等），让 Cherry Studio、Cline、Claude Desktop 等 AI 客户端能用自然语言执行诊断。**仍是实验模块**，官方建议生产环境以只读诊断为主，别让 AI 触发 `redefine`

### 踩坑提醒
- `watch`/`trace` 有性能开销，高频方法必须加 `-n` 或条件过滤，否则打爆 CPU；`-x` 展开最多 3 层
- `trace` 默认只追踪一层内部调用，追多层用 `--maxDepth`，开销大；被 JIT 内联的方法可能追踪不到
- `tt` 默认最多存 100 条、存对象引用（对象后续被修改看到的值可能不对）；退出不会自动清理，用完记得 `tt --delete-all`
- 热更新只能改方法体，不能增删字段和方法；与 `watch`/`trace` 冲突，执行前要先 `reset`

### 典型排查实例
某老服务每天下午三点卡顿、CPU/内存/GC/日志全正常、P99 从 50ms 涨到 800ms。`thread -n 5` 找到 `pool-7-thread-3` 长期占 CPU 在做 `HashMap.get()`，`trace` 后发现缓存 key 拼错导致每次都走同步远程调用——**15 分钟定位，未重启未改码未加日志**。

### AI 排障的边界
AI 能把「现象」翻译成「命令序列」、把「原始输出」整理成「结论」，减少翻手册查语法的时间；但判断结论是否符合业务逻辑仍需人工——「库存服务 RPC 超时」背后是服务挂了、网络问题还是调用量突增，AI 无法判断。

### 适用场景
| 场景 | 推荐程度 |
|------|---------|
| 线上偶发问题排查 | ✅✅✅ 强烈推荐 |
| CPU 飙高定位 | ✅✅✅ 强烈推荐 |
| 接口变慢但 CPU 不高 | ✅✅✅ 强烈推荐（`profiler --wall`） |
| 类冲突/NoSuchMethodError | ✅✅✅ 强烈推荐（`sc`+`jad`+`classloader`） |
| 偶发异常事后排查 | ✅✅✅ 强烈推荐（`tt`） |
| 小 Bug 热修复 | ✅✅ 推荐 |
| AI 辅助排障入门 | ✅✅ 推荐 |
| 生产环境第一次用热更新 | ❌ 不推荐 |

### trace 命令的字节码增强原理（2026-11-03 来源：[[摘要-手把手实现java-agent]]）
`trace` 的实现链条是 Java Agent 机制的教科书级案例：
- `TraceCommand extends EnhancerCommand extends AnnotatedCommand`（模板模式，复杂命令各有一个处理类；exit/logout 等简单命令直接执行）
- `EnhancerCommand#enhance` 走到 `Enhancer#enhance(Instrumentation)`，把 `Enhancer` 自己注册为 `ClassFileTransformer`
- `transform()` 中：先校验目标 ClassLoader 能否加载 `SpyAPI`（否则放弃增强）→ 过滤 `matchingClasses` → `AsmUtils.toClassNode` 解析 → `DefaultInterceptorClassParser` 解析 `SpyInterceptor1/2/3` 与 `SpyTraceInterceptor1/2/3`（`skipJDKTrace` 时换用排除 JDK 类的变体）生成 InterceptorProcessor 集合 → 遍历 `MethodProcessor` 修改原方法字节码 → `AsmUtils.toBytes` 输出增强字节码 → `AdviceListenerManager` 注册监听器收集 trace 数据
- 拦截器本身用 bytekit 注解声明（如 `SpyInterceptor1.atEnter` 用 `@AtEnter(inline=true)` + `@Binding.This/Class/MethodInfo/Args`），核心逻辑只有两步：**解析注解生成处理器 → 遍历处理器改字节码**

## 关联连接
- [[摘要-arthas-4]] — 最新来源
- [[摘要-手把手实现java-agent]] — 来源（trace 命令的 Java Agent 原理拆解）
- [[JavaAgent]] — 底层机制
- [[字节码增强]] — ASM/bytekit 手段
- [[async-profiler]] — 火焰图底层引擎
- [[MCP]] — AI 接入协议
- JFR — JVM 飞行记录
- [[墙钟时间采样]] — 火焰图新能力
- [[Java]] — 诊断对象
- [[JVM]] — 诊断基础
- [[Linux]] — 运行环境
- [[jinfo]] — 对比对象：JDK 自带 JVM 参数查看/修改工具
- [[苏三]] — 最新来源作者
- [[摘要-手把手实现java-agent-IT码徒]] — trace 命令字节码增强原理
