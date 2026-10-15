---
title: "ClaudeCode"
type: entity
tags: [AI工具, Agent, Anthropic]
sources: [raw/01-articles/全网最全！60分钟全面掌握Claude Code~【附完整文档】.md, raw/01-articles/6条Claude Code实践中的经验与思考.md, raw/01-articles/腾讯面试官："为什么 Claude Code 不用 RAG 检索代码，而是 grep？"我："因为...我也不知道"，他沉默了。.md, raw/09-archive/ClaudeCode写SpringBoot代码竟然这么野？这4个Skill让我彻底服了！.md, raw/01-articles/直接让你的 Claude Code 效率拉满，Anthropic 官方神级插件开源了！-2026-06-02 09_14_35.md, raw/01-articles/Codex 和 Claude Code，到底哪个更好？.md, raw/01-articles/Claude Code 最佳学习路线：从“手敲代码”到“指挥AI打工”，强的离谱！！.md, raw/01-articles/老板：“刚刚，阿里全面禁用Claude，我们要不要跟风？”，我：“Claude Code的底层我刚严肃深扒，别上头。”.md, raw/01-articles/Loop Engineering 实战指南.md, raw/01-articles/面试官坏笑：“你用ClaudeCode写代码，不怕它把项目搞炸？”，我：“怕，所以CLAUDE.md、权限和验证，一个都不能少。”.md, raw/01-articles/阿里又开源了一个神级Skill项目！.md, raw/01-articles/2026-08-28 - 面试官坏笑：“你都用ClaudeCode写代码半年了，怎么保证它不会执行危险命令？”，我：“CLAUDE.md”，面试官：“回去等通知吧！”.md, raw/01-articles/2026-09-18-为什么中美头部Agent，不约而同走向开放？.md, raw/01-articles/2026-09-23-开多个 Agent 后 Claude Code 账单翻了 4 倍，一个配置解决了 - 码哥字节.md, raw/01-articles/2026-09-24-Claude Code 把自己改成了任务调度器，这次设计比功能更值得看 - 码哥字节.md, raw/01-articles/2026-09-26-我写了 50 个 Claude Code Skill 才发现，前 30 个都白写了 - 码哥字节.md, raw/01-articles/2026-10-01-一行命令，解锁 Claude Code 全部权限-ClawGod - 绝不原创的飞龙.md, raw/01-articles/2026-10-01-Claude Code + MCP，让一个空文件夹变成了能玩的 Unity 游戏 - 张善友.md, raw/01-articles/2026-10-04-Claude Code 最新版更新 Mods 能力，致敬 DeepSeek Harness？.md, raw/01-articles/2026-10-05-Claude Code Mod 实测：给编程助手做一个自定义面板.md, raw/01-articles/同事的 Claude Code 为什么比你的强？差的就是这4步.md, raw/01-articles/2026-10-10 - Agent 出现幻觉怎么治理？.md, raw/01-articles/Agent 的权限模式（Permission Mode）了解吗？.md]
last_updated: 2026-10-15
---

## 定义
Anthropic 在 2025 年 2 月推出的、原本为编程而生、运行在终端的 Agent 程序，现已能泛用到任何知识工作。

## 关键信息

### 核心特性
- **本地运行**：直接读写本地文件、使用终端、执行命令
- **Harness 工程**：业界领先的 Agent harness 设计，同样大模型效果差别极大

### 底层架构

#### Query Loop（Agent 循环核心）

Claude Code 的 Agent 循环本质是一个 **异步生成器（async generator）**，而非传统 callback 模式：

```
for await (const event of query(input)) {
  render(event)
}
```

**三大优势：**
1. **背压控制**：UI 渲染跟不上模型输出时，generator 自动暂停；callback 模式下消息堆积无法控制
2. **安全取消**：Ctrl+C 或 token 耗尽只需调用 `.return()`，callback 需逐一解绑
3. **精确终止原因**：返回 6 种终止原因（end_turn/user abort/budget exhaustion/hook intervention/max turns/unrecoverable error），调用方可直接模式匹配

**请求路径示例**（"给登录函数加上错误处理"）：
1. 用户输入 → Query Loop
2. 调用模型 API
3. 模型流式返回内容和工具调用
4. 模型指示 Read 工具读取登录函数
5. 执行结果追加历史消息 → 下一轮迭代
6. 模型指示 Edit 工具修改代码
7. 模型判断任务完成，generator 返回 Terminal

#### StreamingToolExecutor（推测执行）

Claude Code 不等待模型完整输出，只要一个工具调用的参数生成完毕且声明为并发安全，就**立即执行**。模型还在生成后续 token，文件可能已经读完。代价是极少数情况下工具调用可能白跑，但整体延迟大幅降低。

#### 自声明工具系统

每个 Tool 实现 5 个维度的接口：
- **Identity** — 名称与功能描述
- **Schema** — 参数定义（JSON Schema）
- **Execution** — 执行逻辑
- **Permissions** — 所需授权级别
- **Rendering** — 终端展示方式

