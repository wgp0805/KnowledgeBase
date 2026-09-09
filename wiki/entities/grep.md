---
title: "grep"
type: entity
tags: [Linux, 文本处理, 命令]
sources: [raw/01-articles/面试官：你掌握哪些 Linux 常用命令？.md, raw/09-archive/同事查日志太慢，我现场教他一套 awk、tail、grep、sed 组合拳.md]
last_updated: 2026-09-09
---

## 定义
grep 是 Linux 文本处理三剑客之一，用于文本搜索（找），在日志中搜索关键词排查异常堆栈。

## 关键信息
- **定位**：文本搜索（找）
- **常用示例**：
  - `grep -A 20 "NullPointerException" app.log`：显示匹配行后 20 行（排查异常堆栈）
  - `grep -rn "public class" --include="*.java" .`：递归搜索 java 文件
  - `grep -vi "debug" app.log`：反向匹配 + 忽略大小写
  - `grep -c "ERROR" app.log`：统计匹配行数
- **面试要点**：与 awk（按列处理）、sed（改）区分

### 日志分析实战四场景（来源：[[摘要-日志分析命令组合拳]]）
在实际业务中简单的关键词搜索往往不够用，作者整理了四个必须掌握的场景：

- **还原报错现场（重点）**：grep -C 20 "NullPointerException" logs/application.log。只看到 NullPointerException 这一行往往无法定位问题，必须知道**报错前**的请求参数和**报错后**的堆栈信息，所以要配合 -C（Context）参数显示该行前后各 20 行
- **全链路追踪 TraceId**：grep "TraceId-20251219001" logs/app.log*。微服务通常用 TraceId 串联请求，日志文件滚动后变成 app.log、app.log.1、app.log.2，需要按通配符搜索所有以 app.log 开头的文件
- **统计异常频次**：grep -c "RedisConnectionException" logs/application.log。老板问"Redis 超时异常今天到底发生了多少次、是偶发还是大规模"时，-c（count）直接给出行数，不需要人工数数
- **排除干扰噪音**：grep -v "HealthCheck" logs/application.log。排查时日志里充斥大量 INFO 心跳或健康检查日志，-v（invert）显示不包含该关键词的所有行

## 关联连接
- [[摘要-面试官你掌握哪些Linux常用命令]] — 来源
- [[摘要-日志分析命令组合拳]] — 来源（四场景实战）
- [[日志分析]] — 场景化排查方法论
- [[distributed-tracing]] — TraceId 全链路追踪
- [[Nginx]] — 另一类日志来源
- [[Linux]] — 运行环境
- [[awk]] — 三剑客之一
- [[sed]] — 三剑客之一
- [[Ripgrep]] — Rust 高性能搜索工具（Claude Code Grep 底层）
