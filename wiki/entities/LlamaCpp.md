---
title: "LlamaCpp"
type: entity
tags: [工具, 推理引擎, GGUF, 本地部署, C++]
sources: [raw/01-articles/抖音视频内容整理_人类智力基线与2张显卡.md]
last_updated: 2026-08-18
---

## 定义
llama.cpp 是开源的 C++ LLM 推理引擎，提供 `llama-server` HTTP API 端点，是本地部署大模型最常用的推理后端之一。通过 OpenAI 兼容 API 暴露本地模型，让 [[DeepSeekHarness]]、[[OpenClaw]]、[[ClaudeCode]] 等上层 Agent 框架可以无缝接入本地模型，无需云端 API Key。

## 关键信息

### 核心能力
- 加载 GGUF 量化模型权重
- 提供 OpenAI 兼容的 HTTP API 端点（`/v1/chat/completions` 等）
- 支持多卡 [[TensorSplit]] 分摊权重和 KV cache
- 支持 KV cache 量化（q8_0/q4_0 等）减小显存占用
- 支持投机解码（MTP / draft model）
- 支持多模态模型（通过 `--mmproj` 加载视觉投影器）

### 关键启动参数（本地 Agent 场景）
| 参数 | 作用 |
|------|------|
| `-m <model.gguf>` | 加载主模型权重 |
| `--mmproj <mmproj.gguf>` | 加载多模态视觉投影器 |
| `-c 262144` | 上下文长度（256K） |
| `-ngl 999` | 全部层 offload 到 GPU |
| `--tensor-split 1,1` | 多卡权重/KV cache 分摊比例 |
| `--cache-type-k/v q8_0` | KV cache 量化（体积减半） |
| `--spec-type draft-mtp` | 用模型内置 MTP 头做投机解码 |
| `--flash-attn on` | Flash Attention 加速 |
| `--fit off` | 显存装不下直接报错，不静默降级上下文 |
| `--jinja` | 用模型内置聊天模板，工具调用必开 |
| `--cont-batching` | 连续批处理 |
| `--batch-size 2048` | 批处理大小 |
| `--ubatch-size 512` | micro-batch 大小 |

### 实测性能（2026-08-18，2× RTX 5090 + Qwen3.8-27B Q4）
- 生成速度：66 tokens/sec（波动 44-100）
- 预填充速度：2,500-2,900 tokens/sec
- 首 Token：平均 2.9 秒
- 启动时间：约 10 秒
- 缓存命中率：98%

### 与同类工具对比
- 与 [[Ollama]]：Ollama 底层即 llama.cpp，但封装了模型管理和 CLI 体验；llama.cpp 直接暴露更底层的参数控制，适合调优
- 与 vLLM：vLLM 偏服务端高吞吐，llama.cpp 偏本地端灵活配置

## 关联连接
- [[摘要-人类智力基线与2张显卡]] — 来源
- [[Qwen3.8-27B]] — 推理对象
- [[RTX5090]] — 运行硬件
- [[DeepSeekHarness]] — 上游 Agent 框架
- [[TensorSplit]] — 多卡分摊参数
- [[GGUF量化]] — 模型权重格式
- [[本地Agent工作站]] — 完整方案
- [[Ollama]] — 同类封装工具
