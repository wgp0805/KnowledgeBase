---
title: "GregBrockman"
type: entity
tags: [OpenAI, 高管, AGI, Computer-Use, AI安全]
sources:
  - raw/09-archive/2026-09-15-OpenAI 总裁最新采访：现在所有人对 AI 的预测，大概率都是错的.md
last_updated: 2026-09-15
---

## 定义
Greg Brockman，OpenAI 联合创始人兼总裁（Co-founder and President）。2026 年 9 月在 a16z 播客采访中提出"AGI 时代已经到来"，是 GPT-6 Astra 时代的核心叙事者之一。

## 关键信息

### 核心观点（2026-09 a16z 访谈）
- **AGI 时代已到来**：Astra 能连续运行 24 小时、跨越非常广泛的领域完成任务，"把它叫做 AGI 是合理的"
- **15→10→9 年推算**：2016-2017 年与 Ilya Sutskever 曾推算——顺利 15 年，大规模投入可 10 年，实际 2026 年距推算约 8-9 年
- **Astra 跃升关键在 computer use**：agent 能否用的两点 = 模型够聪明使用工具 + 能访问需要的上下文。传统做法（建 API/MCP/CLI 接口）是给 AI 打补丁、增加攻击面
- **2015-11 内部会议**就讨论过"如果强化学习的环境是屏幕像素+键鼠输入，是不是任何可以在电脑上做的事都能成为训练任务"
- **Navier-Stokes 方程**：10000 个 AI agent 并行协作解决，写成 Lean 格式形式化——AI 开始创造新知识而非整合已有知识
- **defender window**：AI 网络攻击能力已很强（Hugging Face 事件），这种能力迟早扩散，现在是防御者黄金期
- **defense factory**：发现漏洞→分类→修复→部署→验证全流程自动化。OpenAI 抽调 25% 生产工程师做安全升级
- **Frontline Defenders**：宣布 10 亿美元计划为医院、水务公司、政府关键基础设施提供免费/折扣 AI 安全工具
- **渗透测试案例**：用 Codex 对个人网站 gregbrockman.com 做渗透，**15 分钟找到 13 个漏洞**，让 Codex 修 45 分钟后 Codex 打开云控制台自动完成 HTTP 安全头、迁移到 Cloudflare Pages、启动 DMARC 配置、设置 48 小时后回来自检

### 对 AI 产品形态的判断
- **AI 真正形态不是文本框**：ChatGPT 和 ChatGPT Work 都是文本框，真正的 AI 是语音优先、持久记忆、主动发现问题、可依赖
- **10 亿周活 + 15 亿弃用用户**：曾试用 ChatGPT 然后放弃的用户是重要信号，AI 应主动告诉用户"我可以在这件事上帮你"
- **北极星"简单"**：让 AI 融入你的生活，而不是让你围着 AI 转

### 就业与创业
- **AI 发展几乎不按逻辑推断方式发展**——你对未来的预测大概率是错的，而且会以你没想到的方式错
- 人类不会因为 AI 失去创造价值的能力
- **问责制（accountability）是人类应保留的**：AI 完成任务 vs 人作为人本身的存在
- 创业浪潮会来：听说有批人正在辞职创业，因为 AI 工具降低了启动门槛

### 精力分配与决策
- **今年取消 Sora**：为解放整个公司专注力做出必要决定
- 遵循《The Score Takes Care of Itself》哲学——专注基本动作，不是靠喊"我要赢得超级碗"赢超级碗
- 管理风格："从战壕里领导"，把所有能触碰到这件事不同角度的人拉到一个电话里，逐行讨论 Google Doc

## 关联连接
- [[OpenAI]] — 所属公司
- [[Astra]] / [[GPT-6]] — 讨论的核心模型
- [[AGI]] — 通用人工智能
- [[ComputerUse]] — Astra 跃升关键能力
- [[NavierStokes]] — 10000 agent 解决的方程
- [[Lean]] — 数学证明语言
- [[DefenderWindow]] — 防御者窗口概念
- [[DefenseFactory]] — 防御工厂范式
- [[FrontlineDefenders]] — 10 亿美元安全计划
- [[IlyaSutskever]] — 2016-17 年共同推算者
- [[HuggingFace]] — 触发安全讨论的事件方
- [[Sora]] — 今年被取消的项目
- [[问责制]] — 人类应保留的价值
- [[a16z]] — 访谈方
- [[Codex]] — 渗透测试工具
- [[摘要-OpenAI总裁Brockman最新采访]] — 来源
- [[摘要-gpt6-astra实测体验]] — Astra 实测对比
- [[摘要-GPT-6-Astra改变技术栈]] — 技术栈影响
