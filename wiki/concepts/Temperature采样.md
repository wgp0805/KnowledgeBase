---
title: "Temperature采样"
type: concept
tags: [概念, LLM, 采样, 参数, Temperature]
sources: [raw/01-articles/DeepSeek API 中的 Temperature 有什么用？.md]
last_updated: 2026-11-09
---

## 定义
Temperature 采样是 LLM 生成阶段的参数体系：模型给词表约 12.8 万个候选词打分（Logits），`temperature` 负责**调整候选词之间的概率差距**（先除以 temperature 再 Softmax），`top_p`（核采样）负责**决定哪些候选词有资格参与抽签**（按累积概率截断长尾）。两者按先后顺序起作用，后一个的效果取决于前一个的结果。

## 关键信息
- **Temperature 机制**：logits 除以 temperature 再 Softmax。低（0.1）分差拉大、第一名概率逼近 100%；高（1.5）分差缩小、内容更多样；0.0 时直接选分数最高词
- **Top-K 缺点**：固定保留前 K 个——答案确定时仍留多余候选，开放内容时又过滤掉合适词
- **Top-P（核采样）**：概率从高到低累加达到 top_p 即停、扔掉后面，候选概率按比例放大重新=100%；top_p=0.9 时第一名已 92% 只留 1 个词
- **协同建议**：先改一个、另一个保持默认 1.0（便于看出谁起作用）；temperature 调高会让同样 top_p 保留更多词（如累加到第 30 个）
- **官方场景推荐值（DeepSeek）**：写代码/解数学题 0.0、数据抽取与分析 1.0、日常对话/翻译 1.3、创意写作 1.5
- **各 Harness 处理（2026-11）**：DeepSeek 思考模式忽略 temperature、top_p 看模型（Flash 0.95-1.0 / Pro 固定 0.95 或 1.0）；**Codex 主对话无 temperature/top_p 字段**；**Claude Code 思考模式省略 temperature**；**DSH 适配器不传 top_p、只保留可选 temperature、自动审批写死 0**

## 关联连接
- [[LLM]] — 温度采样与幻觉章节
- [[摘要-deepseek-temperature]] — 来源
- [[沉默王二]] — 作者
- [[DeepSeek]] — API 提供方
- [[ClaudeCode]] — 处理对照
- [[Codex]] — 处理对照
- [[DeepSeekHarness]] — 处理对照
