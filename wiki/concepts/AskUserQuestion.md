---
title: "AskUserQuestion"
type: concept
tags: [Agent, 工具设计, ClaudeCode, HITL, JSONSchema]
sources: [raw/01-articles/用户需求模糊时 Agent 怎么澄清？.md]
last_updated: 2026-10-15
---

## 定义

`AskUserQuestion` 是 Claude Code 源码中用于**向用户提问**的内置工具。它的设计精髓是：把"向用户提问"包装成一个标准工具调用，复用工具权限审批通道挂起 Agent 循环，等用户回答后再以 `tool_result` 形式回到模型，从而在不切断当前推理上下文、不额外消耗 Token 的前提下完成[[需求澄清]]。

## 关键信息

### 1. 用 JSON Schema 锁死问法
- **打包提问**：顶层 `questions` 数组规定最少 1 个、最多 4 个问题，提示词要求把相关问题打包在一次调用里完成，而不是连续追问。
- **给足选项并标明推荐项**：每个问题必须提供 2 个选项，每个选项都要写清楚名称和方案。若模型有倾向方案，把推荐项放在第一个，并在名称末尾加 **Recommended** 标记。
- **留兜底输入框**：工具描述里**严禁模型自己生成 Other 选项**，因为该选项是交给用户输入的。

对比：Pi 的 `questionnaire`（问卷扩展工具）采取同样的设计，默认开启 `allowOther`，自动在列表最后追加一项 "Type something"。

### 2. 复用权限审批通道实现挂起
- 没有单独写一套暂停逻辑，`requiresUserInteraction`（是否需要用户交互）固定返回 true，`checkPermissions`（权限检查）固定返回 `ask`；
- 因此**即使开启了跳过所有权限审批的自动模式**，执行到这个工具时也会被强制拦下来；
- 交互处理器创建一个未决的 Promise（异步占位对象）放进前端确认队列，Agent Loop 就在 `await` 处自然挂起，**不会多消耗任何一个 Token**；
- 用户在界面勾选答案并提交后，前端把回答写进 `updatedInput.answers` 字段唤醒 Promise；系统把回答组装成一条标准 `tool_result`，正文为 "User has answered your questions"，再传回模型继续推理。

### 3. 错误做法对照
- **直接结束本轮对话等下一轮消息**：当轮推理的上下文状态就断了；
- **轮询数据库**：无意义开销。
把提问做成工具（选项 B）才是最优雅的实现。

### 4. 无人在场时必须被拦住
见[[Assumptions假设清单]]：后台定时任务、Headless 模式或 Sub-agent 场景下屏幕前没有人，工具层需要先行拦截（例如 Codex 的 `request_user_input` 只允许 root 线程调用）。

## 关联连接

- [[DiscoverableFacts]] — 提问前必须先查清的部分
- [[偏好与取舍]] — 该工具专门用来收集的信息类型
- [[需求澄清]] — 所属方法论
- [[AgentLoop]] — 工具调用如何挂起并恢复循环
- [[HITL]] — 与人工审批共用同一套通道
- [[计划模式]] — 让 Claude 用该工具采访用户、发现边缘情况
- [[Assumptions假设清单]] — 无人应答场景的兜底
- [[ClaudeCode]] — 该工具的实现方
- [[Pi]] — questionnaire 的同类设计
- [[摘要-用户需求模糊时Agent怎么澄清]] — 来源
