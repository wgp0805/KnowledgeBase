---
title: "摘要-deepseek-temperature"
type: source
tags: [来源, Temperature, 采样参数, DeepSeek, 沉默王二]
sources: [raw/01-articles/DeepSeek API 中的 Temperature 有什么用？.md]
last_updated: 2026-11-09
---

## 核心摘要
沉默王二讲透 DeepSeek API 的 `temperature` 与 `top_p` 采样参数：模型给词表约 12.8 万个候选词打分（Logits），temperature 负责**调整候选词之间的概率差距**（先除以 temperature 再 Softmax），top_p 负责**决定哪些候选词有资格参与抽签**（按累积概率截断长尾）。两者按先后顺序起作用：先用 temperature 调整概率差距，再按 top_p 累加决定去留。官方场景推荐值：写代码/解数学题 0.0、数据抽取与分析 1.0、日常对话/翻译 1.3、创意写作 1.5。

## 关键信息
- **Temperature 机制**：logits 除以 temperature 再 Softmax。温度低（0.1）分差拉大、第一名概率逼近 100%（几乎每次选中）；温度高（1.5）分差缩小、各词概率更接近（内容更多样）；temperature=0.0 时直接选分数最高词
- **Top-K 的缺点**：固定保留前 K 个词——答案很确定时仍把另 49 个词留在候选（应只留 1 个）；开放式内容很多词说得通时只留 50 个又会过滤掉合适词
- **Top-P（核采样）**：按累积概率决定保留个数——概率从高到低累加，达到 top_p 即停、扔掉后面，再把候选概率按比例放大重新=100%；top_p=0.9 时若第一名已 92% 只留 1 个词，若前 15 个各 6% 就留 15 个
- **两者协同**：官方建议先改一个、另一个保持默认 1.0；因为后一个参数的效果取决于前一个结果（如 temperature 调高 1.5，同样 top_p=0.9 可能要累加到第 30 个词）
- **各 Harness 处理（2026-11）**：DeepSeek 默认开思考模式时忽略 temperature；top_p 看模型——Flash 0.95-1.0（低于 0.95 按 0.95）、Pro 忽略传入值（工具调用固定 0.95，否则 1.0）；关思考后 Flash 固定 1.0、Pro 可调。**Codex 主对话请求里没有 temperature 和 top_p 字段**。**Claude Code 开启思考模式时省略 temperature**。**DeepSeek Harness 适配器不传 top_p、只保留可选 temperature，自动权限审批写死 temperature:0**（若审批走思考模式这个 0 也不生效）

## 关联连接
- [[LLM]] — 概念（温度采样与幻觉章节）
- [[Temperature采样]] — 概念
- [[沉默王二]] — 作者
- [[DeepSeek]] — API 提供方
- [[ClaudeCode]] — temperature 处理对照
- [[Codex]] — temperature 处理对照
- [[DeepSeekHarness]] — temperature 处理对照
