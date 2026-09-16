---
title: "AGENTS-md"
type: concept
tags: [AI编程, Agent, 记忆机制, 协议]
sources:
  - raw/01-articles/Pi 大道至简，超越Codex和Claude Code的极简Agent，保姆级全攻略， 一文精通.md
  - raw/01-articles/GitHub狂揽8.6万Star！为什么越来越多人用 Pi ？.md
  - raw/01-articles/Codex 最新焚决发布，快！.md
last_updated: 2026-09-15
---

## 定义
AGENTS.md 是 AI Agent 的跨 Session 记忆机制标准文件，存放项目级或全局级的指令、规范、上下文信息。Agent 在每次会话启动时自动读取该文件，实现跨会话的持久化记忆。[[Pi]]、[[ClaudeCode]] 等主流 Agent 均支持该机制，使 Claude Code 积累的项目知识可无缝迁移到 Pi。

## 关键信息

### 存放位置
- **项目级**：项目根目录 `AGENTS.md`（仅对该项目生效）
- **全局级**：`~/.pi/agent/AGENTS.md`（对所有项目生效，Pi 专用路径）
- 项目级优先级高于全局级

### 优先级机制
- `AGENTS.md`：基础项目上下文
- `APPEND_SYSTEM.md`：追加系统提示词，优先级更高，可覆盖 AGENTS.md
- Agent 启动时按优先级合并加载

### 自动生成
- 可让 Agent（如 [[Pi]]）自动通读项目代码生成 AGENTS.md
- 内容包括：项目结构、编码规范、常用命令、技术栈、注意事项

### 兼容性
- [[Pi]] 自动读取 `AGENTS.md`，[[ClaudeCode]] 积累无缝迁移
- [[ClaudeCode]] 原生支持 AGENTS.md
- 是 Agent 跨工具迁移项目知识的关键桥梁

### 与 .agents/skills 的关系
- `AGENTS.md`：项目级指令和规范（"做什么"）
- `.agents/skills/`：可复用行为模块（"怎么做"）
- 两者配合构成完整的项目级 Agent 配置

### GPT-6 Astra 时代的瘦身
来自 [[摘要-Codex最新焚诀-GPT-6-Astra瘦身指南]]。核心原则：**AGENTS.md 里那些「每次修改前必须先读 XX 文档」的规则，在新模型上就是浪费上下文。GPT-6 Astra 能自己判断什么时候该读什么文档，不需要每次都强制它通读一遍**。

**反面例子**：
> 每次编辑前，都读 architecture.md、database.md 和 deployment.md。

**改法**：给每份文档加读取条件：
> 涉及服务边界时读 architecture.md，修改表结构时读 database.md，准备部署时读 deployment.md。

前者不管改什么都要通读三份文档，后者只在确实需要的时候才加载对应的内容。

**OpenAI 建议给安全工作流显式授权**：减少不必要的确认等待，把可预期的操作直接授权给模型——比如本地测试使用一次性 fixture 数据、无生产环境访问权限，可以在 AGENTS.md 里写一句"直接跑测试、修复失败、重跑受影响的测试，不需要每一步都等确认"。

**放松决策边界**：老模型时代加的限制（"修改文件前必须先问我""禁止自动执行 shell 命令""任何涉及数据库的操作都要等确认"）在新模型上反而让 Astra 过度谨慎。**两类区分**：安全底线保留（不要自动 push 到远程仓库、不要删生产数据、涉及密钥必须确认），日常低风险操作确认交给模型自己判断。

### AGENTS.md 自检清单
- 有没有"每次都要 XX"这样的无条件规则？
- 这些规则各自适用于什么场景？能不能加上触发条件，或者移到具体的 Skill 里？
- 有没有安全的工作流可以显式授权，减少不必要的确认等待？
- 规则里引用的文档，和实际代码还对得上吗？

### 与"AGENTS.md 只该管边界"的呼应
参见 [[摘要-AGENTS.md只该管边界]]——AGENTS.md 应只管"边界"，保留协作习惯/目标驱动/真实性验证/安全边界四类内容。焚诀的瘦身方向与这个原则一致：把"每次都做什么"从 AGENTS.md 移到 Skill，只保留边界类内容。

## 关联连接
- [[Pi]] — 支持 AGENTS.md 的 Agent
- [[ClaudeCode]] — 原生支持 AGENTS.md
- [[AgentSkills]] — 配套的技能扩展机制
- [[摘要-pi-agent-保姆级全攻略]] — 来源
- [[摘要-GitHub狂揽8.6万Star-Pi]] — 来源
- [[摘要-Codex最新焚诀-GPT-6-Astra瘦身指南]] — 来源（Astra 时代瘦身指南）
- [[摘要-AGENTS.md只该管边界]] — 边界管理论
- [[摘要-codex-gpt6-astra额度优化]] — 上下文消耗与 AGENTS.md 精简
- [[GPT-6]] — Astra 模型
- [[Skill]] — 减法定稿
- [[CLAUDE-md]] — Claude Code 对应的全局规则文件
- [[上下文工程]] — 每轮真正送进模型的内容组成
- [[上下文压缩]] — 与 AGENTS.md 瘦身协同