类比 Spring 的 `@Component` + 自定义注解，组件自声明能力，容器只负责扫描调度。工具批处理时，并发安全的放并发组，其余的串行执行。

#### 子 Agent 机制

每个 Task 遵循状态机：`pending → running → completed | failed | killed`。AgentTool 生成 **新的 Query Loop 实例**，拥有独立消息历史、工具集和权限模式。主 Agent 和 Sub-agent 是同一个 Agent 循环的多个实例。Sub-agent 权限默认 `bubble` 模式，危险操作像气泡上浮一样上报给用户决定（类似 Java 双亲委派模型）。

### 权限模式

Claude Code 的权限系统基于**模式路由**而非条件判断。从源码来看共有 7 级模式（从宽松到严格）：

| 模式 | 行为 |
|------|------|
| `bypassPermissions` | 一切放行，不做检查（仅限内部测试） |
| `dontAsk` | 所有操作放行但记录日志 |
| `auto` | 轻量级 LLM 分类器基于上下文判断放行或拒绝 |
| `acceptEdits` | 文件编辑自动批准，其他变更需用户确认 |
| `default` | 标准交互模式，变更操作需用户确认 |
| `plan` | 只读模式，所有写操作被阻止 |
| `bubble` | 决策上报给父 Agent |

用户视角的常用模式映射：**默认模式 → default**、**Plan Mode → plan**、**Accept Edits → acceptEdits**

**auto 模式**的实现是额外跑一个轻量级 LLM 分类器，输入当前对话完整上下文，输出二元判断：当前操作是否和用户原始意图一致。比硬编码规则灵活得多。

**用户视角六模式与分类器内部细节（2026-10-14，详见 [[摘要-agent-permission-mode深度解析]]）**：
- 用户可见模式为六种：`Manual`（默认，读取不用问，编辑/命令要点头）、`acceptEdits`（自动放行文件编辑及 mkdir/touch/rm/rmdir/mv/cp/sed 七个文件命令，限工作目录内）、`plan`（只读，批准计划前一行不改）、`auto`（分类器后台审查）、`dontAsk`（无弹窗，只放行预批准工具，其余拒绝，适合 CI，仅启动参数可开）、`bypassPermissions`（全部放行，官方只建议容器/VM 内用，root 运行直接拒绝启动）。2.1.284 起未手动配置时交互会话默认 auto，Shift+Tab 切换
- **分类器实现（2.1.210+）**：默认跑在 Sonnet 5 上，不随 /model 选的模型变；能看到用户消息、工具调用和 CLAUDE.md，但**剔除工具结果**（防网页/文件藏恶意指令操纵分类器）和 **Claude 自己的输出**（防 Claude 说服分类器放行）；审查先输出一个 token 快速判断，可疑动作再用思维链复核；用户输入可放开部分拦截（明确说"强制 push 这个分支"才算授权，只说"清理一下仓库"不算）；连续拦截 3 次或累计 20 次，auto 暂停退回人工弹窗；正常操作误拦率 0.4%、越权放行率 17%（官方称 "the honest number"）
- **规则体系**：权限规则分 allow/ask/deny，判定顺序先 deny 再 ask 后 allow，第一个命中者说了算；deny 在任何模式下都生效（含 bypassPermissions），任一配置文件写了 deny 其他文件的 allow 都放不开；对根目录等关键路径 rm 任何模式不自动放行；命令跑起来后规则管不到，靠 [[沙箱]] 限制文件与网络。详见 [[权限模式]]

**优先级设计**：系统先检查 Hooks 是否配置了匹配当前操作的规则，命中则直接执行，不进入权限模式。Hook 覆盖不到的操作依然受权限模式兜底。

### 上下文管理
- `/compact`：压缩上下文，保留关键信息释放空间
- `/clear`：彻底清空上下文
- `/context`：查看上下文占比和各组件 token 消耗
- 上下文 >60% 时建议手动 /compact
- **压缩防幻觉（2026-10-10，详见 [[Agent幻觉]]）**：压缩后会从磁盘重新读取读过/改过的文件（最多 5 个，最近修改优先），项目根目录 CLAUDE.md 也从磁盘重新注入；只在对话里交代的指令压缩后可能丢失，官方建议长期规则写进 CLAUDE.md

### 记忆体系
1. **CLAUDE.md**（第一优先级，全部注入上下文）：全局级/项目级/文件夹级三层叠加
2. **Auto Memory**（第二优先级，按需注入）：后台 agent 记录 user/feedback/project/reference 四类
3. **自建参考文档**（渐进式披露）：按需加载的领域文档

### 作为 Agent Memory 的标杆实现（2026-10-13，详见 [[摘要-一文搞懂agent-memory]]）
Claude Code 被列为三条记忆工程路线中"文件系统记忆"的代表，与 [[MemGPT]]/[[Letta]]（Agent 自主管理）和 [[Mem0]]（自动化记忆服务）并列：
- **CLAUDE.md 持久化指令**：`~/.claude/CLAUDE.md` 为用户级指令，项目根目录 CLAUDE.md 为项目级规范，保存技术栈、代码规范与开发约定
- **Auto Memory 自动积累**：把部分经验与知识保存到独立 Markdown 文件，并用 `MEMORY.md` 作为索引；会话开始时加载索引中的部分内容，详细记忆按需读取
- **优势**：透明（用户可直接阅读）、简单（不必引入复杂数据库）、易于编辑维护、与开发者文件系统工作流契合
- **局限**：记忆数量大、关系复杂时，纯文件组织会遇到检索效率与维护成本问题

