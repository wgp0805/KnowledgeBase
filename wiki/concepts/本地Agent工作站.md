---
title: "本地Agent工作站"
type: concept
tags: [概念, 本地部署, Agent, 隐私, 成本优化, 硬件门槛]
sources: [raw/01-articles/抖音视频内容整理_人类智力基线与2张显卡.md]
last_updated: 2026-08-18
---

## 定义
本地 Agent 工作站是指完全在本地硬件上运行 AI Agent 工作流的方案，数据不出本机、无 API 订阅费、无云端依赖。2026 年的门槛已从"企业级 GPU 集群"降到"两张消费级显卡"，标志着"普通人可触及的 AI 智力水平"跨入新阶段。

## 关键信息

### 门槛演进
| 时间 | 跑一个 Agent 级 AI 需要什么 |
|------|---------------------------|
| 2023 年 | 调用 GPT-4 API，按 token 付费，月费数百到数千元 |
| 2024 年 | Claude Code 订阅制，$20/月起步，数据在云端 |
| 2025 年初 | 本地跑 7B-14B 模型，能力有限，只能做简单对话 |
| **2026 年** | **2× RTX 5090 + Qwen3.8-27B + DSH = 完全本地 Agent 工作站** |

### 三大支柱
1. **模型**：[[Qwen3.8-27B]]（Apache 2.0 开源，27B 稠密，256K 上下文）
2. **框架**：[[DeepSeekHarness]]（MIT 开源，"一切皆插件"，OpenAI 兼容端点不挑模型）
3. **推理引擎**：[[LlamaCpp]] 或 [[Ollama]]（免费，提供本地 HTTP API）

### 完整架构
```
DSH (Agent 框架) ──OpenAI 兼容 API──> llama-server (llama.cpp) ──tensor-split 1,1──> 2× RTX 5090
```
- DSH 认 OpenAI 兼容端点，不绑定 DeepSeek API
- llama-server 一起，把 base URL 指过去即可
- 接入协议的统一像插座标准的统一——插头规格定了，电器是谁家的无所谓

### 成本对比
| 方案 | 一次性投入 | 月费 | 数据隐私 |
|------|------------|------|----------|
| 云端 API（DeepSeek/GPT） | ¥0 | 数百-数千元 | 数据在云端 |
| Claude Code 订阅 | ¥0 | $20+ | 数据在云端 |
| **本地双卡工作站** | ¥30,000-40,000 | ¥0（仅电费） | **数据不出本机** |

### 核心意义
1. **能力跃升**：27B + Agent 框架从"尝鲜"变"日常可用"，实测能交付完整 3D 游戏
2. **门槛降低**：从企业级 GPU 集群降到 2 张消费级显卡
3. **完全私有**：数据不出本机，企业 IT 可上 Agent 工作流而不出内网
4. **生态爆发**：DSH 上线 5 天社区插件已超 1400 个
5. **架构解耦**：框架不挑模型，未来模型升级（Qwen4、Qwen5...）硬件配置都不用换

### 实战验证（2026-08-18）
- 任务：从空目录写网页版 Minecraft
- 配置：2× RTX 5090 + Qwen3.8-27B Q4 + DSH + llama.cpp
- 结果：38 步、23 分钟、66 tokens/sec、缓存命中 98%
- 交付：753 行 game.js + 63 行 index.html + 596KB three.js，双击即玩，不联网不装依赖

### 避坑要点
1. DSH 仍是开发者预览版，会有破坏性变更，不适合直接上生产
2. DSH Agent 有读写本地文件、执行 shell 命令的权限，工作区选空测试文件夹，用 Git 做版本管理
3. 双卡没有 NVLink，多卡走 PCIe，解码速度不会翻倍（约 1.6-1.8x）
4. `--fit off` 必须开，否则显存吃紧时 llama.cpp 会悄悄调小上下文
5. `--jinja` 必须开，用模型内置聊天模板，工具调用全靠它
6. 插件安装后必须重启 dsh 进程，仅刷新浏览器通常不够
7. Windows 用户：PowerShell 可能拦截 npx.ps1，换成 `npx.cmd @deepseek-ai/dsh web`
8. Node.js 版本建议 v22.19+，v18 崩溃，v24 可能有兼容性问题

## 关联连接
- [[摘要-人类智力基线与2张显卡]] — 来源
- [[Qwen3.8-27B]] — 模型支柱
- [[DeepSeekHarness]] — 框架支柱
- [[LlamaCpp]] — 推理引擎支柱
- [[RTX5090]] — 硬件门槛
- [[TensorSplit]] — 多卡分摊技术
- [[GGUF量化]] — 模型量化技术
- [[Ollama]] — 同类推理工具
- [[AgentHarness]] — Model + Harness = Agent 核心概念
- [[VibeEngineering]] — AI 时代工程范式
- [[VibeCoding]] — AI 编程范式
