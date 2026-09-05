---
title: "lsof"
type: entity
tags: [Linux, 网络, 命令]
sources: [raw/01-articles/面试官：你掌握哪些 Linux 常用命令？.md]
last_updated: 2026-08-27
---

## 定义
lsof（list open files）是 Linux 命令，用于查看哪个进程占用了指定端口。

## 关键信息
- **定位**：查看端口占用
- **常用示例**：`lsof -i:8080`：看哪个进程占用了 8080
- **替代**：`netstat -anp | grep 端口`、`ss -tunlp | grep 端口`

## 关联连接
- [[摘要-面试官你掌握哪些Linux常用命令]] — 来源
- [[Linux]] — 运行环境
- [[netstat]] — 替代工具
- [[ss]] — 替代工具
