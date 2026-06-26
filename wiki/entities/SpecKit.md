---
title: "SpecKit"
type: entity
tags: [AI编程, 规范驱动, GitHub官方, 七阶段]
sources: [raw/01-articles/Superpowers、OpenSpec、Spec-Kit 傻傻分不清楚.md]
last_updated: 2026-06-26
---

## 定义

**Spec-Kit** 是 **GitHub 官方出品** 的规范驱动开发（Spec-Driven Development）工具包，于 2025 年 8 月发布。它的核心主张是：**规范不只是"指导文档"，而是可执行的——能直接生成工作代码**（Specifications become executable）。

## 关键信息

- **GitHub**：<https://github.com/github/spec-kit>
- **官方背书**：GitHub 官方维护
- **数据**（截至 2026-06）：115K+ Star、10.2K Fork，2026 年增长最快 AI 工具项目之一
- **支持 AI 代理**：25+ 种（Claude Code、GitHub Copilot、Cursor、Gemini CLI 等）
- **技术栈**：Python（基于 `uv`）
- **适用项目**：偏 **绿地项目（greenfield）**，对已有代码库适配不如 OpenSpec 自然

### 七阶段流水线

| 阶段 | 命令 | 作用 |
| --- | --- | --- |
| 宪法 | `/speckit.constitution` | 定义项目级治理原则（代码质量、测试、UX、性能） |
| 规范 | `/speckit.specify` | 描述功能需求（关注 What/Why，不涉及技术栈） |
| 计划 | `/speckit.plan` | 制定技术方案（技术栈、架构、API 契约） |
| 任务 | `/speckit.tasks` | 拆解可执行任务清单 |
| 分析 | `/speckit.analyze` | 一致性检查 |
| 实现 | `/speckit.implement` | 执行实现 |
| —— | —— | 每阶段输入输出明确，像工厂流水线 |

### 安装

```bash
# 安装 uv
curl -LsSf https://astral.sh/uv/install.sh | sh
# 安装 Specify CLI
uv tool install specify-cli --from
```

### 优缺点

- ✅ GitHub 官方背书，长期维护有保障
- ✅ 规范可执行，直接生成工作代码
- ✅ 项目宪法机制从顶层约束 AI 行为
- ❌ 学习曲线陡峭
- ❌ Python/uv 技术栈对 Java 开发者有门槛
- ❌ 对棕地项目适配不如 OpenSpec

## 关联连接

- [[Superpowers]] — 兄弟方案，管"怎么干"
- [[OpenSpec]] — 兄弟方案，管"改了什么"
- [[规范驱动开发]] — 方法论
- [[GitHub]] — 出品方
- [[VibeCoding]] — 共同要解决的现象
- [[ClaudeCode]] — 主要承载平台
- [[摘要-superpowers-openspec-speckit对比]] — 来源
