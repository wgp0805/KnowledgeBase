---
title: "Superpowers"
type: entity
tags: [AI编程, Skill框架, 工程纪律, 开源]
sources:
  - raw/01-articles/全网爆火的Superpowers到底是什么.md
  - raw/01-articles/Superpowers、OpenSpec、Spec-Kit 傻傻分不清楚.md
  - raw/01-articles/有人把 5.7 万星 OpenSpec 和 24 万星 Superpowers 融合成一个工作流在 Github 开源.md
last_updated: 2026-07-09
---

## 定义

**Superpowers** 是由开发者 Jesse Vincent（GitHub: obra）打造的 **AI 编程代理技能框架与开发方法论**。它的目标不是让 AI 更聪明，而是让 AI 更"守规矩"——通过强制流程把软件工程最佳实践"焊死"在 AI Agent 上，将 AI 编码助手从"急于交差的初级开发"改造成"严守纪律的资深工程师"。

## 关键信息

- **作者**：Jesse Vincent（GitHub: obra）
- **GitHub**：<https://github.com/obra/superpowers>
- **数据**（截至 2026-06）：238K Star、21.1K Forks，Anthropic 官方插件市场安装量 68 万+
- **核心理念**：**Process over Prompt（流程大于提示词）**
- **技术形态**：仅一组 `SKILL.md` 文件，无运行时、不锁定模型
- **兼容平台**：Claude Code、Codex CLI、Gemini CLI、Cursor、GitHub Copilot CLI 等
- **协议**：MIT

### 14 个核心 Skill

| 分类 | Skill | 作用 |
| --- | --- | --- |
| 协作 | brainstorming | 入口 Skill，未经用户批准禁止动手写代码 |
| 协作 | writing-plans | 把设计拆成 2-5 分钟细粒度任务 |
| 协作 | executing-plans | 按计划执行 |
| 协作 | subagent-driven-development | 子代理隔离 + F1/F2 两阶段审查 |
| 协作 | dispatching-parallel-agents | 派发并行子代理 |
| 协作 | requesting-code-review | 自动发起代码评审 |
| 协作 | receiving-code-review | 处理评审反馈 |
| 协作 | using-git-worktrees | Git 工作区隔离 |
| 协作 | finishing-a-development-branch | 分支收尾 |
| 测试 | test-driven-development | 强制 TDD（红-绿-重构） |
| 测试 | verification-before-completion | 完成前验证 |
| 调试 | systematic-debugging | 系统化定位根因 |
| 元 | writing-skills | 编写新 Skill |
| 元 | using-superpowers | Superpowers 激活恢复 |

### 五阶段开发流程

任何代码产出必须依次走完：**头脑风暴 → 方案设计 → 编写计划 → 执行开发 → 代码审查**，一步都不能跳。

### 质量门禁四件套

1. **TDD 铁律**：没有失败测试就不准写生产代码，不是建议是强制。AI 若违反，规则要求把写的代码全部删掉，从 failing test 重新开始，把"先写个大概能跑的版本再补测试"这扇门焊死
2. **[[review-gate|Review Gate]]**：四层层层设卡——spec 写完先自审、每个任务完成后审查、整个分支完成后审查、交付前最终验证，任何一层没通过都不能往下走
3. **Red Flags 表**：列出 AI 可能用来跳过流程的借口（"改动太小不需要测试""用户赶时间先跳过 review"），逐条说明为何这些借口不成立
4. **[[subagent-driven-development|SDD]]**：子代理上下文隔离 + 双裁决审查。v6.0 评测显示 token 消耗砍约 50%，速度翻倍。

### 安装

```bash
# 注册市场源
/plugin marketplace add obra/superpowers-marketplace
# 安装插件
/plugin install superpowers@superpowers-marketplace
/reload
```

### 设计取舍与已知问题

- **2000 tokens 引导注入**：会话启动只注入引导文档而非全量 Skill，节省上下文但子 Agent 继承需额外 Hook
- **强制流程 vs 灵活性**：对简单任务有"杀鸡用牛刀"嫌疑
- **子 Agent 上下文继承不完整**：SubagentStart Hook 偶尔失败，需手动触发 `using-superpowers` 恢复，官方预计 v5.2.0 修复

## 关联连接

- [[OpenSpec]] — 兄弟方案，管"改了什么"
- [[SpecKit]] — 兄弟方案，让规范可执行
- [[Skill]] — 实现机制
- [[review-gate]] — 审查门禁机制
- [[subagent-driven-development]] — 子代理驱动开发
- [[SpecSuperflow]] — 与 OpenSpec 的融合插件
- [[摘要-spec-superflow-融合工作流]] — 融合方案来源
- [[VibeCoding]] — 它要消灭的现象
- [[ClaudeCode]] — 首发载体
- [[Cursor]] — 兼容平台
- [[Codex]] — 兼容平台
- [[子Agent编排]] — 核心机制
- [[TDD|test-driven-development]] — 强制 TDD
- [[code-review]] — 自动代码审查
- [[摘要-superpowers到底是什么]] — 来源
- [[摘要-superpowers-openspec-speckit对比]] — 来源
