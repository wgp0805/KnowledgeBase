---
title: "Java高CPU排障"
type: concept
tags: [Java, 性能, 排障, 线上运维]
sources: [raw/01-articles/Java 线上排障：服务 CPU 打满、接口卡死定位方案.md]
last_updated: 2026-10-08
---

## 定义
线上 Java 服务 CPU 打满、接口卡死时的标准排查链路：`进程 → 线程 → 堆栈 → 代码行`，核心原则是保留现场优先、不急于重启。

## 关键信息
- **第一原则**：不急于重启实例——重启会丢失线程现场，无法定位根因
- **五步链路**：
  1. `top` 找到高 CPU Java 进程，记录 PID
  2. `top -Hp <PID>`（-H 显示线程、-p 指定进程）找到占用最高的线程 ID（十进制）
  3. `printf "%x\n" <十进制线程ID>` 转十六进制（jstack 堆栈中线程 ID 为十六进制，必须转换才能匹配）
  4. `jstack <PID> > stack.log` 抓取线程堆栈，建议间隔 1 秒多抓 2~3 次，区分持续阻塞与瞬时问题
  5. 在 stack.log 中搜索十六进制线程号，直接定位问题 Java 代码行
- **常见根因**：死循环（while/for 无退出条件）、复杂正则表达式的灾难性回溯、频繁 GC、大量计算密集型逻辑无限流
- **GC 辅助排查**：怀疑 GC 问题时配合 `jstat -gc <PID> 1000` 观察 GC 频率与 FullGC 情况
- **安全性**：生产环境执行 jstack 对服务影响很小，可安全抓取

## 关联连接
- [[摘要-java-cpu-troubleshooting]] — 来源
- [[jstack]] — 抓堆栈命令
- [[top]] — 定位进程与线程命令
- [[JVM]] — 诊断基础
- [[Arthas]] — 更强大的现代化替代工具
- [[摘要-mysql查询cpu占用过高的方法]] — 数据库侧 CPU 排查对照
