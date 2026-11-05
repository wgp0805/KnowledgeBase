---
title: "摘要-手把手实现java-agent"
type: source
tags: [来源, 原始文件, Java, JavaAgent, 字节码增强, Arthas]
sources: [raw/09-archive/2026-11-03 - 手把手教你实现一个Java Agent.md]
last_updated: 2026-11-04
---

## 核心摘要

终码一生（2026-11-03）从"同事在代码里大量手写 StopWatch 统计方法耗时、侵入性大"的真实痛点出发，手把手讲透 Java Agent 无侵入式解决思路，并延伸拆解 Arthas `trace` 命令的底层实现。

**四个技术层次**：
1. **Instrumentation**（JDK 1.5+ `java.lang.instrument`）：核心接口 `addTransformer`（注册类转换器）、`retransformClasses`（重新转换已加载类）、`getAllLoadedClasses`；两种使用方式——JVM 启动时加 Agent jar（premain）、运行后通过 Attach API 远程加载（agentmain）
2. **Agent 入口**：`premain(String agentArgs, Instrumentation inst)` 在 main() 之前执行；`agentmain(...)` 在 Agent 被 Attach 到运行中 JVM 时执行。案例：给 MyTest 的类用 ASM 改写，在方法进出插入 TimeStatistics.start()/end() 统计耗时；另一个案例用 Attach 把 PrintNumTest 的 getNum() 返回值从 100 改成 50（`VirtualMachine.attach(pid).loadAgent(jar)` 跨进程通信）。Maven 用 maven-assembly-plugin 打 jar-with-dependencies，manifest 指定 `Premain-Class` / `Agent-Class` / `Can-Retransform-Classes=true`
3. **bytekit**（阿里基于 ASM 的简化 API）：用 `@AtEnter`/`@AtExit`/`@AtExceptionExit` 注解 + `@Binding` 参数绑定声明在方法进出/异常退出时插入代码，`inline=true` 直接内联、`false` 调用方法；比裸 ASM 好写得多（反编译可见代码量仍会剧增）
4. **Arthas trace 原理**：`TraceCommand extends EnhancerCommand extends AnnotatedCommand`（模板模式），`EnhancerCommand#enhance` 走到 `Enhancer#enhance(Instrumentation)` 注册自己为 transformer；`transform()` 里解析 `@AtXxx`/`@Binding` 注解生成 InterceptorProcessor 集合（SpyInterceptor1/2/3、SpyTraceInterceptor1/2/3，可按 `skipJDKTrace` 切换排除 JDK 类），遍历 MethodProcessor 修改原方法字节码，最后 `AdviceListenerManager` 注册监听器

**核心认知**：Java Agent = 依附 JVM 的插件，Instrumentation 提供类转换能力，ClassFileTransformer 拦截类字节码，字节码框架（ASM/bytekit）负责改写——这就是"无侵入监控/耗时统计/热更新"的技术底座。

## 关联连接
- [[JavaAgent]] — 本文提炼的核心概念
- [[字节码增强]] — 底层手段（ASM/bytekit）
- Instrumentation — JDK 提供的类转换接口（无独立页，见 [[JavaAgent]]）
- [[Arthas]] — trace 命令原理拆解对象
- [[摘要-arthas-4]] — 同系列 Arthas 文章
- [[JIT编译]] — 与运行时字节码相关的编译机制
- [[AOP]] — 同为"横切关注点分离"的工程手段（AOP 走后端代理，Java Agent 走字节码）
- [[JVM]] — 宿主虚拟机
