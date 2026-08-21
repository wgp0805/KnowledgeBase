---
title: "摘要-deepseek-harness必装10个插件-程序汪"
type: source
tags: [来源, DeepSeek, Harness, 插件, 程序汪]
sources: [raw/01-articles/2026-08-21 - DeepSeekHarness必装的10个插件.md]
last_updated: 2026-08-21
---

## 核心摘要
[[程序汪]] 盘点 DeepSeek Harness（DSH）生态中最值得安装的 10 个插件，覆盖核心体验、交互方式和能力扩展三个层次。截至 2026-08-15，Oh-My-DSH 目录已收录精选插件 1117 个、监测生态仓库 1521 个、累计 Star 301295 颗。文章强调 DSH "一切皆插件"的设计哲学——模型、工具、技能、会话、沙箱、存储、循环、调度、UI 全部可由插件组合而成，并给出按用户类型的选装建议表。

## 关键信息

### 插件安装方式
- 唯一命令：`dsh plugin --profile web add "github:owner/repo#ref"`
- **重要坑**：启动 Web UI 必须加 `--patch` 参数，否则很多插件和技能不生效：`npx @deepseek-ai/dsh web --patch`
- 安装后需重启 dsh web 服务并刷新页面
- 官方建议插件仓库打 `#dsh` 标签便于社区目录自动收录

### 10 个推荐插件

| 序号 | 插件名 | 仓库 | Star | 核心价值 |
|------|--------|------|------|----------|
| 1 | [[ModLens]] | liustack/modlens | 905+ | 给纯文本 DeepSeek 模型装上"眼睛"，图片转结构化文本证据（锁版本号 `@3.17.2`） |
| 2 | dsh-web-ui | zhu1090093659/dsh-web-ui | 1013+ | 一站式全家桶：任务看板/Git 图谱/右侧面板/移动端 UI/桌宠/Token 统计/皮肤中心 |
| 3 | dsh-better-sidebar | omdsh-dev/DSH-better-sidebar | 684+ | Codex 风格侧边栏工作台：文件树/终端/Git/子代理/可扩展 Tab |
| 4 | dsh-TUI | ccch1mneyyy/dsh-TUI | 793+ | 把 Harness 搬回终端，`dsh --profile cc-tui` 进入全屏终端界面 |
| 5 | deepseek-harness-desktop | anywhere-labs/deepseek-harness-desktop | 4745+ | Electron 桌面应用，无需装 Node.js，双击即跑（macOS/Windows） |
| 6 | dsh-at-file | omdsh-dev/dsh-at-file | - | `@` 引用文件，对标 Codex 文件引用体验 |
| 7 | dsh-agent-teams | NanmiCoder/dsh-agent-teams | - | 多智能体团队协作，自然语言驱动，邮箱直达+唤醒无队长中转 |
| 8 | dsh-plan-execute | dsh-external/dsh-plan-execute | - | 双模型路由：规划用推理模型，执行用经济模型，降本增效 |
| 9 | dsh-context-doctor | Zhenyu98/dsh-context-doctor | - | 量化上下文 Token 账单，检测重复与冲突，给出裁剪建议（只读） |
| 10 | dsh-reverse-skill | dhicoc/dsh-reverse-skill | - | 85 个安全研究 SKILL.md，覆盖逆向工程/授权渗透/安全研究 |

### 三层分类
- **第一层（核心体验层）**：dsh-web-ui、dsh-better-sidebar——界面从"毛坯"变"精装"
- **第二层（交互方式层）**：dsh-TUI（终端）、deepseek-harness-desktop（桌面 App）、dsh-at-file（@引用）
- **第三层（能力扩展层）**：ModLens（看图）、dsh-agent-teams（多 Agent）、dsh-plan-execute（双模型）、dsh-context-doctor（上下文审计）、dsh-reverse-skill（安全技能）

### 选装建议
| 用户类型 | 推荐组合 |
|----------|----------|
| 只想用 Harness 干活 | dsh-web-ui + dsh-at-file |
| 想要 Codex 风格界面 | dsh-better-sidebar + dsh-at-file |
| 纯终端爱好者 | dsh-TUI |
| 不想装 Node.js | deepseek-harness-desktop |
| 需要看图 | 加装 ModLens |
| 复杂任务/多 Agent | 加装 dsh-agent-teams 和 dsh-plan-execute |
| 成本敏感 | 加装 dsh-context-doctor |

### 优缺点
- **优点**：极致可定制、生态爆炸式增长（1117 插件/1521 仓库/301295 Star）、安装极简（一条命令）、MIT 协议
- **缺点**：版本波动大（developer preview）、部分插件需额外配置、启动必须加 `--patch`

### 生态数据（2026-08-15）
- Oh-My-DSH 插件聚合社区：1117 个精选插件
- 监测生态仓库：1521 个
- 累计 Star：301295 颗
- DeepSeek Harness 官方仓库：11 万+ Star

## 关联连接
- [[DeepSeekHarness]] — 所属 Agent 框架
- [[DeepSeek]] — 所属公司
- [[程序汪]] — 文章作者
- [[ModLens]] — 推荐插件（给纯文本模型补视觉）
- [[摘要-deepseek-harness命令大全]] — dsh 命令速查
- [[摘要-deepseek-harness教程-掉落的果实]] — DSH 完整教程
- [[摘要-人类智力基线与2张显卡]] — DSH 开源与本地部署
- [[摘要-deepseek-harness内测]] — DSH 内测首发
- [[AgentHarness]] — Harness 通用概念
- [[Codex]] — dsh-better-sidebar 对标的界面风格
- [[ClaudeCode]] — dsh-TUI 对标的工作流风格
