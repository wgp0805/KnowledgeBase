---
title: "cuTile"
type: entity
tags: [工具, NVIDIA, CUDA, GPU编程, Blackwell]
sources: [raw/09-archive/张江芯片员工：32岁税前80个，没有互联网那么卷，现在国产卡都在招人，算是踩中这波算力红利了（附Agent面试题）.md]
last_updated: 2026-10-15
---

## 定义

cuTile 是 [[NVIDIA]] 在 **CUDA 13.1** 中引入的一套以**数据块（tile）为单位**的编程模型，包含三个组成部分：一套新的虚拟指令集 **CUDA Tile IR**、一套面向 Python 开发者的编程接口 **cuTile Python**，再加一个把 Tile IR 字节码直接编译成硬件原生机器码（**SASS**）的编译器。

## 关键信息

- **发布时间**：2025 年 12 月随 CUDA 13.1 正式公开，**首发针对 Blackwell 架构**。
- **为什么值得关注**：它意味着"以数据块为单位的编程模型"**已经被 NVIDIA 正式吸收进了 CUDA 官方底座**——此前这一抽象层主要由社区/第三方框架（如 [[Triton]]）承担。详见 [[DSL]]。
- **与既有工具链的关系**：参见 [[Triton]]（生成 PTX 后经 `ptxas` 汇编为 cubin）与 [[CUDA]]（提供 Tile IR 与 SASS 直通路径），两条路线在"谁来负责块内线程映射与共享内存分配"上形成对照。

## 关联连接

- [[CUDA]] — 所属平台与版本
- [[DSL]] — GPU 编程抽象分层中的官方新层
- [[Triton]] — 同层级的社区事实标准
- [[NVIDIA]] — 出品方
- [[摘要-张江芯片员工与AI编译器面试题]] — 来源
