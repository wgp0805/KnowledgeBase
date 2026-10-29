---
title: "摘要-gpt6.1-terra-codex三招"
type: source
tags: [来源, 原始文件, OpenAI, GPT-6, Codex, 模型]
sources: [raw/09-archive/GPT-6.1 Terra 发布！扒完 Codex 最新源码，我发现了 OpenAI 藏起来的三个大招.md]
last_updated: 2026-10-28
---

## 核心摘要

沉默王二《GPT-6.1 Terra 发布！扒完 Codex 最新源码，我发现了 OpenAI 藏起来的三个大招》（2026-10-27）第一时间升级 Codex 切换 GPT-6.1 Terra 实测，并翻 Codex 源码挖出三个"大招"。

**背景：GPT-6 四档天体命名体系**——从 GPT-6 起 OpenAI 按天体体积从小到大排四档：**Luna**（对标 Haiku 5.5，负责高并发路由）→ **Terra**（对标 Sonnet 5.5，本文主角）→ **Sol**（主力模型，比 Astra 省 Token）→ **Astra**（前沿数学推导与漏洞分析，200 刀用量不够用）。

**三个源码级大招**：
1. **code_mode_only 纯代码执行模式**：Codex 为 Terra 默认开启，把零散工具全部隐藏，只暴露一个运行在独立 V8 沙箱里的 `exec` 工具，文件读写/终端命令/外部 MCP 插件全部挂载到沙箱全局 `tools` 对象；配合延迟加载——先 `tool_search` 用 **BM25 实时检索**当前需要的工具并取 TypeScript 签名，再在同一段 JS 里用 `Promise.allSettled` 把多个互不依赖的文件搜索/读取**一次性并发完成**。对比传统"一次调用一个工具"的 JSON 往返模式（每轮重发历史上下文），这是 Terra 比 Sol/Astra 快 3 倍以上的第一变化
2. **50 万 Token 工作窗口 + 编号寻址跨窗口接力**：GPT-6 全系上下文 105 万 Token，但 Codex 源码里 Astra/Sol/Luna 的 `context_window` 默认锁死在 **27.2 万 Token**，唯独 Terra 放开到 **50 万 Token** 并开启 `supports_image_detail_original`（高清原图不缩略裁剪、像素级可见）；当剩余空间低于 6144 Token 时不做全文摘要压缩，而是调 `notes` 工具把任务进度和关键记录（`window ID`/`item ID`）写成结构化数据 → `new_context` 开新窗口 → `history` 工具按编号**一字不差无损调取**旧窗口内容。长周期多模态评测 **Agents' Last Exam v1** 中 Terra 最高推理档拿下 60 分，反超自家 Sol 的 58.6 分
3. **隐藏 ultra 推理档位 + 自动任务委派**：公开 API 推理强度只有 none~max 五档，Codex 内部给 Astra/Sol/Terra 加隐藏第六档 **ultra**；切 ultra 时主模型推理强度映射到 `xhigh`，调 `spawn_agent` 派生多个并行 Sub-agent，用 `fork_turns` 控制上下文继承（修小函数传 `none` 零负担启动，复杂模块改造传 `all` 继承完整上下文）。另：云端 `memory_consolidation`（会话记忆整理）默认模型从 `gpt-6.1-sol` 换成 `gpt-6.1-terra`

**结论**：Terra 把 V8 沙箱并发执行、50 万原图窗口和低幻觉 Multi-Agent 委派打包在一起，在速度和多模态任务上交出超预期答卷。作者旁白：市面上便宜又快模型够多，真正期待的是能打败 Opus 5.5 的模型。

## 关联连接
- [[GPT-6.1-Terra]] — 本文主角模型实体
- [[code_mode_only]] — 第一招（纯代码执行模式）
- [[跨窗口接力]] — 第二招（编号寻址无损记忆接力）
- [[Codex]] — 被扒源码的 Agent 客户端
- [[GPT-6]] — 所属模型系列（四档命名体系）
- [[Astra]] — 同系列旗舰档
- [[ToolSearch]] — tool_search 延迟加载机制
- [[BM25]] — 工具签名实时检索算法
- [[思考强度]] — ultra 隐藏档位所属概念
- [[子Agent编排]] — spawn_agent/fork_turns 自动委派
- [[沉默王二]] — 作者
- [[OpenAI]] — 发布方
- [[Opus]] — 作者期待的竞品旗舰（Opus 5.5）
