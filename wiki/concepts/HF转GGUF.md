---
title: "HF转GGUF"
type: concept
tags: [模型转换, 格式转换, llama.cpp, 本地部署]
sources: [raw/01-articles/2026-08-27-Ubuntu 大模型HF转GGUF全流程实践指南 - lyshark.md]
last_updated: 2026-08-28
---

## 定义
HF 转 GGUF 是将 Hugging Face 原生格式模型转换为 llama.cpp 专用 GGUF 容器格式的过程。仅做文件格式翻译和封装，不压缩、不损失精度。

## 关键信息
### 核心区分
| 步骤 | 工具 | 作用 | 输出 |
|------|------|------|------|
| **HF→GGUF** | `convert_hf_to_gguf.py` | 格式翻译、封装 | `f16.gguf` 全精度中间文件 |
| **GGUF量化** | `llama-quantize` | 真正权重压缩 | `Q4_K_M.gguf` 量化可用模型 |

### 转换命令
```bash
python convert_hf_to_gguf.py ./HF模型路径 \
  --outtype f16 \
  --outfile ./models/模型名-f16.gguf \
  --no-lazy
```
- `--outtype f16`：输出 FP16 全精度
- `--no-lazy`：禁用懒加载，确保完整转换

### 常见误区
新手易混淆"格式转换"与"权重量化"：GGUF 是容器格式，可存全精度也可存量化权重；量化是单独的压缩步骤。

## 关联连接
- [[摘要-ubuntu-hf转gguf全流程指南]] — 来源
- [[llama.cpp]] — 提供转换脚本
- [[GGUF]] — 目标容器格式
- [[模型量化]] — 后续压缩步骤
- [[HF格式]] — 源格式