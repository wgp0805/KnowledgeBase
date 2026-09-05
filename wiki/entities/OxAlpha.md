---
title: "OxAlpha"
type: entity
tags: [大模型, AI, 免费预览, 多模态]
sources: [raw/01-articles/“牛来”员工：你们可以在 OpenCode 爽用 Ox Alpha 模型了，1M上下文并支持视频输入（附Agent面试题）.md]
last_updated: 2026-08-24
---

## 定义
Ox Alpha 是一款免费预览大模型，主打超大上下文与多模态输入，专为 Coding 和长周期 Agent 任务优化。开发者社区昵称其为"牛来"。

## 关键信息
- **规格**：100 万 Token 上下文，支持文本、图片和视频输入，具备推理和工具调用能力
- **接入入口**（2026-08-24 时点）：
  - OpenRouter，模型 ID 为 `ox-alpha`
  - OpenCode Zen
- **定位**：免费预览模型；沉默王二提醒生产环境需为预览模型突然下线设计降级路径
- 实测案例：一句提示词生成"鹈鹕骑自行车"的 SVG 动画并用 H5 展示，效果不错

## 关联连接
- [[摘要-ox-alpha模型与agent面试题]] — 来源
- [[OpenRouter]] — 接入入口之一
- [[OpenCode]] — 通过 OpenCode Zen 可使用该模型
- [[模型指纹]] — 文章借该匿名模型引出模型识别面试题
- [[降级]] — 预览模型下线的三级降级策略
