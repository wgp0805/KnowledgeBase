---
title: "kernel优化"
type: concept
tags: [概念, 高性能计算, GPU, 生物计算]
sources: [raw/09-archive/2026-09-19-Anthropic 优化 30 多个生物模型，蛋白质设计成本最高降 98%.md]
last_updated: 2026-09-20
---

## 定义
kernel 优化指针对 GPU 计算内核（kernel）进行定制优化以提升计算速度、降低显存占用的技术。Anthropic 让 Claude 开发 FlashPairformer 自定义 kernel 加速生物模型推理。

## 关键信息
- **核心思想**：定制 GPU kernel 提升计算效率
- **效果**：允许极小精度损失时平均提速约 4 倍，要求输出完全一致时平均接近 2 倍加速
- **显存优化**：降低显存占用让大型分子系统可在单张 NVIDIA GPU 节点推理
- **案例**：FlashPairformer 加速 triangle attention，相较 NVIDIA cuEquivariance 快 2.7-2.9 倍
- **应用**：蛋白结构预测、蛋白设计、基因组学

## 关联连接
- [[摘要-anthropic优化生物模型]] — 来源
- [[FlashPairformer]] — 自定义 kernel
- [[triangle attention]] — 计算热点
- [[蛋白设计]] — 应用场景
- [[Anthropic]] — 优化方
- [[Claude]] — 优化模型