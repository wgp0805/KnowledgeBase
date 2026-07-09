---
title: "seven-state-machine"
type: concept
tags: [AI编程, 工作流, 状态机, 规范驱动]
sources:
  - raw/01-articles/有人把 5.7 万星 OpenSpec 和 24 万星 Superpowers 融合成一个工作流在 Github 开源.md
last_updated: 2026-07-09
---

## 定义

七状态机是 [[SpecSuperflow]] 的完整工作流描述，用七个状态串起从探索到归档的全流程：`exploring -> specifying -> bridging -> approved -> executing -> debugging -> closing`。由 workflow-orchestrator 驱动，说"开始"或"继续"即检测当前状态、决定下一步调用哪个 skill。

## 关键信息

### 状态与 Skill 对应

| 状态 | 对应 Skill | 职责 |
| --- | --- | --- |
| exploring | spec-explorer | 梳理需求（brainstorming 融入） |
| specifying | spec-forger | 生成规划工件（writing-plans 融入） |
| bridging | bridge-contract | 生成 [[execution-contract|执行契约]] |
| approved | （人工审批暂停点） | 用户确认契约值得执行 |
| executing | execution-governor | 管控实施 |
| debugging | systematic-debugger | 处理异常 |
| closing | closure-archivist | 收尾归档 |

### 内容级状态检测

关键设计：workflow-orchestrator 不只检查某个文件存不存在，而是读文件内容、分析里面写了什么。例如不问"design.md 存在吗"，而问"design.md 是否覆盖了 specs 里提到的所有关键技术决策"。

设计原因：早期版本用文件存在性检查，AI 生成空的 design.md 占位，状态机误以为规划完成就往下走。改用内容级检测后堵住此类问题。

## 关联连接

- [[SpecSuperflow]] - 所属框架
- [[execution-contract]] - bridging 状态产物
- [[review-gate]] - approved 状态的门禁
- [[OpenSpec]] - exploring/specifying 阶段能力来源
- [[Superpowers]] - executing/debugging 阶段能力来源
- [[摘要-spec-superflow-融合工作流]] - 来源
