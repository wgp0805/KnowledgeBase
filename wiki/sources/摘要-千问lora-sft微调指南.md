---
title: "摘要-千问lora-sft微调指南"
type: source
tags: [Qwen, LoRA, SFT, 微调, 大模型, ChatML, PEFT, HuggingFace]
sources: [raw/01-articles/2026-09-06-千问大模型二次LoRA‑SFT指令微调指南 - lyshark.md]
last_updated: 2026-09-07
---

## 核心摘要

lyshark 基于 Ubuntu 22.04 + RTX 4090 24GB 环境，选用 Qwen3.5-0.8B-Instruct 指令模型，完整演示二次 LoRA-SFT 微调全流程。核心观点：**指令模型二次 LoRA-SFT 微调是工程落地最优方案**——在已对齐的 Instruct 模型基础上低成本注入领域能力，规避基座从零训练的数据门槛。流程包含环境搭建、ModelScope 下载底座、ChatML 数据集制作校验、LoRA 参数配置（r=16, alpha=16, lr=1e-4）、SFTTrainer 训练（40 steps, 144 秒）、效果验证、权重合并导出完整模型。文章强调 `apply_chat_template` 必须使用（手动拼接 `<|im_start|>` 极易格式错误）、`pad_token` 须设为 `eos_token`、`padding_side=right`。

## 关键信息

### 两种微调模式
1. **Base 预训练基座从零 SFT**：消耗算力大，需人工构建对话格式，一般不用
2. **Instruct 指令模型二次 LoRA-SFT**（本文核心）：在已 SFT+DPO/RLHF 对齐的模型上注入领域能力，低成本，最优方案
- 判别方法：模型名带 `-Base` 后缀为裸基座；目录含 `chat_template.jinja` 为 Instruct 模型

### LoRA vs QLoRA
| 项目 | LoRA | QLoRA |
|------|------|-------|
| 核心机制 | 低秩适配器 | 低秩适配器 + INT4/INT8 权重量化 |
| 主干精度 | FP16/BF16 | INT4/INT8 量化冻结 |
| 显存消耗 | 较低 | 更低 |
| 精度损失 | 几乎无 | 轻微量化损失 |
| 适用场景 | 显存≥24GB，8B-14B | 显存受限，27B+，消费级显卡 |

- 8B 模型显存 >24GB 优先 LoRA；14B/27B 或显存受限用 QLoRA 4 比特量化
- 本文 Qwen3.5-0.8B 体量小，直接用 LoRA

### 环境
- Ubuntu 22.04.5 LTS，torch 2.13.0 + CUDA 12.8.1 + Python 3.10.12
- NVIDIA RTX 4090 24GB，驱动 ≥570.133.07
- 依赖：torch/transformers/peft/trl/datasets/accelerate/bitsandbytes/wandb/modelscope

### ChatML 数据集格式
- JSON 数组，每条样本含 `conversation` 数组（多轮对话）
- 角色仅允许 `system`/`user`/`assistant`
- **必须用 `apply_chat_template` 渲染**，不要手动拼接 `<|im_start|>` 标签
- 真实业务建议扩充到几百~几千条，太少易过拟合

### 关键配置
- `pad_token = eos_token`，`padding_side = "right"`
- LoRA: r=16, alpha=16, dropout=0.0, target_modules=[q_proj,k_proj,v_proj,o_proj,gate_proj,up_proj,down_proj]
- 训练: batch_size=2, gradient_accumulation=4, max_steps=40, lr=1e-4, warmup=10
- bf16（30 系及以上显卡支持），梯度检查点开启
- `load_best_model_at_end=True` 保存验证 loss 最优权重

### 训练结果
- trainable params: 6,389,760 (0.8421%)，all params: 758,782,784
- 40 步训练 144 秒，train_loss 2.359
- 产物：`adapter_model.safetensors`（约 25MB）+ `adapter_config.json` + checkpoint

### 权重合并
- LoRA 适配器不能直接用于 llama.cpp/GGUF 导出
- `merge_and_unload()` 将低秩矩阵与基础权重矩阵相加，输出完整独立模型
- 合并后可直接 vLLM 推理或转 GGUF

### 微调要点
- 风格迁移：200-1000 条样本；垂直领域知识增强：2000-10000 条
- 小数据集优先 `max_steps` 防过拟合；大数据集用 `num_train_epochs`（1-3 轮）
- LoRA 学习率常用 1e-4 ~ 3e-4，过大易震荡发散
- 验证集监控过拟合，`eval_loss` 不降甚至上升即为过拟合信号
- 灾难性遗忘：训练数据单一导致丢失基础能力，解决方法是混入通用对话数据

## 关联连接
- [[Qwen]] — 主实体（微调对象）
- [[LoRA]] — 核心微调方法
- [[SFT]] — 监督微调概念
- [[ChatML]] — Qwen 对话模板格式
- [[PEFT]] — HuggingFace 参数高效微调库
- [[QLoRA]] — LoRA 的量化版本
- [[ModelScope]] — 模型下载平台
- [[Transformers]] — HuggingFace 模型库
- [[摘要-transformer-训练微调范式]] — Transformer 训练-微调范式系统讲解
- [[摘要-开源诗词数据集poetry_dataset]] — Qwen2.5 本地 LoRA 微调实践
- [[摘要-ubuntu-hf转gguf全流程指南]] — llama.cpp 量化部署全流程
- [[摘要-llm后训练算法-ppo详解]] — LLM 后训练算法原理
- [[灾难性遗忘]] — 微调常见问题
- [[过拟合]] — 机器学习概念
