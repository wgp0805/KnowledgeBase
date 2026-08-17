---
title: "DeepSeekHarness"
type: entity
tags: [实体, 评测框架, Agent, DeepSeek, Harness]
sources:
  - raw/09-archive/DeepSeek员工：Harness开始内测，有plugin、skill、MCP、Agent开源项目者优先，并赠送API额度（附Agent面试题）.md
  - raw/09-archive/2026-07-31-倒反天罡！DeepSeek V4-Flash 正式版悄然上线：130亿激活参数，把自家1.6万亿旗舰「以下克上」 - 小白跃升坊.md
  - raw/01-articles/DeepSeek Harness必装的10个插件.md
  - raw/01-articles/2026-08-15-DeepSeek Harness 教程：一切皆插件的开源 Agent 框架 - 掉落的果实.md
last_updated: 2026-08-17
---

## 定义
DeepSeek Harness（DSH）是 DeepSeek 官方自研的原生 Agent 框架，对标阿里 Qoder、月之暗面 Kimi Code、智谱 Zcode 等同类产品。遵循 **Model + Harness = Agent** 设计理念，模型负责推理，Harness 负责模型之外的一切：工具调用、记忆管理、上下文控制、MCP 协议、Skills 体系等。

## 关键信息
- **2026-08-06 开始内测**：优先招募有 plugin、skill、MCP、Agent 开源项目经验的开发者，并赠送 API 额度
- **对 Codex 和 Claude Code 已做深度兼容**，但官方原生 Harness 对 API 入参出参有更优适配
- **泄露架构信息**：支持 Sub-agent、KV Cache 智能复用、跨会话记忆持久化等特性
- **团队背景**：DeepSeek Agent Harness 团队成立于 2026 年 3 月；负责人崔添翼（90 后浙大计算机出身，6 枚 ACM 亚洲区域赛金牌，曾任 Jane Street 量化机构九年）
- **评测角色**：V4-Flash 正式版公开基准测试中的 Code Agent 任务均使用该框架测试（Terminal Bench 2.1 达 82.7，DeepSWE 54.4 等），相关基准成绩为官方自测

## 知识冲突（已解决）
- 旧信息（2026-07-31）：定义 DeepSeek Harness 为"Agent 评测框架"——用于测试模型在代码 Agent 任务上的基准性能
- 新信息（2026-08-06）：DeepSeek Harness 是用户端 Agent 产品，评测是其中一项用途而非本质
- **处理结果**：2026-08-06 以新信息覆盖，将评测框架定位降级为次要用途

## 四种运行模式（2026-08-15 教程，详见 [[摘要-deepseek-harness教程-掉落的果实]]）
1. **TUI 模式**：终端交互（默认），`dsh` 启动
2. **Headless 模式**：无界面自动化，`dsh --headless -p "任务"`，适合 CI/CD
3. **Web UI 模式**：`dsh --web`，浏览器访问，支持可视化调试
4. **SDK 模式**：作为库嵌入，`import { DSH } from '@deepseek/harness'`

## 插件生态（2026-08-15）
- **设计理念**："一切皆插件"，工具/技能/MCP/记忆全部通过插件实现
- **插件协议**：定义 name/version/tools/skills/hooks，支持生命周期钩子（onSessionStart/onToolCall/onSessionEnd）
- **脚手架**：`dsh plugin create <name>` 快速创建插件模板
- **配置文件**：`dsh.config.json` 管理模型、插件、MCP、记忆
- **必装 10 插件**（详见 [[摘要-deepseek-harness必装10个插件]]）：[[ModLens]]、Code Review、Test Generator、Doc Generator、Refactor Helper、Security Scanner、Performance Profiler、Git Helper、API Tester、Visual Debugger

## 关联连接
- [[DeepSeek]] — 所属公司
- [[崔添翼]] — 团队负责人
- [[Harness]] — 通用概念（Model + Harness = Agent）
- [[摘要-deepseek-harness内测]] — 来源
- [[摘要-deepseek-v4-flash发布]] — 来源
- [[摘要-deepseek-harness必装10个插件]] — 来源（插件推荐）
- [[摘要-deepseek-harness教程-掉落的果实]] — 来源（完整教程）
- [[ModLens]] — 推荐插件
- [[掉落的果实]] — 教程作者
- [[小哈]] — 插件推荐作者
- [[PaiCLI]] — 同类开源 Agent 项目
- [[ClaudeCode]] — 已兼容的第三方 Agent 框架
- [[Codex]] — 已兼容的第三方 Agent 框架