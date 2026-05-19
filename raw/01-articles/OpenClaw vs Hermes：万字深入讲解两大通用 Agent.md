---
title: "OpenClaw vs Hermes：万字深入讲解两大通用 Agent"
source: "https://zhuanlan.zhihu.com/p/2027492863059993310"
---
最近 Hermes Agent 很火，媒体、Reddit 上"I ditched OpenClaw for Hermes"的帖子接连不断，国内也有不少朋友在问同一个问题：

它们到底是同一类东西吗？Hermes 能直接替代 OpenClaw 吗？

这个问题正好点中了最容易混淆的地方。

先把共识摆出来：OpenClaw 和 Hermes 都属于通用 Agent 系统。它们都不是单点脚本，也不是某个聊天渠道里的 bot。它们都在尝试把模型、工具、会话、记忆、Skills、消息入口和本地运行环境接成一套可以长期使用的系统。

大家觉得它们像，完全正常。它们都聊 [Gateway](https://zhida.zhihu.com/search?content_id=273105374&content_type=Article&match_order=1&q=Gateway&zd_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJ6aGlkYV9zZXJ2ZXIiLCJleHAiOjE3NzkzNjYwOTEsInEiOiJHYXRld2F5IiwiemhpZGFfc291cmNlIjoiZW50aXR5IiwiY29udGVudF9pZCI6MjczMTA1Mzc0LCJjb250ZW50X3R5cGUiOiJBcnRpY2xlIiwibWF0Y2hfb3JkZXIiOjEsInpkX3Rva2VuIjpudWxsfQ.u2V26QYRxwZb7W9-hpDhIR2NL-LjW7ZIfhxJeI5dJ2Y&zhida_source=entity)，都聊 Skills，都聊 Memory，都能接聊天入口，也都关心本地化、工具权限和用户数据迁移。

但工程重心完全不同。

OpenClaw 更像一个本地优先的 Agent Gateway，重点是把真实世界的入口、会话、设备和权限接起来。Hermes 更像一个学习型 Agent Runtime，重点是让 Agent 在执行过程中沉淀经验，下次少走弯路。

![](assets/OpenClaw%20vs%20Hermes%EF%BC%9A%E4%B8%87%E5%AD%97%E6%B7%B1%E5%85%A5%E8%AE%B2%E8%A7%A3%E4%B8%A4%E5%A4%A7%E9%80%9A%E7%94%A8%20Agent/1fedbe99392df1ccfd88728b0cd72c34_MD5.jpg)

之前几篇文章里，我们分别梳理过 OpenClaw 的"作业系统"味道，拆过它最容易混的渠道、账号、Agent、会话、记忆五层关系，也拆过 Hermes 的闭环学习循环和源码实现。具体可以看下我们的往期推文。

本文把它们放在同一张思考里。

不是为了吹嘘谁更强更厉害，而是让我们一起来了解和深入分析：这两个通用 Agent 的区别是什么，它们到底在解决哪一层问题。

## **太长不看版**

- 它们确实是同一大类东西。 OpenClaw 和 Hermes 都可以理解为通用 Agent 系统，都不只是聊天机器人，也不只是工具集合。
- OpenClaw 的核心资产是 Gateway 控制面。 它把 WhatsApp、Telegram、Slack、Discord、Signal、iMessage、Matrix、Feishu、LINE、WeChat、WebChat 等入口接进来，再用 Gateway 管会话、路由、节点、工具和安全策略。
- Hermes 的核心资产是学习型执行循环。 它强调 self-improving agent、closed learning loop、自动创建和修补 skills、[FTS5](https://zhida.zhihu.com/search?content_id=273105374&content_type=Article&match_order=1&q=FTS5&zd_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJ6aGlkYV9zZXJ2ZXIiLCJleHAiOjE3NzkzNjYwOTEsInEiOiJGVFM1IiwiemhpZGFfc291cmNlIjoiZW50aXR5IiwiY29udGVudF9pZCI6MjczMTA1Mzc0LCJjb250ZW50X3R5cGUiOiJBcnRpY2xlIiwibWF0Y2hfb3JkZXIiOjEsInpkX3Rva2VuIjpudWxsfQ.sL0Refl2-bZdBLouLrkNyaK27Dj3F2l9cO_rLyU2jpQ&zhida_source=entity) 会话搜索、Honcho 用户建模，以及本地、Docker、SSH、[Daytona](https://zhida.zhihu.com/search?content_id=273105374&content_type=Article&match_order=1&q=Daytona&zd_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJ6aGlkYV9zZXJ2ZXIiLCJleHAiOjE3NzkzNjYwOTEsInEiOiJEYXl0b25hIiwiemhpZGFfc291cmNlIjoiZW50aXR5IiwiY29udGVudF9pZCI6MjczMTA1Mzc0LCJjb250ZW50X3R5cGUiOiJBcnRpY2xlIiwibWF0Y2hfb3JkZXIiOjEsInpkX3Rva2VuIjpudWxsfQ.BNbUMeXnrSsCD9HYXXscIG9_Tf_H2E7m7eF1uWmAJOs&zhida_source=entity)、Singularity、[Modal](https://zhida.zhihu.com/search?content_id=273105374&content_type=Article&match_order=1&q=Modal&zd_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJ6aGlkYV9zZXJ2ZXIiLCJleHAiOjE3NzkzNjYwOTEsInEiOiJNb2RhbCIsInpoaWRhX3NvdXJjZSI6ImVudGl0eSIsImNvbnRlbnRfaWQiOjI3MzEwNTM3NCwiY29udGVudF90eXBlIjoiQXJ0aWNsZSIsIm1hdGNoX29yZGVyIjoxLCJ6ZF90b2tlbiI6bnVsbH0.U7iaUYG8UYsEqOZ1QAZT5VcEJDy29sufar8k2pJAVAg&zhida_source=entity) 六种执行后端。
- 两者都有 Skill，但语义不同。 OpenClaw 更偏"人定义技能，系统负责加载和治理"；Hermes 更偏"Agent 做完复杂任务以后，把成功路径沉淀成 procedural memory"。
- 安全思路不同。 OpenClaw 走信任模型 + 配置审计路线；Hermes 走纵深防御路线，从审批到容器隔离逐层收紧。
- 迁移能做，但更像低成本试用入口。 Hermes 支持 `hermes claw migrate`，能导入 OpenClaw 的 persona、memory、skills、allowlist、部分 messaging settings 和 allowlisted secrets。但迁移配置，不等于迁移整套使用方式。
- 如果你缺的是多入口助理和治理面，OpenClaw 更贴合。 如果你缺的是长期重复任务里的经验沉淀和自我改进，Hermes 更值得试。

### 最新文章精选（关注、点赞、收藏，获取第一手信息）

[一路狂揽5.3万星的Hermes Agent 安装指南来了](https://zhuanlan.zhihu.com/p/2026310080262357049)

[装完Hermes Agent用了一下，OpenClaw真的可以退场了](https://zhuanlan.zhihu.com/p/2026051186134917689)

[（可能全网最全/长的）2万字Openclaw保姆教程](https://zhuanlan.zhihu.com/p/2012626589477781666)

[打工人必备 AI 新三件套：NotebookLM、Claude Code、Obsidian](https://zhuanlan.zhihu.com/p/2024133568557761035)

[我用两周时间踩完openclaw所有坑，总结出这份完整调教指南](https://zhuanlan.zhihu.com/p/2016823158380995920)

[OpenClaw 生产力翻倍：这20个技能太给力了](https://zhuanlan.zhihu.com/p/2017990909216714962)

[我用 OpenClaw 搞了家16人的公司：全员AI，24小时无休！](https://zhuanlan.zhihu.com/p/2018259939664109626)

[把 OpenClaw 装在本地电脑 24 小时工作，6000 字零基础上手教程](https://zhuanlan.zhihu.com/p/2019706301387666666)

[OpenClaw下载量 Top 20 的神仙级技能包分享](https://zhuanlan.zhihu.com/p/2019428885486388929)

[史上最全 OpenClaw 小龙虾常用操作命令指南](https://zhuanlan.zhihu.com/p/2021967648259408711)

[OpenClaw 十大痛点破解：10 个 Skills 直接对症下药](https://zhuanlan.zhihu.com/p/2022606975700145296)

[Claude Code 深度用法指南：那些让效率翻倍的隐藏技巧](https://zhuanlan.zhihu.com/p/2024783081865846798)

## **它们都是通用 Agent**

OpenClaw 和 Hermes 之所以会被放在一起比较，不是误会。它们确实有相似的系统边界。

一个现代通用 Agent 系统，通常不只是"模型加提示词"。在之前那篇 Harness 文章里，我们把这几层拆开过：

- LLM 更像引擎；
- Agent Loop 更像工作节奏；
- Harness 更像给 Agent 配好的工位、规范、工具链、权限和验收机制；
- Memory、Skills、Context、工具调用、执行环境，都会影响最后的可用性。

从这个角度看，OpenClaw 和 Hermes 都已经越过了"模型包装器"的阶段。

它们都在做一件更接近真实使用的事：**把 Agent 放进一个长期运行的工程环境里**。

这也是容易混淆的根源。

**它们都是通用 Agent，但厚度长在不同位置。**

OpenClaw 把厚度长在入口、控制面和多设备协同上。

Hermes 把厚度长在执行循环、技能沉淀和跨会话经验复用上。

这一点看清楚，后面的架构、安全、迁移和选型都会更容易理解。

## **系统重心不在同一层**

很多对比容易卡住，是因为一上来就列功能表。

功能表有用，但容易把人带偏。两个系统都支持聊天入口、工具调用、skills、memory、模型切换，于是看起来像"同类竞品"。

更有用的拆法是把 Agent 系统分成几层：入口、控制面、执行循环、经验层。

OpenClaw 的 README 里有一句话值得留意："The Gateway is just the control plane — the product is the assistant." 它不只是在做一个聊天机器人，更像一个本地优先、可接多入口、可接设备节点、可接 WebChat 和 Dashboard 的控制面。

![](assets/OpenClaw%20vs%20Hermes%EF%BC%9A%E4%B8%87%E5%AD%97%E6%B7%B1%E5%85%A5%E8%AE%B2%E8%A7%A3%E4%B8%A4%E5%A4%A7%E9%80%9A%E7%94%A8%20Agent/96fc1e389fc8b2f8abe2ea1b32a9e5da_MD5.jpg)

Hermes 的 README 则把自己定义成"The self-improving AI agent"。值得看的地方是 built-in learning loop：从经验中创建 skills，在使用中改进 skills，搜索过去的会话，并逐步构建用户模型。

![](assets/OpenClaw%20vs%20Hermes%EF%BC%9A%E4%B8%87%E5%AD%97%E6%B7%B1%E5%85%A5%E8%AE%B2%E8%A7%A3%E4%B8%A4%E5%A4%A7%E9%80%9A%E7%94%A8%20Agent/fa252c31ae56bdb2f4a0003fd89ac9df_MD5.jpg)

背后的团队也不同。OpenClaw 由独立开发者 Peter Steinberger 创建，凭借极简安装和多渠道接入快速积累了大量 GitHub Star。不过 Steinberger 今年 2 月加入 OpenAI，项目已交给社区基金会维护，后续的发展节奏还在观察。Hermes 背后是 Nous Research，Hermes 系列模型（Hermes 3、Hermes 4）的缔造者，对模型训练和推理优化有第一手积累，上线不到两个月社区增长很快。

用一句话概括：

**OpenClaw 管入口和秩序，Hermes 管执行和经验。**

## **OpenClaw：把真实世界接进来**

我们之前梳理过，OpenClaw 不只是聊天窗口，它更像一个按会话串行执行的作业系统。你看到的是聊天入口，系统内部跑的是一套消息接入、路由、会话和记忆加载机制。

本文对比的语境下，这个判断仍然成立。

OpenClaw 的定位是 personal AI assistant。你把它跑在自己的设备或服务器上，然后通过熟悉的聊天入口和它交互。

它的渠道列表很长：WhatsApp、Telegram、Slack、Discord、Google Chat、Signal、iMessage、BlueBubbles、IRC、Microsoft Teams、Matrix、Feishu、LINE、Mattermost、Nextcloud Talk、Nostr、Synology Chat、Tlon、Twitch、Zalo、WeChat、WebChat。代码仓库里还有专门的 macOS menu bar app、iOS/Android node、Voice Wake、Talk Mode、Live Canvas（A2UI）。

这个细节有分量。对很多真实用户来说，Agent 的第一道门槛经常还没到 ReAct，而是这些更朴素的问题：

- 我能不能从 Telegram 发它？
- 我能不能从 Discord 群里唤起它？
- 我能不能让它跑在家里的小机器上？
- 我能不能让家人、同事、设备节点以不同权限接入？

OpenClaw 的 Gateway 正是在处理这些问题。

![](assets/OpenClaw%20vs%20Hermes%EF%BC%9A%E4%B8%87%E5%AD%97%E6%B7%B1%E5%85%A5%E8%AE%B2%E8%A7%A3%E4%B8%A4%E5%A4%A7%E9%80%9A%E7%94%A8%20Agent/4f85e4e78ea6f8360a273ac83d5b657e_MD5.jpg)

  

**它先把入口和控制面做厚，再让 Agent 在这个秩序里工作。**

这类系统的难点，不只是发起一次模型调用。更麻烦的是多渠道状态、会话隔离、群聊激活规则、消息分片、凭据存放、配对策略、设备节点权限、WebSocket 控制面、Dashboard，以及一堆看起来不起眼但上线后每天都会碰到的边界条件。

所以把 OpenClaw 简化成"一个工具箱"，多少有些低估它了。它更像一个 Agent 版的个人通信与设备控制平面。

更具体的可以了解我们之前整理的文章:

OpenClaw 多 Agent 实战：从"单军作战"到"龙虾军团"

OpenClaw 是怎么工作的？一条消息的旅程讲清楚

深度拆解 Clawdbot（OpenClaw）架构与实现

## **Hermes：让 Agent 把经验写下来**

Hermes 的重心不一样。

它当然也有 CLI 和 Messaging Gateway，也能接 Telegram、Discord、Slack、WhatsApp、Signal 等入口。但如果只从"能接哪些平台"看 Hermes，就会错过它最有意思的地方。

在之前那篇 Hermes 架构拆解里，我们拆过它的几个关键模块：`run_agent.py`、`model_tools.py`、`skill_manager_tool.py`、`hermes_state.py`。

本文只抓和 OpenClaw 对比最相关的一点：**Hermes 把 Agent 的执行过程当成长期资产。**

它的 README 里，closed learning loop 被放在非常靠前的位置：Agent-curated memory、autonomous skill creation、skills self-improve、FTS5 session search、Honcho user modeling。

翻成工程语言，大概是四件事：

1. 1\. 当前任务怎么跑，靠 Agent loop 和 tool runtime。
2. 2\. 过去做过什么，靠 session store 和搜索召回。
3. 3\. 哪些流程值得复用，沉淀成 skill。
4. 4\. 用户长期偏好和行为模式，交给 memory provider 和 Honcho 用户建模。

代码里也能看到这条线。`run_agent.py` 负责完整的 tool calling conversation loop；`model_tools.py` 负责工具发现和分发；`skill_manager_tool.py` 开头就写着"Skills are the agent's procedural memory"，允许 Agent 创建、更新、删除 skills，把成功路径变成 reusable procedural knowledge；`hermes_state.py` 用 SQLite + FTS5 存会话和做全文检索，支持 WAL 模式的并发读写和基于 source tag（cli、telegram、discord 等）的过滤。

Hermes 更关心的问题是：

**当它完成了一个复杂任务以后，这段经验会不会消失？下次做同类任务，它能不能少试错？**

  

![](assets/OpenClaw%20vs%20Hermes%EF%BC%9A%E4%B8%87%E5%AD%97%E6%B7%B1%E5%85%A5%E8%AE%B2%E8%A7%A3%E4%B8%A4%E5%A4%A7%E9%80%9A%E7%94%A8%20Agent/4e33ef48b2916a9c67efcbaf1601d628_MD5.jpg)

  

这套设计想解决的，是一个老问题：

**Agent 每次从零开始，成本很高。**

如果它已经踩过坑、跑通过流程、修过某个复杂错误，就可以把这条路径保存下来。下一次同类任务，不需要重新"聪明"一次，只要复用之前沉淀过的工作方法。

有 Reddit 用户反馈，Agent 在两小时内自动生成了三份技能文档后，重复性研究任务的速度提升了约 40%。这类数据还需要更多验证，但方向感是清楚的。

它把很多 Agent 产品挂在嘴边的"长期记忆"，往 procedural memory 的方向又推了一步。

更具体的可以了解我们之前整理的文章:

Hermes Agent 架构拆解：会复盘、可成长的 Agent，到底怎么实现的?

## **Skill：同一个词，两种味道**

很多对比会说：OpenClaw 是人工写 Skill，Hermes 是自动生成 Skill。

方向没错，但容易过度简化。

在之前那篇 Anthropic Skills 文章里，我们聊过：Skill 可以从提示词开始，但它更像一个 Agent work unit。它可以是一个目录，里面有 `SKILL.md`，也可以有参考资料、脚本、模板、资产和踩坑记录。

把这条线放到 OpenClaw 和 Hermes 上，会更容易看懂差异。

OpenClaw 有一套完整的技能体系。代码仓库里已经内置了 50 多个 skill 目录（1password、discord、slack、github、coding-agent、apple-notes、voice-call 等），支持 AgentSkills-compatible skill folders，每个 skill 是一个包含 `SKILL.md` 的目录。系统按 bundled skills、managed/local skills、personal agent skills、project agent skills、workspace skills 分层，通过加载优先级和 gating 做治理。

这更像一个工程化技能目录：  
mermaid

- 哪些技能来自系统；
- 哪些来自本地用户；
- 哪些属于某个 workspace；
- 哪些需要特定环境变量、二进制或配置；
- 哪些优先级更高；
- 哪些第三方 skills 要当成外部输入来处理。

Hermes 的 skill 侧重点更像"过程记忆"。

它的 `skill_manager_tool.py` 开头就写着：Skills are the agent's procedural memory: they capture how to do a specific kind of task。它们记录的是"怎么做某类具体任务"，不是泛泛的偏好事实。系统提示里也会提醒 Agent：完成复杂任务、修复棘手错误、发现非平凡 workflow 后，可以用 `skill_manage` 把方法保存下来；如果发现 skill 过时或错误，就直接 patch。Hermes 的 skills 目录也预置了 26 个类别（research、software-development、data-science、devops、mlops 等），兼容 agentskills.io 开放标准。

**OpenClaw 的 skill 更像团队里的 SOP 库。Hermes 的 skill 更像一个强执行者不断更新的工作笔记。**

SOP 库的优点是可控、可审计、适合团队治理。

工作笔记的优点是贴近真实任务、迭代快、能把个体使用经验滚起来。

代价也不同。OpenClaw 的 skill 质量更多取决于人和社区。Hermes 的自动沉淀有想象力，但也需要复看和修剪，否则"经验"也可能变成"惯性错误"。

更具体的可以了解我们之前整理的文章:

Skills 详解：拆一个技能，看 Anthropic 和 OpenAI 的思路差异

Skill 到底是什么：从第一性原理深入剖析 Claude Agent Skills

## **Memory：记忆、上下文和经验不是一回事**

在之前那篇 AI Memory 综述里，我们把几个词分开过：

- • Context 是这次任务的临时上下文；
- • Knowledge 更偏稳定知识；
- • Memory 会随时间变化，和用户、任务、历史互动相关；
- • Experience 是从原始记录里蒸馏出来的方法和教训。

用这组词再看 OpenClaw 和 Hermes，会更清楚。

OpenClaw 的记忆走"文件即记忆"路线。核心文件包括定义 Agent 性格的 `SOUL.md`、记录用户偏好的 `USER.md`、按日期组织的日常日志 `memory/*.md`，以及精选长期记忆的 `MEMORY.md`。语义检索工具负责查找，上下文压缩前执行一次静默记忆写入，防止压缩丢信息。更像给 Agent 一个笔记本。

Hermes 的记忆更系统化，分三层：

| 层级 | 内容 | 特点 |
| --- | --- | --- |
| 会话记忆 | 当前对话上下文 | 仅维持于当次会话 |
| 持久记忆 | 跨会话的事实和偏好（MEMORY.md + USER.md） | 自动累积，每次对话带上关键信息 |
| 技能记忆 | 从成功任务中学到的解决方案模式 | SQLite + FTS5 全文检索，支持 LLM 摘要召回，可搜索、可复用、自我迭代 |

更像给 Agent 装了一个搜索引擎式的大脑。

所以它们都讲 Memory，但侧重点不同。

OpenClaw 的 Memory 更容易和"身份、会话、工作区边界"放在一起看。

Hermes 的 Memory 更容易和"执行轨迹、搜索召回、Skill 沉淀、用户建模"放在一起看。

更具体的可以了解我们之前整理的文章:

2026 AI Memory 最新综述：从4W分类到单/多智能体记忆机制

## **安全：两种完全不同的思路**

安全是容易被略过、但实际影响很大的维度。两个项目在这方面的思路差异很明显。

### **OpenClaw：信任模型 + 配置审计**

OpenClaw 的安全模型是"personal assistant"（one trusted operator），不是多租户共享。SECURITY.md 里写得很清楚：authenticated Gateway callers are treated as trusted operators for that gateway instance。

它提供了 `openclaw security audit --deep` 命令来扫描网关配置风险，DM pairing、allowlist、sandbox 和 doctor 机制共同构成安全边界。代码仓库里的安全文档非常详细，覆盖了 Workspace Memory Trust Boundary、Plugin Trust Boundary、Temp Folder Boundary、Sub-agent delegation hardening 等多个层面。

不过 OpenClaw 在安全方面的历史不太平静。今年 2 月被曝出 WebSocket Token 泄露漏洞，外部安全团队发现第三方 Skill 存在数据外泄和 Prompt 注入风险，ClawHub 上也发现了一批恶意 Skill。官方的响应和修复速度不慢，但这些事件提醒我们：一个入口足够多、生态足够开放的系统，攻击面也会相应扩大。

### **Hermes：纵深防御 + 容器隔离**

Hermes 在部署层面更强调逐层收紧。它支持六种 terminal backend（local、Docker、SSH、Daytona、Singularity、Modal），其中 NixOS 模式提供了 Namespace 隔离（`ProtectSystem=strict`）。

安全策略包括：

- • 危险命令审批：终端命令、文件写入等默认需要人工确认，超时未批准自动拒绝
- • 容器隔离：可以把 Agent 的执行环境限制在 Docker 或远程后端里
- • 凭据过滤：防止敏感信息泄露到上下文
- • 上下文注入扫描：检测 Prompt 注入风险

截至目前，Hermes 没有被公开披露过重大安全漏洞。当然，这也和它上线时间更短、用户规模更小有关，不能简单等同于"更安全"。

**一句话区分：OpenClaw 更多在"人该怎么管 Agent"这一层做安全，Hermes 更多在"Agent 运行时该怎么被约束"这一层做安全。**

更具体的可以了解我们之前整理的文章:

从误删邮箱到 Skill 投毒：OpenClaw 安全到底该怎么做

你的 Moltbot 很可能正在裸奔：安全宝典清单

## **能力对比**

下面这张表可以当成快速索引。

| 维度 | OpenClaw | Hermes Agent |
| --- | --- | --- |
| 大类 | 通用 Agent 系统 | 通用 Agent 系统 |
| 核心定位 | 本地优先个人 AI 助手，重点是 Gateway 控制面 | self-improving AI agent，重点是学习型执行循环 |
| 入口能力 | 很强，覆盖 25+ 聊天渠道、WebChat、macOS/iOS/Android 节点、Live Canvas | 支持 CLI 和 Telegram/Discord/Slack/WhatsApp/Signal/Email |
| 架构重心 | Gateway、会话、路由、设备节点、权限、Dashboard | Agent loop、工具分发、skills、memory、session search、执行后端 |
| 技能体系 | AgentSkills-compatible，强调加载来源、优先级、gating 和治理；50+ 内置 skill | skills 作为 procedural memory，强调自动创建、修补和复用；26 个类别 |
| 记忆方向 | workspace 文件、memory 插件、语义检索与 agent state | SQLite + FTS5 会话搜索、memory provider、Honcho 用户建模 |
| 安全策略 | 信任模型 + 配置审计 + DM pairing / allowlist / sandbox | 纵深防御：审批 + 容器隔离 + 凭据过滤 + 注入扫描 |
| 技术栈 | Node.js / TypeScript | Python 3.11 |
| 安装体验 | openclaw onboard --install-daemon，偏 Gateway 和渠道上手 | hermes setup、hermes model、hermes gateway，偏 CLI 和模型配置 |
| 模型支持 | 多 provider，支持 OAuth + API key failover | 200+ 模型（OpenRouter、Anthropic、OpenAI、智谱、Kimi、MiniMax 等），一条命令切换 |
| 迁移支持 | 更偏 OpenClaw 自身跨机器迁移 | 支持从 OpenClaw 导入 persona、memory、skills、allowlist、部分 settings 和 secrets |
| 更适合 | 多渠道个人助理、设备联动、团队入口治理 | 长期重复任务、研究工作流、个人经验沉淀、RL 轨迹数据生成 |

  

这张表核心只有一句：

**OpenClaw 的价值在"接入复杂世界"，Hermes 的价值在"沉淀复杂经验"。**

## **安装路径，也暴露了产品性格**

安装方式也值得看。

OpenClaw 推荐路径是：

```bash
npm install -g openclaw@latest
openclaw onboard --install-daemon
```

它会引导你设置 Gateway、workspace、channels、skills、模型和守护进程（launchd/systemd user service）。文档里还会让你验证 `openclaw gateway status`，再打开 dashboard。

这条路径说明 OpenClaw 很关心"长期运行"和"入口可用"。你启动的不只是一段 CLI 会话，更像是在机器上装一个长期运行的 assistant 控制面。

Hermes 的快速安装是：

```bash
curl -fsSL https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.sh | bash
hermes
```

后续常见命令包括：

```bash
hermes model        # 选模型
hermes tools        # 配工具
hermes config set   # 改配置
hermes gateway      # 起 messaging gateway
hermes setup        # 全量设置向导
hermes claw migrate # 从 OpenClaw 迁移
hermes doctor       # 诊断
```

它的文档强调模型切换（200+ 模型，一条命令换，不改代码）、CLI 和 messaging 两种入口、skills、memory、MCP、cron 定时任务、六种 terminal backend、RL trajectory 等能力。部署门槛低，$5/月的 VPS 就能跑，Daytona 和 Modal 还支持 serverless 持久化模式，闲时几乎零成本。

Hermes 首先希望你把一个会执行、会记忆、会沉淀经验的 Agent 跑起来，再按需接到聊天平台或远程环境里。

如果你只是想装一个"能在微信和 Telegram 里随叫随到的个人助理"，OpenClaw 的上手路径更贴合。

如果你想让 Agent 进入一个长期研发或研究工作流，让它跨会话记住东西、把复杂流程沉淀成技能，Hermes 的路径更贴合。

## **迁移：能做，但不是简单换壳**

Hermes 对 OpenClaw 用户的迁移路径做得很直接。

安装 Hermes 后，`hermes setup` 会自动检测 `~/.openclaw` 目录并提供迁移。也可以随时手动执行：

```bash
hermes claw migrate              # 交互式迁移（full preset）
hermes claw migrate --dry-run    # 预览会迁什么
hermes claw migrate --preset user-data   # 不含 secrets 的谨慎迁移
hermes claw migrate --overwrite  # 覆盖已有冲突
```

能迁的内容包括：

- • `SOUL.md`（persona 文件）
- • `MEMORY.md` 和 `USER.md`
- • 用户创建的 skills（导入到 `~/.hermes/skills/openclaw-imports/`）
- • command allowlist（审批模式）
- • 部分 messaging settings（平台配置、allowed users、工作目录）
- • allowlisted secrets（Telegram、OpenRouter、OpenAI、Anthropic、ElevenLabs 等 API Key）
- • TTS assets
- • workspace instructions（`AGENTS.md`）
![](assets/OpenClaw%20vs%20Hermes%EF%BC%9A%E4%B8%87%E5%AD%97%E6%B7%B1%E5%85%A5%E8%AE%B2%E8%A7%A3%E4%B8%A4%E5%A4%A7%E9%80%9A%E7%94%A8%20Agent/6775c35f54900935735ef695b3679389_MD5.jpg)

  

有社区实操记录值得参考：基础迁移跑完以后，Discord、Telegram 这类机器人配置、模型 API 和记忆同步，往往还要单独确认。有用户迁移后发现 Hermes 还没有配置模型，需要额外一步设置 provider 和 API Key。

真实迁移里，至少有几个边界要留意：

- • `--dry-run` 建议先跑一遍，看看会迁什么；
- • `user-data` preset 会排除 secrets，更适合谨慎迁移；
- • `full` preset 会导入 allowlisted secrets，但不会把所有凭据一股脑搬过去；
- • WhatsApp 这类二维码配对型渠道仍可能需要重新处理；
- • imported skills 通常要新 session 或重启后才生效；
- • OpenClaw 的 Gateway 工作方式和 Hermes 的 Gateway 工作方式不完全一样，迁移配置不等于迁移架构。

  

![](assets/OpenClaw%20vs%20Hermes%EF%BC%9A%E4%B8%87%E5%AD%97%E6%B7%B1%E5%85%A5%E8%AE%B2%E8%A7%A3%E4%B8%A4%E5%A4%A7%E9%80%9A%E7%94%A8%20Agent/47ba417d7473e848c9b600edf9317929_MD5.jpg)

  

更稳妥的做法：

**把迁移当成试用 Hermes 的低成本入口，而不是"一键把 OpenClaw 变成 Hermes"。**

可以先迁 user-data，再试一两个重复性强的工作流。如果 Hermes 的 skill 沉淀和 session search 确实帮你减少了重复劳动，再考虑扩大使用范围。

## **选 OpenClaw，还是选 Hermes**

这个问题可以从三个角度想。

**第一，你的主要复杂度在哪？**

如果复杂度在入口，比如 Telegram、Discord、Slack、WeChat、WebChat、iOS、Android、macOS 节点、群聊、私聊、配对、远程 Gateway，那 OpenClaw 更自然。

如果复杂度在任务本身，比如研究、代码修改、数据分析、日报周报、PR 审查、重复性排障、长链路自动化，那 Hermes 更值得试。

**第二，你更担心不可控，还是更担心不成长？**

如果更担心不可控，可以先看 OpenClaw 的 Gateway、allowlist、pairing、sandbox、doctor、workspace 边界。

如果更担心 Agent 每次都从零开始，可以先看 Hermes 的 skills self-improve、FTS5 session search、memory provider、Honcho 用户建模。

**第三，你是一个人用，还是要带进团队流程？**

个人折腾、研究工作流、长任务，Hermes 的成长性更有吸引力。

团队协作、多入口接入、设备联动、权限治理，OpenClaw 的控制面价值更高。

当然，也可以两者都试。

看 Hermes，就看它的学习循环有没有帮你减少重复劳动。

看 OpenClaw，就看它的 Gateway、渠道、会话和设备治理有没有让你的 Agent 更容易进入日常场景。

更直接一点：

**我现在缺的，是入口、秩序，还是经验？**

## **我自己的看法**

坦率说，如果只看概念，Hermes 确实更容易让人多看一眼。

"Agent 从经验里生成技能"这件事，确实切中了当前 Agent 产品的一个痛点：很多 Agent 看起来很聪明，但每次任务都像第一次上班。它能解决问题，却不一定能沉淀下来。

Hermes 把 procedural memory 拉到台前，是一个值得关注的方向。

但如果看真实使用，OpenClaw 也没有那么容易被替代。

多渠道、Gateway、设备节点、DM pairing、Dashboard、workspace、skills precedence、plugins、Voice Wake、Live Canvas、远程访问，这些东西不一定性感，但它们决定了一个 Agent 能不能进入真实生活和真实团队。

所以说"OpenClaw 过时了"，可能有些简单了。

我更倾向于这样理解：

**OpenClaw 更像是在回答：Agent 如何进入世界。Hermes 更像是在回答：Agent 如何积累经验。**

前者解决"我怎么触达它、约束它、让它出现在正确的地方"。

后者解决"它怎么记住做过的事、少重复犯错、把方法沉淀下来"。

更完整的 Agent 系统，最后大概率两边都少不了。

一个只会学习、但入口和权限一团糟的 Agent，不太容易长期跑在真实环境里。

一个入口很全、治理也稳、但每次复杂任务都从零开始的 Agent，用久了也会觉得累。

所以这场对比更有价值的地方，不是告诉大家今天卸载谁、安装谁。

它提醒我们：

**Agent 框架的竞争，已经从"能不能调用工具"，进入到"能不能管理入口、治理风险、沉淀经验"的阶段。**

这也是它们值得放在一起看的原因。