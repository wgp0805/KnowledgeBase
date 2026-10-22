---
title: "VMware"
type: entity
tags: [虚拟化, DevOps]
sources: [raw/01-articles/比 VMware 更快，更轻的虚拟机，横空出世！.md]
last_updated: 2026-10-22
---

## 定义
VMware 是全球领先的虚拟化和云计算软件提供商，其桌面虚拟化产品（VMware Workstation/Fusion）允许在一台物理机上运行多个虚拟机操作系统。

## 关键信息
- VMware Workstation：Windows/Linux 桌面虚拟化
- VMware Fusion：macOS 桌面虚拟化
- 快照（Snapshot）：保存和恢复虚拟机状态
- 共享文件夹：宿主机与虚拟机之间文件共享
- 网络模式：桥接、NAT、Host-Only
- VMware ESXi：企业级服务器虚拟化

### 轻量替代：Multipass（2026-10-21，详见 [[摘要-multipass轻量虚拟机]]）
- **VMware 的短板**：功能多、配置灵活，但**要付费且续费不便宜**
- **[[Multipass]]**（Canonical 开源）：轻量级虚拟机命令行管理工具，支持 Linux / Windows / macOS，免费、几分钟搭起一台 Linux 环境；`launch` / `list` / `info` / `shell` / `exec` / `stop` / `start` / `delete` / `purge` 全命令行，支持 `--cloud-init` 自动化初始化
- **唯一限制**：只支持 Ubuntu 镜像（由 Canonical 开发所致）

## 关联连接
- [[Ubuntu]] — 常在 VMware 中安装
- [[Linux]] — 虚拟机常见操作系统
- [[Docker]] — 容器化替代方案
- [[Multipass]] — 更轻量、免费的命令行虚拟机方案
- [[Hyper-V]] — 同类虚拟化方案
- [[摘要-multipass轻量虚拟机]] — 来源（Multipass 对比）
- [[摘要-windows系统释放休眠文件和保留空间占用的硬盘空间]] — 介绍通过 Windows 管理员命令行释放休眠文件（powe…
