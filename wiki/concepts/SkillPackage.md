---
title: "SkillPackage"
type: concept
tags: [Skill管理, AgentBro, 技能包, 开关机制, 生产环境隔离]
sources: [raw/01-articles/别再乱装skill了，这个开源项目教你如何有效管理Skill.md]
last_updated: 2026-07-29
---

## 定义

技能包是 AgentBro 引入的"开关"机制。中心库当库存，技能包当开关。长期不用的 Skill 不分发；偶尔用的留在对应技能包；生产环境只开启稳定、必要的最小集合。一个 Skill 可同时属于多个技能包，无需复制。

## 核心原则

1. **库存与生效分离**：收藏了多少 Skill ≠ 当前该生效多少 Skill
2. **按需开关**：技能包是开关，非文件夹；多包同时开启取并集，共同 Skill 只生效一次
3. **多维组织**：技能包可按来源、工作场景、稳定性分别组织
4. **Agent 级独立**：同一中心库可给不同 Agent 应用不同技能包组合

## 关键信息

**典型技能包分类：**
- `NiceTry` / `NiceTry-测试` — 社区发现的 Skill 试用区与稳定区
- `SZ-内容创作` / `SZ-内容创作-测试中` — 个人工作场景包，按稳定性分层
- `anthropics/skills` — 创作者来源包（Anthropic 官方 Skill 组）
- 公司内部包 — 仅公司 Agent 开启，个人 Codex 不可见

**并集生效示例：**
```
内容创作-测试中 = {视频剪辑, 口播字幕, 视频发布}
创作者来源包     = {视频发布, 浏览器操作}
最终生效         = {视频剪辑, 口播字幕, 视频发布, 浏览器操作}
```
共同的 `视频发布` 只生效一次。关测试包后它仍因创作者包生效；两包全关才真正失效。

**Agent 级差异化：**
- Codex 开启：内容创作 + NiceTry
- Claude Code：另一套组合
- 公司 Agent：仅公司内部包

## 关联连接

- [[AgentBro]] — 核心工具
- [[SkillCentralLibrary]] — 库存层
- [[SkillTestPackage]] — 测试包观察期
- [[SkillConflictResolution]] — 冲突处理
- [[ShirenChuang]] — 作者