---
title: "OpenAI"
type: entity
tags: [AI公司, OpenAI]
sources: [raw/01-articles/40分钟学会Codex！"零基础"终级教程～【附完整文档】.md, raw/01-articles/连 Karpathy 都开始恐慌：AI 正在重新定义「程序员」｜ 硅基时间.md, raw/01-articles/2026-09-06-实测GPT-6 Astra：曾经的那个OpenAI，回来了。.md, raw/01-articles/2026-09-05 - GPT-6 最让人后背发凉的，不是它变强了，而是它开始自己训练自己.md, raw/01-articles/2026-09-07-"GPT-6 Astra 正式登场"会怎样改变现有技术栈？.md, raw/01-articles/2026-09-15-OpenAI 总裁最新采访：现在所有人对 AI 的预测，大概率都是错的.md, raw/01-articles/2026-09-18-为什么中美头部Agent，不约而同走向开放？.md, raw/01-articles/2026-09-24-A社O社，坐不住了.md, raw/01-articles/2026-09-30-OpenAI连放20多个大招：GPT-6.1-Sol价格砍掉80%，自带云电脑的Dots彻底颠覆打工逻辑.md, raw/01-articles/2026-10-09-OpenAI宣布攻破数百个难题，"数学之死"担忧成真？.md, raw/01-articles/2026-10-12-模型长出交互界面，“手搓”AI应用要全面退潮了？.md, raw/01-articles/2026-10-12-从 0 到 1：Electron41 + Vite8 + OpenAI SDK 接入 DeepSeek-V4.1-Flash 桌面端AI系统 - yxybox.md]
last_updated: 2026-10-13
---

## 定义
美国 AI 研究公司，推出了 Codex（桌面 Agent）和 ChatGPT 等产品。联合创始人包括 Andrej Karpathy。

## 关键信息
- **OpenAI SDK 成为跨模型标准接口**：第三方模型与本地推理服务普遍提供 OpenAI 兼容端点，桌面/终端客户端直接用 OpenAI SDK 接入（如 Electron + OpenAI SDK 接 DeepSeek-V4.1-Flash，详见 [[摘要-electron41-vite8-deepseek桌面ai]]）；[[DeepSeekHarness]] 等 Harness 也因此"认 OpenAI 兼容端点、不绑定自家 API"
- ChatGPT 手机端可远程操控电脑上的 Codex
- 提供 GPT-4o 系列模型
- Codex Pro 会员 $20/月，额度较大方
- **Vibe Engineering 内部实践**：
  - 工程师对 Codex 采用率超过 92%
  - 所有内部 PR 都由 Codex 审核
  - 用 Codex 的工程师产出的合并 PR 比不用的人多 70%
- **核心团队成员**：Romain Huet（开发者体验负责人）、Aaron Friel（工程师）
- **GPT-6 Astra**（2026-09-03 发布）：详见 [[GPT-6]]，ARC-AGI-3 从 7.8% 提升至 99.9%，总裁 Brockman 称"Welcome to the AGI era"，首款让前代模型参与训练监督的前沿大模型
- **Stargate 基地**：得州，GPT-6 预训练动用超 10 万块 GPU（GPT-4 约 2.5 万块）
- **GPT-6 Astra 技术栈影响**（2026-09-07 分析）：只支持 [[ResponsesApi]]，推动后端升级为 [[AgentRuntime]]、前端升级为 [[TaskConsole]]、安全升级为 [[AIControlPlane]] 独立层，成本管理从 Token 转向 [[任务级成本]]（详见 [[摘要-GPT-6-Astra改变技术栈]]）
- **Codex 公开用户里程碑**（2026-09-08 统计，各阶段口径不完全一致）：5 月底 500 万 → 7 月 22 日 1000 万 → 8 月底 2500 万。同期 4—8 月共 36 次公开额度重置，其中 61.1% 并非故障补偿，而是庆祝、产品节点与临时重置，构成一套[[事件营销]]机制（详见 [[摘要-codex重置的真正原因]]）
- **Greg Brockman 访谈（2026-09 a16z）**：详见 [[摘要-OpenAI总裁Brockman最新采访]]
  - **AGI 时代已到来**：Astra 能连续运行 24 小时、跨越非常广泛的领域完成任务
  - **15→10→9 年推算**：2016-2017 与 Ilya Sutskever 推算顺利 15 年/大规模投入 10 年，实际约 8-9 年
  - **Astra 跃升关键在 [[ComputerUse]]**：让 AI 直接用人类界面，不需任何特殊 API 或重新设计系统，2015-11 内部会议就讨论过
  - **10000 agent 并行解决 [[NavierStokes]]** 并形式化成 [[Lean]] 格式——AI 开始创造新知识而非整合已有知识
  - **[[DefenderWindow]] 防御者窗口**：Hugging Face 事件后 AI 网络攻击能力已强，现在是防御者黄金期。Brockman 用 Codex 对个人网站做渗透 15 分钟找到 13 个漏洞、45 分钟自动修复。OpenAI 抽调 25% 生产工程师做安全升级，目标建 [[DefenseFactory]]
  - **[[FrontlineDefenders]] 10 亿美元计划**：为医院、水务公司、政府关键基础设施提供免费/折扣 AI 安全工具
  - **AI 真正形态不是文本框**：语音优先 + 持久记忆 + 主动 + 可依赖；北极星"简单"
  - **10 亿周活 + 15 亿弃用用户**是重要信号——AI 应主动告诉用户"我可以在这件事上帮你"
  - **就业判断**："AI 发展几乎不按逻辑推断方式发展，你对未来的预测大概率是错的，而且会以你没想到的方式错"。创业浪潮会来，[[问责制]] 是人类应保留的
  - **精力分配**：2026 年取消了 [[Sora]] 项目以解放专注力，遵循《The Score Takes Care of Itself》哲学

