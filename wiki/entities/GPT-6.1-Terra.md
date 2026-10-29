---
title: "GPT-6.1-Terra"
type: entity
tags: [AI模型, OpenAI, GPT-6, Codex, 模型版本]
sources: [raw/09-archive/GPT-6.1 Terra 发布！扒完 Codex 最新源码，我发现了 OpenAI 藏起来的三个大招.md]
last_updated: 2026-10-28
---

## 定义

GPT-6.1 Terra 是 OpenAI GPT-6 系列四档天体命名中的**第二档**（由小到大：Luna → Terra → Sol → Astra），对标 Anthropic **Sonnet 5.5**。2026-10-27 随 Codex 客户端更新发布，官方示例能力为"把 2D 建筑蓝图还原成 3D 交互模型"（Three.js 实现，支持剖面切换与日照阴影、构件联动高亮）。

## 关键信息

### 分档定位

| 档位 | 对标 | 定位 |
|------|------|------|
| Luna | Haiku 5.5 | 高并发路由（最小档） |
| **Terra** | **Sonnet 5.5** | **本文主角，速度 + 多模态均衡** |
| Sol | — | 主力模型，比 Astra 省 Token |
| Astra | — | 前沿数学推导与漏洞分析（旗舰） |

### Codex 源码三大发现（2026-10-27）

1. **code_mode_only 纯代码执行模式**（默认开启）——V8 沙箱并发脚本编程，`tool_search` BM25 实时检索工具签名 + `Promise.allSettled` 并发执行，详见 [[code_mode_only]]
2. **50 万 Token 工作窗口 + 编号寻址跨窗口接力**——`context_window` 放开到 50 万（Astra/Sol/Luna 锁 27.2 万），`supports_image_detail_original` 高清原图不裁剪；剩余 <6144 Token 时走 `notes` → `new_context` → `history` 无损接力，详见 [[跨窗口接力]]
3. **隐藏 ultra 推理档位 + 自动任务委派**——`spawn_agent` 并行 Sub-agent + `fork_turns` 上下文继承控制；`memory_consolidation` 默认模型换用 terra

### 评测表现

- **Agents' Last Exam v1**（长周期多模态）：Terra 最高推理档 60 分，反超自家 Sol（58.6 分）
- 强项场景：2D 工程图纸转 3D 模型、逐帧审查动画成片等长周期多模态任务
- 作者实测：2D 建筑蓝图转 3D 模型工具效果不错

### 作者评价

- 速度优势：V8 沙箱并发执行，Terra 执行任务比 Sol/Astra 快 3 倍以上
- 作者旁白：市面上便宜又快模型够多，期待能打败 Opus 5.5 的模型

## 关联连接
- [[GPT-6]] — 所属模型系列（四档命名体系）
- [[Astra]] — 同系列旗舰档（对照）
- [[Codex]] — 提供此模型的 Agent 客户端
- [[code_mode_only]] — 纯代码执行模式（第一招）
- [[跨窗口接力]] — 跨窗口无损记忆接力（第二招）
- [[思考强度]] — ultra 隐藏档位所属概念
- [[ToolSearch]] — 工具延迟加载机制
- [[BM25]] — 工具签名检索算法
- [[摘要-gpt6.1-terra-codex三招]] — 来源
- [[沉默王二]] — 作者
- [[OpenAI]] — 发布方
- [[Opus]] — 竞品旗舰（Opus 5.5，作者期待被超越）
