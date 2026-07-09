---
title: "Transformer"
type: entity
tags: [AI, 深度学习, 架构, NLP, 自注意力]
sources: [raw/01-articles/2026-07-07-Transformer、"训练-微调"范式-AI 相关概念之（核心技术与架构） - 橙子家.md]
last_updated: 2026-07-08
---

## 定义
Transformer 是 Google 于 2017 年在论文《Attention Is All You Need》中提出的神经网络架构，核心在于通过自注意力机制（Self-Attention）实现全局上下文建模，彻底解决了传统 RNN 的长距离依赖建模瓶颈和并行计算效率问题。当前 90% 以上的大模型均基于 Transformer 或其变体构建，是真正意义上的"AI 通用语言"。

## 关键信息

### 架构演进
- **CNN（1989）**：专注图像空间特征提取，感受野有限
- **RNN（1986）**：专注序列时序依赖，串行计算效率低、长距离依赖失效
- **Transformer（2017）**：抛弃循环结构，用自注意力实现任意距离直接关联，完全并行化训练

### 基本结构
- **编码器-only**（如 BERT）：双向自注意力，适用于分类、语义分析
- **解码器-only**（如 GPT 系列）：掩码自注意力，专为自回归生成任务设计
- **完整架构**（如 T5）：用于翻译、摘要等序列到序列任务

### 应用领域
- **NLP**：GPT-4/Claude/Qwen 等大语言模型，金融价格预测
- **CV**：ViT 图像分类、DETR 端到端目标检测、工业质检（13 亿参数视觉大模型）
- **自动驾驶**：[[Tesla]] FSD 端到端架构（99.8% 场景识别率，决策速度提升 3 倍）
- **生物医药**：AlphaFold2 蛋白质结构预测（接近原子级精度，解决生物学 50 年难题）
- **多模态生成**：Sora 视频生成、BlockNeRF 3D 场景重建
- **其他**：农业病害识别（93.59%）、情绪识别（93.2%）

### 本质局限
- 计算复杂度 O(n²)，长序列显存压力大

## 关联连接
- [[Google]] — Transformer 论文发布者
- [[自注意力机制]] — 核心机制
- [[QKV]] — 注意力计算三要素
- [[CNN]] — 前置架构（空间建模）
- [[RNN]] — 前置架构（序列建模）
- [[预训练]] — 基于 Transformer 的训练范式
- [[OpenAI]] — GPT 系列基于解码器-only 架构
- [[Anthropic]] — Claude 基于 Transformer
- [[Sora]] — 基于 Transformer 的视频生成模型
- [[AlphaFold2]] — 基于 Transformer 的蛋白质预测
- [[摘要-transformer-训练微调范式]] — 来源
- [[FigureAI]] — 具身智能机器人，分层 Transformer 架构
