---
title: "code-review"
type: concept
tags: [软件工程, 质量保障, 协作]
sources: []
last_updated: 2026-05-29
---

## 定义
代码审查（Code Review）是软件开发中的质量保障实践，由团队成员对代码变更进行系统性检查，旨在发现缺陷、分享知识、维护代码质量标准。

## 关键信息
- 审查维度：正确性、可读性、性能、安全性、测试覆盖
- Pull Request 流程：提交 PR → 自动化检查 → 人工审查 → 合并
- 审查工具：GitHub PR、GitLab MR、Gerrit
- AI 辅助审查：Claude Code review skill、GitHub Copilot
- 最佳实践：小批量提交、明确描述变更目的、关注架构而非风格

## 关联连接
- [[CI-CD]] — 自动化检查集成
- [[Git]] — 版本控制基础
- [[GitHub]] — PR 审查平台
- [[incident-severity-classification]] — 事故预防
