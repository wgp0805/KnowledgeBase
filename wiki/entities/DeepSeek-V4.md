---
title: "DeepSeek V4"
type: entity
tags: ["DeepSeek-V4", "国产模型"]
last_updated: 2026-09-01
---

# DeepSeek V4

DeepSeek V4 是国产旗舰模型，采用 CSA/HCA 替换 MLA，优化 KV Cache。Flash 正式版仅 13B 激活参数，通过后训练在 9 项 Agent 测试中全面碾压 49B 的 Pro 预览版——证明后训练比参数量更重要。灰度曝光后热血沸腾。

## V4.1-Flash 升级与 Harness 差异化（2026-09-17，详见 [[DeepSeek-V4.1-Flash]]）
升级版 V4.1-Flash 技术文件指出：大模型很少只跑在固定 Harness 里，不同脚手架的系统提示词/工具定义/上下文管理/交互协议都会影响结果。两个反常识发现：
- **DSH Minimal 模式** 在两项测试中都高于 Standard 和 PTC（功能更多更复杂 ≠ 成功率更高）
- **Claude Code 或 Codex** 接 DeepSeek-V4.1-Flash，开箱即用接近峰值

[[老章]] 用 [[SimonWillison|Simon Willison]] 的 Space Invaders 原题横评四种 Harness，综合排名：① Claude Code 9.2 分 ② Pi Agent 8.9 分 ③ DSH 标准 8.7 分 ④ DSH 极简 7.2 分（失败）。详见 [[摘要-deepseek-v4-1-flash-harness横评]]。

## 关联连接
[[CSA]], [[HCA]], [[MLA]], [[KVCache]], [[MoE]], [[后训练]], [[沉默王二]], [[DeepSeek-V4.1-Flash]], [[摘要-deepseek-v4-1-flash-harness横评]], [[老章]], [[ClaudeCode]], [[DeepSeekHarness]], [[Harness差异化]]
