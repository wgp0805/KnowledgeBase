---
title: "摘要-podroid-安卓容器指南"
type: source
tags: [来源, Docker, Android, 容器, 自托管]
sources: [raw/01-articles/PoDroid安装使用指南.md]
last_updated: 2026-10-09
---

## 核心摘要
PoDroid 是在 Android 手机上运行完整 Linux 容器环境的应用：无需 ROOT、无需刷机，通过 QEMU 软件虚拟化启动 Alpine Linux 虚拟机（自定义 Linux 7.1.5 内核），预装 Podman/Docker/LXC 三大容器引擎。要求 ARM64 + Android 8+，VM 磁盘 2GB-512GB 可选；支持端口转发（手机端口须 ≥1024，SSH 用 9922）、Dropbear SSH 远程连接、VS Code Remote、X11 桌面（XFCE/Firefox）、服务器模式息屏挂机、VM 内调 Android（通知/打开浏览器）。与 Termux 的关键区别：Termux 共享宿主内核、proot 只是 chroot 模拟跑不了真 Docker 镜像，PoDroid 是完整 VM 所有 OCI 镜像直接可用；Pixel 8/9/10 系列可开 AVF (pKVM) 硬件加速接近原生速度。性能提示：必须用 ARM64 镜像（x86 镜像双重模拟慢 50-100 倍），IO 密集任务流畅、CPU 密集/长编译慢。典型用例：Nginx、Pi-hole、Gitea、Vaultwarden、code-server 自托管。

## 关联连接
- [[PoDroid]] — 文章主角实体页
- [[Docker]] — 三大容器引擎之一
- [[端口转发]] — 关键配置机制
- [[SFTP传输]] — 文件传输方式