### 高级扩展
- **Skill**：技能包，四类（领域知识/工作流/工具组合/最佳实践）
  - Thariq 的 9 类分类法：知识、验证、数据访问、自动化、脚手架、代码审查、部署、调试、运维
- **MCP**：外部服务转接头
- **CLI 工具**：命令行工具扩展
- **SubAgent**：子 agent 并行处理
- **Hook**：条件反射式自动触发器
  - 生命周期事件驱动：SessionStart/UserPromptSubmit/PreToolUse/PostToolUse/PermissionRequest/Stop/PreCompact 等
  - 五类 handler：command（优先）/http/mcp_tool/prompt/agent（experimental）
  - 三个最小示例：Notification 通知、PostToolUse 自动格式化、PreToolUse 拦截危险命令和敏感文件
  - 详见 [[Hooks]] 和 [[摘要-claude-code-hooks-防危险命令]]
- **插件（Plugin）**：Skill + SubAgent + Hook + MCP 打包
  - **[[claude-plugins-official]]**：Anthropic 官方开源的插件应用商店（GitHub 近 3 万 Star），已内置在 Claude Code 中，通过 `/plugin install` 命令零配置安装
  - 三类插件：LSP 语言服务（TypeScript/Python/Java/Go/C++ 等）、开发工作流（feature-dev、code-review、commit-commands）、外部工具集成（GitHub、GitLab、Figma、Linear、Playwright、Vercel、Sentry 等）
  - 插件目录结构：`.claude-plugin/plugin.json`（必填）+ 可选 `mcp.json`、`commands/`、`agents/`、`skills/`
  - **[[claude-code-setup]]**：项目级一键自动化配置工具，背后通过 [[claude-automation-recommender]] Skill 扫描项目并产出 MCP/Skill/Hook/Subagent/Slash Command 五大能力的差异化推荐清单，全程只读不动文件

### 社区最佳实践与工作流范式
- **[[claude-code-best-practice]]**（GitHub 57k+ Star）系统整理 Claude Code 生态：核心能力、热门功能、工作流、Skill/Agent 精选集、83 条实战 Tips
- **[[Command-Agent-Skill编排]]**：Command 触发 → Agent 扮演角色 → Skill 提供专业能力，系统工程化的核心模式
- **[[Research-Plan-Execute-Review-Ship]]**：先研究→再计划→再执行→再审查→交付，主流工作流项目（Superpowers/Spec Kit/OpenSpec 等）共用范式
- **[[跨模型工作流]]**：通过 Plugin/MCP/Router 三种机制与 Codex、Gemini、DeepSeek 等其他模型协同
- 实战 Tips 经典两条：CLAUDE.md 单文件 ≤ 200 行；`.claude/rules/*.md` 在每个会话自动加载

### Dynamic Workflows（动态工作流）
Claude Code 提供基于 JavaScript 的可执行脚本编排能力，用于在会话内动态驱动多 Agent 协作：

- **设计范式**：代码即编排（Code-as-Orchestration），编排逻辑是图灵完备的 JavaScript 代码
- **运行环境**：Claude Code CLI 会话内，Node.js 沙箱（无文件系统/网络访问）
- **触发方式**：用户调用 `/workflow` 或使用 Workflow 工具
- **核心 API**：
  - `agent(prompt, {schema})` — 生成子 Agent 执行特定任务，支持 JSON Schema 输出校验
  - `pipeline(items, stage1, stage2, ...)` — 流式多阶段处理，无同步屏障
  - `parallel(thunks)` — 并行执行多个任务，有同步屏障
  - `phase('Verify')` — 进度分组显示
  - `budget.remaining()` — Token 预算感知
  - 支持 `isolation: 'worktree'` 隔离并行修改
- **适用场景**：快速审查 PR、多维度研究分析、一次性探索性分析
- **与 OpenClaw.NET MetaSKILL 对比**：Workflows 灵活度高适合探索，MetaSKILL 安全审计完善适合生产

### 多模态能力扩展 Skill
- **[[QianWen-AI]]**：阿里开源的 Agent 原生多模态技能包，一行命令 `npx skills add QianWen-AI/qianwen-ai` 接入 Claude Code，补齐图片生成/识别、语音合成、视频生成等多模态短板
- 8 个技能：认证（/qianwen-ops-auth）、图片生成、视觉理解（/qianwen-vision）、语音合成、视频生成、文本、模型选择、用量查询
- 详见 [[摘要-阿里开源qianwen-ai-skill项目]]