### 开放 Codex Harness（2026-09-10）
OpenAI 将 Codex 背后的 [[Harness]] 做成托管服务开放公测（一个月前已开源核心代码），把原本只供自家产品使用的系统变成别人开发 Agent 的起点。开放路径是"模型+Harness+托管运行连成一体"（Agent 的 AWS 时刻）。与 [[Anthropic]]（Claude Code SDK 扩展为通用 Agent SDK）、[[腾讯]]（开放 WorkBuddy 基座）方向一致。详见 [[摘要-中美头部agent走向开放]]。

### GPT-6 Sol / Luna 降价（2026-09-22）
Anthropic 发布 Claude Opus 5.5 约一个半小时后，OpenAI 连推 **GPT-6 Sol** 与 **GPT-6 Luna**，把"便宜"当卖点（构成 [[大模型价格战]]，详见 [[摘要-a社o社价格战]]）：Sol 每百万输入/输出 token 降至 2/10 美元，为上一代 GPT-5.6 Sol 的一半，官方强调是长期定价而非促销；Luna 输入 0.2→0.1 美元、输出 1.2→0.5 美元，最高降幅 58%。两款沿用 GPT-6 Astra 的训练方法，把 Astra 的专业工作/编程/计算机使用能力下放；Sol 事实错误数量约为上代一半。分档逻辑：Astra 保留最高能力定位，Sol/Luna 承接数量更多、价格敏感的日常调用。商业压力：年化收入 8 月超 400 亿美元，但 2026 Q2 经营亏损从 93 亿扩大到 123 亿美元，已秘密递交上市申请，赌的是用量涨得比价格降得快。

### DevDay 2026（2026-09-29，连发 20+ 更新）
开场公布 **ChatGPT 周活跃用户突破 12 亿**，主线是终结"人工敲 Prompt"的旧时代、走向 7×24 自主协作生态（详见 [[摘要-openai-devday-2026-gpt61sol-dots]]）：
- **[[Dots]]**：自带独立云电脑的常驻自主智能体（[[常驻智能体]] 形态），Proactive Research 后台只读巡检 4000+ 应用，Specialist Dots 企业版整合进微软 Microsoft Agent 365
- **[[GPT-6]] 6.1 Sol**：缓存输入 0.10 美元/百万 token，性能逼近 Astra（详见 GPT-6 页）
- **Ultrafast 极速引擎**：Codex 内最高 8 倍提速（约 300 tokens/s）、API 最高 6 倍；新推 Pro 500 订阅档（25 倍 Plus 配额 + Ultrafast 独享）
- **开发者底座**：Codex in the Cloud（云端共享开发沙箱）、Codex CLI 刷新（语音唤起、/agents 指令、任务挂起恢复）、Codex Security Cloud（内置网络安全模型 Daybreak Blue，全量渗透扫描 + 生成修复补丁）、Decisions API、Agents API 注入 Computer use、AWS Bedrock 托管 Managed Agents
- **生态打通**：Sign in with ChatGPT 全球身份登录，Plus/Pro 配额可在 Devin、Notion、Vercel、[[OpenClaw]] 等首批 16 家伙伴产品抵扣；ChatGPT Space/Pages/协同演示文稿；OpenAI Marketplace（32 家企业伙伴）；Private Intelligence 零数据留存隐私方案

