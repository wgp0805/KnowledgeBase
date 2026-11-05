---
title: "JavaAgent"
type: concept
tags: [概念, Java, JVM, 字节码, Instrumentation]
sources: [raw/09-archive/2026-11-03 - 手把手教你实现一个Java Agent.md]
last_updated: 2026-11-04
---

## 定义

Java Agent 是依附 JVM 运行的"插件"机制：借助 JDK 1.5 起引入的 `java.lang.instrument` 包，在**类加载时拦截并改写字节码**，实现无侵入的监控、耗时统计、热更新、诊断等功能。Arthas、SkyWalking、async-profiler 等诊断/监控工具都建立在这套机制之上。

## 关键信息

### Instrumentation 核心接口

- `addTransformer(ClassFileTransformer, canRetransform)`：注册类转换器
- `removeTransformer(transformer)`：移除转换器
- `retransformClasses(Class<?>...)`：重新转换已加载的类（活跃栈帧继续运行旧方法）
- `isRetransformClassesSupported()`：当前 JVM 是否支持重转换
- `getAllLoadedClasses()`：获取所有已加载类

### 两种加载方式

| 方式 | 入口方法 | 时机 |
|------|---------|------|
| 启动加载 | `premain(String agentArgs, Instrumentation inst)` | JVM 启动、main() 之前 |
| 运行期 Attach | `agentmain(String agentArgs, Instrumentation inst)` | Agent 被 Attach 到运行中的 JVM 时 |

- **Attach 机制**：外部 Java 程序用 `VirtualMachine.attach(pid)` 建立跨进程通信，`loadAgent(jarPath)` 加载 Agent；`agentmain` 里可用 `retransformClasses` 动态转换已加载类并生效
- **打包**：maven-assembly-plugin 打 `jar-with-dependencies`，manifest 指定 `Premain-Class`/`Agent-Class`/`Can-Redefine-Classes`/`Can-Retransform-Classes`

### 执行流程

```
JVM 启动 → 执行 premain()
   → instrumentation.addTransformer(ClassFileTransformer)
   → JVM 加载类时把字节数组交给 transform()
   → transform() 内改写字节码（ASM/bytekit）
   → JVM 加载改写后的类
```

`transform()` 返回 null 表示不处理；返回非 null 则 JVM 用返回的字节数组替换原类。

### 典型应用

- 方法耗时统计（无侵入埋点）
- 线上诊断（Arthas 的 watch/trace/monitor 都依赖它）
- 热更新（jad + mc + redefine）
- APM 链路追踪（SkyWalking/async-profiler 的探针）

## 关联连接
- [[摘要-手把手实现java-agent]] — 来源
- [[字节码增强]] — 核心手段（ASM/bytekit）
- [[Arthas]] — 典型应用（trace 命令原理）
- [[JVM]] — 宿主虚拟机
- [[AOP]] — 同为横切关注点分离手段（AOP 走代理、Agent 走字节码）
- [[JIT编译]] — 运行时编译相关机制
