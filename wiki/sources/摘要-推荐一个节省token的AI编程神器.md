---
title: "推荐一个节省token的AI编程神器"
type: source
tags: [AI, Agent, Pi, token优化, 终端编程, TypeScript扩展]
sources: [raw/09-archive/推荐一个节省token的AI编程神器！.md]
last_updated: 2026-08-12
---

## 核心摘要

Pi 是由 Mario Zechner（libGDX 作者）开发的极简终端编码代理，GitHub 87.3k Stars。其核心设计哲学是**用最少的 token 完成编码任务**——系统提示词仅约 1000 token（Claude Code 约 14,000），核心工具仅 6 个（read/write/edit/bash/glob/grep），通过 TypeScript 扩展、Skills 和提示词模板按需补齐功能，而非预置庞大工具集。

## 关键要点

### 极简设计哲学
- **系统提示词 ~1000 token**：对比 Claude Code ~14,000 token，每次对话节省约 93% 的系统提示词开销
- **核心工具仅 6 个**：read、write、edit、bash、glob、grep，其余能力通过扩展按需加载
- **支持 15+ Provider**：包括 Anthropic、OpenAI、DeepSeek、Qwen、GLM 等主流模型，用户可按任务选模型

### 三层扩展体系
1. **TypeScript 扩展**：用 TS 编写自定义工具和命令，运行在 Deno 运行时中
2. **Skills**：类似 Claude Code 的 Skill 机制，按需加载领域知识
3. **提示词模板**：预置常用提示词，减少重复输入

### 与 Claude Code 的对比
| 维度 | Pi | Claude Code |
|------|-----|-------------|
| 系统提示词 | ~1,000 token | ~14,000 token |
| 核心工具数 | 6 | 15+ |
| 扩展语言 | TypeScript (Deno) | 原生 |
| Provider 支持 | 15+ | Anthropic 为主 |
| 设计哲学 | 极简按需 | 功能完备 |

### 适用人群
- 追求 token 成本最优化的开发者
- 需要多模型切换的用户
- 喜欢极简工具链、愿意自行配置扩展的高手

## 关联连接
- [[PiAgent]] — Pi Agent 实体页面（已有，含工程化能力详解）
- [[AgentHarness]] — 编码代理 Harness 概念
- [[ContextEngineering]] — 上下文工程，Pi 的极简提示词是该理念的极致实践
- [[Token估算]] — Token 成本控制相关概念
- [[ClaudeCode]] — 对比对象
- [[Anthropic]] — Pi 支持的 Provider 之一
- [[DeepSeek]] — Pi 支持的 Provider 之一
- [[AICoding]] — AI 辅助编程范式
