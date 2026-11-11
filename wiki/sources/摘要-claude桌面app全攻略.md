---
title: "摘要-claude桌面app全攻略"
type: source
tags: [来源, 原始文件, ClaudeCode, 桌面端, Agent工具, 教程]
sources: [raw/09-archive/Claude(Code)桌面APP，保姆级全攻略，一期视频精通.md]
last_updated: 2026-11-11
---

## 核心摘要

技术爬爬虾（2026-11-10，视频教程 11 章）系统拆解 Claude 桌面端"完全体"：已把 Claude Code（编程）、Claude Design（设计）、Claude Cowork（办公）全部收进同一个桌面客户端，配 Opus 5.5 可称"地表顶级 Agent 工具"。

**1. 接入国产模型（免官方订阅）**：设置 → 故障排查 → 启用开发者模式 → 开发者 → 配置第三方推理（Credential 选 static API key）→ 填 DeepSeek API key + Anthropic 兼容 Base URL，开启百万上下文 → 模型列表按映射配置（Claude Opus 开头→DeepSeek V4 Pro，Claude Sonnet 开头→DeepSeek Flash，如填 `claude-sonnet-5.5`）→ Apply changes 重启。限制：无内置浏览器、无 Claude Design/PPT/Excel 等功能，功能不全。

**2. 三栏布局与三种模式**：左对话列表 / 中对话窗口 / 右多功能区。**Chat**（对话 Agent：问答/解释代码/翻译/查资料，不操作本地电脑）、**Cowork**（通用办公 Agent：调研/分析文件/文档报表 PPT）、**Code**（软件开发 Agent：改代码/跑命令/测试/修 bug）；新 UI 灰度把 Chat 与 Cowork 合并为"Claude + Code"两按钮，Claude 会自动判断工作类型。实测 Code 比 Cowork 更强更主动，多数场景建议直接用 Code。三种模式都消耗订阅额度（含网页端聊天）。

**3. 工作区**：Code 模式叫 **Environment（环境）**，Cowork 模式叫 **Project（项目）**；环境可设环境变量（如 `OPENAI_API_KEY`，不污染全局）、选多个工作文件夹（前后端分目录）。

**4. 云端工作环境**：先配 GitHub 连接器（Customize → Connectors → GitHub Connect）→ 创建环境时选云端 + GitHub 仓库 → 四个选项：网络访问（默认白名单，可全开）、密钥、环境变量、setup script（每次启动云端环境先跑）→ Add Environment。云端环境关掉本地桌面端也在后台跑，网页端也能指挥。

**5. 模型、思考强度与权限**：编程/创意/高难度任务用 Opus 5.5（AA 榜单上 Fable 5.1 评分不如它）；普通任务 Sonnet；简单重复任务 Haiku（智力高于多数开源模型、成本极低）。Effort 思考强度：Opus 选 medium/high 足够。权限：**Auto**（自动审查放行/拦截高危命令，效率与安全平衡最好，默认不启用沙箱）+ **Plan**（先出计划等确认再改代码）两种。

**6. 用量限额**：5 小时限额 + 周限额，任一到达上限即不可用；See all 可看各模式消耗（最多是 Claude Code，其次对话）。

**7. 三种追加指令**：**Steering**（默认，回车发送，执行完当前工具调用后读取新指令调整后续）、**Queue**（Ctrl+Enter，整轮完成后才读取，排队）、**Send Now**（直接打断当前工具调用插入新指令，最激进，用于纠正错误方向）。

**8. 后台任务**：耗时任务（如渲染视频）主会话直接停下、启动后台任务执行，完成发通知回主窗口继续——**等待过程零 Token 消耗**，是相对其他 Agent 的关键优势。

**9. Session Rail 对话侧边栏**：顶部环境与工作文件夹 / 中间 **Context**（系统工具、对话历史、MCP 工具、系统提示词等上下文占用明细）/ 底部 **Outputs**（改动的代码、生成的图片等产物）。建议上下文不要超过 50%（过大导致注意力下降与 Token 消耗快）；可用 `/compact`（可附"重点保存哪些信息"）手动压缩，实测 39%→8%。Remote Control 开关可让手机端接管对话。

**10. 计划模式小项目实战 + 侧边栏工具**：Plan 模式做宠物洗护预约网站（弹窗卡片确认生图方式与数据存储，输出计划→确认→分步执行→启动 Server 可启停）；侧边栏 **Terminal**（本机 PowerShell）、**Changes**（相对 main 未提交改动）、**内置浏览器**（元素选择器可直接把页面元素信息贴进对话，"把按钮调大一点"即可）、文件列表。

