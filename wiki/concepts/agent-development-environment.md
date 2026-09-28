---
title: "agent-development-environment"
type: concept
tags: [概念, ADE, 多Agent, 开发环境]
sources: [raw/01-articles/2026-09-25 - GitHub 6.7万 Star，一个多 Agent 协作、手机远程指挥的开源神器！.md]
last_updated: 2026-09-28
---

## 定义

ADE（Agent Development Environment，智能体开发环境）是一类以 Agent 为干活主力的开发环境：传统 IDE 里 AI 只是插件，ADE 里人主要负责派任务、看进度，跑完挑结果。代表实现是 [[Orca]]。

## 关键信息

- **与 IDE 的差别**：主客易位——IDE 的主体是人写代码、AI 辅助；ADE 的主体是 Agent 执行，人做任务分发与结果验收
- **不含模型**：ADE 本身不卖模型、不收订阅费，复用用户本地已登录的命令行 Agent（终端里能跑就能接入），各 Agent 额度照旧各自计算
- **核心能力组合**：
  - 并行 [[Worktree]]：同一需求多 Agent 各自独立目录+分支，跑完并排 diff 挑一份合并
  - 分屏终端与状态通知：一眼看谁完成、谁卡住
  - Design Mode：点选页面元素连同 HTML/CSS/截图发给 Agent，省去口头描述样式
  - Diff 行级批注：像给人 review 代码一样在哪行提意见
  - 远程与移动端：SSH 远程 worktree 跑重活，手机 App 收通知、发指令
  - 账号与用量管理：多账号一键切换，显示限流重置时间
- **成本提醒**：并行 Agent 数量即 token 消耗倍数，ADE 把杂事管起来但不替你省 token
- **适用判断**：已同时用两三个 AI 编程工具、被窗口和分支搞得头疼的人适合；单 Agent 一次一事的人偏重

## 关联连接
- [[Orca]] — 代表实现
- [[Worktree]] — 并行协作隔离机制
- [[multi-agent-collaboration]] — 多 Agent 协作模式
- [[ClaudeCode]] — 可接入的 Agent
- [[Codex]] — 可接入的 Agent
- [[AICoding]] — 所属领域
- [[摘要-orca-ade多agent协作]] — 来源