### Spring 生态专属 Skill
- **核心理念**：Claude Code 的上限完全取决于装了什么 Skill
- **搭载专属 Spring Skill 后**：变身「资深Spring架构师」，懂 Spring Boot 4.x、Spring Framework 7.x 最新规范、企业级工程最佳实践、测试闭环、AI Agent 调度
- **四大 Spring Skill 项目**：
  - [[dr-jskill]]：企业级项目脚手架技能（JHipster作者新作）
  - [[agent-skill-java-spring-framework]]：强制使用 Spring 最新 API 规范
  - [[sivalabs-agent-skills]]：统一 AI 技能封装规范
  - [[spring-testing-skills]]：自动生成全套测试用例

### Mods 实测："雨姐"面板六步搭建（2026-10-05，赛博禅心，详见 [[摘要-claude-code-mod-雨姐面板]]）
以一个拦截危险命令的"雨姐"主题 Mod 完整走通 Mod 开发闭环，补充 [[Mods]] 的实战细节：
- **三文件最小结构**：`.claude-plugin/plugin.json`（名字/版本/作者）+ `hooks/hooks.json`（指向 register.tsx）+ `register.tsx`（导出 register 函数，on 事件挂钩子）；改完保存自动热重载（`yujie: reloaded (7 hooks…)`）不用重启会话
- **事件模型**：session.start / prompt.submit / tool.call / ui.render / turn.complete 等事件上挂钩子；状态存 `$.state`，状态一变读过它的界面自动重画
- **三种钩子处理**：旁观（await next(e) 后按结果反应）/ 改写（prompt.compose 注入系统提示词段落）/ 接管（危险命令直接 deny）——**deny 的理由原样进入模型上下文，Claude 会顺着规矩把命令交还用户而不是换写法重试**
- **验证体系**：`claude plugin validate --strict` 静态列 hooks/calls（一眼看出联网/读文件/调模型权限），`claude plugin test` 事件级自动化测试（不登录不联网几百毫秒跑完）实测抓到无界面环境 bug
- **分发**：临时目录 `~/.claude/dev-mods/` → git+marketplace.json 团队安装 → 托管设置企业统一 → 公开仓库；`claude plugin marketplace add` + `claude plugin install 名字@集市`，按版本号缓存、改版本号才有更新；**Mod 不在沙箱、以用户身份运行**，安装前先 validate 看 hooks/calls
- Claude Code 内置的 `/diff` 面板本身即内置 Mod，AGENTS.md 加载、统计上报同理

### 与 Codex 对比（2026-06 苏三视角）
完整对比详见 [[摘要-codex-vs-claude-code-对比]]。核心结论：

- **Harness 哲学**：Claude Code = 本地执行 + 协作子 Agent（"并肩作战"），透明输出每一步，敏感操作要确认；Codex = 云端沙箱 + 并行子 Agent（"派任务等结果"）
- **GitHub Star（2026-06）**：Claude Code 12.4 万 vs Codex 8.3 万
- **基准测试**：
  - SWE-bench Pro（复杂任务）：Claude Code 64.3% **领先** Codex 58.6%
  - SWE-bench Verified：Codex 88.7% 微弱领先 Claude Code 87.6%
  - Terminal-Bench 2.0：Codex 82.7% 大幅领先 Claude Code 69.4%
  - 至顶 AI 实验室综合评测：Codex 91.6 > Manus 86.4 > Claude Code 82.5 > [[OpenClaw]] 79.9
- **上下文窗口**：Claude Code **1M tokens** vs Codex 200K tokens
- **Token 效率**：Codex 约为 Claude Code 的 3 倍；构建 Figma 插件 Codex 用 150 万 vs Claude Code 620 万
- **功能先发**：24 项共有功能中 **18 项 Claude Code 先发**（headless、MCP、斜杠命令、上下文压缩、subagents、hooks、skills 等），4 项 Codex 先发
- **执行环境**：Claude Code 本地机器（更灵活但有 `git push --force`、降级 Spring Boot 版本等误操作风险）vs Codex 云端沙箱（更安全）
- **额度问题**：3 分钟用掉 5 小时配额 60% 的反馈；2026-04 曾因配置 Bug 思考深度骤降 67%
- **开源**：Claude Code CLI **非开源** vs Codex Apache-2.0
- **最佳实践**：复杂重构 → Claude Code；批量并行 → Codex；组合拳互补使用

### 最佳实践要点（2026-07 最新版）

