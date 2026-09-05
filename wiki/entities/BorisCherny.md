---
title: "BorisCherny"
type: entity
tags: [人物, Anthropic, Claude-Code]
sources: [raw/01-articles/腾讯面试官："为什么 Claude Code 不用 RAG 检索代码，而是 grep？"我："因为...我也不知道"，他沉默了。.md, raw/01-articles/连 Karpathy 都开始恐慌：AI 正在重新定义「程序员」｜ 硅基时间.md, raw/01-articles/2026-08-23-对话 Claude Code 之父：当模型越来越聪明，还在设计复杂工作流的人只是在假装做产品.md]
last_updated: 2026-08-24
---

## 定义
Anthropic 资深工程师（首席工程师），Claude Code 的创造者和负责人。2024 年加入 Anthropic，此前在 Meta 工作近七年，任首席工程师，负责 Instagram 的服务端架构、开发基础设施和代码质量。也是技术书籍《Programming TypeScript》的作者。2025 年 5 月 7 日在 Latent Space 播客上公开阐述 Claude Code 为何放弃 RAG 改用 Agentic Search。

## 关键信息

### 关于 Agentic Search vs RAG 的核心观点
- Claude Code 早期版本确实用过 RAG（使用 Voyage Embedding 模型做本地向量索引）
- 试用 Glob + Grep + Read 后发现全面超越 RAG，原话 "outperformed everything, by a lot"
- 放弃 RAG 的两大原因：
  1. **性能**：Agentic Search 搜索质量更高，grep 返回精确代码行可直接使用，RAG 返回"相关"片段需二次筛选
  2. **简洁**：RAG 需维护索引同步、增量更新、向量数据库生命周期；Agentic Search 无需预处理

### AI 编程实践
- 上个月作为一个工程师，第一次完全没打开 IDE
- 全靠 Opus 4.5 写了大约 200 个 PR，每一行代码都是 AI 生成的
- 观察：新来的应届毕业生，因为没有"模型能做什么、不能做什么"的先入之见，反而最会用模型

### 信息来源
- 2025 年 5 月 7 日 Latent Space 播客，同场嘉宾 Catherine Wu
- Andrej Karpathy X 帖子评论区
- 2026 年 8 月 YC Startup School 对谈（视频：https://www.youtube.com/watch?v=qyPCVqFUyDo）

### YC 对谈核心观点（2026-08）
- **Opus 5 可连续运行数周**：配合 Auto Mode，无需复杂脚手架即可围绕目标持续推进
- **Prompt Injection 已可控**：模型对齐 + 注入检测器（机制可解释性观察神经元激活）+ Auto Mode classifier 三层防护
- **删除 80% System Prompt**：Opus 5 足够聪明，消融实验显示去掉 prompt 后模型反而更聪明
- **Product Overhang**：模型已具备大量未被产品释放的能力，真正的机会是拿掉妨碍模型发挥的设计（Unhobbling）
- **Dynamic Workflows**：可编排数千个 Agent，本质是 test time compute 的新形式
- **Routines 自动维护**：Anthropic 内部每天 20-30 个 routines 自动清理死代码、补充测试、统一抽象
- **编程接近被解决**：真正拉开差距的是提出问题、设计产品、理解用户的能力
- **Bun 代码库重写案例**：1 个 prompt、11 天，将整个代码库从 Zig 重写为 Rust

## 关联连接
- [[摘要-为什么Claude-Code不用RAG检索代码]] — Agentic Search 来源
- [[摘要-vibe-engineering-era]] — AI 编程实践来源
- [[ClaudeCode]] — 主导产品
- [[Anthropic]] — 所属公司
- [[AgenticSearch]] — 力推的搜索范式
- [[RAG]] — 放弃的检索方案
- [[AndrejKarpathy]] — 在其帖子评论区分享实践
- [[VibeCoding]] — Boris 的实践接近 Vibe Coding 的极端
- [[ProductOverhang]] — 提出的核心概念
- [[Unhobbling]] — 对应的实践方法
- [[AblationStudy]] — 每次新模型发布的标准做法
- [[PromptInjection]] — Opus 5 已实现三层防护
- [[dynamic-workflow]] — 编排数千 Agent 的机制
- [[auto-mode]] — Opus 5 连续运行的基础
- [[摘要-对话claude-code之父boris-cherny]] — YC 对谈来源
