---
title: "SpecSuperflow"
type: entity
tags: [AI编程, 工作流, 规范驱动, Claude Code插件, 开源]
sources:
  - raw/01-articles/有人把 5.7 万星 OpenSpec 和 24 万星 OpenSpec 融合成一个工作流在 Github 开源.md
  - raw/01-articles/253k Superpowers 和 60k OpenSpec 被融合了！spec-superflow 工作流登上热榜.md
last_updated: 2026-07-14
---

## 定义

SpecSuperflow 是一个开源的 Claude Code 插件（MIT 协议，零外部运行时依赖），由 [[MageByte-Zero]] 开发。它将 [[OpenSpec]]（规划引擎）与 [[Superpowers]]（执行纪律框架）**源码级融合**为一个自动化工作流，用 contract-builder 桥接层生成 execution-contract.md 作为规划到实现的唯一交接层（Guarded Handoff），由 8 状态路由引擎自动驱动流转，消除手动在两个框架间切换、归档、检查漂移的"人肉胶水"成本。

## 关键信息

- **GitHub**：https://github.com/MageByte-Zero/spec-superflow
- **协议**：MIT，零运行时依赖（纯 TypeScript devDependency）
- **Star**：380+（2026-07）
- **支持平台**：跨 17 个客户端（Claude Code、Cursor、Copilot、Kimi、Pi 等），同一套 skills/scripts/docs/templates/hooks 通过各平台 manifest 和安装器分发
- **Star 来源**：253k Superpowers + 60k OpenSpec 用户

### 设计理念：源码级融合，不是简单并列

不是分别装两个插件再手工串联，而是把两者的核心引擎源码级吸收进同一个插件：

- **从 OpenSpec 借来**：规划侧引擎（Schema、验证、解析、Requirement/Scenario/Delta/Change/Spec 类型定义、delta spec 机制）
- **从 Superpowers 借来**：执行侧纪律（TDD 铁律、SDD 子代理驱动、根因调试、代码审查三级严重度、完成前验证）
- **独创两块**：contract-builder 桥接层 + 8 状态路由引擎

### contract-builder 桥接层（核心创新）

将四份规划工件（proposal/specs/design/tasks）自动压缩成一份 `execution-contract.md`，作为规划到实现的**唯一交接层**。没有这份契约，或者契约没被批准，就不准进入实现。

**六类提取约束**（与 [[execution-contract]] 一致）：

| 约束 | 作用 |
| --- | --- |
| Intent Lock | 锁定变更意图，防止目标漂移 |
| Scope Fence | 圈定变更范围（In Scope / Out of Scope） |
| Non-Goals | 明确不做的事 |
| Test Obligations | 测试覆盖义务 |
| Review Gates | 审查节点 |
| Rewind Triggers | 回滚触发条件 |

### 9 个核心 Skill

| Skill | 对应阶段 | 职责 |
| --- | --- | --- |
| workflow-start | 入口 | 内容级状态检测、8 状态路由、阻止非法跳转 |
| need-explorer | exploring | 探索，一次一问 + 方案对比 + 推荐 |
| spec-writer | specifying | 产出四份规划工件，Schema 引擎实时验证 |
| contract-builder | bridging | 自动生成 execution-contract.md |
| build-executor | executing | TDD + SDD + Review Gate 三重纪律 |
| bug-investigator | debugging | 四阶段根因分析，三次失败质疑架构 |
| code-reviewer | executing | 结构化审查，Critical/Important/Minor 三级 |
| release-archivist | closing | 验证收口 + 归档 + 风险总结 |
| spec-merger | archiving | delta spec 智能合并回主规范，防规范腐烂 |

### 八状态机

`workflow-start → need-explorer → spec-writer → contract-builder → DP-3（人工审批）→ build-executor → bug-investigator → release-archivist → spec-merger`

详见 [[eight-state-machine]]。

**两条快速路径**：
- **hotfix**（≤2 文件，不引入新模块）：跳过完整规划工件，但仍必须生成最小 execution-contract.md 并完成 [[DP-3]]
- **tweak**（≤4 文件，纯配置或文档）：直接编辑

### 校验规则

- proposal.md 的 `## Why` 不能少于 50 个字符
- spec.md 每个 Requirement 必须含 SHALL 或 MUST，且至少一个 `#### Scenario:` 块
- 实现验证按 Completeness/Correctness/Coherence 三维度比对 diff 和 spec

### 安装

```bash
# Claude Code
/plugin marketplace add MageByte-Zero/spec-superflow
/plugin install spec-superflow@spec-superflow

# Cursor
npx spec-superflow@latest install-cursor

# 全局 CLI
npm install -g spec-superflow
ssf validate <dir>
```

### 可选配置

项目根目录放 `spec-superflow.config.json`，为不同执行角色配置模型（机械性修改用小模型、架构和审查用强模型）。

### 适用边界

- **适合**：大型功能开发、多人协作、长期维护、需 TDD + Review Gate 的棕地项目
- **不适合**：快速原型、一次性脚本、纯咨询问答
- **经验法则**：不需要写 proposal 和 design doc 就能想清楚的事，spec-superflow 太重

## 关联连接

- [[OpenSpec]] - 融合的规划层
- [[Superpowers]] - 融合的执行层
- [[execution-contract]] - 核心创新机制（桥接层）
- [[eight-state-machine]] - 八状态路由引擎
- [[DP-3]] - 人工审批检查点
- [[delta-spec]] - 增量变更机制（spec-merger 合并）
- [[review-gate]] - 审查门禁
- [[subagent-driven-development]] - 子代理开发
- [[规范驱动开发]] - 上层方法论
- [[MageByte-Zero]] - 开发者
- [[程序员追风]] - 文章作者
- [[ClaudeCode]] - 宿主工具
- [[摘要-spec-superflow-融合工作流]] - 来源
- [[摘要-spec-superflow-融合工作流-源码级详解]] - 来源（2026-07-13 深度解读）
