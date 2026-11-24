---
title: "Apple"
type: entity
tags: [公司, 硬件, 操作系统, AI]
sources: ["raw/09-archive/2026-11-22 - 黑苹果续作：让普通PC运行macOS 27系统.md"]
last_updated: 2026-11-24
---

## 定义
Apple（苹果公司）是消费电子与操作系统厂商，自研 M 系列芯片（Apple Silicon，ARM64 架构）并围绕其构建 macOS、iOS 生态；在 AI 领域以端侧模型、私有云计算与开发者工具链参与竞争。

## 关键信息
- **架构迁移**：从 Intel x86 迁移到自研 Apple Silicon（ARM64），macOS 27 的官方兼容列表已全部是 M 芯片机型，Intel 版 macOS 停止更新
- **兼容层**：Rosetta 2 把 x86 应用翻译到 ARM64 运行，是"指令翻译"最成功的商业案例之一
- **对第三方硬件的影响**：官方不支持非苹果硬件，[[黑苹果]] 路线的合法性来自 EULA 以外的技术手段但违反许可协议；这也催生了 [[Stela]] 这类"逆向翻译 ARM64 macOS 到 x86"的实验
- **生态特征**：软硬一体带来高度优化的图形栈（Metal）与功耗控制，代价是平台锁定与可编程性限制
- **AI 侧**：端侧推理与隐私计算是其差异化叙事，模型能力与生态开放度常被拿来与 [[OpenAI]]、[[Google]] 对比

## 关联连接
- [[Stela]] — 试图在 x86 PC 上跑 Apple Silicon 版 macOS 的项目
- [[黑苹果]] — 非苹果硬件运行 macOS 的旧路线
- [[指令集翻译]] — Rosetta 2 与 Stela 同属的机制
- [[Mesa]] — 开源图形栈（与 Metal 对照）
- [[OpenAI]] / [[Google]] — AI 竞争对照
- [[摘要-黑苹果续作-stela运行macos27]] — 来源
