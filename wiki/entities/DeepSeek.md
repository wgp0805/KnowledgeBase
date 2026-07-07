---
title: "DeepSeek"
type: entity
tags: [AI, 模型, 公司]
sources: [raw/01-articles/推荐一款DeepSeek V4 编程神器！.md, raw/01-articles/Ollama+DeepSeek本地部署（新人必看）.md, raw/01-articles/国产大模型跑分一个比一个高，到底谁能真的干活？.md, raw/01-articles/DeepSeek、Gemini、Qwen、Step 3.7 Flash实测，谁才是国产黑马？.md]
last_updated: 2026-06-30
---

## 定义
深度求索（DeepSeek）推出的 AI 大语言模型系列，以高性价比和长上下文能力著称。

## 关键信息

### 模型系列
- **DeepSeek V4**：最新主力模型，支持 Agent 编程场景
- **deepseek-v4-pro**：Pro 版本，用于 DeepSeek TUI 等工具的高强度推理任务
- **DeepSeek-R1**：开源 Transformer 大语言模型，128K 长文本上下文，代码生成和数学推理表现出色。支持 1.5B/7B/8B/14B 等全尺寸版本，可通过 [[Ollama]] 本地部署

### 性能与成本
- 处理 200 万+ token 仅需不到 2 元人民币，性价比极高
- 输出速度快，适合交互式编程场景

### 实战表现（liuxin 2026-06 横评，详见 [[摘要-国产大模型实战横评]]）

| 场景 | 表现 |
|------|------|
| **Django 大型代码库 Bug 修复** | 错指 `resolvers.py`，与 [[Kimi]] 反应高度相似，需提示后才正确修复 |
| **3D 城市躲避游戏（Three.js）** | ⭐ **速度第一**、效果最好；构建密集街区"水泥森林"；车辆碰撞抖动+变色特效细致；偶发玩家初始位置被障碍物卡住的小 Bug；车辆有时互相穿模 |
| **英伟达年报 PDF 问答** | 总体表现好；表格定位略粗（与 [[Kimi]] 都找到了粗略表格，而非 [[MiniMax]] 找到的最精确表格） |

### 综合定位
代码"写得快、写得老道"，3D 游戏视觉呈现最佳；在 Bug 定位精度上略弱于 [[MiniMax]] M3。

### Flash 模型 Agent 任务横评
[[摘要-step-3-7-flash-agent横评]] 中，DeepSeek V4 Flash 在从零搭建开发者日志站任务中成本最低、可一轮交付可用成品，但编译过程中出现 3 次错误并自行修复。文章认为 DeepSeek 的单次 Token 成本优势明显，但在 Agent 场景下还需要把工具调用失败、代码错误返工和人工介入一起计入综合成本。

## 关联连接
- [[DeepSeekTUI]] — 基于 DeepSeek V4 的终端编程智能体
- [[Ollama]] — 本地部署 DeepSeek 模型
- [[AICoding]] — AI 编程范式
- [[摘要-Ollama+DeepSeek本地部署]] — Ollama 本地部署 R1 教程
- [[摘要-国产大模型实战横评]] — 来源（2026-06 横评）
- [[摘要-step-3-7-flash-agent横评]] — 来源（Flash 模型 Agent 任务横评）
- [[Step3Flash]] — 横评对比模型
- [[Qwen]] — 横评对比模型
- [[Kimi]] — 同期国产对手
- [[MiniMax]] — 同期国产对手
- [[GLM]] — 同期国产对手
- [[摘要-如何在Spring-Boot中无缝集成LangChain4j]] — LangChain4j 提供 Spring Boot Sta…
