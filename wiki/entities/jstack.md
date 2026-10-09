---
title: "jstack"
type: entity
tags: [JDK, Java诊断, 命令]
sources: [raw/01-articles/面试官：你掌握哪些 Linux 常用命令？.md, raw/01-articles/Java 线上排障：服务 CPU 打满、接口卡死定位方案.md]
last_updated: 2026-10-08
---

## 定义
jstack 是 JDK 自带的 Java 诊断工具，用于打印线程堆栈，是 CPU 飙高、死锁排查的核心工具。

## 关键信息
- **定位**：打印线程堆栈
- **典型场景**：CPU 飙高、死锁排查
- **CPU 飙高排查流程**：top 找进程 → top -Hp 找线程 → printf "%x\n" 线程PID → jstack PID | grep 十六进制
- **属于**：JDK 自带 Java 诊断工具集（jps/jstack/jmap/jstat/jinfo/jhat）
- **生产环境安全性（2026-10-08 补充）**：生产执行 jstack 对服务影响很小，可安全抓取；`jstack <PID> > stack.log` 建议间隔 1 秒多抓 2~3 次，区分持续阻塞与瞬时问题
- **十六进制匹配要点**：jstack 输出中线程 ID 为十六进制，须用 `printf "%x\n"` 把 top 的十进制线程 ID 转换后再搜索
- **GC 疑问分流**：若怀疑频繁 GC 而非线程问题，转用 `jstat -gc <PID> 1000` 观察 GC 频率与 FullGC

## 关联连接
- [[摘要-面试官你掌握哪些Linux常用命令]] — 来源
- [[摘要-java-cpu-troubleshooting]] — 2026-10-08 排障流程来源
- [[Java高CPU排障]] — 提炼的排障链路概念
- [[Java]] — 诊断对象
- [[JVM]] — 诊断基础
- [[top]] — 配合排查 CPU 飙高
- [[Arthas]] — 更强大的现代化替代
- [[jhat]] — 同属 JDK 诊断工具集（heap dump 分析）
