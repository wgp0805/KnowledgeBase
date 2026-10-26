---
title: "Worktree"
type: concept
tags: [Git, 隔离, Agent, 工作流, Codex]
sources: [raw/09-archive/3 分钟掌握 Codex 97% 的功能，超实用教程！.md, raw/09-archive/2026-09-24-Claude Code 把自己改成了任务调度器，这次设计比功能更值得看 - 码哥字节.md, raw/09-archive/2026-09-25 - GitHub 6.7万 Star，一个多 Agent 协作、手机远程指挥的开源神器！.md, raw/09-archive/2026-10-19-Claude Code桌面版迎来重大更新.md]
last_updated: 2026-10-21
---

## 定义
Worktree（工作树隔离）是给 AI Agent 开一个隔离工作区的机制，Agent 可以在其中改代码、试功能、跑实验，但不直接污染主项目。做坏了直接丢掉，不用在主目录收拾残局。

## 关键信息
- 核心价值：多个需求并行时互不影响（一个分支做登录、一个做支付、一个修 bug）
- 选择标准：
  - **Local**：小修补（如改一句文案）
  - **Worktree**：重要构建、大范围改代码、多需求并行
  - **Cloud**：长时间运行的自动化任务
- 大部分情况下 Worktree 是最安全的选择

### Claude Code 的自动 Worktree 隔离（2026-09）
来自 [[摘要-claude-code-agent视图与goal]]。Agent 视图开启新后台任务时，Claude 自动把它隔离到 `.claude/worktrees/` 下的独立 worktree——解决多个并行会话改同一仓库的文件冲突，各自 merge/push 后互不干扰。坑：会话异常终止会遗留孤儿 worktree，用 `git worktree list` 排查、`git worktree remove <path>` 清理。

### Orca 的并行 Worktree 对比挑选（2026-09）
来自 [[摘要-orca-ade多agent协作]]。Orca 把 worktree 用成「多方案竞速」：同一需求派给多个 Agent，每个分到独立目录+独立分支，跑完在统一界面并排看 diff，挑一份最满意的合并、其余丢弃；还可从 GitHub/Linear 任务一键开出新 worktree。

### Claude Code 桌面版的会话级 Worktree（2026-10-20，详见 [[摘要-claude-code桌面版嵌套会话更新]]）
桌面版"环境"功能中，环境中每个文件夹可独立选分支并决定是否启用 worktree——多个会话同时改同一仓库时各在独立 worktree 工作，避免互相覆盖。默认创建在项目根 `.claude/worktrees/` 下。**关键坑**：`.env` 等被 `.gitignore` 忽略的文件**不会自动出现在新 worktree**，子会话依赖这些配置时必须写入 `.worktreeinclude`，否则新会话因缺环境变量启动不了项目。此时 worktree 的角色从"并行开发分支"扩展为"多 AI 会话安全并发改同一仓库的隔离层"。

### 多 Agent 并发改同一文件：worktree 的四道检查与漏洞（2026-10-21，详见 [[摘要-多agent并发改文件冲突]]）

**Claude Code 的做法是给每个 Agent 一整个仓库**：
- 启动加 `--worktree <名字>` → 在 `.claude/worktrees/` 下建独立工作目录、切一条 `worktree-<名字>` 分支
- 该目录由 git worktree 出来，有自己的文件与分支，但**和主仓库共享同一份提交历史**
- Sub-agent 在 frontmatter 里加 `isolation: worktree` 即可获得隔离；若无改动，Claude Code 会自动清理该目录

**光建目录不够**——Agent 完全可以用一条绝对路径把文件写回主仓库。所以 Claude Code 加了四道检查：

| 检查 | 规则 |
|---|---|
| ① 文件编辑 | Edit / Write / NotebookEdit 三个工具，目标路径落在主仓库里 → 直接拒绝 |
| ② 命令在哪里执行 | Bash 命令如果在主仓库里执行 → 拒绝 |
| ③ git 重定向 | 想用 `git -C`、`--git-dir` 把 git 指回主仓库 → 拒绝 |
| ④ 命令形态 | 命令文本无法确认里面的 git 会留在 worktree 里（如命令名是运行时算出来的）→ 拒绝 |

**明确的漏洞**（官方文档也写了）：这些检查看的是**编辑的目标路径、命令在哪里执行、命令文本本身**，**没有跟踪 shell 命令实际写入了哪些文件**——用 `cp` 或重定向把内容往主仓库里写，这几道检查拦不住。

> **Claude Code 没有解决冲突，它只是让冲突暂时不可能发生**——冲突被延迟到合并那一步，git 该报冲突还是会报，只不过需要人来处理。

**对照方案**：Pi 没有 worktree，靠**时间**——模块级 Map 实现的文件变更队列让同一文件的写操作串成 Promise 链。详见 [[Agent并发写冲突]]。

**worktree 检不出的冲突类型**：**语义冲突**——两个 Agent 分别改了不同文件里的一致性契约（函数返回值类型、接口约定），git 一个冲突都不报，merge 后运行时才炸。详见 [[语义冲突]]。

## 关联连接
- [[Codex]] — 核心使用工具
- [[Git]] — 底层版本控制机制
- [[ClaudeCode]] — 自动创建 worktree 的工具
- [[Orca]] — 并行 worktree 对比挑选的 ADE
- [[agent-view]] — 后台会话的 worktree 隔离
- [[Subagent]] — 隔离的并行执行单元
- [[摘要-codex-97percent-技巧]] — 来源
- [[摘要-claude-code-agent视图与goal]] — 来源（Claude Code 自动隔离）
- [[摘要-orca-ade多agent协作]] — 来源（Orca 并行对比）
- [[摘要-claude-code桌面版嵌套会话更新]] — 来源（桌面版会话级 worktree 与 .worktreeinclude 坑）
- [[摘要-多agent并发改文件冲突]] — 来源（四道检查与漏洞、与 Pi 队列的对照）
- [[Agent并发写冲突]] — 空间隔离 vs 时间串行两条路线
- [[语义冲突]] — worktree 检不出的跨文件契约冲突
- [[Pi (coding harness)]] — 对照方案（模块级文件变更队列）
