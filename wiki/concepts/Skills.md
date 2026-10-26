---
title: "Skills"
type: concept
tags: ["Skills", "AI-Agent", "GPT-6"]
sources:
  - raw/09-archive/2026-09-07-“GPT-6 Astra 正式登场”会怎样改变现有技术栈？.md
  - raw/09-archive/Codex 最新焚决发布，快！.md
  - raw/09-archive/2026-09-22-我把463个AI视频做成了Skill和提示语模版，全都开源！.md
last_updated: 2026-09-23
---

# Skills

Skills 是预定义指令集，告诉 AI Agent 遇到特定任务时怎么做、遵循什么规范、输出什么格式。三要素：名称（标识）、描述（触发条件）、文件路径（指令内容）。与 Prompt 的区别：Skills 具备沉淀、复用、进化三能力。一个 SKILL.md 可获 2.3 万 Star。

## GPT-6 Astra 时代的 Skills
- Astra 支持 Skills：需要时再加载能力说明，避免一次塞进上下文
- 与 [[ToolSearch]] 配合：Tool Search 按需加载工具定义，Skills 按需加载能力说明
- 推动 [[RAG]] 继续细分：模型接到任务后按需选择知识源/业务工具/处理方法，只把当前步骤需要的内容送入上下文
- 详见 [[摘要-GPT-6-Astra改变技术栈]]

## 焚诀：Astra 时代的 Skills 瘦身
来自 [[摘要-Codex最新焚诀-GPT-6-Astra瘦身指南]]。OpenAI 官方博客《Rethinking skills and prompts for GPT-6 Astra》（500 多万浏览）结论：**模型能力变强后，Skill 要少一些**。

**反面案例**：Postgres 迁移 Skill 描述写成"涉及数据库、查询或数据模型时使用"太宽——用户只想写一条 SQL 查询语句，模型也会触发这个 Skill，把一整套迁移流程的指令加载进来。改法收窄到"**新增或修改迁移、审查迁移发布时使用**"。

**Claude Code 项目里的同类问题**：`browser-act` Skill 描述写了整整 4 行，触发条件覆盖了从「fetch URL」到「take screenshots」到「fill forms and click through workflows」几乎所有浏览器操作。只要任务里沾一点网页相关的事情，模型就会把它加载进来。

**"过详细的 SOP 也是过度约束"**：很多 Skill 是老模型时期写的，操作步骤恨不得精确到每一步。新模型已经能处理模糊和复杂性了，过度详细的步骤清单反而会限制它的发挥。**OpenAI 提醒：你留下的指令不只是给自己的模型看的，其他 Agent 也可能用到——对一个模型合适的约束，可能对另一个模型就是过度约束**。

### Skill 描述自检清单
- 每个 Skill 的描述能不能在一两句话内说清"做什么"和"什么时候用"？
- 有没有 Skill 的触发条件太宽，导致不相关的任务也会加载它？
- 多个 Skill 的描述有没有重叠？模型能不能分清该选哪个？
- 详细的操作步骤是放在子文档里，还是全塞在描述里？

## 关联连接
[[AI-Agent]], [[Skill命中率]], [[SkillCreator]], [[SkillHub]], [[沉默王二]], [[GPT-6]], [[ToolSearch]], [[ResponsesApi]], [[摘要-GPT-6-Astra改变技术栈]], [[摘要-Codex最新焚诀-GPT-6-Astra瘦身指南]], [[AGENTS-md]], [[CLAUDE-md]], [[上下文工程]]
