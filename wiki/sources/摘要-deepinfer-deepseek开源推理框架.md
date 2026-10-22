---
title: "摘要-deepinfer-deepseek开源推理框架"
type: source
tags: [来源, 大模型推理, 开源, DeepSeek]
sources: [raw/01-articles/2026-10-21 - 真正的 OpenAI！DeepSeek 开源内部推理框架 DeepInfer。.md]
last_updated: 2026-10-22
---

## 核心摘要
DeepSeek 首次开源支撑自家线上亿级流量的生产级推理引擎 [[DeepInfer]]，以及用 Rust 编写的编解码组件 [[DeepSeekRecipe]]。DeepInfer 基于 vLLM 演进并吸收 SGLang、TensorRT-LLM 思路，原生兼容英伟达 SM100 架构 GPU 与华为昇腾 950 NPU；据《DeepSeek V4.1 Flash 大规模推理部署实践》报告，单集群日吞吐高达 155 万亿 Tokens，KV Cache 保留时间拉长至 72 小时以上，开源不到 24 小时 GitHub Star 突破 1.46 万。

deepseek-recipe 的价值在于把 Chat Completions API、Responses API、Messages API 统一转换为标准对话格式，并用特殊 Token 边界匹配解决"提示词注入"（把 `<｜User｜>`、`</think>` 编码成普通 Token）与"分段并行分词"（沿特殊 Token 边界多线程并行编码）两大难题；输出端用基于 KMP 算法的状态机做跨 Chunk 流式解析，工具名解析完即返回、参数逐段输出 JSON 片段。

DeepInfer 的四项核心工程设计：**三阶段分离部署**（视觉编码器放最便宜单卡、Prefill 放 8 卡做小规模专家并行、Decode 放 64~128 卡超节点做 Wide-EP，配合 EPLB 动态负载均衡）；**100 PiB 独立分布式存储 + SWA Bounded Replay**（基于自研 3FS，峰值聚合读带宽 10 TiB/s，128 Token 分页块缓存全量落盘，SWA KVCache 只留内存 180 秒、线上命中率超 98%，未命中时只重算最近 128 Token 使预填充计算量降近一半）；**DSpark 置信度投机解码**（置信度预测头只把验证算力分配给收益最高的前缀子集，相比固定验证 5 个 Token 吞吐提升 6%）；**零开销异步批调度**（GPU 执行第 N 步时 CPU 并行做第 N+1 步调度与第 N-1 步后处理，GPU 全程零空闲）。

对开发者的三点红利：自建模型网关可直接安装 deepseek-recipe 接管多协议转换与流式工具调用解析；KV Cache 落盘 72 小时让"需人工审批或跨天恢复"的 Agent 暂停两天仍能命中服务端缓存；开启 `DEEPINFER_BATCH_INVARIANT=1` 批次无关确定性推理后相同输入永远产出相同结果。

## 关键信息
- **开源二元结构**：推理引擎（DeepInfer）+ 编解码组件（deepseek-recipe），后者是很多私有化部署"权重一样但深度思考/工具调用不如官方 API 稳定"的病根所在
- **定位对比**：过去开源给的是"发动机图纸和散装零件"（FlashMLA / DeepGEMM / DeepEP / TileLang 等底层算子），本次直接交出"整车生产线"
- **硬件覆盖**：英伟达 SM100 架构 GPU + 华为昇腾 950 NPU 两大平台
- **实践建议**：克隆 deepseek-recipe 跑自带编解码可视化网页，重点读 KMP 状态机做跨数据块流式工具参数解析的源码

## 关联连接
- [[DeepInfer]] — 生产级推理引擎主体
- [[DeepSeekRecipe]] — Rust 编解码组件
- [[DeepSeek]] — 开源方
- [[DeepSeek-V4.1-Flash]] — 部署报告对应的模型
- [[KV Cache]] — 72 小时磁盘级 KV 缓存与 SWA Bounded Replay
- [[投机解码]] — DSpark 置信度投机解码
- [[推理系统]] — 推理软件栈定位
- [[昇腾]] — 昇腾 950 NPU 适配
- [[NVIDIA]] — SM100 架构适配
- [[字节跳动]] — 字节在推理基础设施上的同类开源动作参照
