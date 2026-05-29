---
title: "Hyper-V"
type: entity
tags: [虚拟化, Windows]
sources: []
last_updated: 2026-05-29
---

## 定义
Hyper-V 是微软的硬件虚拟化技术，内置于 Windows 10/11 专业版和企业版，允许在一台物理机上运行多个虚拟机操作系统。

## 关键信息
- 类型 1 虚拟化：直接运行在硬件上（裸金属）
- 支持 Windows 和 Linux 虚拟机
- 虚拟交换机：支持内部、外部和专用网络
- 检查点（Checkpoint）：类似 VMware 快照
- 与 Docker Desktop 集成：WSL2 后端依赖 Hyper-V

## 关联连接
- [[Windows]] — 所属操作系统
- [[VMware]] — 竞品虚拟化方案
- [[DockerDesktop]] — 依赖 Hyper-V/WSL2
