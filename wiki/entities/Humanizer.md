---
title: "Humanizer"
type: entity
tags: [实体, Skill, 去AI味, 文本处理]
sources: [raw/09-archive/2026-11-24 - 像高手一样做自己的 Skill！【小白教程】.md]
last_updated: 2026-11-25
---

## 定义
Humanizer 是国外开发者 blader 制作的"去 AI 味" Skill（GitHub 约 7 万 Star，截至 2026-11 仍在更新），归纳了 6 种常见 AI 腔，是制作个人专属文风 Skill 时常用的成熟底子。

## 关键信息
- **定位**：去除 AI 写作痕迹的 Skill，秋芝2046 称其为"去 AI 味最火的现成 Skill"
- **方法**：归纳 6 种常见 AI 腔（具体条目见其 SKILL.md），作为改稿的规则底子；直接拿它改稿能去掉一些 AI 味，但"读起来还是不像我写的"——这正是需要叠加个人标准的起点
- **使用注意**：下载的现成 Skill 要留意更新时间——老模型写的写死规矩反而会束缚新模型；换新模型后应先关掉 Skill 裸跑一次，若不如不用则删掉
- **作为底子定制个人 Skill**：秋芝2046 的案例是先让 Agent 把英文 SKILL.md 翻译成中文 → 用原版改稿 → 从自己 10 篇语料提炼个人风格清单 → 用 [[SkillCreator]] 在 Humanizer 基础上生成新 Skill，**保留原作者署名和 MIT 协议** → 砍掉与自身目标无关的规则（如英文习惯）→ 拆分文件（SKILL.md 只留主流程，清单/样文放 reference/，检测脚本放 scripts/）
- **盲评对比**：同一提示词同一件活儿让三个子 Agent 分别"不用 Skill / 用原版 Humanizer / 用改好的文风 Skill"，三份打乱标 A/B/C 盲评，借此看清哪些指令真正影响结果
- **中文版**：[[HumanizerZh]] 是 op7418 做的中文版（op7418/Humanizer-zh），处理空泛拔高、三段式、宣传腔等中文 AI 写作特征；两者是原版与中文版关系，不是竞争替代

## 关联连接
- [[摘要-做自己的skill小白教程]] — 来源
- [[个人Skill定制七步法]] — 作为"找底子"步骤的成熟样本
- [[HumanizerZh]] — 中文版
- [[去AI味]] — 上位概念
- [[SkillCreator]] — 在其基础上生成个人 Skill
- [[秋芝2046]] — 定制案例作者
