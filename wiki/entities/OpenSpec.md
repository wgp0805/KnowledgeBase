---
title: "OpenSpec"
type: entity
tags: [AI编程, 规范驱动, 开源工具]
sources:
  - raw/01-articles/同事："Claude Code都能自动写代码了，还要什么Spec Coding？" 我反问："屎山代码你来维护？".md
  - raw/09-archive/有人把 5.7 万星 OpenSpec 和 24 万星 Superpowers 融合成一个工作流在 Github 开源.md
last_updated: 2026-07-09
---

## 定义

OpenSpec 是一个面向 AI 编程的规范驱动框架，核心思想是"先对齐需求，再写代码"。它通过生成提案、需求规格、技术设计和任务清单等规划文档，经人工确认后再让 AI 实现，让 AI 编程的结果更加符合预期。

## 关键信息

- **开源方**：[[FissionAI]]，MIT 协议
- **GitHub Star**：57k+（5.7 万星，截至 2026-07）
- **版本**：v1.4.1
- **核心理念**：先对齐需求，再写代码
- **中文版**：https://github.com/studyzy/OpenSpec-cn
- **原版**：https://github.com/Fission-AI/OpenSpec
- **支持平台**：25+ 个 AI 编码平台（Claude Code、Cursor、Codex、Gemini CLI 全覆盖）
- **定位边界**：规划引擎，把规划做到极致，有意不碰从规划到落地这段路

### 核心工作流

1. **探索模式** (`/opsx:explore`): 通过纯对话方式探讨需求，理清需求再动手
2. **提案模式** (`/opsx:propose`): 生成规划制品，包括：
   - proposal.md：变更提案，为什么要做和做什么
   - specs/spec.md：需求规格，用结构化格式描述具体需求和验收场景
   - design.md：技术设计，描述技术实现方案
   - tasks.md：任务清单，列出实现步骤
3. **应用模式** (`/opsx:apply`): 按清单逐项实现，生成实际代码+tasks进度更新
4. **归档模式** (`/opsx:archive`): 完成后归档存档，将规划文档移入archive目录

### 工件依赖图

工件依赖链：proposal（变更意图）-> specs（具体需求，用 SHALL/MUST 确定性词汇 + Given/When/Then 场景）-> design（技术方案）-> tasks（可执行步骤）-> implement。每个工件有 schema 定义，靠 YAML 引擎做拓扑排序。依赖关系是"使能"而非"卡死"--随时可回去修改前面工件。

### Delta Spec 增量变更

详见 [[delta-spec]]。用 ADDED/MODIFIED/REMOVED 三标记描述变更差异，不动已有 spec，只描述差异。棕地项目改一处不必重写整份 spec。通过 `/opsx:sync` 同步 delta spec 到主 spec。

### 安装与初始化

```bash
# 安装
npm install -g @studyzy/openspec-cn@latest

# 初始化（交互式，会提示选择工具）
cd your-project
openspec-cn init

# 非交互式：--tools 支持逗号分隔多工具、all、none
openspec-cn init --tools claude,cursor,codex   # 指定多个
openspec-cn init --tools all                     # 全部 31 个工具
openspec-cn init --tools none                    # 跳过工具配置
openspec-cn init --tools opencode                # 单个工具

# 查看仪表盘
openspec-cn view
```

**支持的工具 ID（31 个）**：`amazon-q`, `antigravity`, `auggie`, `bob`, `claude`, `cline`, `codex`, `forgecode`, `codebuddy`, `continue`, `costrict`, `crush`, `cursor`, `factory`, `gemini`, `github-copilot`, `iflow`, `junie`, `kilocode`, `kimi`, `kiro`, `lingma`, `vibe`, `oh-my-pi`, `opencode`, `pi`, `qoder`, `qwen`, `roocode`, `trae`, `windsurf`

每个工具按各自目录约定生成 Skills（`.../skills/openspec-*/SKILL.md`）和 Commands（`.../commands/opsx-<id>.md`）。

## 关联连接

- [[摘要-OpenSpec规范驱动AI编程框架]] — 来源
- [[摘要-superpowers-openspec-speckit对比]] — 三方对比来源
- [[规范驱动开发]] — 上层方法论
- [[FissionAI]] — 开源方
- [[delta-spec]] — 增量变更机制
- [[SpecSuperflow]] — 与 Superpowers 的融合插件
- [[摘要-spec-superflow-融合工作流]] — 融合方案来源
- [[Superpowers]] — 兄弟方案，管"怎么干"
- [[SpecKit]] — 兄弟方案，让规范可执行
- [[AICoding]] — AI 辅助编程范式
- [[OpenCode]] — 支持 OpenSpec 的编程工具
- [[Skill]] — 技能扩展机制
- [[ClaudeCode]] — AI 编程工具
