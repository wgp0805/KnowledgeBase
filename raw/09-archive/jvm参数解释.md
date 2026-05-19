---
title: jvm参数解释
tags:
  - java
categories:
  - java
date: 2023-12-21 13:38:34
---

```
# 这个参数会启动JVM的"server"模式，这种模式下JVM会进行更多的优化，但是启动速度会稍慢一些。
-server
## 设置JVM堆的初始大小				-Xms 和 -Xmx：-Xms 参数设置 JVM 初始堆大小，-Xmx 参数设置最大堆大小。一般推荐将这两个参数设置为相同的值，以避免 JVM 频繁调整堆大小，这样可以提高性能。
-Xms8192m
## 设置JVM堆的最大大小
-Xmx8192m
## 设置年轻代大小 					一般推荐将 -Xmn 设置为堆大小（由 -Xmx 或 -Xms 设置）的 1/3 到 1/4。这样可以保证足够的空间进行对象分配，同时也有足够的空间进行老年代的垃圾收集。
-Xmn2048m
## 设置新生代最小空间大小。
-XX:NewSize=2048m
## 设置新生代最大空间大小。         -XX:NewSize 和 -XX:MaxNewSize 一般推荐将这两个参数设置为相同的值，并且与 -Xmn 的值相同。
-XX:MaxNewSize=2048m
## 用于设置元空间的初始大小。		如果未指定此参数，元空间将根据运行时的应用需求动态地调整大小。
-XX:MetaspaceSize=1024m
## 用于设置元空间的最大大小。即以前的永久代  如果你的应用有大量的类或者使用了大量的反射，你可能需要增加这个值。
-XX:MaxMetaspaceSize=1024m
## 设置代码缓存的初始大小                    用来存储已编译方法生成的本地代码
-XX:InitialCodeCacheSize=512m
## 设置代码缓存的最大大小                    注意： 过大的编译缓存，有可能导致，本地的编译代码，不是 ”实时的“ 导致引用错误，需要 idea invalidate caches
-XX:ReservedCodeCacheSize=1024m

## 启用并发标记清除（CMS）垃圾收集器。 是 HotSpot 虚拟机第一款真正意义上的并发收集器，它第一次实现了让垃圾收集线程与用户线程（基本上）同时工作
## CMS（并发标记清除）垃圾收集器的 JVM 参数。CMS 是一个以获取最小垃圾收集停顿时间为目标的收集器，适用于对响应时间有严格要求的系统。
## 但是，CMS 有一些缺点，例如无法处理浮动垃圾，可能导致内存碎片化，以及在并发阶段可能会与应用线程竞争 CPU 资源。
## -XX:+UseConcMarkSweepGC
## CMS垃圾收集器，设置CMS垃圾收集器在堆内存使用率达到70%时开始垃圾收集    当老年代达到62%时，触发CMS垃圾回收
## -XX:CMSInitiatingOccupancyFraction=70
## 与CMSInitiatingOccupancyFraction配合使用，只在堆内存使用率达到CMSInitiatingOccupancyFraction设置的值时开始CMS垃圾收集。   只使用设定的阈值进行回收，如果不指定后续JVM会自动调整
## -XX:+UseCMSInitiatingOccupancyOnly

## 高性能，高并发和大内存，推荐使用以下垃圾收集器垃圾收集器：
## -XX:+UseG1GC                                    G1垃圾收集器（G1 GC）：G1 GC 是一个面向服务器的垃圾收集器，适用于多核处理器和大内存的系统。它可以处理大量的堆内存，并且可以预测垃圾收集的停顿时间。
## -XX:+UnlockExperimentalVMOptions -XX:+UseZGC    Z垃圾收集器（ZGC）：ZGC 是一个可扩展的低延迟垃圾收集器。ZGC 可以处理大量的堆内存，同时保持低延迟。但是，ZGC 在 JDK 11 中仍然是实验性的。
## -XX:+UseParallelGC                              并行垃圾收集器（Parallel GC）：Parallel GC 是一个多线程的垃圾收集器，适用于多核处理器的系统。它在吞吐量上表现优秀，但可能会导致较长的垃圾收集停顿。

## 使用G1垃圾收集器，它在处理大内存时表现更好。
-XX:+UseG1GC
## 这些是G1垃圾收集器的参数，用于控制垃圾收集的行为。
## 用于设置 G1 垃圾收集器的堆区域大小。      G1 垃圾收集器将堆内存分割成多个相同大小的区域，每个区域都可以是 Eden、Survivor 或 Old 区域。-XX:G1HeapRegionSize 参数用于设置这些区域的大小。
## 这个参数的值可以是 1MB、2MB、4MB、8MB、16MB 或 32MB。默认值由 JVM 根据你的硬件配置自动选择。
## 请注意，这个参数的设置可能会影响到 G1 垃圾收集器的性能。如果区域太大，可能会导致垃圾收集的效率降低；如果区域太小，可能会导致堆内存的利用率降低。
-XX:G1HeapRegionSize=32M
## 用于设置垃圾收集器的目标停顿时间。单位是毫秒。主要目的是控制垃圾收集器的停顿时间，以减少应用程序的停顿时间。垃圾收集器会尽力保证停顿时间不超过设置的值，但这并不是一个硬性的限制，实际的停顿时间可能会超过这个值。
## =200，那么垃圾收集器会尽力保证每次垃圾收集的停顿时间不超过200毫秒。这个参数对于需要控制垃圾收集停顿时间的应用程序非常有用，例如实时系统或者具有严格响应时间要求的系统。
-XX:MaxGCPauseMillis=200
## 用于设置 G1 垃圾收集器在进行并行阶段（如初始标记和全局并行清除阶段）时的线程数。
-XX:ParallelGCThreads=12
## 用于设置 G1 垃圾收集器在进行并发阶段（如并发标记和并发清除阶段）时的线程数。
-XX:ConcGCThreads=12
## 编译器线程的总数 设置并行编译线程的数量，在使用分层编译时，JVM会自动分配这些线程给C1和C2编译器。
-XX:CICompilerCount=12
## 控制最大数量嵌套调用内联  默认值为9，控制最大数量嵌套调用内联。 内联越多也将导致生成的机器码越长,越容易填满 ReservedCodeCacheSize , C2 不支持内联超过 9 层的调用
## 增加了方法内联的最大深度，以提高性能。
-XX:MaxInlineLevel=15

## 这个参数设置了软引用对象的清理策略。每MB的空闲堆内存会保留50ms的软引用对象。  默认值是1000
## 这个参数只在使用并行垃圾收集器（-XX:+UseParallelGC）或者串行垃圾收集器（-XX:+UseSerialGC）的情况下有效。
## 如果这个值设置得过大，可能会导致软引用对象占用过多的内存，从而增加垃圾收集的压力，降低性能。反之，如果这个值设置得过小，可能会导致软引用对象过早被回收，从而增加对象创建和初始化的开销，也可能降低性能。
-XX:SoftRefLRUPolicyMSPerMB=500

## 开启分层编译
-XX:+TieredCompilation
## Java8默认开启了「分层编译」
## 在开发环境中，为了加快应用启动速度，可以设置 -XX:TieredStopAtLevel=1。在生产环境中，为了获取最高的运行性能，通常不应设置这个参数，让JVM使用所有可用的优化级别。
## 请注意，这个参数只在开启了分层编译（-XX:+TieredCompilation）的情况下有效。
### 参数的值从0到4，每个值的含义如下：
## - 0：解释执行，不进行任何编译优化。
## - 1：使用C1编译器进行简单优化。
## - 2：使用C1编译器进行有限的优化。
## - 3：使用C1编译器进行全优化。
## - 4：使用C2编译器进行全优化。      让 JVM 在启动时尽可能将所有代码编译为最高的 C4 级别（也就是 C2 编译器的编译级别），以提高程序运行时的效率。可能会增加 JVM 启动时的编译开销，因此可能会导致程序启动时间变长。
##
## 从启动速度和执行效率的角度对比排序如下：
##
## - 启动速度：0 > 1 > 2 > 3 > 4     级别越高，启动时，越消耗 cpu，启动时间越长
## - 执行效率：4 > 3 > 2 > 1 > 0     级别越高，运行时，效率越高
## 用于设置Java的多层编译系统的最高优化级别。
-XX:TieredStopAtLevel=4

## 即时编译 C4 第4层（最高级）  ## 如果你的应用有一些热点方法，这些方法在应用启动后很快就会被频繁调用，那么可以考虑降低这些值，让这些方法更早地被编译到最高优化级别。
## 用于设置方法被调用多少次后才会被编译到第4级别。   =10000（默认） 表示一个方法被调用10000次后，JVM会尝试将其编译到第4级别。
-XX:Tier4MinInvocationThreshold=100
## 设置方法被解释执行多少次后才会被编译到第4级别。    =2000（默认） 表示一个方法被解释执行2000次后，JVM会尝试将其编译到第4级别。
-XX:Tier4InvocationThreshold=100
## 设置方法被编译执行多少次后才会被编译到第4级别。    =15000（默认） 表示一个方法被编译执行15000次后，JVM会尝试将其编译到第4级别。
-XX:Tier4CompileThreshold=100

## 这个参数让JVM在出现内存溢出错误时生成堆转储文件。
-XX:+HeapDumpOnOutOfMemoryError
## 这个参数禁止了快速抛出异常时省略堆栈跟踪，可以帮助调试。
-XX:-OmitStackTraceInFastThrow
## 这个参数启用了Java断言功能。
-ea
## 这个参数禁用了规范化路径缓存，可以避免在某些情况下出现文件锁定问题。
-Dsun.io.useCanonPrefixCache=false
## 这个参数让JVM优先使用IPv4网络栈。
-Djava.net.preferIPv4Stack=true
## 这个参数用于设置JDK HTTP认证中禁用的隧道协议。设置为空字符串""表示没有禁用任何协议。
-Djdk.http.auth.tunneling.disabledSchemes=""
## 这个参数允许JVM自我附加。这通常用于某些类型的监控和管理操作。
-Djdk.attach.allowAttachSelf=true
## 这个参数用于控制Kotlin协程的调试模式。设置为"off"表示关闭调试模式。
-Dkotlinx.coroutines.debug=off
## 用于控制Java 9及以上版本中的模块系统对非法访问的处理。在Java 9中，引入了模块系统，它对类的可见性进行了更严格的控制。默认情况下，如果一个类试图访问它不应该访问的另一个模块中的类，JVM会在控制台输出一个警告。
## 设置为 true JVM将不会输出这些警告。这可以使控制台输出更加清晰，但是可能会隐藏一些潜在的问题。
-Djdk.module.illegalAccess.silent=true

-XX:+IgnoreUnrecognizedVMOptions
-Dsun.io.useCanonCaches=false
-XX:ErrorFile=$USER_HOME/java_error_in_idea_%p.log
-XX:HeapDumpPath=$USER_HOME/java_error_in_idea.hprof
```