- **CLAUDE.md 保持简短**：控制在 60 行以内，硬上限 300 行；只放 Claude 可能忽略的信息（构建命令、测试命令、分支规范）；能从代码推断的不要写进去；关键规则用标签包裹；运行 `/doctor` 检查冗余指令
- **分阶段工作流**：理解代码库 → 修改；先规划 → 再实现；生成 → 验证；不要把所有步骤压缩到一个大提示词里
- **3-5 分钟能完成的小任务，直接用原生 Claude Code**，复杂工作流适用于多文件多步骤的大任务
- **模型选择策略**：日常编码用 Sonnet 5（默认，1M 上下文，性价比最高）；复杂架构设计切 Opus 4.8；极限推理切 Fable 5；`/model claude-fable-5` 临时切换；配置 `fallbackModel` 防主模型不可用
- **重复性监控用 /loop**：`/loop 5m 检查 staging 部署是否完成`，间隔支持 `5m`/`30s`/`1h`；`/proactive` 是别名；按 `Esc` 取消；远程会话不受持续唤醒
- **输出复杂结果用 Artifacts**：依赖 `project-artifact` 插件，发布到 claude.ai 私有链接，适用 PR 走查、数据仪表盘、文档输出；Team/Enterprise 计划 beta 可用
- **调试：粘贴 bug，说"fix"**：不要指导怎么修，不要猜测原因，管得越多越容易带偏
- **两次失败 = /clear 重启**：同一个问题修正超过两次就重启，上下文污染会降低性能；用 `/rewind` 回退到 /clear 之前
- **走偏了按 Esc Esc 或 /rewind 回滚**：不要在同一上下文中纠正偏差
- **要求重写平庸方案**：说"知道你现在知道的一切，抛弃这个，实现优雅的解决方案"
- **上下文 50% 时手动 /compact**：60-70% 时性能明显下降，不要等自动压缩；`/compact focusing on API changes` 指定压缩策略；Sonnet 5 拥有 100 万 token 窗口
- **切换目录用 /cd 不要用 /clear**：不会破坏提示缓存，上下文窗口不受影响
- **Checkpoints**：每次操作自动创建，可独立回滚对话或代码，跨会话持久化，不是 git 替代品
- **子智能体**：专用子智能体 > 通用 mega-agent；子智能体有独立上下文窗口，防止污染和偏见；可嵌套最多 5 层；后台子智能体可重启后自动恢复
- **Skills 管理**：技能是文件夹结构（SKILL.md + references/ + scripts/ + examples/）；渐进式披露，Claude 只在需要时读取子目录；一行可调用最多 5 个技能；嵌套 Skills 自动按路径加载
- **Gotchas（坑点记录）**：每次 Claude 犯错时记录失败模式；包含问题/表现/修复/预防四要素；出现 3 次以上转化为正式规则；超 30 天未出现移到归档区
- **权限与安全**：`deny` 比 Hooks 更安全（deny 后文件对 Claude"不可见"）；权限评估顺序 deny → ask → allow；`--dangerously-skip-permissions` 仅限封闭无网络环境；`disableBypassPermissionsMode: true` 全局禁用
- **三重栈组合**：OpenSpec 管 WHAT，Superpowers 管 HOW，Claude Code 负责执行；CLAUDE.md 中路由规则避免重复

### 8 大常见陷阱

| 陷阱 | 表现 | 缓解方法 |
| --- | --- | --- |
| 过早放弃 | "已实现大部分功能，但 XX 不工作" | 拆分任务为更小单元 |
| 上下文压缩后变笨 | 忘记之前纠正的错误 | 50% 手动 /compact，必要时 /clear |
| 初始测试质量差 | 测试看起来对但实际失败 | TDD 模式，仔细审查测试 |
| 修改测试而非代码 | 降低测试标准匹配错误代码 | 严格审查测试变更 |
| 忘记编译 | 测试失败因为未编译 | CLAUDE.md 中明确编译步骤 |
| 工作目录混乱 | 留下测试脚本、构建产物 | git status 检查，手动清理 |
| Git 操作危险 | 错误的变更合并到 PR | 人工执行 Git 操作 |
| 重写但不删除旧代码 | 新旧代码共存 | 审查 diff 确认删除 |

### 四件套工程化与判断权边界（《Claude Code 实战》视角，2026-10，详见 [[摘要-claude-code四步差距]]）
同款工具同款模型下效率差距的根源是"把工程经验外化成机制"，四件套 = [[CLAUDEmd]]（三层体系，禁止事项优先）+ [[Hooks]]（软约束变纪律，2 秒内返回，把关人非拦截器）+ [[AgentSkills]]（渐进式披露，description 决定自动触发）+ [[子Agent编排]]（任务书写全、git worktree 隔离；**单任务 >20 分钟且弱依赖才并行**，3 个子 Agent 即 3 倍 token）。工具假设对比：Copilot 假设"知道怎么写只是手速慢"、[[Cursor]] 假设"知道改哪里"、Claude Code 假设"瓶颈是把想法变成跨文件实现"——心态应是"30 秒给出 80% 可用草稿"。上下文地基：窗口如固定桌面、每轮回车整段重新打包故无跨轮记忆，污染四症状（记错/重复否定/废话/变慢）出现前两个即处理；决策树：任务完成且无关 /clear、完成且相关 /compact、死循环 /clear；跨天写 session-notes.md 快照后 /clear 重开。**判断权不能外包**：架构选型、安全评审、产品决策三类任务让 AI"梳理利弊不给推荐"，人做决定。

### 学习路线（三阶段）
[[摘要-claude-code-learning-roadmap]] 将 Claude Code 学习拆成三层：
- **青铜级**：完成安装、启动、项目理解、代码生成、Bug 修复等日常任务，目标是“一天上手”。
- **白银级**：通过 [[CLAUDEmd]]、Thinking Mode、计划模式、提示词四要素和 [[Skill]] 定制 Claude Code，使其遵守个人和项目工作方式。
- **王者级**：使用 Subagents、[[MCP]] 和自动化流水线，让 AI 参与需求分析、方案设计、实现、测试、代码审查和部署。

