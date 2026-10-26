---
title: "摘要-multipass轻量虚拟机"
type: source
tags: [来源, 虚拟化, 运维工具, Ubuntu]
sources: [raw/09-archive/比 VMware 更快，更轻的虚拟机，横空出世！.md]
last_updated: 2026-10-22
---

## 核心摘要
文章推荐 [[Multipass]] 作为比 [[VMware]] 更轻量的虚拟机命令行管理工具，运行环境支持 Linux、Windows 和 macOS。VMware 的优势是功能强、修改虚拟机配置非常方便，但需要付费且续费不便宜；Multipass 由 Ubuntu 背后的 Canonical 公司开发开源，定位"非常轻量级的虚拟机命令管理工具"。

基本流程：官网下载对应操作系统版本安装 → `multipass version` 查看版本 → `multipass find` 查看可下载的 Ubuntu 镜像列表（core18/core20、16.04 xenial、18.04 bionic、20.04 focal/lts、20.10 groovy，以及 appliance:adguard-home / mosquitto / nextcloud / openhab / plexmediaserver 等应用镜像）→ `multipass launch --name dg` 启动实例 → `multipass exec dg -- lsb_release -d` 确认系统版本。

操作命令：`multipass list` 查看虚拟机列表（Name/State/IPv4/Image）；`multipass info --all` 查看详细信息（State、IPv4、Release、Image hash、Load、Disk usage、Memory usage）；`multipass shell dg` 进入虚拟机交互终端（不想进系统也可用 `multipass exec` 直接执行命令）；`multipass stop dg` / `multipass start dg` 暂停与启动；`multipass delete dg` 删除后虚拟机实际仍存在，需再 `multipass purge dg` 才彻底释放。自动化初始化用 `multipass launch --name ubuntu --cloud-init config.yaml`，config.yaml 为 `#cloud-config` 格式，`runcmd` 指定容器首次启动时运行的命令（如安装 Node.js、dpkg 安装 lean-cli）。

## 关键信息
- **适用场景**：搞 Linux 小试验几分钟搭起系统；本地快速搭建虚拟机集群测试小型数据库集群
- **唯一不足**：只能使用 Ubuntu 镜像——工具由 Canonical 开发开源所致
- **官方地址**：https://multipass.run/ ，文档 https://multipass.run/docs/

## 关联连接
- [[Multipass]] — 工具主体
- [[VMware]] — 对照的成熟虚拟机方案
- [[Hyper-V]] — 同类虚拟化方案的另一选项
- [[Ubuntu]] — 唯一支持的镜像体系与 [[Linux]] 试验环境
- [[小哈]] — 本文作者
- [[摘要-VMware17-安装ubuntu]] — 同类主题：VMware 安装 Ubuntu
