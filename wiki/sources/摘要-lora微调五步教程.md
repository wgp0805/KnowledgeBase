---
title: "摘要-lora微调五步教程"
type: source
tags: [来源, 原始文件, LoRA, 微调, LLaMA-Factory]
sources: [raw/09-archive/2026-10-05-小白也能上手的 LoRA 微调：五步走通训练到落地.md]
last_updated: 2026-10-08
---

## 核心摘要
产品经理用 LLaMA-Factory 对 Qwen2.5-0.5B-Instruct 做 LoRA 微调并接入 Dify，全流程成本不到 6 元。五步：①租算力——选预装 LLaMA-Factory 镜像的 50 系显卡实例，JupyterLab 打开 Train/Chat 标签页（别自己配环境，用现成镜像开箱即用）；②准备数据——600 条猫娘角色问答（input/Completion result 两列），清理空内容、重复与错误样本，先定"统一语气或格式"的具体目标；③选模型和参数——基座 Qwen2.5-0.5B-Instruct（小参数试错成本低），训练阶段 SFT、微调方式 LoRA、轮次 3、留 10% 数据验证、保存间隔 20，训练前先在 Chat 页记录原模型回答做对比基线；④训练与检查——检查 LoRA 权重与配置文件是否保存，加载"原模型+LoRA 权重"用训练前后同题对比+新增未见问题，重点看语气格式/内容合理性/多轮稳定性，**损失下降只能作参考，实际回答必须人工检查**；⑤接入 Agent——API 工具加载基座+LoRA 启动 OpenAI 兼容服务，记下 Base URL/API Key/model_id 三项，在 Dify 模型供应商选 OpenAI-API-compatible 填入即对话测试，测完关闭实例核对计费。

## 关联连接
- [[LoRA]] — 核心微调方法
- [[SFT]] — 训练阶段
- [[LlamaFactory]] — 微调框架
- [[Dify]] — 落地接入平台
- [[Qwen]] — 基座模型系列
- [[摘要-千问lora-sft微调指南]] — 同主题的进阶指南
