---
title: "Mods"
type: concept
tags: [ClaudeCode, Agent扩展, 事件中间件, Mods]
sources: [raw/09-archive/2026-10-04-Claude Code 最新版更新 Mods 能力，致敬 DeepSeek Harness？.md, raw/09-archive/2026-10-05-万字拆解 DeepSeek Harness 桌面版：产品设计、任务实测与能力边界.md, raw/09-archive/2026-10-05-Claude Code Mod 实测：给编程助手做一个自定义面板.md]
last_updated: 2026-10-08
---

## 定义
Claude Code Mods（模组）是 Claude Code v2.1.287（2026-10 发布）引入的进程内事件扩展机制：开发者编写小型 TypeScript/JavaScript 函数挂载到 Claude Code 生命周期事件流上，像中间件管道（Middleware Chain）一样观察、改写或接管工具调用，并可在终端/桌面绘制自定义界面组件。

## 关键信息
- **三类操作**：观察（Observe，只读事件数据并放行，如记录 token 消耗/统计轮次）；改写（Rewrite，在数据发给模型或执行前动态修改，如敏感路径脱敏、高危命令参数改写为安全选项）；接管（Answer，直接处理事件并返回结果，跳过默认逻辑）
- **四扩展选型**：Skills（Markdown 载体，作用于模型上下文，沉淀 SOP/规范）；MCP（外部进程/网络服务，提供外部工具）；Settings Hooks（settings.json 配置的 Shell/HTTP/Prompt，生命周期事件触发外部运行）；Mods（进程内事件函数，常驻运行时，适合自定义 UI、重写事件流、跨钩子共享状态、动态调整推理参数）——四者互补协同，一个插件包可同时包含
- **官方示例**：Token Weather（约 80 行 Mod，在输入框上方画上下文消耗天气条，25% 以下晴天、90% 以上提示即将压缩）；Blast Radius（高危命令弹黄框确认，列受影响文件与编号选项）；Replay Theater（分步复盘面板：步骤指示条、单行变更对比、上一页/下一页）；cc-plugin-you-should-know（内置实验 Mod，后台副代理观察长任务、发现疏漏弹便签提醒，`/plugin enable` 启用且仅限开启遥测的第一方会话）
- **架构演进信号**：部分内置能力已以 Mod 形式交付（/diff → cc-plugin-diff、AGENTS.md 加载 → cc-plugin-agents-md），官方计划把更多内置功能迁移为 Mods，让用户把 Claude Code 缩减为小 Core 按需装配——探索把宿主本身解耦，但仍处早期
- **与 DeepSeek Harness 的关系**：共同点是把定制单元从外部提示词/工具挂载推进到 Agent 运行时内部、内置与扩展共享同一套底层机制、调用链引入类似中间件的 next/提前返回流水线；差异在架构范围——DSH 用 Cordis 插件树装配整套 Harness（服务契约级组件插拔），Mods 在已有宿主上开放关键生命周期做事件拦截与改写（会话流水线级）；两者 API 与上下文模型完全不同，基于 Cordis Context 的服务无法直接进 Claude Code，Mods 的 register 与事件钩子也无法直接在 dsh 中运行
- **安全边界**：官方明确 "Mods aren't sandboxed"——代码跑在受控 JS 环境（无原生 require/全局定时器/直接网络，底层操作须经宿主 $ API），但 $.fs/$.process 行使当前用户实际系统权限；Mod 自启进程在 Claude Code Bash 沙箱之外，勿装来源不可信的第三方 Mod；**Mod 不能改绘系统权限提示框**（permission prompt），显示保护与执行授权是两项独立边界
- **企业管控**：配置 Managed Settings 或以 Team/Enterprise 登录时，内置 cc-plugin-sec-default 先于用户 Mods 加载，保护托管指令/Hooks/设置/MCP；管理员可设 `allowManagedModsOnly: true` 阻止用户自带 Mods
- **环境支持**：终端完整支持事件与 UI；Desktop 的 Code 标签页支持绘制（WSL 会话暂不支持）；VS Code 聊天面板、`claude -p`、Agent SDK 事件正常但 UI 不显示；Remote Control 与 Cloud Session 界面仅/不本地渲染
- **三产品定制路径对比（2026-10-05，详见 [[摘要-deepseek-harness-桌面版万字拆解]]）**：沿"创建与调用/修改与生效/影响范围"看三家——[[DeepSeekHarness]] 把运行部件纳入插件组合、创造模式生成的能力进插件体系、**按运行配置管理**（改代码重启生效，多会话共用同一配置一次改全影响）；**Mods 按会话试用**（热重载经批准在回合结束加载、默认仅创建它的会话，跨会话需保留目录另加载或市场分发，有停用入口）；[[Codex]] plugins 按项目启停（改市场条目指向的目录后重启应用生效、Hooks 需用户审阅信任、可停用保留安装）。选型建议：先拿一项实际改动走完整条路径再评估维护投入
- **"雨姐"面板六步实测（2026-10-05，赛博禅心，详见 [[摘要-claude-code-mod-雨姐面板]]）**：与 Skill/MCP/settings hooks 的本质区别——**Mod 是跑在 Claude Code 进程里的 JS/TS 代码**，能直接画界面（右侧面板 Pane/AbovePrompt 提示条/状态栏/toast）。三文件结构（plugin.json + hooks.json + register.tsx）；三种处理：旁观（tool.call 里 await next(e) 后按结果换表情）、改写（prompt.compose 注入东北话口吻，用户原话不动）、接管（匹配 rm -rf/强推/`git reset --hard` 时直接回 deny 不调 next——**拒绝理由原样进 Claude 上下文**，Claude 会把命令交还用户而非绕开）；Raster 字符画布一格"▀"装上下两像素画像素头像（踩坑 tmux 降 256 色、通道压 16 档偏色）；坑：`npm test | tail` 管道尾成功导致整条命令不标报错，需另扫输出 "fail" 字样；`claude plugin validate --strict` 静态审查 hooks/calls、`claude plugin test` 不联网事件级测试抓到无界面环境拉面板的 bug；分享走 git+marketplace.json、按"名字@集市"安装、版本号不改别人拿不到更新；**Mod 不在沙箱、以用户身份运行**，只装可信作者的；Claude Code 内置 /diff 面板本身就是一个 Mod
- **上手**：要求 v2.1.287+，`/plugin` 查看已加载模组，`claude plugin validate ./your-mod-dir` 校验 Mod 声明的事件钩子与系统调用

## 关联连接
- [[ClaudeCode]] — Mods 的宿主产品
- [[摘要-claude-code-mods机制]] — 来源
- [[摘要-deepseek-harness-桌面版万字拆解]] — 来源（三产品定制路径对比）
- [[摘要-claude-code-mod-雨姐面板]] — 来源（雨姐面板六步实测）
- 赛博禅心 — 雨姐面板实测作者（公众号）
- [[Codex]] — 定制路径对比的第三方
- [[DeepSeekHarness]] — 对比的"一切皆插件"路线
- [[Cordis]] — DSH 插件树底座
- [[AgentHarness]] — 上位概念
- [[Anthropic]] — 发布方
- [[Agent]] — 所属运行时形态
