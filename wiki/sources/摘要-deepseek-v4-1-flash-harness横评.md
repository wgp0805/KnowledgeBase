---
title: "摘要-deepseek-v4-1-flash-harness横评"
type: source
tags: [DeepSeek, V4.1-Flash, Harness, Claude Code, Pi Agent, DSH, Token效率, Simon Willison]
sources: [raw/09-archive/2026-09-16-DeepSeek-V4.1-Flash 的最佳 Harness 搭档，我觉得可能是 Claude Code.md]
last_updated: 2026-09-17
---

## 核心摘要
[[DeepSeek-V4.1-Flash]] 技术文件指出：大模型很少只跑在固定 Harness 里，不同脚手架的系统提示词、工具定义、上下文管理、交互协议都不一样，跑出来的结果也有差异。官方测试显示 **DSH Minimal 模式反常识地优于 Standard 与 PTC**，而 [[ClaudeCode|Claude Code]] 或 [[Codex]] 接 DeepSeek-V4.1-Flash 开箱即用接近峰值。作者用两个任务（Astra 网页风格复刻 + [[SimonWillison|Simon Willison]] 的 Space Invaders HTML/JS）横评 Pi Agent、Claude Code、DSH 标准、DSH 极简四种 Harness，综合排名：**① Claude Code ② Pi Agent ③ DSH 标准 ④ DSH 极简**。

## 核心论点：Harness 影响模型表现
DeepSeek 技术文件提到：大模型很少只跑在一个固定 Harness 里，不同脚手架的：
- 系统提示词
- 工具定义
- 上下文管理
- 交互协议

都会影响结果。官方测试两个反常识发现：
1. **DSH Minimal 模式** 在两项测试中都高于 Standard 和 PTC 模式——功能更多、流程更复杂，并没有换来更高的成功率
2. **Claude Code 或 Codex** 接 DeepSeek-V4.1-Flash，开箱即用的水平接近峰值

## Space Invaders 横评（Simon Willison 原题）

### 四种 Harness 数据对比
| Harness | 用时 | Token 用量 | 缓存命中 | TPS | 任务结果 |
|---------|------|-----------|----------|-----|----------|
| Pi Agent | 36分09秒 | 9.7M tok | 98.9% | 未提供 | 完成 |
| DSH 标准模式 | 8分54秒 | 4.2M tok | 98% | 275 tok/s | 完成 |
| DSH 极简模式 | 40分04秒 | 1.5M tok | 99% | 295 tok/s | **失败** |
| Claude Code | 9分34秒 | 3.0M tok | 98% | 205.5 tok/s | 完成 |

### 综合评分
| 版本 | 综合分 | 评价 |
|------|--------|------|
| Claude Code | 9.2 | 最懂原版。街机竖屏/飞碟/掩体破损等细节齐全，外壳和数据面板专业。暂停后按钮仍显示 Pause；手机真机缩放有风险 |
| Pi Agent | 8.9 | 视觉效果最强。画面最大/星空/发光/爆炸/拖动操作抓人。窄屏首页标题压住计分区、底部文字重叠、难度偏高 |
| DSH 标准模式 | 8.7 | 最稳最规整。刷新和宽窄屏都正常，玩法完整克制。画面偏小；暂停页同时出现"恢复"和"开始"易困惑 |
| DSH 极简模式 | 7.2 | 首次宽屏效果很好。刷新页面后卡死只剩空战场 |

### 功能维度对比
1. **首次打开**：四个版本都正常
2. **开始/移动/射击/计分**：四个版本都能玩
3. **暂停与恢复**：功能都可用，CC 和 Standard 的提示文字有问题
4. **页面刷新**：CC/Pi/DSH Standard 正常；DSH Minimal 失败
5. **窄屏**：Standard 最稳但偏小；CC 需上下滚动；Pi 首页重叠；DSH Minimal 刷新后空白
6. **辅助使用**：CC 和 DSH Standard 的操作按钮标注最好；Pi Agent 手机操作键对键盘和读屏不友好

## Token 与耗时深度分析

### Claude Code（生产级工业落地 ROI 最高标杆）
- 交付质量、代码准确率、工程完整性均第一
- 上下文管理极其精炼：仅用 Pi Agent 约 1/3 的 Token 和 1/4 的耗时拿到全场最优效果
- 适合生产级工业落地

### Pi Agent（探索性任务利器）
- 生成效果紧随 Claude Code，工具链调用和深度推理能力强
- 代价是沉重的上下文膨胀：172 条消息、85 次工具调用
- Token 消耗全场最高（9.7M tok，约为极简模式 6.4 倍），端到端耗时 36 分钟
- 适合对质量有极致要求、对成本与耗时完全不敏感的探索性任务

### DSH 标准模式（高吞吐日常开发工具）
- 8分54秒极限速度全场领跑，TPS 高达 275 tok/s
- 执行流畅利落
- 复杂任务的逻辑闭环和细节处理弱于 CC 和 Pi
- 适合交付时效要求极高、任务复杂度适中的日常高吞吐开发

### DSH 极简模式（Token 极致但有代价）
- Token 消耗全场极致（仅 1.5M tok，比常规方案省 84.5%）
- 单次上下文被极端压榨，模型缺乏全局视野，多轮反复试探和多步反思推进
- 总用时反向拉长至 40 分钟（全场最慢），最终效果垫底

## 关键启示
**如果你觉得某个模型不太好，或许可以换一个 Harness。** 同一模型在不同 Harness 下的表现差异巨大，Harness 选择直接影响：交付质量、Token 消耗、耗时、辅助使用友好度。

## 关联连接
- [[DeepSeek-V4.1-Flash]] — 被测模型实体
- [[DeepSeek-V4]] — V4 系列
- [[ClaudeCode]] — 综合排名第一的 Harness
- [[DeepSeekHarness]] — DSH 标准与极简模式
- [[Pi]] — Pi Agent
- [[Codex]] — 官方提到开箱即用接近峰值的另一个 Harness
- [[SimonWillison]] — Space Invaders 测试原题作者
- [[HarnessEngineering]] — Harness 工程概念
- [[TokenEfficiency]] — Token 效率概念
- [[Harness差异化]] — 概念页
- [[老章]] — 文章作者
