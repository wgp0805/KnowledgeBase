---
title: "top"
type: entity
tags: [Linux, 性能监控, 命令]
sources: [raw/01-articles/面试官：你掌握哪些 Linux 常用命令？.md, raw/01-articles/Java 线上排障：服务 CPU 打满、接口卡死定位方案.md]
last_updated: 2026-10-08
---

## 定义
top 是 Linux 实时系统资源监控命令，查看 CPU、内存使用情况，是线上问题排查的起点。

## 关键信息
- **定位**：实时查看系统资源占用（CPU、内存）
- **用法**：`top`（按 1 看各 CPU 核心）、`top -Hp PID`（看某进程的线程；-H 显示线程、-p 指定进程 PID）
- **CPU 飙高排查流程**：top 找进程 → top -Hp 找线程 → printf 转十六进制 → jstack 看堆栈
- **替代**：htop（更友好版本，需安装）
- **现场优先原则（2026-10-08 补充）**：CPU 打满、接口卡死时用 top 定位后**不要立刻重启**——重启丢失线程现场将无法定位根因；第一步记录 Java 进程 PID，第二步 `top -Hp <PID>` 找占用最高的线程 ID（十进制）

## 关联连接
- [[摘要-面试官你掌握哪些Linux常用命令]] — 来源
- [[摘要-java-cpu-troubleshooting]] — 2026-10-08 排障流程来源
- [[Java高CPU排障]] — 提炼的排障链路概念
- [[Linux]] — 运行环境
- [[jstack]] — 配合排查 CPU 飙高
- [[JVM]] — 诊断基础
