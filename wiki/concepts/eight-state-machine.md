---
title: "eight-state-machine"
type: concept
tags: [AI编程, 工作流, 状态机, 规范驱动]
sources:
  - raw/09-archive/有人把 5.7 万星 OpenSpec 和 24 万星 Superpowers 融合成一个工作流在 Github 开源.md
  - raw/09-archive/253k Superpowers 和 60k OpenSpec 被融合了！spec-superflow 工作流登上热榜.md
last_updated: 2026-07-14
---

## 定义

八状态机是 [[SpecSuperflow]] 的完整工作流描述，由 workflow-start 入口技能驱动，将规划与执行统一成一条显式状态机，并阻止一切非法跳转。全流程八个状态串起从探索到归档的完整链路。

## 关键信息

### 八状态流转

`workflow-start → need-explorer → spec-writer → contract-builder → DP-3（人工审批）→ build-executor → bug-investigator → release-archivist → spec-merger`

| 状态 | 对应 Skill | 职责 |
| --- | --- | --- |
| exploring | need-explorer | 探索需求，一次一问加方案对比加推荐，把方向失控掐死在萌芽 |
| specifying | spec-writer | 产出 proposal、specs、design、tasks 四份工件，Schema 引擎实时验证 |
| bridging | contract-builder | 自动提取四份工件，压缩成 execution-contract.md |
| approved（DP-3） | （人工审批暂停点） | 唯一一次人工介入：契约批准后才允许写业务代码 |
| executing | build-executor | TDD 铁律 + SDD 子代理驱动 + Review Gate 三重纪律 |
| debugging | bug-investigator | 四阶段根因分析，三次修复失败必须质疑架构 |
| closing | release-archivist | 验证收口 + 归档 + 风险总结 |
| archiving | spec-merger | 把 delta spec 智能合并回主规范，防止规范腐烂 |

### 内容级状态检测

关键设计：workflow-start 检测的是工件内容，不是文件时间戳。关掉会话再打开，它能准确判断自己停在哪一步。早期版本用文件存在性检查，AI 生成空占位文件可骗过状态机；内容级检测堵住此类问题。

### 两条快速路径

- **hotfix**：改动不超过两个文件、不引入新模块时，可跳过完整规划工件，但仍必须生成最小 execution-contract.md 并完成 DP-3
- **tweak**：不超过四个文件、纯配置或文档修改时，直接编辑，无需规划工件

### 版本演化

早期版本（2026-07-09）描述为七状态机（`exploring → specifying → bridging → approved → executing → debugging → closing`）。后续版本（2026-07-13）扩展为八状态机，新增 archiving 阶段（spec-merger 规范合并防腐烂），并将 skill 命名对齐为 need-explorer/spec-writer/build-executor/bug-investigator/release-archivist/spec-merger 等更语义化的名称。

## 关联连接

- [[SpecSuperflow]] - 所属框架
- [[execution-contract]] - bridging 状态产物
- [[DP-3]] - 人工审批检查点
- [[review-gate]] - executing 阶段的质量门禁
- [[OpenSpec]] - exploring/specifying 阶段能力来源
- [[Superpowers]] - executing/debugging 阶段能力来源
- [[spec-merger]] - archiving 阶段 skill，delta spec 合并
- [[摘要-spec-superflow-融合工作流-源码级详解]] - 来源
- [[摘要-spec-superflow-融合工作流]] - 来源
