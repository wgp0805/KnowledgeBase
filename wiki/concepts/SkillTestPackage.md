---
title: "SkillTestPackage"
type: concept
tags: [Skill管理, AgentBro, 测试包, 观察期, 试用区]
sources: [raw/01-articles/别再乱装skill了，这个开源项目教你如何有效管理Skill.md]
last_updated: 2026-07-29
---

## 定义

测试包是新 Skill 的"观察期"容器。零散看到的 Skill 先放入 `NiceTry-测试`，确认好用再晋升稳定的 `NiceTry`；创作者批量 Skill 直接组成来源包。测试包非垃圾桶，而是给新 Skill 明确观察期，也让用户知道哪些还没资格进生产。

## 核心原则

1. **明确观察期**：新 Skill 进入测试包，设定验证周期
2. **晋升机制**：验证通过 → 移入稳定包；验证失败 → 清理
3. **来源隔离**：创作者批量 Skill 直接组成来源包，不混入零散试用区
4. **生产隔离**：测试包不开启于生产 Agent，调试时打开，正式任务关闭

## 关键信息

**工作流：**
1. 看到好用社区 Skill → 放入 `NiceTry-测试`
2. 确认真好用 → 移入稳定 `NiceTry`
3. Anthropic 等创作者一组 Skill → 市场安装时直接组成 `anthropics/skills` 来源包

**Case 6 实战：** 作者调试视频/口播剪辑相关 Skill 时，把不稳定 Skill 全移进 `SZ-内容创作-测试中`。调试时开包，写文章/剪片/发布时关包，只留稳定的 `SZ-内容创作`。

**习惯养成：** 正在开发的 Skill，不要和生产 Skill 常年混在一起。

## 关联连接

- [[SkillPackage]] — 技能包开关机制
- [[SkillCentralLibrary]] — 库存层
- [[AgentBro]] — 核心工具
- [[ShirenChuang]] — 作者