### math 仓库：722 篇数学手稿批量发布（2026-10-06）
无发布会、无同行评审，仅在 GitHub 创建 math 仓库一次上传 722 篇数学预印本、归为 372 个结果家族，覆盖数论到代数几何 17 个方向（详见 [[摘要-openai-math仓库722手稿]]、[[AI数学证明]]）：
- **代表成果**：宣称证明 ζ 函数与狄利克雷 L 函数在实部 >7/8 区域无零点（"准黎曼猜想"）；霍奇猜想在 CM 阿贝尔簇/K3 曲面的关键缺口；唯一游戏猜想。235/372 个结果家族附 [[Lean]] 形式化证明可机器核验
- **效率**：模型尝试约 1.2 万个开放问题，平均每题约 3 小时 ChatGPT Pro 算力、5.8 次失败尝试、23 轮提示词迭代
- **争议**：数学界撕裂——有人称"数学史上意义重大的时刻"，也有人斥"学术大屠杀"；25 位菲尔兹奖得主（含陶哲轩）9 月联名声明批评把解题当能力基准，"人类数学协会"呼吁终止与 OpenAI 合作。此前时间线：5 月埃尔德什单位距离猜想反例 → 8 月 [[Astra]] 解决 10 个悬而未决问题（Lean 4 零 sorry、成本约 2000 美元）→ 9 月一个月内解决 100+ 问题

### Intelligent UI：模型长出交互界面（2026-10-07）
OpenAI 将 [[IntelligentUI]] 与 GPT-6 带入更广泛的 ChatGPT 日常聊天：用户提问除文字回答外，还能直接获得可点击图表、表单和交互式小工具，模型根据问题自动选择回答形式。信号意义：**模型从信息提供者变为任务交互入口**，一部分原本需要独立 App 提供的功能成为通用模型回答问题时即可调用的能力，直接冲击"手搓 AI 应用"赛道（详见 [[摘要-intelligent-ui模型交互界面]]）。与 [[Anthropic]] 2024 年的 Claude Artifacts 相比，Artifacts 是创作工作区（生成结果持续编辑复用），Intelligent UI 把交互组件嵌入回答，更容易进入日常问答。

## 关联连接
- [[Codex]] — OpenAI 的 Agent 产品
- [[Tibo]] — Codex 负责人，额度重置的执行者
- [[事件营销]] — Codex 重置机制的本质
- [[摘要-codex重置的真正原因]] — 来源（重置机制与用户里程碑）
- [[摘要-中美头部agent走向开放]] — 来源（开放 Harness）
- [[Anthropic]] — 竞品，同期出现封号风波
- [[ClaudeCode]] — 竞品
- [[AndrejKarpathy]] — 联合创始人
- [[RomainHuet]] — 开发者体验负责人
- [[AaronFriel]] — 工程师
- [[VibeEngineering]] — 内部实践的编程模式
- [[摘要-vibe-engineering-era]] — Vibe Engineering 内部分享来源
- [[GPT-6]] — GPT-6 Astra 新一代模型
- [[摘要-gpt6-astra实测体验]] — GPT-6 Astra 实测来源
- [[摘要-gpt6-自训练信号]] — GPT-6 自训练信号分析来源
- [[摘要-GPT-6-Astra改变技术栈]] — GPT-6 Astra 技术栈影响分析来源
- [[AgentRuntime]] — 后端升级方向
- [[TaskConsole]] — 前端升级方向
- [[AIControlPlane]] — 安全控制独立层
- [[ResponsesApi]] — Astra 唯一支持接口
- [[任务级成本]] — 成本管理方向
- [[GregBrockman]] — 联合创始人兼总裁
- [[摘要-OpenAI总裁Brockman最新采访]] — 来源（AGI 时代 + Navier-Stokes + 安全计划）
- [[Astra]] — GPT-6 旗舰模型
- [[ComputerUse]] — Astra 跃升关键能力
- [[NavierStokes]] — 10000 agent 解决的方程
- [[Lean]] — 数学证明形式化语言
- [[DefenderWindow]] — 防御者窗口
- [[DefenseFactory]] — 防御工厂范式
- [[FrontlineDefenders]] — 10 亿美元安全计划
- [[HuggingFace]] — 触发安全讨论的事件方
- [[Sora]] — 2026 年被取消的项目
- [[问责制]] — 人类应保留的价值
- [[IlyaSutskever]] — 2016-17 年共同推算者
- [[Harness]] — 开放的核心系统
- [[腾讯]] — 同步开放基座
- [[大模型价格战]] — GPT-6 Sol/Luna 参与的行业现象
- [[Opus]] — 同日应战的 Anthropic 模型系列
- [[摘要-a社o社价格战]] — 来源（Sol/Luna 降价与分档逻辑）
- [[Dots]] — DevDay 2026 发布的常驻智能体
- [[常驻智能体]] — Dots 代表的产品形态
- [[摘要-openai-devday-2026-gpt61sol-dots]] — 来源（DevDay 2026 全量更新）
- [[摘要-openai产品设计负责人对话]] — 产品设计负责人 Ian Silber 对谈来源
- [[摘要-openai-math仓库722手稿]] — 来源（math 仓库 722 篇手稿与学界反弹）
- [[AI数学证明]] — math 事件提炼的概念
- [[IntelligentUI]] — 2026-10-07 推出的原生交互界面
- [[摘要-intelligent-ui模型交互界面]] — 来源（Intelligent UI 与手搓 AI 应用退潮分析）
- [[手搓AI应用]] — 被该能力冲击的赛道
