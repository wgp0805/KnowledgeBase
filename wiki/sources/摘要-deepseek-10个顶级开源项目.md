---
title: "摘要-deepseek-10个顶级开源项目"
type: source
tags: [来源, DeepSeek, 开源, 大模型, Agent]
sources: [raw/01-articles/2026-10-31 - 推荐 10 个 DeepSeek 顶级开源项目.md]
last_updated: 2026-11-02
---

## 核心摘要

「苏三说技术」系统性盘点 DeepSeek 开源的 10 个最有价值的项目，按影响力、受众范围、Star 数量、repo 质量综合排序。文章核心判断：DeepSeek 的开源是「自上而下的全链路解剖」，与大多数厂商只开源推理 Demo 形成对比。

按层次排列：

**算子层**
- **DeepSeek-Math**（第 10）：7B 数学模型，从 DeepSeek-Coder-Base 启动，构建 120B Token 高纯度数学语料库；首次提出 **GRPO**，后来 R1-Zero 和 R1 的算法底层完全脱胎于此
- **FlashMLA**（第 7）：针对 NVIDIA Hopper 架构的 MLA 解码高性能算子库，直接适配压缩后的 KV Cache、TMA 与流水线调度、支持变长序列与分页缓存

**通信层**
- **DeepEP**（第 9）：MoE 通信库，解决跨卡/跨节点 All-to-All 集合通信瓶颈；机内 NVLink、机间 RDMA、通信与计算重叠、支持 FP8 数据分发

**存储层**
- **3FS**（第 8）：AI 工作负载专用存储系统，解决预训练海量小文件并发吞吐和 Checkpoint 秒级刷盘两大 IO 场景；存算分离、CRAQ 强一致复制、RDMA 高速访问；丢弃传统 POSIX 包袱

**模型层**
- **DeepSeek-V3**（第 2）：671B 总参数 / 37B 激活，2048 张 H800 训练成本约 557.6 万美元；MLA 压 KV Cache、MoE 无辅助损失负载均衡、FP8 混合精度训练、MTP 多 Token 预测
- **DeepSeek-R1**（第 3）：打破 o1 垄断；R1-Zero 纯强化学习探索推理、GRPO 省去独立价值模型、多阶段训练、蒸馏让小模型也能学会推理
- **DeepSeek-Coder**（第 4）：2023 年 10 月第一代，2 万亿 Token 从头预训练；2024 年 6 月演进出 Coder-V2，全球首个开源 MoE 代码大模型（236B 总参 / 21B 激活），338 种语言、128K 上下文

**服务层**
- **DeepInfer**（第 6）：DeepSeek 线上同款推理引擎，基于 vLLM 演进，定制算子、MoE 专家并行与负载均衡、异步调度、投机解码（DSpark）

**应用层**
- **DeepSeek-OCR**（第 5）：开创「上下文光学压缩」，把整页文档渲染为高清图像，经视觉编码器压缩到几十至几百个视觉 Token，避免纯文本转录的 Token 爆炸与结构信息丢失
- **DeepSeek Harness**（第 1）：2026 年 8 月 MIT 协议开源，两个多月 Star 破 25 万；基于 Cordis 微内核的原生 Agent 运行底座，全面拥抱「一切皆插件」与驾驭工程

## 关联连接
- [[DeepSeek]] — 主体公司
- [[DeepSeekHarness]] / [[DeepInfer]] — 应用层与服务层开源项目
- [[DeepSeek-V3]] / [[DeepSeek-Coder]] / [[DeepSeek-OCR]] / [[DeepSeek-Math]] — 模型层项目
- [[FlashMLA]] / [[DeepEP]] / [[3FS]] — 算子/通信/存储层项目
- [[GRPO]] / [[MLA]] / [[MoE]] / [[KV Cache]] — 相关技术概念
- [[苏三]] — 文章作者
