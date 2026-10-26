---
title: "摘要-OpenAI总裁Brockman最新采访"
type: source
tags: [来源, 原始文件, OpenAI, Greg-Brockman, AGI, Computer-Use]
sources: [raw/09-archive/2026-09-15-OpenAI 总裁最新采访：现在所有人对 AI 的预测，大概率都是错的.md]
last_updated: 2026-09-15
---

## 核心摘要
深思圈整理 OpenAI 联合创始人兼总裁 **Greg Brockman** 在 a16z 播客的访谈。核心结论：**AGI 时代已经到来**，Brockman 说 Astra（OpenAI 最新旗舰模型）能连续运行 24 小时、跨越非常广泛的领域完成任务，"把它叫做 AGI 是合理的"。他说与 Ilya Sutskever 早在 2016-2017 年就推算过——如果一切都顺利 AGI 大概需要 15 年，如果愿意真的大规模投入、建超级计算机、花几千亿美元，可能 10 年就够了。Astra 跃升的关键是 **computer use**（AI 直接操作电脑界面，用鼠标、键盘、截图完成任务）——agent 能不能用的两点：模型够不够聪明去使用工具 + 能不能访问到需要的上下文。传统做法（建 API、MCP server、CLI 接口）本质是给 AI 打补丁、增加攻击面，而 computer use 让 AI 直接用人类界面，不需要任何特殊 API、不需要重新设计系统。2015 年 11 月内部会议就讨论过"如果强化学习的环境是屏幕像素+键鼠输入"的想法。**10000 个 AI agent 并行协作解决了 Navier-Stokes 方程**（流体力学难题），并写成 Lean 格式形式化——AI 开始创造新知识而非整合已有知识。**安全的窗口期（defender window）**：Hugging Face 事件让他们意识到 AI 网络攻击能力已很强，这种能力迟早扩散，现在是防御者黄金期。Brockman 用 Codex 对个人网站 gregbrockman.com 做渗透测试，**15 分钟找到 13 个漏洞**，让 Codex 修 45 分钟后 Codex 打开云控制台自动完成所有 HTTP 安全头、迁移到 Cloudflare Pages、启动 DMARC 配置、设置 48 小时后回来自检。OpenAI 抽调 25% 生产工程师专门做安全升级，目标建"defense factory"（发现漏洞→分类→修复→部署→验证全流程自动化）。**宣布 10 亿美元 Frontline Defenders 计划**为医院、水务公司、政府关键基础设施提供免费/折扣 AI 安全工具。Greg 的观点：**AI 的真正形态还没出现**——ChatGPT 和 ChatGPT Work 都是文本框，真正的 AI 是语音优先、持久记忆、主动发现问题、可依赖的。OpenAI 有 10 亿周活用户，还有约 15 亿曾经用过 ChatGPT 然后放弃的用户——AI 应主动告诉用户"我可以在这件事上帮你"，而不是让用户挖掘它能做什么。北极星是"简单"。就业：**AI 发展历史几乎从来不按照逻辑推断的方式发展**，人类不会因为 AI 失去创造价值的能力，问责制（accountability）是人类应保留的，创业浪潮会来。最后聊精力分配：今年取消了 Sora 项目以解放专注力，遵循《The Score Takes Care of Itself》哲学——专注基本动作，"你不是靠喊我要赢得超级碗赢超级碗的"。

## 核心观点
- **AI 的进展几乎从来不按逻辑推断方式发展，你对未来的预测大概率是错的，而且会以你没想到的方式错**
- **Astra 的意义在 computer use**：AI 不再需要世界为它改造，而是它来适应已有的世界
- **10000 agent 解 Navier-Stokes + Lean 形式化** = AI 开始创造新知识而非整合已有知识
- **defender window**：前沿实验室比攻击者早拿工具的黄金期，防御工厂以机器速度运转
- **AI 真正形态不是文本框**：语音优先 + 持久记忆 + 主动 + 可依赖；北极星"简单"
- 问责制是人类应保留的：AI 完成任务 vs 人作为人本身的存在
- **15 亿弃用用户**是重要信号：AI 应主动引导，而非让用户挖掘

## 关联连接
- [[GregBrockman]] — 本文主角
- [[OpenAI]] — 所属公司
- [[Astra]] — 本文讨论的旗舰模型（GPT-6 Astra）
- [[GPT-6]] — 详细技术规格与实测数据
- [[AGI]] — 通用人工智能
- [[ComputerUse]] — 计算机操作能力
- [[NavierStokes]] — 流体力学方程
- [[Lean]] — 数学证明语言（形式化验证）
- [[DefenderWindow]] — 防御者窗口概念
- [[DefenseFactory]] — 防御工厂范式
- [[FrontlineDefenders]] — 10 亿美元安全计划
- [[HuggingFace]] — 触发安全讨论的事件方
- [[Sora]] — 今年被取消的项目
- [[问责制]] — 人类应保留的价值
- [[摘要-gpt6-astra实测体验]] — Astra 实测对比
- [[摘要-GPT-6-Astra改变技术栈]] — Astra 技术栈影响
- [[摘要-gpt6-自训练信号]] — Astra 自训练信号分析
- [[摘要-对话claude-code之父boris-cherny]] — 类似视角的对谈
- [[a16z]] — 访谈方
- [[Claude]] — 对标产品
