---
title: "ss"
type: entity
tags: [Linux, 网络, 命令]
sources: [raw/01-articles/面试官：你掌握哪些 Linux 常用命令？.md]
last_updated: 2026-08-27
---

## 定义
ss 是 Linux 新一代网络统计工具，比 netstat 快，用于查看监听端口。

## 关键信息
- **定位**：查看监听端口（新一代工具）
- **常用示例**：`ss -tunlp`：查看所有监听端口
- **优势**：比 netstat 快
- **替代**：`netstat -tunlp`、`lsof -i:端口`

## 关联连接
- [[摘要-面试官你掌握哪些Linux常用命令]] — 来源
- [[Linux]] — 运行环境
- [[netstat]] — 老一代工具
- [[lsof]] — 替代工具
