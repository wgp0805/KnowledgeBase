---
title: "ComputerUse"
type: concept
tags: ["Codex", "Computer-Use", "OpenAI", "AGI", "安全围栏"]
sources:
  - raw/09-archive/2026-09-15-OpenAI 总裁最新采访：现在所有人对 AI 的预测，大概率都是错的.md
  - raw/09-archive/说说 Codex 的 Computer Use 原理。.md
last_updated: 2026-10-27
---

## 定义
Computer Use 是让 AI Agent 直接操作电脑界面（用鼠标、键盘、截图的方式来完成任务），就像一个真实的人坐在电脑前操作一样的能力。是 GPT-6 Astra 时代的核心跃升点，也是 Greg Brockman 判断"AGI 时代已经到来"的关键依据。

## 关键信息

### Astra 时代 Computer Use 的意义
- **Agent 能否用的两点**：模型够不够聪明去使用工具 + 能不能访问到需要的上下文
- **传统做法**（建 API/MCP server/CLI 接口）本质是给 AI 打补丁——把软件改造成 AI 勉强能用的格式，又麻烦又别扭，而且会引入额外的安全风险（多一层接口多一层可能被攻击的面）
- **Computer Use 完全不同**：让 AI 直接用人类界面操作软件，不需要任何特殊 API、不需要重新设计任何系统
- **方向上的根本转变**：以前是人类改变自己去适应软件，然后我们又在改造软件去适应 AI，但现在 AI 终于可以直接用人类用的那套界面了
- **不依赖任何中间层**：从长远看这条路会走得更远

### 2015-11 OpenAI 内部会议
OpenAI 早在 2015 年 11 月的一次内部会议上就讨论过这个想法——**"如果强化学习的环境是屏幕像素加上键鼠输入，那是不是任何可以在电脑上做的事都能成为训练任务？"** 当时有过早期尝试，但一直到现在才真正实现。

### 与 Codex 内置 Computer Use 的关系
- **Codex 的 Computer Use**：Codex 2026 大版本更新引入，让 Agent 直接操作 IntelliJ IDEA、Chrome 浏览器等桌面应用
- **Astra 的 Computer Use**：GPT-6 Astra 更广泛的能力——不只是 IDE 和浏览器，而是任何可以在电脑上做的事
- Codex 的 Computer Use 是 Astra 通用 Computer Use 能力在 Codex 产品形态下的落地

### 与 MCP/CLI 接口对比
| 维度 | API/MCP/CLI | Computer Use |
|-----|------------|-------------|
| 依赖 | 需要为 AI 建接口 | 用人类现有界面 |
| 攻击面 | 多一层接口多一层攻击面 | 无额外接口 |
| 覆盖 | 只覆盖已建模的部分 | 任何可在电脑上做的事 |
| 改造成本 | 需重新设计系统 | 不需任何改造 |

### Codex Computer Use 底层实现原理（2026-10-26 来源：[[摘要-codex-computer-use原理]]）
Computer Use 不是给大模型暴露一堆 `click`/`move`/`type` 原子工具（每做一个动作请求一次模型）。与 [[BrowserUse]] 靠网页无障碍树拿元素编号点击不同，Computer Use 面对的是操作系统——很多原生桌面软件没有统一结构化接口，必须结合屏幕画面和系统状态来操作。

**1. `cua_repl` 脚本编排（核心设计）**
Codex 内置插件挂载 `cua_repl` MCP 服务，向模型暴露的核心工具叫 `js`，只收两个参数：`title`（动作意图描述，Codex 据此把连续多次操作折叠显示为 `Using computer · N actions`）和 `code`（JavaScript 代码）。模型在持久化 Node.js REPL 环境里直接调用全局 `cua` 对象——`await cua.getState()` 获取桌面状态，完成点击/输入/截屏，返回文本输出 + Base64 PNG 截图；回合结束或中断时内置钩子调用 `turn_ended` 释放桌面焦点。

**为什么不让模型逐动作调用原子工具**：桌面操作往往是一连串动作，移动一下鼠标、敲一下回车都要走一轮模型推理并重传高清截图，延迟和 Token 消耗不可承受；持久化 REPL 里一次调用就能执行完整个动作串。