该路线强调开发者角色从“手敲代码”转向“定义目标、拆分任务、审查验证和指挥 Agent”。

### 适用场景
- ✅ 大型代码库深度重构（SWE-bench Pro 领先）
- ✅ 需要超长上下文（1M tokens）
- ✅ 喜欢协作式体验（每一步都输出）
- ✅ 追求最新功能（迭代节奏快）
- ✅ 需要 Agent Teams 间通信
- ✅ 团队已有 Anthropic 生态

- @文件引用、图片拖拽、斜杠命令（/help /model /btw /simplify 等）
- `!` 前缀进入 bash 模式
- Ctrl+B 后台运行命令
- Mac: Option+Enter 换行，Windows: Ctrl+Enter 换行

### 代码搜索方式（Agentic Search）
- 使用 **Glob + Grep + Read** 三工具组合，而非 RAG
- 早期版本曾用 Voyage Embedding RAG，后全面替换为 Agentic Search
- 三个工具均 `isConcurrencySafe = true`，可并行执行
- Grep 底层为 ripgrep，中型仓库搜索约 200ms
- LLM 自身充当 Reranker，多轮迭代式搜索

### 实践经验（二师兄总结）
1. 能用插件/Skill 尽量用，工业标准化规避幻觉
2. 工程师需具备 Leader 能力（拆分任务→描述→管理→验收）
3. 任务拆分越细越好，减少幻觉空间
4. 培养完全 AI Coding 感觉
5. 编程经验依旧重要，需判断 AI 方案利弊
6. 培养产品感觉，行业 Know-How 被放大

## 作为 DeepSeek-V4.1-Flash 最佳 Harness 搭档（2026-09-17，详见 [[摘要-deepseek-v4-1-flash-harness横评]]）
[[老章]] 用 [[SimonWillison|Simon Willison]] 的 Space Invaders 原题横评 [[DeepSeek-V4.1-Flash]] 在四种 Harness 下的表现，**Claude Code 综合排名第一（9.2 分）**：
- 交付质量、代码准确率、工程完整性均第一
- 上下文管理极其精炼：仅用 Pi Agent 约 1/3 的 Token（3.0M vs 9.7M）和 1/4 的耗时（9分34秒 vs 36分09秒）拿到全场最优效果
- 最懂原版：街机竖屏/飞碟/掩体破损等细节齐全，外壳和数据面板专业
- 定位：生产级工业落地 ROI 最高标杆
- DeepSeek 技术文件指出"Claude Code 或 Codex 接 DeepSeek-V4.1-Flash，开箱即用接近峰值"

对比：Pi Agent 视觉效果最强但 Token 全场最高（9.7M）；DSH 标准速度最快（8分54秒）但复杂任务弱；DSH 极简省 Token 但最终失败。

### 开放 Agent SDK（2026-09）
Anthropic 去年 9 月将 Claude Code SDK 扩展为通用 Agent SDK，今年补上企业插件生态和 Managed Agents，走"模型往外长"（[[ProductOverhang]]）路线。与 [[OpenAI]]（开放 Codex Harness）、[[腾讯]]（开放 WorkBuddy 基座）方向一致。详见 [[摘要-中美头部agent走向开放]]。

### 多 Agent 成本与分层模型路由（2026-09）
来自 [[摘要-claude-code-多agent账单分层路由]]。Claude Code 的多 Agent 是自动决策创建的：一条指令可拆出 3-5 个独立子 Agent，各自上下文各自计费，一次"轻量任务"账单可翻 3-5 倍。解法是重指内部「模型级别 → 实际模型」路由层：`ANTHROPIC_BASE_URL` 指向 DeepSeek Anthropic 兼容端点，Opus/Sonnet 级绑 `deepseek-v4-pro[1m]`，Haiku 级用 `ANTHROPIC_DEFAULT_HAIKU_MODEL` + `CLAUDE_CODE_SUBAGENT_MODEL` 显式绑 `deepseek-v4-flash`（两变量同时配，覆盖自定义与内置 Explore 子 Agent）。实测 240 万 token 重构任务：全 Sonnet 4.6 约 $22.4 → 分层路由折扣后 $1.29（约 1/17）。踩坑：兼容端点不支持图片输入（可 `--model claude-sonnet-4-6` 临时切回或用 claude-code-router 自动路由）、模型名写错静默 fallback、`[1m]` 不加只有 200K 上下文、Agent YAML `model` 字段区分大小写、base URL 末尾不能加 `/v1`；也可写进项目 `.claude/settings.json` 的 `env` 字段只对单项目生效。详见 [[模型路由]]、[[Subagent]]。

