---
title: "CNN"
type: concept
tags: [AI, 深度学习, 神经网络, 计算机视觉]
sources: [raw/01-articles/2026-07-07-Transformer、"训练-微调"范式-AI 相关概念之（核心技术与架构） - 橙子家.md]
last_updated: 2026-07-08
---

## 定义
CNN（Convolutional Neural Network，卷积神经网络）是 1989 年工程化提出的神经网络架构，专注提取图像等空间数据（2D 网格结构）的局部空间特征，是计算机视觉领域的基础架构。

## 关键信息

### 核心特征
- 专注图像等空间数据
- 卷积操作天然支持并行计算
- 通过卷积核提取局部空间特征

### 本质局限
- 感受野有限，难以建模长距离依赖
- 在序列建模（NLP/语音）领域被 Transformer 替代

### 在架构演进中的位置
CNN（1989，空间）→ RNN（1986，序列）→ Transformer（2017，全局）

### 与 Transformer 的关系
- CNN 是"关注细节的局部观察者"
- Transformer 是"统筹全局的并行计算大师"
- ViT（Vision Transformer）在 ImageNet 上准确率已超越 CNN

## 关联连接
- [[Transformer]] — 替代 CNN 在主流 NLP 领域地位的架构
- [[RNN]] — 另一前置架构（序列建模）
- [[自注意力机制]] — Transformer 的核心，区别于 CNN 的卷积
- [[摘要-transformer-训练微调范式]] — 来源
