---
title: "jstack"
type: entity
tags: [JDK, Java诊断, 命令]
sources: [raw/01-articles/面试官：你掌握哪些 Linux 常用命令？.md]
last_updated: 2026-08-27
---

## 定义
jstack 是 JDK 自带的 Java 诊断工具，用于打印线程堆栈，是 CPU 飙高、死锁排查的核心工具。

## 关键信息
- **定位**：打印线程堆栈
- **典型场景**：CPU 飙高、死锁排查
- **CPU 飙高排查流程**：top 找进程 → top -Hp 找线程 → printf "%x\n" 线程PID → jstack PID | grep 十六进制
- **属于**：JDK 自带 Java 诊断工具集（jps/jstack/jmap/jstat/jinfo/jhat）

## 关联连接
- [[摘要-面试官你掌握哪些Linux常用命令]] — 来源
- [[Java]] — 诊断对象
- [[JVM]] — 诊断基础
- [[top]] — 配合排查 CPU 飙高
- [[Arthas]] — 更强大的现代化替代
