---
title: "摘要-claude-code-best-practice-苏三视角"
type: source
tags: [Claude Code, 最佳实践, 上下文管理, Hook]
sources: [raw/01-articles/开源了！Claude Code 最佳实践 60 天斩获 54k Star，前后端开发直接起飞了！.md]
last_updated: 2026-06-26
---

## 核心摘要

苏三从研发实战视角解读了 60 天斩获 54.1K Star 的 [claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) 仓库，强调它与 Anthropic 官方文档/Cookbook 的差异：**官方教"会用"，社区教"用对"**。仓库分四大板块：核心概念（10 个，含 Subagents/Commands/Skills/Workflows/Hooks/MCP/Plugins 等）、热门 beta 功能、开发工作流（13 个 GitHub 工作流横向对比，共同收敛到 [[Research-Plan-Execute-Review-Ship]] 五步）、83 条实战技巧。

文章特别提炼了三条立即可用的研发技巧：

1. **上下文 40% 阈值**：Context rot 在 300-400k token 处显现，维持总 context 利用率 < 40%，超过 300k 立即 `/compact`
2. **Plan 与 Execute 分 Session**：Plan 阶段结果 commit 到 Markdown，新开 Session 让 Claude 读 markdown 执行，避免中间稿污染 context
3. **Hook 用于强制纪律而非加功能**：例如 `PostToolUse` hook 在改 src/ 时自动 `mvn test`，省掉"忘跑测试就 commit"的坑

还提到 **Claude Code 写代码 + Codex 评审** 的跨模型互查组合。中文版可通过 PR 分支获取，作者因更新频繁未合并。

## 关联连接

- [[claude-code-best-practice]] — 主体仓库实体
- [[ClaudeCode]] — 主载体
- [[Codex]] — 跨模型评审搭档
- [[Hooks]] — 强制纪律机制
- [[ContextManagement]] — 上下文管理
- [[Research-Plan-Execute-Review-Ship]] — 共同收敛工作流
- [[Superpowers]] — 仓库对比的工作流之一
- [[SpecKit]] — 仓库对比的工作流之一
- [[摘要-claude-code-best-practice]] — 同主题早期摘要
