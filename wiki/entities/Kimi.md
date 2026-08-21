---
title: "Kimi"
type: entity
tags: [AI, 模型, 月之暗面]
sources: [raw/09-archive/国产大模型跑分一个比一个高，到底谁能真的干活？.md, raw/01-articles/强模型时代，删掉SuperpowersAI编程工作流到底该怎么选.md]
last_updated: 2026-08-21
---

## 定义
月之暗面（Moonshot AI）推出的国产大语言模型系列，以长上下文和文档处理能力著称。

## 关键信息

### 主力版本
- **Kimi 2.7**（2026 年）：当前主力版本，对标 [[DeepSeek]] V4 Pro、[[MiniMax]] M3，配备 1M 级上下文
- **Kimi K3**：被 [[摘要-强模型时代删掉Superpowers该怎么选]] 列为"强模型"代表之一（与 GPT-5.6、Fable-5 并列），原生能力已具备规划/子 Agent/Review/测试，适合搭配轻量 Skill 工作流（详见 [[强模型时代工作流选型]]）

### 实战表现（liuxin 2026-06 横评，详见 [[摘要-国产大模型实战横评]]）

| 场景 | 表现 |
|------|------|
| **Django 大型代码库 Bug 修复** | 错指 `resolvers.py`，需提示才正确修复（与 DeepSeek 反应相似） |
| **3D 城市躲避游戏（Three.js）** | 一次跑通，街区空旷、建筑错落、玩法丝滑；开场存在"上下键反向" Bug，提示后修复；角色形象、道路质感、垃圾桶/长椅/路灯偏简陋 |
| **英伟达年报 PDF 问答** | 总体表现好，能完成多步计算（如 CAGR）；表格定位略粗（与 DeepSeek 类似找到了粗略表格而非最精确表格） |

### 综合定位
中规中矩、可用，但在 Bug 定位精度、3D 游戏效果细节方面略弱于 DeepSeek V4 Pro 和 MiniMax M3。

## 关联连接
- [[摘要-国产大模型实战横评]] — 来源
- [[DeepSeek]] — 同期国产对手
- [[MiniMax]] — 同期国产对手
- [[GLM]] — 同期国产对手
- [[AICoding]] — 应用范式
