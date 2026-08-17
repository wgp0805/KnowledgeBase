---
title: "DeepSeek"
type: entity
tags: [AI, 模型, 公司]
sources: [raw/01-articles/推荐一款DeepSeek V4 编程神器！.md, raw/09-archive/Ollama+DeepSeek本地部署（新人必看）.md, raw/09-archive/国产大模型跑分一个比一个高，到底谁能真的干活？.md, raw/01-articles/DeepSeek、Gemini、Qwen、Step 3.7 Flash实测，谁才是国产黑马？.md, raw/01-articles/2026-07-31-倒反天罡！DeepSeek V4-Flash 正式版悄然上线：130亿激活参数，把自家1.6万亿旗舰「以下克上」 - 小白跃升坊.md, raw/09-archive/DeepSeek员工：Harness开始内测，有plugin、skill、MCP、Agent开源项目者优先，并赠送API额度（附Agent面试题）.md, raw/09-archive/DeepSeek 员工：DeepSeek V4 Pro 正式发布，Harness 也进入最后一个内测版本（附Agent面试题）.md, raw/01-articles/DeepSeek V4 Pro 正式版是夯还是拉？深度实测来了！.md, raw/01-articles/DeepSeek Harness必装的10个插件.md, raw/01-articles/2026-08-15-DeepSeek Harness 教程：一切皆插件的开源 Agent 框架 - 掉落的果实.md]
last_updated: 2026-08-17
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

### V4 Pro 正式版（0813，2026-08-13 上线）
- 总参数 1.6T / 激活参数 49B（MoE），与 Flash（284B / 13B）均支持 100 万上下文，但激活参数差近 4 倍，直接影响推理深度与 Agent 工具调用准确率
- 正式版支持 [[ResponsesApi]]（与 Flash 一致），可完美适配 [[Codex]]；Preview 版本不支持
- 正式版有 SLA 保障，行为变更提前通知；后训练做得更好，Agent 特定场景表现力更强
- 价格约为 Flash 的 3 倍（缓存未命中输入价），但**缓存命中价格差距很小**——这决定了 Agent 上下文布局策略：不变内容放前面以命中前缀缓存
- 版本管理建议：锁定具体版本号（如 `deepseek-v4-pro-0813`）替代通用名，配合离线回归测试集保证线上可复现
- **Harness 进入最后内测**：DeepSeek Harness 团队公众号已开通（34 人关注，未发文），即将公测，对标 [[ClaudeCode]] 和 [[Codex]]，自家模型配自家 Harness 可做最深层次适配
- 详见 [[摘要-deepseek-v4-pro-发布-harness-内测]]

### V4-Flash 正式版（0731，2026-07-31 上线）
- 结构/尺寸与 4 月预览版一致（总参数 284B / 激活参数 13B，MoE，1M tokens 原生上下文，最大输出 384K），**仅重新进行后训练**，后台自动切换，仅限 API
- 与 V4-Pro（总 1.6T / 激活 49B）对比：在 Agent 能力多项基准上反超 Pro 预览版
  - Terminal Bench 2.1 达 82.7（预览 61.8）；DeepSWE 54.4（预览 7.3）；Toolathlon Verified 70.3；Cybergym 76.7；NL2Repo 54.2；DSBench-FullStack 68.7；DSBench-Hard 59.6；Agent Last Exam 25.2；Automation Bench 25.1
  - 逼近 Claude Opus 4.8（Terminal Bench 85.0），反超 GLM-5.2（81.0）
- 价格约为 V4-Pro 的三分之一（输入未命中 1 元/百万 tokens、输出 2 元），并发上限 2500（Pro 仅 500）；预告峰谷定价（高峰 2 倍）
- 生态：原生支持 OpenAI Responses API（Flash 独占），Codex CLI/桌面端/IDE 可接入；预览版已适配 Claude Code、OpenClaw、OpenCode、CodeBuddy
- **Harness 内测（2026-08-06）**：DeepSeek Harness（DSH）开始内测，优先招募有 plugin、skill、MCP、Agent 开源项目经验的开发者，赠送 API 额度。支持 Sub-agent、KV Cache 智能复用、跨会话记忆持久化，对 Codex 和 Claude Code 已做深度兼容
- 技术基础（V4 系列共通）：CSA+HCA 混合稀疏注意力、mHC 流形约束超连接、Muon 优化器、FP4 QAT
- 待解问题：权重未开源、基准均为官方 Harness 自测、高推理强度依赖会放大 Token 消耗、无原生多模态

### V4 Pro 正式版实测（小哈 2026-08，详见 [[摘要-deepseek-v4-pro-正式版实测]]）
- 跑分提升：Aider Polyglot 78.5%（Preview 74.0%）、SWE-bench 68.0%（Preview 65.5%）、HumanEval 98.5%
- 实测任务：基础代码一次生成可用；复杂项目（后台管理系统、微服务）需人工微调细节
- **API 峰谷定价**：高峰 10:00-24:00（输入 2 元/输出 8 元），低谷 00:00-10:00（输入 0.5 元/输出 2 元），缓存命中减半
- 选型建议：日常编程用 Flash 性价比更高，复杂推理任务用 Pro

### Harness 教程与插件生态（2026-08-15）
- DSH 完整教程发布（详见 [[摘要-deepseek-harness教程-掉落的果实]]）：四种运行模式（TUI/Headless/Web UI/SDK）、插件协议、配置文件
- 必装 10 插件推荐（详见 [[摘要-deepseek-harness必装10个插件]]）：[[ModLens]]、Code Review、Test Generator 等
- 设计理念："一切皆插件"，工具/技能/MCP/记忆全部通过插件实现

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
- [[DeepSeekHarness]] — Agent 评测框架
- [[崔添翼]] — Harness 团队负责人
- [[后训练]] — 正式版核心方法
- [[Codex]] — 被适配的生态
- [[摘要-deepseek-v4-flash发布]] — 来源（V4-Flash 正式版）
- [[摘要-deepseek-v4-pro-发布-harness-内测]] — 来源（V4 Pro 正式版 + Harness 最后内测）
- [[ResponsesApi]] — V4 Pro/Flash 正式版支持的有状态 API
- [[BetterHarness]] — PaiCLI 的 Agent 质量审计工具（非 DeepSeek Harness）
- [[摘要-deepseek-v4-pro-正式版实测]] — 来源（V4 Pro 正式版实测）
- [[摘要-deepseek-harness必装10个插件]] — 来源（DSH 插件推荐）
- [[摘要-deepseek-harness教程-掉落的果实]] — 来源（DSH 完整教程）
- [[ModLens]] — DSH 推荐插件
- [[掉落的果实]] — DSH 教程作者
