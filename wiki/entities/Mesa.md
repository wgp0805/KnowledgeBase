---
title: "Mesa"
type: entity
tags: [工具, 图形栈, 开源, 驱动]
sources: ["raw/09-archive/2026-11-22 - 黑苹果续作：让普通PC运行macOS 27系统.md"]
last_updated: 2026-11-24
---

## 定义
Mesa 是 Linux 上开源的图形库实现（OpenGL / Vulkan / OpenCL 等 API 的驱动中间层），对上提供标准图形 API，对下对接各家 GPU 驱动；NIR 是其内部的中间表示（New IR）。

## 关键信息
- **在跨架构场景中的角色**：[[Stela]] 的 Metal 驱动把苹果的 **AIR 着色器中间表示直接编译为 Mesa 的 NIR**，从而在非苹果硬件上支撑 Metal 3 与 Apple7 GPU 加速
- **为什么选 NIR**：它是一个成熟、可做优化 pass 的着色器 IR，比自己从零写后端成本低得多
- **架构位置**：应用（Metal/OpenGL/Vulkan）→ 驱动前端（如 Stela 的 Metal 实现）→ NIR → 硬件后端（Intel/AMD/NVIDIA 开源驱动）
- **同类对照**：Windows 上对应的是厂商私有驱动 + DirectX；苹果是 Metal 闭源；Mesa 是开源世界的事实标准
- **现实限制**：性能与特性覆盖取决于后端驱动成熟度，这也是 Stela 目前图形能力有限的原因之一

## 关联连接
- [[Stela]] — 把 AIR 编到 NIR 的项目
- [[指令集翻译]] — 同属跨架构兼容层
- [[Apple]] — Metal 的所有方
- [[摘要-黑苹果续作-stela运行macos27]] — 来源
