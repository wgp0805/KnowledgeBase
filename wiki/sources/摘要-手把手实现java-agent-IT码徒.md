---
title: "摘要-手把手实现java-agent-IT码徒"
type: source
tags: [来源, JavaAgent, 字节码增强, IT码徒]
sources: [raw/09-archive/2026-11-08 - 手把手教你实现一个JavaAgent.md]
last_updated: 2026-11-09
---

## 核心摘要
IT码徒从 0 到 1 手把手实现 Java Agent：用 Instrumentation + ClassFileTransformer + ASM（AdviceAdapter）给方法做无侵入耗时统计，用 Attach（agentmain + VirtualMachine.attach + retransformClasses）在运行期动态改写已加载类，并拆解 Arthas trace 命令的字节码增强原理（EnhancerCommand 模板模式 + SpyInterceptor + bytekit 注解）。起因是团队同事写了大量 StopWatch 埋点代码、侵入性大，用 Java Agent 可无侵入解决。

## 关键信息
- **Instrumentation 核心**：addTransformer/removeTransformer/retransformClasses/isRetransformClassesSupported/getAllLoadedClasses；ClassFileTransformer.transform 返回 null 不处理、返回非 null 用新字节数组替换
- **两种加载**：premain（JVM 启动、main 前）/ agentmain（Agent 被 Attach 到运行 JVM 时）
- **计时 demo**：MyClassFileTransformer 用 ASM 的 ClassReader/ClassWriter(COMPUTE_FRAMES)/TimeStatisticsVisitor/AdviceAdapter，onMethodEnter 插 TimeStatistics.start、onMethodExit 插 end，`<init>` 构造方法跳过；`java -javaagent:aop.jar com.example.aop.agent.MyTest`
- **Attach demo**：PrintNumTest 循环打印 getNum()=100，PrintNumAgent.agentmain 里 addTransformer + getAllLoadedClasses 找到目标类 + retransformClasses，用 ASM 改 getNum 前插入 BIPUSH 50 + IRETURN，打印变为 50；发起端 MyAttachMain 用 `VirtualMachine.attach(pid)` + `loadAgent(jar)` + `detach`（跨进程通信，需 tools.jar）
- **打包**：maven-assembly-plugin 打 jar-with-dependencies，manifest 指定 Premain-Class/Agent-Class/Can-Redefine-Classes/Can-Retransform-Classes
- **Arthas trace 源码**：TraceCommand extends EnhancerCommand extends AnnotatedCommand（模板模式）；EnhancerCommand.enhance 把 Enhancer 注册为 ClassFileTransformer；transform 里校验 ClassLoader 能加载 SpyAPI→过滤 matchingClasses→AsmUtils.toClassNode→DefaultInterceptorClassParser 解析 SpyInterceptor1/2/3（+SpyTraceInterceptor 或 ExcludeJDK 变体，取决于 skipJDKTrace）→遍历 MethodProcessor 改字节码→AdviceListenerManager 注册监听器；拦截器用 bytekit @AtEnter(inline=true)+@Binding 声明
- **bytekit 注解**：@AtEnter/@AtExit/@AtExceptionExit、inline 控制内联还是调用、suppress+suppressHandler 包 try/catch

## 关联连接
- [[JavaAgent]] — 概念
- [[字节码增强]] — 概念
- [[Arthas]] — trace 命令原理（源码拆解）
- [[IT码徒]] — 作者
- [[AOP]] — 对比：代理 vs 字节码
