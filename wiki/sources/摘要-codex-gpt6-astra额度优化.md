---
title: "摘要-codex-gpt6-astra额度优化"
type: source
tags: [来源, 原始文件, Codex, Token, 上下文, 优化]
sources: [raw/01-articles/2026-09-14-Codex GPT-6 Astra额度掉得太快？我用一段提示词，把上下文消耗大幅降低了！.md]
last_updated: 2026-09-15
---

## 核心摘要
GPT-6 Astra 上线后 Codex 额度下降极快（原来三天用完变大半天花完），退回 GPT-5.6 Sol 后消耗依然快。作者排查后发现额度不是模型变贵，而是被上下文一点点吃掉：两条 GPT-5.6 Sol 中等推理长任务累计输入 token 分别接近 **1599 万和 1582 万**，任务后期单次调用输入已达 **22.8 万–25.4 万 token**；界面里只发一句短话，模型实际收到的是聊天记录 + 工具返回 + 项目规则 + Skills 描述 + 插件说明。作者本机有 **274 份 Skill 定义**、全局 `AGENTS.md` **5284 字节**，与 OpenAI 官方文章《Rethinking skills and prompts for GPT-6 Astra》结论一致：Skill 描述太多太长会持续占用上下文，AGENTS.md 也不该要求每个小任务前都读一整套文档，应该只在当前任务确实需要时按需加载。三类调整：(1) `AGENTS.md` 从 5284 字节压缩到 **1705 字节**，保留品牌名/公众号发布规则/飞书操作等关键约束，删重复解释；(2) 在 `config.toml` 加自动压缩与工具输出限制——`model_auto_compact_token_limit = 160000`、`model_auto_compact_token_limit_scope = "total"`、`tool_output_token_limit = 8000`、`[skills] max_context_tokens = 4000`（这些数字不是标准答案，解决的是「不让单个任务和工具输出无限膨胀」）；(3) 不粗暴卸载插件/MCP/Skills，先判断是否真在每轮注入上下文。作者给出一段完整提示词让 Codex 自行诊断+备份+优化+验证，并特别加了一条防坑规则：不要让 Codex 为了省额度擅自换模型，也不要擅自停 OpenCodex 等第三方代理（曾遇到 OpenCodex 修改模型目录导致界面只显示「自定义」）。使用方式也要跟着变：一个任务不要无限续下去，一个阶段完成就新建任务，只把必要文件和最终结论交给新任务；日常小任务不要默认最高推理强度。结论：Codex 消耗由模型 + 任务长度 + 全局规则 + Skills + 工具输出共同组成，先看清 token 花在哪再决定压缩上下文、拆任务还是调模型。

## 关联连接
- [[Codex]] — 被优化的工具
- [[GPT-6]] — Astra 额度消耗快的背景
- [[上下文压缩]] — model_auto_compact_token_limit 机制
- [[TokenEfficiency]] — Token 效率衡量
- [[Skill]] — 274 份 Skill 定义持续注入上下文
- [[AGENTS-md]] — AGENTS.md 只该管边界
- [[上下文工程]] — 每轮真正送进模型的内容组成
- [[OpenAI]] — 官方文章《Rethinking skills and prompts for GPT-6 Astra》
