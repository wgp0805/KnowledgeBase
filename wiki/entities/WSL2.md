---
title: "WSL2"
type: entity
tags: [Windows, Linux, 开发工具]
sources: []
last_updated: 2026-05-29
---

## 定义
WSL2（Windows Subsystem for Linux 2）是微软在 Windows 上运行 Linux 环境的子系统，使用真正的 Linux 内核，提供完整的系统调用兼容性。

## 关键信息
- 真正的 Linux 内核（非模拟层）
- 文件系统性能大幅提升（相比 WSL1）
- 支持 systemd（WSL 0.67.6+）
- Docker Desktop 的推荐后端
- 支持 GPU 直通（GPU-P）
- 网络：与 Windows 共享 IP，端口自动互通

## 关联连接
- [[Windows]] — 所属操作系统
- [[Linux]] — 运行的 Linux 环境
- [[DockerDesktop]] — 推荐使用 WSL2 后端
- [[Ubuntu]] — 默认安装的 Linux 发行版