### Agent 视图与 /goal 目标收敛（v2.1.139，2026-09）
来自 [[摘要-claude-code-agent视图与goal]]。**Agent 视图**（`claude agents`）由独立 Supervisor 进程托管后台会话，与终端解耦、冷热分离、自动 worktree 隔离，状态含 Needs input/Working/Completed 并直接显示 PR + CI 状态——人从"盯着屏幕按 Enter"转为"派任务+扫一眼"，详见 [[agent-view]]。**`/goal`** 引入目标状态收敛执行模型：每个 turn 结束自动评估是否达标，不满足自动继续，控制权从用户转给模型，与 Kubernetes Reconcile Loop 同构但基于语言判断，因此目标必须写成可机器验证的命令（如「curl 返回 ok 且 npm test 无失败」），详见 [[goals]]。配套：MCP Server 自动接收 `CLAUDE_PROJECT_DIR`、`claude plugin details` 输出插件 token 成本、`/context all` 按模型分词器精确计数。坑：多后台会话配额是乘法、机器睡眠中断需 `claude respawn --all`、worktree 残留需清理。

### Skill 设计的 7 大反模式（2026-09）
来自 [[摘要-claude-code-skill-7大反模式]]：SKILL.md 写成长篇 prompt、description 写成功能介绍而非触发条件、工具调用写进 Skill（应走 MCP）、多 Skill 边界重叠、不写 Gotchas、示例用伪代码、不分项目级/用户级。完整清单与 frontend-design 正面拆解见 [[Skill]]。

### Skill 与 MCP 的上下文开销权衡（2026-10，详见 [[摘要-claude-code-mcp-unity游戏]]）
来自 Unity 实战总结的 context 治理经验：**Skill 每次调用仅占约 8 个 token**、按需加载平时不占窗口，而 **MCP 工具开销重且常驻 prompt**（无论是否使用）——装多了模型智能明显下降。实践建议：优先 Skills 而非 MCP 工具；用不到的 MCP 工具（Gmail、Calendar 等）在 `/mcp` 里禁掉；任务间 `/clear`。该文用"薄服务器+动态注册"的 GameDev-MCP-Server 从空文件夹做出可玩 Unity 游戏（见 [[UnityMCP]]）。

### Mods 事件扩展能力（v2.1.287，2026-10，详见 [[摘要-claude-code-mods机制]]、[[Mods]]）
Anthropic 在 v2.1.287 推出 **Claude Mods**：用 TypeScript/JavaScript 进程内函数挂载到事件流上，执行观察（Observe）/改写（Rewrite）/接管（Answer）三类操作，类中间件管道（Middleware Chain），并可在终端/桌面绘制自定义界面。与 Skills（Markdown 教模型）、MCP（外部工具）、Settings Hooks（外部脚本）四者互补协同。**架构演进信号**：内置能力已开始以 Mod 形式交付（/diff → cc-plugin-diff、AGENTS.md 加载 → cc-plugin-agents-md），官方计划把更多内置功能迁移为 Mods、让宿主缩减为小 Core 按需装配——与 [[DeepSeekHarness]] 的"一切皆插件"方向相似但 API 完全不兼容（前者服务契约级组件插拔，后者会话流水线事件拦截）。**安全要点**：Mods 无沙箱、行使当前用户 OS 权限，Mod 自启进程在 Bash 沙箱之外；不能改绘权限提示框；企业可经 cc-plugin-sec-default + `allowManagedModsOnly` 管控。

### 第三方解锁补丁 ClawGod（2026-10，详见 [[摘要-clawgod解锁claude-code]]）
开源 GPL-3.0 补丁工具 [[ClawGod]] 一行命令修改本地 Claude Code 客户端：伪装内部用户解锁 Opus 4.6 + 1M 上下文、解锁 Agent Teams、删除安全话题拒答等三条内部限制、用本地 JSON 覆盖功能开关、支持自定义 apiKey/baseURL；`claude --uninstall` 可恢复原版（保留 `claude.orig`）。属**第三方非官方修改**，会放大 prompt 注入与误操作风险，与本页所述官方权限体系（deny→ask→allow、Hooks 优先）方向相反，引用时须区分。

