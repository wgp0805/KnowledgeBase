---
title: "Multipass"
type: entity
tags: [实体, 虚拟化, 运维工具, Ubuntu, Canonical]
sources: [raw/01-articles/比 VMware 更快，更轻的虚拟机，横空出世！.md]
last_updated: 2026-10-22
---

## 定义
Multipass 是由 Ubuntu 背后的 **Canonical** 公司开发开源的**轻量级虚拟机命令行管理工具**，运行环境支持 Linux、Windows 和 macOS。定位是比 [[VMware]] 更快、更轻的虚拟机工具——免费、命令行驱动、几分钟就能搭起一台 Linux 环境。

## 关键信息
- **镜像体系**：`multipass find` 可用镜像含 core18/core20、Ubuntu 16.04 xenial、18.04 bionic、20.04 focal/lts、20.10 groovy，以及 appliance:adguard-home / mosquitto / nextcloud / openhab / plexmediaserver 等应用镜像。**只支持 Ubuntu 镜像**（由 Canonical 开发所致），这是该工具唯一被提及的不足
- **核心命令**：
  - `multipass version` — 查看版本
  - `multipass find` — 列出可用镜像
  - `multipass launch --name dg` — 启动实例
  - `multipass list` — 查看列表（Name / State / IPv4 / Image）
  - `multipass info --all` — 查看详细信息（State、IPv4、Release、Image hash、Load、Disk usage、Memory usage）
  - `multipass shell dg` — 进入交互终端；`multipass exec dg -- <cmd>` — 直接在实例内执行命令（如 `lsb_release -d`）
  - `multipass stop dg` / `multipass start dg` — 暂停与启动
  - `multipass delete dg` — 删除（虚拟机实际仍存在）；`multipass purge dg` — 彻底释放
- **自动化初始化**：`multipass launch --name ubuntu --cloud-init config.yaml`，config.yaml 为 `#cloud-config` 格式，`runcmd` 指定首次启动时运行的命令（如安装 Node.js、`dpkg -i` 安装 lean-cli），用于保持开发环境与线上环境一致并节省部署时间
- **适用场景**：做 Linux 小试验几分钟搭起系统；本地快速搭建虚拟机集群测试小型数据库集群
- **官方地址**：https://multipass.run/ ，文档 https://multipass.run/docs/

## 关联连接
- [[VMware]] — 对照的成熟虚拟机方案
- [[Hyper-V]] — 同类虚拟化方案的另一选项
- [[Ubuntu]] — 唯一支持的镜像体系
- [[Linux]] — 主要使用场景
- [[摘要-multipass轻量虚拟机]] — 来源
