---
title: "netstat"
type: entity
tags: [Linux, 网络, 命令]
sources: [raw/01-articles/面试官：你掌握哪些 Linux 常用命令？.md]
last_updated: 2026-08-27
---

## 定义
netstat 是 Linux 网络统计命令，用于查看端口占用情况，是部署服务时报"端口被占用"的必用工具。

## 关键信息
- **定位**：查看端口占用
- **常用示例**：
  - `netstat -anp | grep 8080`：看 8080 端口被谁占了
  - `netstat -tunlp`：查看所有监听端口（推荐）
- **替代**：`ss -tunlp`（新一代工具，比 netstat 快）、`lsof -i:8080`
- **面试要点**：答出两种以上端口查看方式加分

## 关联连接
- [[摘要-面试官你掌握哪些Linux常用命令]] — 来源
- [[Linux]] — 运行环境
- [[lsof]] — 替代工具
- [[ss]] — 替代工具
