---
title: "摘要-java-cpu-troubleshooting"
type: source
tags: [来源, Java, 排障, 性能, 线上运维]
sources: [raw/09-archive/Java 线上排障：服务 CPU 打满、接口卡死定位方案.md]
last_updated: 2026-10-08
---

## 核心摘要
线上 Java 服务 CPU 突然飙到 400%、接口卡死时的定位方案：优先保留现场、不要立刻重启（重启会丢失线程现场、问题难复现），排查链路为 `进程 → 线程 → 堆栈 → 代码行`。五步操作：① `top` 找高 CPU Java 进程记下 PID；② `top -Hp <PID>` 找占用最高的线程 ID（十进制）；③ `printf "%x\n"` 把线程 ID 转十六进制（jstack 堆栈里是十六进制）；④ `jstack <PID> > stack.log` 抓堆栈，建议间隔 1 秒多抓 2~3 次以区分持续阻塞与瞬时问题；⑤ 在堆栈文件中搜十六进制线程号定位到具体代码行。常见根因：死循环、复杂正则灾难性回溯、频繁 GC（可配 `jstat -gc <PID> 1000` 观察 GC 频率与 FullGC）、大量计算密集逻辑无限流。生产执行 jstack 对服务影响很小，可安全抓取。

## 关联连接
- [[Java高CPU排障]] — 流程提炼的概念页
- [[jstack]] — 核心诊断命令
- [[top]] — 排查起点命令
- [[JVM]] — 排障对象
