---
title: "摘要-arthas-4"
type: source
tags: [来源, Arthas, Java诊断, JVM, AI运维]
sources: [raw/09-archive/2026-11-01 - 为什么越来越多人用Arthas 4 ？.md]
last_updated: 2026-11-02
---

## 核心摘要

「苏三说技术」拆解 **Arthas 4** 的升级方向：跟上 JDK 演进、补全性能分析、拥抱 AI 工作流。

**Arthas 是什么**：Java Agent，通过 attach 机制挂到正在运行的 JVM 上，不需要重启、不需要改代码、不需要提前埋点。核心能力分类：

- 看全局：`dashboard`、`jvm`
- 看线程：`thread`、`thread -n`（CPU 最高）、`thread -b`（死锁）
- 看方法：`watch`（入参返回值）、`trace`（调用链路耗时）、`monitor`（周期统计）、`tt`（时间隧道）
- 看类：`sc`（搜索已加载类）、`jad`（反编译）、`classloader`
- 热更新：`jad` + `mc` + `redefine` 一条龙
- 性能分析：`profiler`（火焰图）、`jfr`（JFR 采集）

**4.x 三大升级**：

1. **JDK 支持 8 到 25**：官方明确支持 JDK 17、21、25；Jackson、Fastjson2、OGNL、Netty 等依赖升级
2. **火焰图从「看 CPU」到「看墙钟时间」**：`profiler` 内置 async-profiler 升级到 4.4，4.0.2 起支持 `--wall` 参数。解决 CPU 不高但接口慢的问题——锁等待、网络 IO 阻塞、数据库连接池耗尽时线程在「等」，传统 CPU 火焰图看不出来。会话默认超时从 30 分钟放宽到 3 小时
3. **MCP Server 让 AI 跑诊断命令**：在 HTTP 服务上实现 MCP 端点，暴露 29 个诊断工具（`dashboard`、`thread`、`trace`、`jad`、`profiler` 等），AI 客户端连上来后可用自然语言执行诊断。Cherry Studio、Cline、Claude Desktop 等客户端配置后即可用。**仍是实验模块**，官方建议生产环境以只读诊断为主，别让 AI 触发 `redefine` 这类热替换

配置示例：`arthas.properties` 设 `arthas.mcpEndpoint=/mcp`、`arthas.httpPort=8563`、`arthas.password`；AI 客户端按 streamableHttp 类型接入并带 Bearer 认证。

**踩坑提醒**：

- `watch`/`trace` 有性能开销，高频方法必须加 `-n` 限制次数或条件过滤，否则打爆 CPU；`-x` 展开最多 3 层
- `trace` 默认只追踪一层内部调用，追多层用 `--maxDepth`，开销大；被 JIT 内联的方法可能追踪不到
- `tt` 默认最多存 100 条记录、存对象引用（对象后续被修改看到的值可能不对）；退出 Arthas 不会自动清理，用完记得 `tt --delete-all`
- 热更新只能改方法体，不能增删字段和方法；与 `watch`/`trace` 冲突，执行前要先 `reset`

**AI 排障边界**：AI 能把「现象」翻译成「命令序列」、把「原始输出」整理成「结论」，减少翻手册查语法的时间；但判断结论是否符合业务逻辑仍需人工——「库存服务 RPC 超时」背后是服务挂了、网络问题还是调用量突增，AI 无法判断。

## 关联连接
- [[Arthas]] — 被介绍的工具
- [[MCP]] — AI 接入协议
- [[async-profiler]] — 火焰图底层引擎
- JFR — JVM 飞行记录
- [[苏三]] — 文章作者