**11. 回滚与并行开发**：**Rewind**（Revert 三选项：回退代码+对话 / 只回退对话 / 只回退代码；基于文件快照不依赖 Git；只能回退 Claude 直接改的文件；连按两次 Esc 触发）。**Fork**（会话分叉，只分叉对话历史不分叉代码）+ **Git Worktree**（创建新分支并复制代码到新文件夹，主干与 Worktree 并行开发、可合并回主干）；新建 Session 时可直接勾选 Worktree。**`/btw`** 开 Side Chat 侧边对话（可看主线上下文但不污染、不中断主线；Ctrl+; 快捷键）。**Split View** 分屏（拖拽形成左右/上下/4 视图/3 列）。**Nested Session 嵌套会话**（主 Session 拆多个子 Session 并行，如查询 5 个州天气；类似 Sub Agent 但每个子会话做什么一目了然；可 Detach to top level 提升为平级；官方趋势将逐渐取代 Sub Agent，详见 [[NestedSession]]）。

**12. 记忆系统（两套完全独立）**：
- **Code 模式**：项目级 `CLAUDE.md`（`/init` 自动生成，建议 ≤200 行，可按前后端拆分并在主文件留指针）；**更推荐 `AGENTS.md`**（所有 Agent 通用，Codex/WorkBuddy 也能读）；全局记忆在 `~/.claude/CLAUDE.md`（对所有项目生效）；还有一套隐藏的"按项目隔离"记忆（每条一个 Markdown），但 Claude 很少主动写
- **Chat/Cowork 模式**：设置 → Your Claude 填记忆 + Memory 开关（允许搜索历史对话、从历史总结记忆），**只对 Chat/Cowork 生效**

**13. 浏览器自动化与 Computer Use**：
- **Chrome**：装 Claude 扩展 + 设置开启 Claude in Chrome；支持黑名单（允许所有+禁用站点）与白名单（禁止所有+允许站点）；优势是自带登录状态
- **内置浏览器**：调试网页更顺手（看网络请求/控制台），开发测试优先用；Cookie 三档 Until quit / Shared（长期保留）/ Per session
- **Computer Use**：鼠标键盘操作软件，Denied apps 可禁某些应用；**慢且费 Token**，官方优先级：连接器 > Bash > Chrome > 最后才是 Computer Use

**14. Claude Design 与 Design System**：Claude Design 已整合进桌面端（Artifacts → Design），自然语言生成 UI/原型/信息图/海报，画布可直接编辑元素。Design System 固化配色/字体/图片等规范批量产出统一风格资产。三段式：准备 `DESIGN.md`（文字规则手册，可从 GitHub「Awesome Claude Design」下载各厂商设计语言）→ 转成 Design System → 拼装成设计成品。实战：把 Anthropic 官网文章转成继承其设计语言的 HTML 互动 PPT。

**15. Artifacts**：
- **Docs**：类似飞书云文档，人与 AI 共同编辑，可插入日期表格/甘特图/任务看板/图表/流程图/四象限/图片/待办，可 Share 与导出 Word/PDF
- **Slides**：PPT，元素可直接改，可导出 PPTX
- **Dashboard**：数据看板（热力图/柱状图/表格），**数据是活的**——提供实时数据源后可设定时刷新（Routines 里可见，Run now 手动跑）

**16. Skills**：Skill = 带目录的专业说明书。安装：项目 `.claude/skills/`（注意 Claude 只认 `.claude`，其他 Agent 可写 `.agents`）→ `/reload-skills` → `/` 调用；全局放 `~/.claude/skills/`。自写：用 `anthropic-skills:skill-creator` 元技能 + 给足工具（语音识别模型/API key）+ 真实验收样本，生成的 `SKILL.md` 文件夹可复制到全局。

**17. 连接器**：Customize → Connectors，可接 Google Drive/Gmail/日历、Supabase（云端 Postgres）、Vercel（零成本部署）；实测把本地宠物店应用改造成 Supabase 云数据库并部署到 Vercel 上线。

**18. Claude Code Project（AI 主导并行工作流，上月新功能）**：注意与 Cowork 的 Project 不同——Code 的 Project 是一套 AI 主导的任务编排：给目标（如"优化性能与导出速度/UI 性能"）→ 选 GitHub 远端仓库（云端开发环境是理想形态）→ Claude 自动分析并建 Thread（线程）调查 → 协调员拆出多个 Thread 并行工作 → 各线程完成后询问是否推送并开 PR → 在界面审代码、Merge；冲突可交回更熟悉该代码的线程处理。价值：**不用手动管理 Session，给任务即可自动拆解并行**。

## 关联连接
- [[ClaudeCode]] — 主题实体（桌面端完全体）
- [[技术爬爬虾]] — 作者
- [[NestedSession]] — 嵌套会话机制（本文详解）
- [[CLAUDE-md]] — 项目记忆文件（本文补 AGENTS.md 推荐与全局/隐藏记忆）
- Claude Design — 设计能力（无独立页，见本页与 ClaudeCode 页）
- [[Skill]] — 能力扩展机制
- [[MCP]] — 连接器相关生态
- [[ComputerUse]] — 电脑自动化
- [[Worktree]] — 并行开发隔离
- [[上下文压缩]] — /compact 手动压缩
- [[Subagent]] — 被 Nested Session 逐步取代的旧机制
- [[Opus]] — Opus 5.5 模型
- [[DeepSeek]] — 第三方推理接入示例
- [[GitHub]] — 云端环境与 PR 工作流
- [[Vercel]] / Supabase — 连接器示例（无独立页）
