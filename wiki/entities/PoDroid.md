---
title: "PoDroid"
type: entity
tags: [开源工具, Android, 容器, Docker, 自托管]
sources: [raw/01-articles/PoDroid安装使用指南.md]
last_updated: 2026-10-09
---

## 定义
PoDroid 是一款在 Android 手机上运行完整 Linux 容器环境的应用：无需 ROOT、无需刷机，通过 QEMU 软件虚拟化启动 Alpine Linux 虚拟机，预装 Podman、Docker、LXC 三大容器引擎，让旧手机变身可自托管服务的迷你服务器。

## 关键信息
- **仓库**：GitHub ExTV/Podroid（不在 Google Play 上架），APK 约 200MB；官方文档 extv.github.io/Podroid
- **要求**：ARM64（arm64-v8a）+ Android 8.0+，推荐 4GB 内存；VM 磁盘 2GB-512GB 稀疏镜像可选
- **技术底座**：自定义 Linux 7.1.5 内核（overlay2、cgroup v2、netfilter），QEMU TCG 软件模拟；Pixel 8/9/10 系列可开 AVF (pKVM) 硬件加速接近原生
- **与 Termux 的区别**：Termux 共享宿主内核、proot 仅 chroot 模拟无法跑真 Docker 镜像；PoDroid 是完整 VM，所有 OCI 镜像直接可用
- **关键机制**：端口转发（`podroid-forward`，手机端口须 ≥1024、SSH 用 9922）、Dropbear SSH（root/podroid）、X11 查看器（仅 X11 不支持 Wayland）、服务器模式息屏挂机（`podroid-server on`）
- **VM 调 Android**：`podroid-notify` 发通知、`podroid-open` 打开手机浏览器、`podroid-power` 控制 VM
- **性能**：IO 密集任务流畅；CPU 密集与长编译慢（JVM 启动 10-30 秒）；必须用 ARM64 镜像，x86 镜像双重模拟慢 50-100 倍
- **典型用例**：Nginx、Pi-hole、Gitea、Vaultwarden、code-server 自托管与开发环境

## 关联连接
- [[摘要-podroid-安卓容器指南]] — 来源
- [[Docker]] — 预装容器引擎
- [[端口转发]] — 服务暴露方式
- [[Linux]] — VM 内运行的系统
