---
title: "StableHLO"
type: entity
tags: [编译器, 中间表示, 机器学习]
sources: [raw/09-archive/张江芯片员工：32岁税前80个，没有互联网那么卷，现在国产卡都在招人，算是踩中这波算力红利了（附Agent面试题）.md]
last_updated: 2026-10-15
---

## 定义

StableHLO 是**介于框架代码与底层指令之间的中间表示（IR）**，用于承载深度学习框架导出的算子图。在 [[AI编译器]] 的工具链中，它位于前端（PyTorch 等框架的计算图）与后端（硬件指令集）之间。

## 关键信息

- **在编译链中的位置**：AI 编译器"往上接深度学习框架导出的计算图，比如 PyTorch 这一层，或者 StableHLO 这类介于框架代码和底层指令之间的中间表示"。
- **典型用例**：[[ByteIR]]（字节基于 [[MLIR]] 的模型编译方案）的前端**先把模型转换成 StableHLO 中间表示**，编译器部分再复用上游 MLIR 的方言。
- **与 MLIR 的关系**：StableHLO 本身即以 MLIR 方言形式存在，因此可以与其他抽象层次的方言共存于同一模块，参与渐进式降级（progressive lowering），详见 [[MLIR]]。

## 关联连接

- [[MLIR]] — StableHLO 的宿主基础设施
- [[AI编译器]] — StableHLO 在编译链中的位置
- [[ByteIR]] — 以 StableHLO 为前端的实际项目
- [[摘要-张江芯片员工与AI编译器面试题]] — 来源
