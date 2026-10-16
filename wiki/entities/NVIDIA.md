---
title: "NVIDIA"
type: entity
tags: [芯片公司, GPU, 算力, 硬件]
sources: [raw/09-archive/张江芯片员工：32岁税前80个，没有互联网那么卷，现在国产卡都在招人，算是踩中这波算力红利了（附Agent面试题）.md]
last_updated: 2026-10-15
---

NVIDIA（英伟达）是 GPU 与加速计算芯片公司，其 GPU 是大模型训练与推理的主要算力载体——生物模型优化资料中即以单张 NVIDIA GPU 节点作为推理单位（见 [[摘要-anthropic优化生物模型]]）。

## AI 编译器相关（2026-10-15 补充）
来自 [[摘要-张江芯片员工与AI编译器面试题]]。NVIDIA 是 AI 编译器与算子开发的核心硬件目标平台：
- **指令链**：虚拟指令集 **PTX** → 汇编器 `ptxas` → 硬件机器码 **SASS** / 可执行二进制 **cubin**（[[Triton]] 的编译终点即在此）。
- **硬件代际**：Hopper（H100，SXM5 132 个 SM / 完整 GH100 144 个 / PCIe 版 114 个，80GB HBM3）引入 [[TMA]] 与[[线程块簇]]；Blackwell（B200 180GB HBM3e、最高 8TB/s）新增[[张量内存]]与 `tcgen05.mma`（Hopper 的 `wgmma.mma_async` 已弃用）。
- **官方编程模型**：[[CUDA]] 提供平台底座，CUDA 13.1 引入 [[cuTile]]（CUDA Tile IR + cuTile Python + Tile IR→SASS 编译器，首发针对 Blackwell），标志 tile 编程模型被正式收进官方底座。
- **生态竞争**：社区事实标准 [[Triton]] 与官方 cuTile 形成同层对照；CuTe DSL（CUTLASS 4.0 起的 Python 接口）与 ThunderKittens 则位于更贴近硬件的一层，详见 [[DSL]]。

## 关联连接
- [[RustFS]] — 来源（死链修复）
- [[摘要-谷歌gemini38flash-harness-engineering]] — 来源（死链修复）
- [[摘要-rustfs-ga正式版]] — 来源（死链修复）
- [[摘要-anthropic优化生物模型]] — GPU 算力语境
- [[摘要-张江芯片员工与AI编译器面试题]] — 来源（AI 编译器与硬件代际）
- [[CUDA]] — 官方并行计算平台
- [[cuTile]] — CUDA 13.1 的 tile 编程模型
- [[Triton]] — 社区事实标准算子 DSL
- [[GPU架构]] / [[GPU存储层级]] — 硬件架构与存储层级
- [[TMA]] / [[线程块簇]] / [[张量内存]] — Hopper 与 Blackwell 新增机制
- [[AI编译器]] — 面向其硬件的编译器生态
