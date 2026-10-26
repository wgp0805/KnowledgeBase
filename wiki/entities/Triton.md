---
title: "Triton"
type: entity
tags: [工具, GPU编程, DSL, 编译器, 开源]
sources: [raw/09-archive/张江芯片员工：32岁税前80个，没有互联网那么卷，现在国产卡都在招人，算是踩中这波算力红利了（附Agent面试题）.md]
last_updated: 2026-10-15
---

## 定义

Triton 是目前 GPU 算子开发领域的**事实标准**编程语言/编译器：开发者只管**数据块（block/tile）这一级**的逻辑，至于一个数据块里的数据怎么分给 warp 里的 32 个线程、片上共享内存怎么分配，全部交给编译器自动决定。写起来很像写 NumPy 数组运算，跑出来的性能却能达到**手写 CUDA 代码的大部分水平**。

## 关键信息

- **归属变迁**：开源仓库现在放在 `triton-lang` 组织下，原来的 `openai/triton` 地址已重定向过去。
- **与 PyTorch 的关系**：PyTorch 里调用 `torch.compile` 自动生成的 GPU 算子代码，**底层生成的就是 Triton 代码**。
- **四级编译流程**（[[MLIR]] 最直观的案例）：
  1. 开发者写的 Python 源码 → **TTIR**（以数据块为单位、与具体显卡型号无关的中间表示）；
  2. → **TTGIR**（开始带具体 GPU 硬件信息：数据在各 warp 之间怎么分布、显存读写怎么合并、共享内存用哪种排布，都在这一层确定；中间执行的都是 MLIR 的编译优化 pass，如 `remove_layout_conversions` 消除多余内存排布转换、`accelerate_matmul` 把矩阵乘法替换成 Tensor Core 硬件加速指令、`optimize_dot_operands` 优化点积运算操作数）；
  3. → **LLVM IR** → 生成 NVIDIA 虚拟指令集 **PTX**；
  4. → 由 NVIDIA 汇编器 `ptxas` 编译成 GPU 可直接执行的二进制 **cubin**。
- **多后端结构**：各硬件后端把这些编译阶段注册在自己的 `compiler.py` 文件里。AMD 显卡后端前三级完全一样，只是最后换成 AMD 自己的汇编表示 `amdgcn` 和二进制 `hsaco`。
- **在 DSL 分层中的位置**：见 [[DSL]]——高于 CuTe DSL / ThunderKittens（要手工管到寄存器与共享内存），低于 Helion（写法更接近普通 Python 函数，编译产物是自动调优后的 Triton 代码）。
- **工程结论**：在 NVIDIA 显卡上手写自定义算子，**Triton 依然是最省力的入口**（社区现成代码最多、报错最容易搜到解法）；只有要榨干最后百分之几的极限性能时才下沉到 CuTe 或 C++。
- **国产适配**：华为昇腾走兼容适配 Triton 的路线，`triton-ascend` 已正式迁移到 `triton-lang` 官方组织下（2025 年 5 月开源，2026 年 1 月发布 3.2.0 正式版，底层依赖 [[CANN]] 社区版 9.0.0）。

## 关联连接

- [[AI编译器]] — Triton 是其工具链入口
- [[MLIR]] — Triton 四级编译的实现基础
- [[DSL]] — 五层抽象图谱中的第二层
- [[GPU存储层级]] — TTGIR 层决定共享内存与访存排布
- [[访问合并]] — 在 TTGIR 层确定
- [[华为昇腾]] / [[CANN]] — 国产适配路线
- [[摘要-张江芯片员工与AI编译器面试题]] — 来源
