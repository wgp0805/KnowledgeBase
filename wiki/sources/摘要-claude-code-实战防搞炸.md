---
title: "摘要-claude-code-实战防搞炸"
type: source
tags: [来源, Claude Code, 实战, 权限, CLAUDE.md]
sources:
  - raw/09-archive/面试官坏笑：“你用ClaudeCode写代码，不怕它把项目搞炸？”，我：“怕，所以CLAUDE.md、权限和验证，一个都不能少。”.md
last_updated: 2026-07-09
---

## 核心摘要

[[程序汪]] 分享一年多 [[ClaudeCode]] 实战经验，核心论点：防"项目搞炸"靠三件事--[[CLAUDEmd|CLAUDE.md]]（项目备忘录规范）、权限管理（分层授权 + deny 规则 + [[auto-mode|Auto Mode]]）、验证（测试/build/截图）。文章系统区分了 CLAUDE.md/Rules/Skills/MCP/Sub-Agent/Hooks/插件各自的职责边界，并给出最常用工作流：探索-计划-执行-验证、TDD、让 Claude 自己验证、代码库问答、Bug 修复提供错误信息、多实例与 [[Worktree]] 隔离、小步提交。

## 关键信息

- CLAUDE.md 应控制在 200 行内，只留"Claude 易猜错的规则、代码里读不出的约定"，删规则判断标准：删掉后 Claude 会不会更易犯错
- 四层层级（组织级/用户级/项目级/本地级），后加载的更具体规则更易被采纳；`/memory` 可验证当前加载了哪些规则
- 权限分层：只读命令（git diff/status/rg）可放行，rm -rf/git push --force/读 .env 用 deny 规则硬拦；prompt 里的"别读"只是建议，deny 才是硬保证
- Auto Mode 用分类器判风险低放行、高风险阻断，但不提供安全沙箱；v2.1.142+ 忽略项目级 auto 设置防仓库自启
- Sub-Agent 内置三类：Explore（Haiku 只读）、Plan（只读）、general-purpose（继承主会话工具）；支线任务隔离上下文，只回结论
- Hooks 在生命周期节点执行动作（PreToolUse 拦危险命令、编辑后格式化、结束前跑测试）；HTTP Hook 拦截需返回 2xx + decision:block
- Code Intelligence（LSP 集成）让 Claude 跳定义查引用，少靠 rg 搜全文

## 关联连接

- [[程序汪]] - 文章作者
- [[ClaudeCode]] - 核心工具
- [[CLAUDEmd]] - 项目指令规范
- [[auto-mode]] - 权限自动模式
- [[Hooks]] - 生命周期钩子
- [[子Agent编排]] - Sub-Agent 隔离
- [[Worktree]] - Git 工作树隔离
- [[TDD]] - 测试驱动开发
- [[MCP]] - 模型上下文协议
- [[Skill]] - 技能扩展机制
- [[Superpowers]] - 现成 Skill 示例
- [[code-review]] - 代码审查
- [[AICoding]] - AI 编程范式