**KV Cache 保护**：Codex 不在系统提示词里塞满接口文档——只有当模型写错方法名触发 `"Script error"` 时，`cua_repl` 才把完整的 Computer Use API 文档拼接到报错末尾（按需加载，保护 [[KV Cache]]）。

**2. 应用访问控制（黑白名单）**
`computer_use` 配置块里用 `default_app_access` 设定默认 allow/deny，再按操作系统原生应用标识逐个控制：macOS 绑 `bundle_ids`（如 Safari allow、Terminal deny），Windows 绑 `aumids` 和可执行文件签名信息。不是靠系统提示词叮嘱"别点无关窗口"，而是配置层硬控制。

**3. 四级敏感动作确认策略**
- 第一级：必须移交用户的操作（密码、银行卡、验证码、两步验证、签署协议），严禁 Agent 触碰
- 第二级：动作发生前一刻必须确认（发送消息、付款、删除文件、修改安全设置），不接受提前授权
- 第三级：允许预先授权的常规修改
- 第四级：免确认只读操作（截图、滚动、切换窗口）

`js` 脚本运行中途即将触发桌面动作时，`cua_repl` 反向给 Codex 发 `elicitation/create` 审批请求，Codex 检查 `codex_sensitive_action` 标记：普通点击自动 `Accept` 静默放行不打断用户；敏感动作立刻挂起脚本、弹窗让用户确认或转交安全围栏——**普通点击静默放行保流畅，高危动作中途挂起保安全**。

**4. Guardian 安全围栏（防屏幕内容注入）**
屏幕上的网页/文档可能藏着攻击者伪造的恶意指令，截图给模型看就可能被劫持（[[PromptInjection]]）：
- `cua_repl` 返回的文本 + PNG 截图存入上限 **8M** 的证据缓冲区（超限优先淘汰旧图片、保留文本记录）
- 审查下一步操作时，历史截图和输出打上**不可信证据标签**，连同原图发给 Guardian 模型，核对点击目标是否符合用户本意
- **Guardian V2 自适应模式**：会话首次调用 `cua_repl` 的 `js` 时上下文里还没有外部截图进入、不存在注入可能，直接走 `initial_cua_call` 快速通道；同时后台启动 `LunaSampler` 异步对会话风险打分（低风险 0 / 高风险 1）——低风险期间快速放行，一旦截图触发高风险评分立刻切同步阻塞审查

**5. 跨应用接管 Agent**：Codex 可直接操控另一个桌面 Agent（如 [[DeepSeekHarness]]，DSH 左上角显示"被电脑控制"图标）——Agent 操控 Agent 的真实演示。

## 关联连接
- [[GregBrockman]] — 提出 Computer Use 重要性的判据者
- [[OpenAI]] — 实现方
- [[GPT-6]] / [[Astra]] — 核心模型
- [[Codex]] — 落地产品
- [[AGI]] — Computer Use 是 AGI 时代的钥匙
- [[MCP]] — Computer Use 对照方案
- [[NavierStokes]] — Computer Use 支撑的高阶能力案例
- [[摘要-OpenAI总裁Brockman最新采访]] — 来源
- [[摘要-GPT-6-Astra改变技术栈]] — Astra 技术栈影响
- [[摘要-gpt6-astra实测体验]] — Astra 实测（前端能力）
- [[摘要-codex-obsidian-自生长知识库]] — 同赛道 Computer Use 实践
- [[摘要-codex-computer-use原理]] — 来源（Codex cua_repl/黑白名单/确认策略/Guardian 围栏源码级拆解）
- [[BrowserUse]] — 对照物（无障碍树 vs 屏幕画面+系统状态）
- [[DeepSeekHarness]] — 被 Codex 接管操控的桌面 Agent 实例
- [[PromptInjection]] — 屏幕恶意内容劫持风险的本质
- [[KV Cache]] — API 文档按需加载的保护对象
- [[HITL]] — 四级确认策略的人机协同本质
