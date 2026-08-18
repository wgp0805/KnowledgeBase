---
title: "DeepSeekHarness"
type: entity
tags: [实体, 评测框架, Agent, DeepSeek, Harness]
sources:
  - raw/09-archive/DeepSeek员工：Harness开始内测，有plugin、skill、MCP、Agent开源项目者优先，并赠送API额度（附Agent面试题）.md
  - raw/09-archive/2026-07-31-倒反天罡！DeepSeek V4-Flash 正式版悄然上线：130亿激活参数，把自家1.6万亿旗舰「以下克上」 - 小白跃升坊.md
  - raw/01-articles/DeepSeek Harness必装的10个插件.md
  - raw/01-articles/2026-08-15-DeepSeek Harness 教程：一切皆插件的开源 Agent 框架 - 掉落的果实.md
  - raw/01-articles/抖音视频内容整理_人类智力基线与2张显卡.md
last_updated: 2026-08-18
---

## 定义
DeepSeek Harness（DSH）是 DeepSeek 官方自研的原生 Agent 框架，对标阿里 Qoder、月之暗面 Kimi Code、智谱 Zcode 等同类产品。遵循 **Model + Harness = Agent** 设计理念，模型负责推理，Harness 负责模型之外的一切：工具调用、记忆管理、上下文控制、MCP 协议、Skills 体系等。

## 关键信息
- **2026-08-06 开始内测**：优先招募有 plugin、skill、MCP、Agent 开源项目经验的开发者，并赠送 API 额度
- **2026-08-13 正式开源**：MIT 协议，TypeScript 实现，基于 Cordis 插件内核（Koishi 同源技术，4 年 4000+ 社区插件验证）
- **GitHub 涨星记录**：发布 2 小时破万，12 小时超 5 万，42 小时约 10 万——**GitHub 史上涨星最快项目**
- **对 Codex 和 Claude Code 已做深度兼容**，但官方原生 Harness 对 API 入参出参有更优适配
- **泄露架构信息**：支持 Sub-agent、KV Cache 智能复用、跨会话记忆持久化等特性
- **团队背景**：DeepSeek Agent Harness 团队成立于 2026 年 3 月；负责人崔添翼（90 后浙大计算机出身，6 枚 ACM 亚洲区域赛金牌，曾任 Jane Street 量化机构九年）
- **评测角色**：V4-Flash 正式版公开基准测试中的 Code Agent 任务均使用该框架测试（Terminal Bench 2.1 达 82.7，DeepSWE 54.4 等），相关基准成绩为官方自测
- **不绑定 DeepSeek API**：认 OpenAI 兼容端点，可接入本地 llama-server / Ollama 等任意 OpenAI 兼容推理后端，详见 [[摘要-人类智力基线与2张显卡]]

## 知识冲突（已解决）
- 旧信息（2026-07-31）：定义 DeepSeek Harness 为"Agent 评测框架"——用于测试模型在代码 Agent 任务上的基准性能
- 新信息（2026-08-06）：DeepSeek Harness 是用户端 Agent 产品，评测是其中一项用途而非本质
- **处理结果**：2026-08-06 以新信息覆盖，将评测框架定位降级为次要用途

## 知识冲突（已解决，2026-08-18 核对官方文档）
- 旧信息 A（2026-08-15 教程）：四种运行模式为 TUI / Headless / Web UI / SDK
- 旧信息 B（2026-08-18 抖音视频）：四种运行模式为 标准模式 / PTC 模式 / 极简模式 / 创造模式
- **官方文档核对**（2026-08-18，https://github.com/deepseek-ai/deepseek-harness/blob/master/apps/cli/README.md）：
  - 官方 **Entry modes** 按 profile（配置文件）划分：`dsh --profile <name>`、`dsh --profile headless "job"`、`dsh web`（= `--profile web` 别名）、`dsh plugin --profile <name>`
  - 官方**没有**"TUI/Headless/Web UI/SDK"四分法，也**没有**"标准/PTC/极简/创造"四分法
- **处理结果**：两组分类均为第三方归纳，非官方术语
  - 教程的 TUI/Headless/Web UI 对应官方 profile 概念（web 和 headless 是官方明确 entry mode，TUI 是文档示例中提到的 `--profile tui`，SDK 指独立的 Python SDK 指南）
  - 抖音视频的标准/PTC/极简/创造更像是**工具集预设（preset）或 profile 配置**，描述的是工具集与行为，而非 entry mode
  - 两者是**不同维度的切面**：前者按交互形态，后者按工具集配置。已将两组并存并标注来源，以官方 Entry modes 为权威基准

