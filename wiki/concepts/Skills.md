---
title: "Skills"
type: concept
tags: ["Skills", "AI-Agent", "GPT-6"]
sources:
  - raw/01-articles/2026-09-07-"GPT-6 Astra 正式登场"会怎样改变现有技术栈？.md
last_updated: 2026-09-08
---

# Skills

Skills 是预定义指令集，告诉 AI Agent 遇到特定任务时怎么做、遵循什么规范、输出什么格式。三要素：名称（标识）、描述（触发条件）、文件路径（指令内容）。与 Prompt 的区别：Skills 具备沉淀、复用、进化三能力。一个 SKILL.md 可获 2.3 万 Star。

## GPT-6 Astra 时代的 Skills
- Astra 支持 Skills：需要时再加载能力说明，避免一次塞进上下文
- 与 [[ToolSearch]] 配合：Tool Search 按需加载工具定义，Skills 按需加载能力说明
- 推动 [[RAG]] 继续细分：模型接到任务后按需选择知识源/业务工具/处理方法，只把当前步骤需要的内容送入上下文
- 详见 [[摘要-GPT-6-Astra改变技术栈]]

## 关联连接
[[AI-Agent]], [[Skill命中率]], [[SkillCreator]], [[SkillHub]], [[沉默王二]], [[GPT-6]], [[ToolSearch]], [[ResponsesApi]], [[摘要-GPT-6-Astra改变技术栈]]
