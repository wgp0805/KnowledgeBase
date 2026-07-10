---
title: "poetry_dataset"
type: entity
tags: [开源项目, LLM微调, 诗词生成, GitHub]
sources: [raw/01-articles/2026-07-09-开源诗词数据集poetry_dataset｜Mac本地微调诗词大模型全方案，配套诗词检索站shi-ci.cn - Java码界探秘.md]
last_updated: 2026-07-10
---

## 定义

`poetry_dataset` 是博客园作者 daichangya 开源的面向 Apple Silicon 用户的古诗词大模型本地微调数据集与工具集，提供清洗完毕的训练数据、MLX 格式转换脚本和平仄校验工具，支持 Qwen2.5 系列模型在 16GB Mac 上完成 LoRA 微调。

## 关键信息

### 开源地址
- GitHub：<https://github.com/daichangya/poetry_dataset>
- 配套站点：<https://www.shi-ci.cn>

### 项目结构
- `poetry_train.json` / `poetry_val.json`：原始诗词训练语料
- `mlx_data/train.jsonl` / `mlx_data/valid.jsonl`：MLX 格式对话训练集
- `build_dataset.py`：批量构建诗词训练数据集
- `convert_to_mlx.py`：通用文本转换为 MLX 标准训练格式
- `pingze_check.py`：古诗词平仄、句式简易校验工具

### 训练流程
1. `conda create -n poetry python=3.10` → `pip install mlx-lm pypinyin`
2. `git clone` 项目
3. `mlx_lm.convert` 量化底座模型（4bit）
4. `mlx_lm.lora` 启动 LoRA 微调（`--iters 1000`）
5. `mlx_lm.generate` 生成诗词测试
6. `python pingze_check.py` 格律校验

### 常见问题
- 内存不足：调低 batch-size、减少微调层数、开启 4bit 量化
- HuggingFace 下载慢：配置 `HF_ENDPOINT=https://hf-mirror.com`
- 生成诗词重复度过高：降低迭代次数、监控验证集 loss 避免过拟合

## 关联连接

- [[Qwen]] — 支持的底座模型（Qwen2.5-1.5B/3B）
- [[LoRA]] — 微调方法
- [[shi-ci.cn]] — 配套诗词资源站
- [[摘要-开源诗词数据集poetry_dataset]] — 来源摘要
