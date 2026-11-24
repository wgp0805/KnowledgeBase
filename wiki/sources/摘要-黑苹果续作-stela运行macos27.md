---
title: "摘要-黑苹果续作-stela运行macos27"
type: source
tags: [来源, 黑苹果, 指令翻译, 开源项目, macOS]
sources: ["raw/09-archive/2026-11-22 - 黑苹果续作：让普通PC运行macOS 27系统.md"]
last_updated: 2026-11-24
---

## 核心摘要
码农学习联盟 2026-11-22 报道开源项目 [[Stela]]（github.com/tylertms/Stela）：macOS 27 官方兼容列表已全部是 Apple Silicon 机型，Stela 走了一条和传统黑苹果完全不同的路——**不装 x86 版 macOS，而是在 UEFI 启动阶段把 PC 模拟成 M2 Mac mini，再用指令翻译让 x86-64 处理器执行 Apple Silicon 版 macOS 的 ARM64 代码**。转译器结合 AOT 与 JIT，覆盖 3000+ 种 AArch64 指令编码，靠寄存器映射与翻译缓存减少重复处理；图形侧 Metal 驱动把苹果 AIR 着色器中间表示直接编译成 Mesa NIR，支持 Metal 3 与 Apple7 GPU 加速，目标是启动未经修改的 macOS 系统。附带收益是能直接跑 ARM64 原生应用，不依赖苹果兼容层。

硬件门槛：支持 x86-64-v2 的 Intel/AMD、≥8GB 内存、可关闭安全启动的 64 位 UEFI、NVIDIA GTX16 或 RX 20/30/40/50 系列显卡、≥60GB 磁盘、有线网卡（暂不支持 WiFi 与音频）；安装需联网下载 macOS 镜像，无网口设备要备 USB 有线网卡。项目仍在活跃开发（启动、以太网、SATA、USB），速度慢，受支持硬件上也可能起不来，建议用闲置设备试。

> 时代意义：传统黑苹果依赖 Intel 版 macOS 与 x86 的兼容性，这条路随苹果停发 x86 版本走到尽头；Stela 把"兼容性"问题转成了"[[指令集翻译]]"问题。

## 关联连接
- [[Stela]] — 项目本身
- [[指令集翻译]] — 技术核心（AArch64 → x86-64 二进制翻译）
- [[Mesa]] — Metal 驱动落到 Mesa NIR 的实现路径
- [[Apple]] — macOS 27 与 Apple Silicon 的发布方
- [[黑苹果]] — 该路径试图延续的旧生态（待沉淀）
- [[Ubuntu]] / [[VMware]] — 普通 PC 上的另类"装别的系统"路线对比
