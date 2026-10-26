---
title: "CUDA"
type: entity
tags: [工具, GPU, NVIDIA, 编程模型]
sources: [raw/09-archive/张江芯片员工：32岁税前80个，没有互联网那么卷，现在国产卡都在招人，算是踩中这波算力红利了（附Agent面试题）.md]
last_updated: 2026-10-15
---

## 定义

CUDA 是 NVIDIA 的 GPU 并行计算平台与编程模型，也是文中多处技术结论的官方出处（CUDA 编程指南、CUDA 文档、CUDA 计算能力版本、CUDA 运行时）。

## 关键信息

- **架构论断出处**：CUDA 的编程指南指出"GPU 把更多晶体管用于数据处理，而不是数据缓存和流程控制"；CUDA 文档明确写了 **GPU 的指令是按顺序发射的，没有分支预测，也没有提前猜测并执行后续指令的推测执行机制**。详见 [[GPU架构]]。
- **计算能力版本**：**9.0** 引入线程块簇（Thread Block Cluster），即 Hopper 一代的分布式共享内存机制，详见[[线程块簇]]。常量缓存每 SM 工作集 8KB "从早期的 CUDA 计算能力版本到现在都没变过"。
- **CUDA 运行时**：在共享内存分配中自己预留了 1KB（单线程块最多可用 227KB，而硬件上限为 228KB）；**静态声明的共享内存上限仍是 48KB，超过必须用动态分配方式向运行时申请**。详见 [[GPU存储层级]]。
- **CUDA 13.1（2025 年 12 月公开）**：引入 **cuTile**——包含新的虚拟指令集 CUDA Tile IR、面向 Python 的 cuTile Python 接口，以及把 Tile IR 字节码直接编译成硬件原生机器码（SASS）的编译器；首发针对 Blackwell 架构。这标志着**以数据块（tile）为单位的编程模型被 NVIDIA 正式吸收进 CUDA 官方底座**。详见 [[DSL]]、[[cuTile]]。
- **生态位置**：CUDA 之上有 CuTe DSL（CUTLASS 4.0 起的 Python 接口）等更贴近硬件的抽象；[[Triton]] 则通过生成 PTX 再经 `ptxas` 汇编成 cubin 与其对接。

## 关联连接

- [[GPU架构]] — CUDA 文档是架构论断的出处
- [[GPU存储层级]] — 共享内存档位与 48KB 静态上限
- [[线程块簇]] — CUDA 计算能力 9.0 引入
- [[cuTile]] — CUDA 13.1 新增的 tile 编程模型
- [[Triton]] — 生成 PTX/cubin 的上层 DSL
- [[DSL]] — GPU 编程抽象分层
- [[NVIDIA]] — 所属公司
- [[摘要-张江芯片员工与AI编译器面试题]] — 来源
