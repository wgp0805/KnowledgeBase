---
title: "LoRA"
type: concept
tags: [微调, 参数高效微调, PEFT, 大模型, 低秩适配]
sources:
  - raw/01-articles/2026-09-06-千问大模型二次LoRA‑SFT指令微调指南 - lyshark.md
  - raw/01-articles/抖音视频内容整理_人类智力基线与2张显卡.md
  - raw/01-articles/2026-07-09-开源诗词数据集poetry_dataset｜Mac本地微调诗词大模型全方案，配套诗词检索站shi-ci.cn - Java码界探秘.md
last_updated: 2026-09-07
---

## 定义

LoRA（Low-Rank Adaptation）是一种参数高效微调方法，通过冻结大模型主干权重，仅训练注意力层的低秩适配器矩阵，在几乎不损失模型性能的前提下大幅降低训练参数量。与 QLoRA 同属 PEFT（参数高效微调）家族，是工程落地与轻量化模型定制的最优方案。

## 关键信息

### LoRA vs QLoRA
| 项目 | LoRA | QLoRA |
|------|------|-------|
| 核心机制 | 低秩适配器 | 低秩适配器 + INT4/INT8 权重量化 |
| 主干精度 | FP16/BF16 | INT4/INT8 量化冻结 |
| 显存消耗 | 较低 | 更低 |
| 精度损失 | 几乎无 | 轻微量化损失 |
| 工程复杂度 | 低，稳定通用 | 较高，存在量化适配问题 |
| 适用场景 | 显存≥24GB，8B-14B | 显存受限，27B+，消费级显卡 |

### 选型依据
- 8B 模型显存 >24GB → 优先 LoRA
- 14B/27B 或显存受限 → QLoRA 4 比特量化
- 小模型（如 0.8B）直接用 LoRA 即可

### 核心参数
- **r（秩）**：常用 8/16/32，r 越大可训练参数越多；r 太小表达能力不足，r 太大易过拟合
- **alpha**：缩放系数，常用与 r 相同值
- **dropout**：常用 0.0
- **target_modules**：q_proj/k_proj/v_proj/o_proj/gate_proj/up_proj/down_proj
- **学习率**：常用 1e-4 ~ 3e-4，过大易震荡发散

### 两种微调模式
1. **Base 预训练基座从零 SFT**：消耗算力大，需人工构建对话格式，一般不用
2. **Instruct 指令模型二次 LoRA-SFT**（推荐）：在已 SFT+DPO/RLHF 对齐的模型上注入领域能力，低成本
- 判别：模型名带 `-Base` 为裸基座；目录含 `chat_template.jinja` 为 Instruct 模型

### 训练要点
- **必须用 `apply_chat_template`** 渲染对话，不要手动拼接 `<|im_start|>` 标签
- `pad_token = eos_token`，`padding_side = "right"`
- 小数据集优先 `max_steps` 防过拟合；大数据集用 `num_train_epochs`（1-3 轮）
- 风格迁移：200-1000 条样本；垂直领域知识增强：2000-10000 条
- `load_best_model_at_end=True` 保存验证 loss 最优权重
- bf16（30 系及以上显卡支持）比 fp16 更稳

### 权重合并
- LoRA 适配器不能直接用于 llama.cpp/GGUF 导出
- `merge_and_unload()` 将低秩矩阵与基础权重相加，输出完整独立模型
- 合并后可直接 vLLM 推理或转 GGUF
- 新版 vLLM 支持直接加载 PEFT 标准 LoRA 适配器（无需合并）

### 常见问题
- **灾难性遗忘**：训练数据单一导致丢失基础能力，解决方法是混入通用对话数据
- **过拟合**：eval_loss 不降甚至上升；输出重复、背诵训练集；减少训练步数，增加数据多样性
- **loss 下降 ≠ 微调成功**：必须在真实问题上做人工评测，同时看验证集 loss

## 关联连接
- [[SFT]] — 监督微调概念
- [[QLoRA]] — LoRA 的量化版本
- [[PEFT]] — HuggingFace 参数高效微调库
- [[Qwen]] — 常用微调对象
- [[ChatML]] — Qwen 对话模板格式
- [[ModelScope]] — 模型下载平台
- [[Transformers]] — HuggingFace 模型库
- [[摘要-千问lora-sft微调指南]] — 完整微调流程来源
- [[摘要-transformer-训练微调范式]] — Transformer 训练-微调范式
- [[摘要-开源诗词数据集poetry_dataset]] — Qwen2.5 本地 LoRA 微调实践
- [[摘要-人类智力基线与2张显卡]] — 本地 Agent 部署
- [[灾难性遗忘]] — 微调常见问题
- [[过拟合]] — 机器学习概念
