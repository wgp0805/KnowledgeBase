---
title: "摘要-anthropic优化生物模型"
type: source
tags: [来源, 原始文件, Anthropic, Claude, 生物模型, 蛋白设计, kernel优化]
sources: [raw/01-articles/2026-09-19-Anthropic 优化 30 多个生物模型，蛋白质设计成本最高降 98%.md]
last_updated: 2026-09-20
---

## 核心摘要
Anthropic 让 Claude 用不到四周优化了 30 多个生物研究开源模型，覆盖蛋白结构预测、蛋白设计、Protein Language Model 和基因组学。允许极小精度损失时平均提速约 4 倍，要求输出完全一致时平均接近 2 倍加速，并降低显存占用让大型分子系统可在单张 NVIDIA GPU 节点推理。Claude 开发了 FlashPairformer 自定义 kernel 专门加速 triangle attention 和 triangle multiplication（AlphaFold3/OpenFold3/Boltz-2 大量使用），相较 NVIDIA cuEquivariance 快 2.7-2.9 倍。还开发低显存 Big mode，单节点准确预测超 1 万 Token 生物分子系统。蛋白设计成本从每靶点约 1 万美元（约 2500 H100 GPU 小时）降到约 150 美元（单 Claude 模型 + 单张 H200 + 24 小时 + 1100 词 Prompt）。优化代码已开源。

## 关联连接
- [[Anthropic]] — 公司
- [[Claude]] — 优化模型
- [[FlashPairformer]] — 自定义 kernel
- [[triangle attention]] — 计算热点
- [[kernel优化]] — 概念
- [[蛋白设计]] — 应用场景
- [[AlphaFold3]] — 被优化模型
- [[有新Newin]] — 作者