## 关联连接
- [[摘要-60分钟全面掌握Claude-Code]] — 来源
- [[摘要-6条Claude-Code实践经验与思考]] — 来源
- [[摘要-中美头部agent走向开放]] — 来源（开放 Agent SDK）
- [[摘要-agent-hallucination-governance]] — 来源（幻觉治理：压缩重读、Stop hook、Sub-agent 审查）
- [[摘要-一文搞懂agent-memory]] — 来源（作为"文件系统记忆"路线标杆）
- [[AgentMemory]] — 上位概念
- [[MemGPT]] / [[Letta]] — Agent 自主管理路线对照
- [[Mem0]] — 自动化记忆服务路线对照
- [[Agent幻觉]] — 治理机制所属的概念框架
- [[Codex]] — 对标产品
- [[Anthropic]] — 所属公司
- [[Agent]] — 核心概念
- [[CLAUDEmd]] — 指令系统
- [[AutoMemory]] — 自动记忆
- [[Skill]] — 技能扩展
- [[SkillCreator]] — 元技能创建工具
- [[meta-skill]] — 元技能概念
- [[摘要-为什么Claude-Code不用RAG检索代码]] — 来源
- [[摘要-claude-code-springboot-skills]] — 来源（Spring Skill 实战）
- [[摘要-claude-code-plugins-official]] — 来源（官方插件市场开源）
- [[摘要-claude-code-setup-plugin]] — 来源（一键配置插件）
- [[摘要-claude-code-best-practice]] — 来源（57k+ Star 最佳实践仓库）
- [[claude-code-setup]] — 官方一键配置插件
- [[claude-automation-recommender]] — 配置推荐 Skill
- [[claude-plugins-official]] — 官方插件市场
- [[claude-code-best-practice]] — 社区最佳实践仓库
- [[Command-Agent-Skill编排]] — 工作流核心架构
- [[Research-Plan-Execute-Review-Ship]] — 五阶段开发范式
- [[dynamic-workflow]] — 动态工作流概念
- [[跨模型工作流]] — 多模型协同范式
- [[AgenticSearch]] — 代码搜索范式
- [[Ripgrep]] — Grep 底层工具
- [[BorisCherny]] — 首席工程师
- [[Thariq]] — 工程师，分享 Skills 使用经验
- [[Cursor]] — 对比产品（混合检索）
- [[MCP]] — 外部服务协议
- [[AICoding]] — AI 编程范式
- [[Greptile]] — 开发者工具公司
- [[spring-skill-usage-guide]] — Spring Skill 使用时机与组合策略
- [[摘要-Claude-Code-Workflows-vs-MetaSKILL]] — 来源
- [[摘要-codex-vs-claude-code-对比]] — 来源（2026-06 苏三视角对比）
- [[LoopEngineering]] — 循环工程方法论
- [[摘要-claude-code-learning-roadmap]] — 来源（三阶段学习路线）
- [[摘要-loop-engineering-guide]] — 来源
- [[摘要-沉默王二-claude-code-底层深扒]] — 来源（源码架构深扒）
- [[沉默王二]] — 作者
- [[计划模式]] — Plan Mode 概念
- [[ContextManagement]] — 上下文管理
- [[摘要-claude-code-best-practice-最新版]] — 来源（2026-07 最新最佳实践）
- [[摘要-ai-agent-抓包协作]] — 这是一篇 SegmentFault 上的技术提问帖，询问在使…
- [[摘要-Codex保姆级入门教程]] — 本文是 Codex 的保姆级入门教程，系统讲解了这款由 Op…
- [[摘要-doubao-seed2-1-pro-douyin]] — 摘要-doubao-seed2-1-pro-douyin
- [[摘要-claude-code-实战防搞炸]] — 来源（程序汪实战经验）
- [[摘要-claude-code-hooks-防危险命令]] — 来源（程序汪 Hooks 实战教程）
- [[auto-mode]] — 权限自动模式
- [[QianWen-AI]] — 多模态能力扩展 Skill
- [[摘要-阿里开源qianwen-ai-skill项目]] — 来源
- [[摘要-agent-skills-经济学-月增5万星]] — 来源（Skills 经济学）
- [[摘要-agent-skills-普通人教程-龙叔]] — 来源（普通人 Skill 教程）
- [[mattpocock-skills]] — 月增 5 万星的技能包仓库
- [[摘要-deepseek-v4-1-flash-harness横评]] — 来源（DeepSeek V4.1-Flash 最佳 Harness 搭档）
- [[DeepSeek-V4.1-Flash]] — 接入的最佳搭档模型
- [[老章]] — 横评作者
- [[DeepSeekHarness]] — 横评中对比的 DSH 标准/极简模式
- [[ProductOverhang]] — 开放路线概念
- [[OpenAI]] — 同步开放 Harness
- [[腾讯]] — 同步开放基座
- [[摘要-claude-code-多agent账单分层路由]] — 来源（子 Agent 分层路由降成本）
- [[摘要-claude-code-agent视图与goal]] — 来源（Agent 视图与 /goal）
- [[摘要-claude-code-skill-7大反模式]] — 来源（Skill 反模式）
- [[agent-view]] — 后台会话管理界面
- [[模型路由]] — 分层模型路由概念
- [[码哥字节]] — 三篇文章作者
- [[摘要-claude-code-mcp-unity游戏]] — 来源（Skill 与 MCP 上下文开销权衡、Unity 实战）
- [[UnityMCP]] — 该实战使用的 MCP 服务器
- [[摘要-clawgod解锁claude-code]] — 来源（第三方解锁补丁）
- [[ClawGod]] — 修改本地客户端的开源补丁
- [[摘要-claude-code-mods机制]] — 来源（Mods 机制与四扩展选型）
- [[Mods]] — v2.1.287 新增的进程内事件扩展机制
- [[摘要-claude-code-mod-雨姐面板]] — 来源（雨姐面板六步实测）
- [[摘要-手搓claude-code-面试]] — 12 层架构手搓 Claude Code 的面试纪实来源
- [[摘要-claude-code-8问最狠难题怎么破]] — Skill/MCP/代码图谱八大排障来源
- [[摘要-claude-code四步差距]] — 来源（四件套工程化与判断权边界）
