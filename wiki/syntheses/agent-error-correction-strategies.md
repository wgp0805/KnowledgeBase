---
title: "agent-error-correction-strategies"
type: synthesis
tags: [AI Agent, Claude Code, Codex, 纠偏, 控制机制, 实战]
sources:
  - wiki/concepts/steering.md
  - wiki/sources/摘要-claude-code-实战防搞炸.md
  - wiki/sources/摘要-6条Claude-Code实践经验与思考.md
  - wiki/sources/摘要-claude-code-best-practice-苏三视角.md
  - wiki/sources/摘要-AI-agent工具应该怎么使用.md
  - wiki/sources/摘要-codex-97percent-技巧.md
last_updated: 2026-07-10
---

# AI Agent 运行出错后的纠正策略

发现 AI Agent（[[Codex]] / [[ClaudeCode]] 等）运行方向偏离或生成错误代码时，有五个层次的纠正手段可用，从即时干预到事后回退形成完整闭环。

## 五层纠正体系

| 层次 | 手段 | 时机 | 适用场景 |
|------|------|------|---------|
| 即时 | [[steering]] 增量纠偏 | 运行中 | 方向跑偏、理解偏差 |
| 流程 | Plan 模式先行 | 执行前 | 大任务防跑偏 |
| 隔离 | Plan/Execute 分 Session | 跨阶段 | 上下文污染 |
| 自动 | [[Hooks]] 拦截 | 工具调用前后 | 危险命令/漏测 |
| 回退 | Git 小步提交 + diff | 事后 | 已生成坏代码 |

---

## 一、即时纠偏：Steering

[[steering]] 是 AI Agent 运行过程中最核心的纠偏机制——你随时可以打断 Agent，在不丢失已有上下文的前提下纠正方向。

> 与传统"停止→重新写 prompt"不同，steering 是增量修正。

**操作方式**：直接在当前对话中打断，明确告诉 Agent 刚才的方向不对，给出正确的指引。Agent 会基于已有上下文继续工作，而不是从头开始。

核心哲学（来自 [[摘要-把Codex用到极致]]）：
> 人没有被踢出回路，Agent 不是替你拍板，而是把决策点提前暴露。

---

## 二、流程防线：Plan 模式先行

从 [[摘要-AI-agent工具应该怎么使用]] 和 [[摘要-codex-97percent-技巧]] 提炼的共识：

- 任务超过两三步，**先开计划模式（Plan Mode）**，让 Agent 输出执行计划再写代码
- **审计划比推翻重来高效得多**——方向性问题在计划阶段就能发现
- 计划确认后再执行，把大风险拆成可验证的小步骤

---

## 三、上下文隔离：Plan/Execute 分 Session

[[摘要-claude-code-best-practice-苏三视角]] 中提炼的关键技巧：

1. Plan 阶段的结果 **commit 到 Markdown 文档**
2. **新开一个 Session**，让 Agent 读 markdown 执行
3. 避免中间稿污染上下文——context rot 在 300-400k token 处显现
4. 维持总 context 利用率 **< 40%**，超过 300k 立即 `/compact`

这样即使执行阶段出错，计划阶段的知识不受污染，可以直接复用计划重新执行。

---

## 四、自动防护：Hooks

[[摘要-claude-code-实战防搞炸]] 中提到的 Hook 机制，在 Agent 生命周期的关键节点自动执行防护动作：

- **PreToolUse Hook**：拦截危险命令（如 `rm -rf`、`git push --force`），返回 `decision:block` 阻断
- **PostToolUse Hook**：修改 `src/` 目录后自动跑 `mvn test`，防止"忘跑测试就 commit"
- Hook 用于强制纪律而非加功能

> 注意：prompt 里的"别读"只是建议，deny 规则才是硬保证。

---

## 五、事后回退：Git 小步提交

[[摘要-claude-code-实战防搞炸]] 和 [[摘要-codex-97percent-技巧]] 共同强调：

- **小步提交**：每个步骤都是可回退的锚点
- 至少会看 **Git diff**：知道改了哪些文件、哪些是新增/删除、能否回退
- 重要构建用 [[Worktree]] 隔离工作区，不污染主项目
- 选择标准：小修补用 Local、重要构建用 Worktree、长时间自动化用 Cloud

---

## 补充原则

### 不要手动改 AI 代码

[[摘要-AI-agent工具应该怎么使用]] 第 5 条警告：手动修改 AI 生成的代码会导致 AI 下次覆盖你的改动。**正确做法**是开新对话，明确告诉 Agent 需要修改的内容，让它重新生成。

### 多模型交叉验证

Codex 写代码 + Claude Code 审查（或反之），至少两个 session——一个负责执行，一个负责审核。用另一个 Agent 交叉验证代码质量，降低单一模型幻觉风险。

---

## 总结

| 阶段 | 做什么 | 核心工具 |
|------|--------|---------|
| 事前 | Plan 模式、写 AGENTS.md | [[计划模式]], [[CLAUDEmd]] |
| 事中 | Steering 纠偏、Hooks 拦截 | [[steering]], [[Hooks]] |
| 跨阶段 | 分 Session 隔离上下文 | [[ContextManagement]] |
| 事后 | Git diff + 回退、多模型审查 | [[Git]], [[code-review]] |
| 长期 | 权限分层、deny 规则 | [[auto-mode]] |

**核心理念**：不要让 Agent 在无人监管的情况下长时间跑，把人的决策点提前暴露到每个可校验的节点。

## 关联连接

- [[steering]] — 增量纠偏控制机制
- [[Hooks]] — 生命周期钩子
- [[计划模式]] — Plan Mode 先出方案再执行
- [[CLAUDEmd]] — 项目说明书/指令文件
- [[Worktree]] — Git 工作树隔离
- [[ContextManagement]] — 上下文窗口管理
- [[code-review]] — 代码审查
- [[auto-mode]] — 权限自动模式
- [[ClaudeCode]] — Anthropic 终端 AI Agent
- [[Codex]] — OpenAI 桌面端 AI Agent
- [[摘要-claude-code-实战防搞炸]] — 权限/验证/CLAUDE.md 三位一体
- [[摘要-AI-agent工具应该怎么使用]] — 9 条实战使用技巧
- [[摘要-claude-code-best-practice-苏三视角]] — 上下文 40% 阈值等实战技巧
