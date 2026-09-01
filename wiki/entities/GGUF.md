---
title: "GGUF"
type: entity
tags: [模型格式, 容器格式, llama.cpp, 量化]
sources: [raw/01-articles/2026-08-27-Ubuntu 大模型HF转GGUF全流程实践指南 - lyshark.md]
last_updated: 2026-08-28
---

## 定义
GGUF（GPT-GGML Unified Format）是 llama.cpp 专用的模型容器格式，非量化格式。可存放全精度（FP16/f16）和量化精度（Q4_K_M 等）权重。取代旧版 GGML 格式，支持更丰富的元数据、张量命名、架构标识。

## 关键信息
- **核心定位**：模型文件容器格式，非量化格式
- **存储内容**：FP16 全精度权重、量化权重、词表、元数据、架构信息
- **兼容性**：llama.cpp 原生支持，llama-server 直接加载
- **文件命名约定**：`model-f16.gguf`（全精度中间文件）、`model-Q4_K_M.gguf`（量化可用模型）
- **对比优势**：比 GGML 支持更多架构、更好的元数据、更高效的加载

## 关联连接
- [[摘要-ubuntu-hf转gguf全流程指南]] — 来源
- [[llama.cpp]] — 核心工具链
- [[HF转GGUF]] — 格式转换流程
- [[模型量化]] — 量化后的存储格式
- [[Q4_K_M]] — 常用量化等级
- [[Qwen2]] — 存储案例模型