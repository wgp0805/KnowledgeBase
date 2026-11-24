---
title: "Stela"
type: entity
tags: [开源项目, 黑苹果, 指令翻译, 虚拟化]
sources: ["raw/09-archive/2026-11-22 - 黑苹果续作：让普通PC运行macOS 27系统.md"]
last_updated: 2026-11-24
---

## 定义
Stela（github.com/tylertms/Stela）是开源项目，让普通 AMD/Intel x86-64 PC 运行 Apple Silicon 版 macOS 27 及后续版本——思路不是装 x86 版 macOS，而是**在 UEFI 启动阶段把 PC 模拟为 M2 Mac mini，再用 [[指令集翻译]] 把 ARM64 指令交给 x86 处理器执行**。

## 关键信息
- **与黑苹果的根本差别**：传统黑苹果依赖"Intel 版 macOS + x86 兼容性"，苹果已停供 x86 版 macOS，该路线走到尽头；Stela 把兼容性问题转成指令翻译问题
- **转译器**：AOT + JIT 结合，覆盖 3000+ 种 AArch64 指令编码，用寄存器映射与翻译缓存减少重复编译
- **图形**：Metal 驱动把苹果 AIR 着色器中间表示直接编译为 [[Mesa]] 的 NIR，支持 Metal 3 与 Apple7 GPU 加速，目标是启动未经修改的 macOS 系统
- **附带价值**：x86 机器因此能直接跑 ARM64 原生应用，不依赖苹果兼容层（Rosetta）
- **硬件要求**：支持 x86-64-v2 的 Intel/AMD、≥8GB 内存、可关闭 Secure Boot 的 64 位 UEFI、NVIDIA GTX 16 系或 AMD RX 20/30/40/50 系显卡、≥60GB 磁盘、有线网卡（**暂不支持 WiFi 与音频**）
- **安装前提**：需联网下载 macOS 镜像；无网口设备要备 USB 有线网卡
- **现状（2026-11）**：活跃开发中（启动、以太网、SATA、USB），速度慢，受支持硬件上也可能启动失败；建议用闲置设备试
- 法律与合规风险始终存在（macOS EULA 不允许非苹果硬件运行），仅供技术研究

## 关联连接
- [[黑苹果]] — 被它延续/取代的旧路线
- [[指令集翻译]] — 核心技术原理
- [[Mesa]] — 图形栈落地路径
- [[Apple]] — macOS 与 Apple Silicon 的提供方
- [[摘要-黑苹果续作-stela运行macos27]] — 来源
