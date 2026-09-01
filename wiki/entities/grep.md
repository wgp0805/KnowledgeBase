---
title: "grep"
type: entity
tags: [Linux, 文本处理, 命令]
sources: [raw/01-articles/面试官：你掌握哪些 Linux 常用命令？.md]
last_updated: 2026-08-27
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

## 关联连接
- [[摘要-面试官你掌握哪些Linux常用命令]] — 来源
- [[Linux]] — 运行环境
- [[awk]] — 三剑客之一
- [[sed]] — 三剑客之一
- [[Ripgrep]] — Rust 高性能搜索工具（Claude Code Grep 底层）
