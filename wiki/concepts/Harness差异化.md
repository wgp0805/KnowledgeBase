---
title: "Harness差异化"
type: concept
tags: [Harness, Agent, 模型表现, 脚手架, 上下文管理]
sources: [raw/01-articles/2026-09-16-DeepSeek-V4.1-Flash 的最佳 Harness 搭档，我觉得可能是 Claude Code.md]
last_updated: 2026-09-17
---

## 定义
Harness 差异化指同一模型在不同 Harness（脚手架）下表现差异巨大的现象。不同脚手架的系统提示词、工具定义、上下文管理、交互协议都会影响模型跑出来的结果——甚至出现"功能更多更复杂反而成功率更低"的反常识现象。

## 关键信息

### DeepSeek 技术文件核心观点
大模型很少只跑在一个固定 Harness 里，不同脚手架的：
- 系统提示词
- 工具定义
- 上下文管理
- 交互协议

都会影响结果。

### 反常识发现
- **DSH Minimal 模式** 在两项测试中都高于 Standard 和 PTC——功能更多、流程更复杂，并没有换来更高的成功率
- 极简模式省 84.5% Token 但缺乏全局视野，总用时全场最慢（40 分钟）且最终失败

### Space Invaders 横评（[[老章]]，[[SimonWillison|Simon Willison]] 原题）
四种 Harness 综合排名：① Claude Code 9.2 ② Pi Agent 8.9 ③ DSH 标准 8.7 ④ DSH 极简 7.2（失败）

| Harness | 用时 | Token | TPS | 结果 | 定位 |
|---------|------|-------|-----|------|------|
| Claude Code | 9分34秒 | 3.0M | 205.5 | 完成 | 生产级 ROI 最高 |
| Pi Agent | 36分09秒 | 9.7M | - | 完成 | 探索性任务利器 |
| DSH 标准 | 8分54秒 | 4.2M | 275 | 完成 | 高吞吐日常开发 |
| DSH 极简 | 40分04秒 | 1.5M | 295 | **失败** | Token 极致但有代价 |

### 各维度差异
- **交付质量**：Claude Code 最懂原版，细节齐全；Pi Agent 视觉最强
- **Token 消耗**：Claude Code 仅用 Pi Agent 约 1/3 的 Token
- **耗时**：DSH 标准最快（8分54秒），DSH 极简最慢（40分04秒）
- **辅助使用**：Claude Code 和 DSH Standard 的操作按钮标注最好

### 关键启示
**如果你觉得某个模型不太好，或许可以换一个 Harness。** 同一模型在不同 Harness 下表现差异巨大，Harness 选择直接影响交付质量、Token 消耗、耗时、辅助使用友好度。

## 关联连接
- [[DeepSeek-V4.1-Flash]] — 被测模型
- [[ClaudeCode]] — 综合排名第一的 Harness
- [[DeepSeekHarness]] — DSH 标准/极简模式
- [[Pi]] — Pi Agent
- [[老章]] — 横评作者
- [[SimonWillison]] — Space Invaders 原题作者
- [[摘要-deepseek-v4-1-flash-harness横评]] — 来源
- [[HarnessEngineering]] — Harness 工程概念
- [[TokenEfficiency]] — Token 效率概念
