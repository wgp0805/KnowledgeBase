---
title: "Vector API"
type: concept
tags: [JVM, Performance, AI, JDK 27]
sources: [raw/01-articles/JDK27正式发布，人麻了!.md]
last_updated: 2026-09-17
---

## 定义
Vector API，JDK 27的JEP 537（第十二孵化），允许在支持的CPU上利用SIMD指令（如AVX-512、ARM SVE）进行向量计算，专为AI推理和科学计算等高频数值操作设计。

## 核心概念
- **SIMD指令**：一条指令处理多个数据，实现单指令多数据并行
- **向量加法示例**：`FloatVector.add(FloatVector b)` 同时处理多个float值
- **AI推理加速**：矩阵运算、向量相似度计算等高频操作性能提升数量级
- **硬件依赖**：支持AVX-512（x86）或ARM SVE的CPU发挥最大效益
- **Java代码暴露**：硬件向量计算能力直接暴露给Java开发者

## 关联连接
- [[JDK27]] — 包含该特性（需--enable-preview）
- [[SIMD]] - 单指令多数据流
- [[AI Inference]] - AI推理
- [[Scientific Computing]] - 科学计算
- [[CPU Instructions]] - CPU指令集