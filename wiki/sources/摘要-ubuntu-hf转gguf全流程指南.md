---
title: "摘要-ubuntu-hf转gguf全流程指南"
type: source
tags: [来源, 原始文件, llama.cpp, GGUF, 模型量化, 本地部署]
sources: [raw/01-articles/2026-08-27-Ubuntu 大模型HF转GGUF全流程实践指南 - lyshark.md]
last_updated: 2026-08-28
---

## 核心摘要
lyshark 基于 Ubuntu 26.04 纯 CPU 无 CUDA 环境，完整演示基于 llama.cpp 实现 HF 原始模型转换 GGUF 格式与 CPU 量化的落地实操流程。以 Qwen2-0.5B-Instruct 为案例，涵盖：Swap 分区配置（8G）、系统依赖安装、llama.cpp 源码编译、Python 虚拟环境部署、HF 模型下载、HF 转 GGUF 格式封装、Q4_K_M 等级量化。核心区分：HF→GGUF 仅做格式翻译不压缩（输出 f16.gguf 全精度中间文件），GGUF 量化才是真正权重压缩（FP16→4bit/5bit）。GGUF 是文件容器格式非量化格式，可存放全精度和量化精度权重。

## 关联连接
- [[llama.cpp]] — 核心推理引擎与转换工具链
- [[GGUF]] — 模型容器格式
- [[HF转GGUF]] — 格式转换流程
- [[模型量化]] — 权重压缩技术
- [[Q4_K_M]] — 4bit 量化等级
- [[Qwen2]] — 案例模型
- [[ModelScope]] — 模型下载源
- [[Swap分区]] — 内存不足时的虚拟内存方案
- [[本地部署]] — 纯 CPU 推理场景