---
title: "Q4_K_M"
type: concept
tags: [量化等级, GGUF, 4bit量化, 推荐配置]
sources: [raw/01-articles/2026-08-27-Ubuntu 大模型HF转GGUF全流程实践指南 - lyshark.md]
last_updated: 2026-08-28
---

## 定义
Q4_K_M 是 GGUF 格式中最主流的 4bit 量化等级：K-quant 量化方法、Medium 精度平衡版本。在模型体积、推理速度、生成质量三者间达到最佳平衡，是本地部署的首选量化等级。

## 关键信息
- **量化方法**：K-quant（按行/列分组量化，保留异常值）
- **精度档位**：Medium（平衡版），对比 S（Small/更小更快）、L（Large/更高精度）
- **适用场景**：纯 CPU 推理、内存受限设备、本地离线 Agent
- **体积压缩**：相对 FP16 全精度约 4 倍压缩
- **生成质量**：主观评测接近 FP16，远优于老版本 Q4_0

## 关联连接
- [[摘要-ubuntu-hf转gguf全流程指南]] — 来源
- [[模型量化]] — 所属技术
- [[GGUF]] — 存储格式
- [[llama.cpp]] — 量化工具
- [[本地部署]] — 核心场景
- [[Qwen2]] — 案例量化模型