---
title: "ChrisLattner"
type: entity
tags: [人物, 编译器, LLVM, MLIR]
sources: [raw/09-archive/张江芯片员工：32岁税前80个，没有互联网那么卷，现在国产卡都在招人，算是踩中这波算力红利了（附Agent面试题）.md]
last_updated: 2026-10-15
---

## 定义

Chris Lattner 是 LLVM 的创建者，也是把 [[MLIR]] 推入 LLVM 官方体系的关键人物。文中记录的具体动作：**2019 年 9 月，Chris Lattner 在 llvm-dev 邮件列表发起提案**，同年 10 月 LLVM 基金会正式接受，12 月底代码合入 LLVM 主仓库（目录名 `mlir`）。

## 关键信息

- **MLIR 归属时间线**：2018 年在 Google 内部启动 → 2019 年 4 月开源在 TensorFlow 仓库 → 2019 年 9 月 Chris Lattner 在 llvm-dev 发起提案 → 2019 年 10 月 LLVM 基金会接受 → 2019 年 12 月底合入 LLVM 主仓库，此后属于 LLVM 官方项目的一部分。
- **技术影响**：MLIR 的渐进式降级（progressive lowering）与方言（dialect）体系，成为 [[AI编译器]] 处理多维张量与多层循环结构的主流基础设施（[[Triton]]、[[ByteIR]] 均建立其上）。

## 关联连接

- [[MLIR]] — 由其提案进入 LLVM 官方体系
- [[LLVM]] — 其创建的编译器基础设施
- [[AI编译器]] — MLIR 的主要应用领域
- [[摘要-张江芯片员工与AI编译器面试题]] — 来源
