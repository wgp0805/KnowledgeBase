---
title: "DeepInfer"
type: entity
tags: [实体, 大模型推理, 开源, DeepSeek, 推理引擎]
sources: [raw/01-articles/2026-10-21 - 真正的 OpenAI！DeepSeek 开源内部推理框架 DeepInfer。.md]
last_updated: 2026-10-22
---

## 定义
DeepInfer 是 [[DeepSeek]] 于 2026 年 10 月开源的**生产级大模型推理引擎**，基于 vLLM 演进、同时吸收 SGLang 与 TensorRT-LLM 思路打造，支撑 DeepSeek 自家线上亿级流量。它是 DeepSeek 第一次把"整车生产线"而不只是"发动机图纸和散装零件"（此前开源的 FlashMLA、DeepGEMM、DeepEP、TileLang 等底层算子）交到社区手上。

## 关键信息
- **性能基准**：据《DeepSeek V4.1 Flash 大规模推理部署实践》报告，基于 DeepInfer 的 [[DeepSeek-V4.1-Flash]] 单集群日吞吐高达 **155 万亿 Tokens**，KV Cache 保留时间拉长至 **72 小时以上**；开源不到 24 小时 GitHub Star 突破 1.46 万
- **硬件覆盖**：原生兼容英伟达 **SM100 架构** GPU 与华为 **昇腾 950 NPU** 两大平台
- **四大工程设计**：
  1. **三阶段分离部署** —— 视觉编码器放最便宜的单卡、计算密集的 Prefill 放常见 8 卡做小规模专家并行、显存带宽与通信密集的 Decode 放 64~128 卡超节点做大规模专家并行（Wide-EP），配合预留冗余专家副本的动态负载均衡器 EPLB 压低跨卡空转损耗
  2. **100 PiB 独立分布式存储 + SWA Bounded Replay** —— 基于自研 3FS 分布式文件系统搭建约 100 PiB SSD 存储集群，峰值聚合读取带宽 10 TiB/s，把按 128 Token 分页的块缓存全量写盘；只在活跃会话有效的滑动窗口缓存（SWA KVCache）只留内存约 180 秒，线上命中率超 98%，未命中时只截断重算最近 128 Token，使重算代价与上下文长度和层数无关，预填充在解码层的总计算量减少近一半
  3. **DSpark 置信度投机解码** —— 通过置信度预测头预测每个草稿 Token 的接受概率，只把验证算力分给收益最高的前缀子集，相比固定验证 5 个 Token，线上吞吐提升 6%
  4. **零开销异步批调度** —— GPU 执行第 N 步前向计算与采样时，CPU 并行执行第 N+1 步批次调度与第 N-1 步后处理，GPU 全程零空闲
- **确定性开关**：`DEEPINFER_BATCH_INVARIANT=1` 开启批次无关确定性推理，不论并发批次怎么变，相同输入永远产出相同结果，对线上复现与评测极为便利

## 关联连接
- [[DeepSeekRecipe]] — 同批开源的编解码组件
- [[DeepSeek]] — 开源方
- [[DeepSeek-V4.1-Flash]] — 部署报告对应的模型
- [[KV Cache]] — 72 小时磁盘级 KV 缓存与 SWA Bounded Replay 机制
- [[投机解码]] — DSpark 置信度投机解码
- [[推理系统]] — 上位概念
- [[EPD分离架构]] — 三阶段分离部署与 EPD 思路
- [[确定性]] — 批次无关确定性推理
- [[昇腾]] / [[NVIDIA]] — 硬件适配平台
- [[字节跳动]] — 字节在推理基础设施上的同类开源动作参照
- [[摘要-deepinfer-deepseek开源推理框架]] — 来源