## 官方 Entry modes（2026-08-18 核对，权威基准）
| 命令 | 用途 |
|------|------|
| `dsh --profile <name>` | 启动命名 profile（位于 `$DSH_HOME/profiles/<name>`） |
| `dsh --profile headless "job"` | 无界面运行一次性任务，打印最终答案后退出 |
| `dsh web` | `--profile web` 的别名，启动 Web UI（默认 `http://127.0.0.1:3080`） |
| `dsh plugin --profile <name> <pnpm args>` | 管理 profile 的插件（转发给 pnpm） |

- 调用目录是默认工作区根目录
- `web` 和 `headless` profile 首次使用时从内置模板自动初始化
- 其他 profile 必须通过 `dsh plugin` 创建
- Profile 目录包含 `package.json`（out-of-tree 插件依赖 + `dsh.profile` 清单）、`cordis.patch.yml`（用户补丁层）

## 第三方归纳：按交互形态（2026-08-15 教程，详见 [[摘要-deepseek-harness教程-掉落的果实]]）
1. **TUI 模式**：终端交互（默认），`dsh` 启动
2. **Headless 模式**：无界面自动化，`dsh --headless -p "任务"`，适合 CI/CD
3. **Web UI 模式**：`dsh --web`，浏览器访问，支持可视化调试
4. **SDK 模式**：作为库嵌入，`import { DSH } from '@deepseek/harness'`

## 第三方归纳：按工具集预设（2026-08-18 抖音视频，详见 [[摘要-人类智力基线与2张显卡]]）
| 预设 | 特点 | 适用场景 |
|------|------|----------|
| 标准模式 | 完整工具集：文件编辑、Shell、搜索、Skills、子 Agent、工作流 | 日常开发 |
| PTC 模式 | 模型写 TypeScript 代码一次性组合多步工具调用，大幅省 Token | 批量自动化 |
| 极简模式 | 仅保留 bash + 文件编辑器 | 模型基准测试 |
| 创造模式 | 标准模式 + 运行时检查 + 插件实验 + 自定义预设 | 插件开发、定制 Agent |

## 插件生态（2026-08-15）
- **设计理念**："一切皆插件"，工具/技能/MCP/记忆全部通过插件实现
- **插件协议**：定义 name/version/tools/skills/hooks，支持生命周期钩子（onSessionStart/onToolCall/onSessionEnd）
- **脚手架**：`dsh plugin create <name>` 快速创建插件模板
- **配置文件**：`dsh.config.json` 管理模型、插件、MCP、记忆
- **必装 10 插件**（详见 [[摘要-deepseek-harness必装10个插件]]）：[[ModLens]]、Code Review、Test Generator、Doc Generator、Refactor Helper、Security Scanner、Performance Profiler、Git Helper、API Tester、Visual Debugger

## 插件生态（2026-08-18，社区爆发）
- 上线 5 天，社区插件已超 **1400+** 个
- GitHub 搜索话题 `dsh-plugin`
- 代表插件：dsh-web-ui 全家桶（任务看板/Git 图谱/右侧面板/桌宠/Token 统计/皮肤中心）、[[ModLens]]（给纯文本模型补视觉）、dsh-genui（交互式 UI 渲染）、dsh-at-file（@ 引用文件）、dsh-tool-git（模型侧 Git）、dsh-browser-bridge（浏览器自动化）、dsh-memory-evolve（跨会话长期记忆+自我进化）、梁神模式（V4 Pro 调优预设，两阶段锚定 trick）

## 本地部署接入（2026-08-18）
- DSH 认 OpenAI 兼容端点，不绑定 DeepSeek API
- 接入本地 [[LlamaCpp]] / [[Ollama]]：Settings → Models → 添加自定义模型 → 填本地地址（如 `http://127.0.0.1:8080/v1`）→ API 协议选 `openai-completions` → 保存即时生效
- 配合 [[Qwen3.8-27B]] + 2× [[RTX5090]] 构成完全本地 Agent 工作站，详见 [[本地Agent工作站]]
- 注意：DSH 仍是开发者预览版，会有破坏性变更，不适合直接上生产；Agent 有读写文件/执行 shell 权限，工作区选空测试文件夹

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
- [[摘要-人类智力基线与2张显卡]] — 来源（开源发布 + 本地部署接入）
- [[Qwen3.8-27B]] — 本地部署配套模型
- [[RTX5090]] — 配套硬件
- [[LlamaCpp]] — 本地推理引擎
- [[本地Agent工作站]] — 完整本地方案
- [[TensorSplit]] — 多卡分摊技术
- [[GGUF量化]] — 模型量化技术