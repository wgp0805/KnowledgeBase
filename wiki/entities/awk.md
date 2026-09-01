---
title: "awk"
type: entity
tags: [Linux, 文本处理, 命令]
sources: [raw/01-articles/面试官：你掌握哪些 Linux 常用命令？.md]
last_updated: 2026-08-27
---

## 定义
awk 是 Linux 文本处理三剑客之一，用于文本分析（按列处理），适合统计、分析访问日志等场景。

## 关键信息
- **定位**：文本分析（按列处理）
- **常用示例**：
  - `ps aux | sort -rnk 3 | head -5`：查看 CPU 使用率前 5 的进程
  - `awk '{print $1}' access.log | sort | uniq -c | sort -rn | head`：统计 IP 出现次数
  - `awk -F':' '{print $1, $3}' /etc/passwd`：按 ":" 分隔打印列
- **面试要点**：与 grep（找）、sed（改）区分

## 关联连接
- [[摘要-面试官你掌握哪些Linux常用命令]] — 来源
- [[Linux]] — 运行环境
- [[grep]] — 三剑客之一
- [[sed]] — 三剑客之一
