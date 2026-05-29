---
title: "DockerDesktop"
type: entity
tags: [容器, DevOps, 桌面工具]
sources: []
last_updated: 2026-05-29
---

## 定义
Docker Desktop 是 Docker 官方提供的桌面端容器运行环境，支持 Windows 和 macOS，内置 Docker Engine、Docker CLI、Docker Compose 和 Kubernetes。

## 关键信息
- Windows 上通过 WSL2 后端运行 Linux 容器
- 支持 Docker Compose 编排多容器应用
- 内置 Kubernetes 集群（可选启用）
- 提供图形化界面管理容器、镜像、卷和网络
- 支持 Volume Mount 实现数据持久化
- Resource Allocation：可配置 CPU、内存、磁盘限制

## 关联连接
- [[Docker]] — 容器引擎
- [[WSL2]] — Windows 上的 Linux 子系统
- [[Kubernetes]] — 容器编排（可选集成）
- [[docker安装及使用-windows环境]] — 安装指南来源
