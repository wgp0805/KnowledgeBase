---
title: "code-review"
type: concept
tags: [软件工程, 质量保障, 协作]
sources: []
last_updated: 2026-07-27
---

## 定义
代码审查（Code Review）是软件开发中的质量保障实践，由团队成员对代码变更进行系统性检查，旨在发现缺陷、分享知识、维护代码质量标准。

## 关键信息
- 审查维度：正确性、可读性、性能、安全性、测试覆盖
- Pull Request 流程：提交 PR → 自动化检查 → 人工审查 → 合并
- 审查工具：GitHub PR、GitLab MR、Gerrit
- AI 辅助审查：Claude Code review skill、GitHub Copilot
- 最佳实践：小批量提交、明确描述变更目的、关注架构而非风格

### Matt Pocock 的两轴审查法
在 [[MattPocock]] 的 `mattpocock/skills` 中，`/code-review` 被归类为 **Model-invoked（纪律层）** skill，采用两轴并行审查架构：

- **Standards 轴**：检查代码是否符合团队的编码规范、命名约定、项目标准
- **Spec 轴**：检查代码是否满足规格说明（Spec）中的功能需求

两轴以并行子 agent 方式运行，互不污染。这种设计确保了审查不会遗漏规范性或功能性的任何一个维度。

## 关联连接
- [[CI-CD]] — 自动化检查集成
- [[Git]] — 版本控制基础
- [[GitHub]] — PR 审查平台
- [[incident-severity-classification]] — 事故预防
- [[MattPocock]] — 两轴审查法提出者
- [[摘要-mattpocock-skills]] — 来源（两轴审查架构）
- [[TDD]] — 测试驱动开发实践
