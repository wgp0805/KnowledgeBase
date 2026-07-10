---
title: "摘要-开源诗词数据集poetry_dataset"
type: source
tags: [来源, LLM微调, 诗词生成, MLX, LoRA]
sources: [raw/01-articles/2026-07-09-开源诗词数据集poetry_dataset｜Mac本地微调诗词大模型全方案，配套诗词检索站shi-ci.cn - Java码界探秘.md]
last_updated: 2026-07-10
---

## 核心摘要

博客园作者 daichangya 分享的面向 Apple Silicon 用户的古诗词大模型本地微调全方案。核心项目 `poetry_dataset`（GitHub 开源）内置清洗完毕的诗词训练数据集、MLX 格式转换脚本和平仄校验工具，依托苹果 MLX 框架，16GB 内存 Mac 即可完成 Qwen2.5-1.5B/3B 的 LoRA 微调，无需 CUDA、数据不上云。配套诗词资源站 shi-ci.cn 提供数十万古诗词库（含原文/拼音/译文/平仄标注），可用于扩充训练集和校验模型输出的格律。文章覆盖从环境初始化（conda + mlx-lm + pypinyin）到模型量化、LoRA 训练、诗词生成测试、格律校验的完整工作流，并提供内存不足、HF 下载慢、生成重复度高等常见问题解决方案。

## 关键信息

- **底座模型**：支持 Qwen2.5-1.5B-Instruct / Qwen2.5-3B-Instruct 等主流开源底座
- **训练框架**：Apple MLX，支持 4bit 量化，完全不需要 CUDA 环境
- **数据脚本**：build_dataset.py（构建训练集）、convert_to_mlx.py（转换 MLX 格式）、pingze_check.py（平仄校验）
- **配套站点**：shi-ci.cn（无广告、数十万诗词、支持全文检索与标准化文本导出）

## 关联连接

- [[Qwen]] — 底座模型（Qwen2.5 系列）
- [[LoRA]] — 微调方法
- [[poetry_dataset]] — 开源项目实体
- [[shi-ci.cn]] — 配套诗词资源站
