---
title: "摘要-用户需求模糊时Agent怎么澄清"
type: source
tags: [来源, Agent, 需求澄清, AskUserQuestion, ClaudeCode, Codex]
sources: [raw/09-archive/用户需求模糊时 Agent 怎么澄清？.md]
last_updated: 2026-10-15
---

## 核心摘要

沉默王二（二哥）以面试题形式拆解「用户需求模糊时 Agent 怎么澄清」，核心论点是：**只靠一句"遇到不清楚的需求先反问用户"的提示词必然失败**，要么退化成十万个为什么，要么把问题原封不动踢回给用户。生产级 Agent 的处理原则是**先调用只读工具查清事实，再带着方案给用户选择**。

文章给出四层递进的答案：

1. **分类未知信息**。Codex 在 Plan 模式系统提示词中把未知信息拆成两类：**Discoverable facts**（可发现的事实，如框架选型、现有接口位置、Redis 配置——先探索后提问）与 **Preferences and tradeoffs**（个人偏好与方案取舍，如限流阈值、超限后排队还是报错——必须用户拍板）。Claude Code 源码中的同义铁律是 "Never ask what you could find out by reading the code"。即使搜索出两套鉴权模块，Agent 也要先有自己的判断，带着现成方案去问。
2. **用 JSON Schema 锁死问法**。Claude Code 的 `AskUserQuestion` 工具规定：打包提问（`questions` 数组最少 1 个最多 4 个）、每个问题必须给 2 个选项并写清名称与方案、推荐项放第一个并在名称末尾标 Recommended、严禁模型自己生成 Other 选项（该选项留给用户输入）。Pi 的 `questionnaire` 扩展工具同样默认开启 `allowOther`，自动追加 "Type something"。
3. **把提问本身做成工具**。直接结束本轮对话会切断推理上下文；最优雅的实现是把"向用户提问"包装成标准工具。Claude Code 的 `AskUserQuestion` 复用了工具权限审批通道：`requiresUserInteraction` 固定返回 true、`checkPermissions` 固定返回 ask，即使开启跳过全部审批的自动模式也会被强制拦下；交互处理器创建未决 Promise 放进确认队列，Agent Loop 在 `await` 处自然挂起，不额外消耗 Token；用户提交后答案写入 `updatedInput.answers` 唤醒 Promise，组装成 `tool_result`（正文 "User has answered your questions"）回传模型继续推理。
4. **无人在场时的兜底**。工具层拦截：Codex 的 `request_user_input` 第一行检查是否为 root 线程，Sub-agent 调用直接报错 "request_user_input can only be used by the root thread"；`codex exec` 非交互模式下，外部 MCP 服务端通过 elicitation 发来的追问请求也会被自动取消（源码直接返回 Cancel）；Pi 的 questionnaire 执行前检查是否 TUI 模式，不是则报错返回。提示词兜底：Codex 规定无法获取用户回答时不要停下来，直接按最稳妥的推荐选项继续执行，但必须在最终输出的 **Assumptions（假设清单）** 小节里把替用户做出的所有假设逐条写清，供用户事后核对。

## 关联连接

- [[DiscoverableFacts]] — 与偏好相对的另一半：能从代码里查出来的事实必须先查
- [[偏好与取舍]] — 代码里查不到、且会改变执行结果的信息才需要用户拍板
- [[AskUserQuestion]] — 把提问做成工具的典型实现（Claude Code 源码）
- [[AgentLoop]] — 提问工具挂起循环、等待 tool_result 的机制
- [[Assumptions假设清单]] — 无人在场时替用户做决策的兜底交付物
- [[Codex]] — Discoverable facts 分类与 request_user_input 线程限制出处
- [[ClaudeCode]] — "Never ask what you could find out by reading the code" 与 AskUserQuestion 出处
- [[Pi]] — questionnaire 扩展工具的 allowOther/TUI 检查设计
- [[沉默王二]] — 原文作者
- [[HITL]] — 人类在环审批与提问共用同一套通道
- [[计划模式]] — AskUserQuestion 在计划模式中的用法
