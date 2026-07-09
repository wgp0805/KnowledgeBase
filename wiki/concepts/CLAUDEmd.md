---
title: "CLAUDEmd"
type: concept
tags: [AI, 记忆, 指令系统]
sources: [raw/01-articles/全网最全！60分钟全面掌握Claude Code~【附完整文档】.md, raw/01-articles/6条Claude Code实践中的经验与思考.md, raw/01-articles/3 分钟掌握 Codex 97% 的功能，超实用教程！.md, raw/01-articles/面试官坏笑：“你用ClaudeCode写代码，不怕它把项目搞炸？”，我：“怕，所以CLAUDE.md、权限和验证，一个都不能少。”.md]
last_updated: 2026-07-09
---

## 定义
Claude Code 的核心指令与记忆系统，以 CLAUDE.md 文件为载体，三层叠加生效，确保 Agent 在每次对话时都能获取用户/项目的核心规则。

## 关键信息

### 三层体系
1. **全局级** (`~/.claude/CLAUDE.md`)：对所有项目生效，写个人习惯相关规则
2. **项目级** (项目根目录)：团队共享可提交 Git，写技术架构/文件结构/开发规范
3. **文件夹级** (子文件夹)：仅对该文件夹的修改生效

### 四层层级与加载顺序（程序汪实战视角）
- 组织级（/etc/claude-code/CLAUDE.md 或 C:\Program Files\ClaudeCode\CLAUDE.md）：IT/DevOps 统一下发
- 用户级（~/.claude/CLAUDE.md）：个人通用偏好
- 项目级（./CLAUDE.md 或 ./.claude/CLAUDE.md）：团队共享，提交 Git
- 本地级（./CLAUDE.local.md）：个人配置，加进 .gitignore
- 加载从全局到局部，后加载的更具体规则更易被采纳；子目录 CLAUDE.md 按需加载非开局全塞
- 官方建议控制在 200 行内，膨胀时拆到带 paths 的 .claude/rules/，低频参考放 Skills
- 删规则判断标准：删掉后 Claude 会不会更易犯错；/memory 验证当前加载了哪些规则文件

### 设计原则
- 第一优先级，每次对话自动注入上下文
- 不应塞太多内容，理想情况只写最顶层不变化的原则
- 项目级应是动态的：项目加功能、踩了坑就同步更新
- 用 `/init` 自动扫描项目生成项目级 CLAUDE.md

### Codex 的对应物
Codex 使用 `agents.md` 作为手动持久记忆文件，分全局级和项目级，机制类似。

### 实践经验
- CLAUDE.md 本质是"与 AI 签订的契约"
- 积累的错误经验越多，犯错越少
- 可在 CLAUDE.md 中引用自建参考文档实现渐进式披露

### Codex AGENTS.md 写作建议
- **控制长度**：200 行以内，只写最核心的约束（最高优先级限制、技术栈、编码规范、开发流程）
- **AGENTS.md 也占上下文**，写太多适得其反
- **动态优化**：第一版不可能完美，每次 AI 犯错后把新约束补进去
- 内容至少包括：最高优先级限制（如不要每次改代码就 build）、项目技术栈和目录结构、编码规范、开发流程

### AGENTS.md 四块关键内容（苏三视角）
来自 [[摘要-codex-97percent-技巧]]，新对话开始后 Codex 优先读此文件：
1. **构建和测试命令** — Agent 最常用的信息，写清多种测试方式（快速回归/全量/单个），Agent 按场景选择
2. **项目特有的编码规范** — 只写和行业默认不一样的部分（如请求对象用 Params 后缀、响应用 Response）
3. **红线规则** — 用明确的否定句式（"禁止""不要""Never"），如"禁止提交 .env 文件""不要往 codex-core 添加新功能"
4. **代码定位策略** — 告诉 Agent 用什么方式找代码最高效，明确优先级减少无效操作

## 关联连接
- [[ClaudeCode]] — CLAUDE.md 所属产品
- [[AutoMemory]] — 第二优先级记忆
- [[Codex]] — 对应 agents.md
- [[AICoding]] — AI 编程实践
- [[摘要-AI-agent工具应该怎么使用]] — 来源
- [[摘要-codex-97percent-技巧]] — 来源（AGENTS.md 四块关键内容）
- [[摘要-claude-code-实战防搞炸]] — 来源（程序汪实战视角）
- [[auto-mode]] — 配合的权限模式
