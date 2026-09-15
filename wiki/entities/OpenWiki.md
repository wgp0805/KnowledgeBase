---
title: "OpenWiki"
type: entity
tags: [实体, 工具, Wiki, Agent, 知识库, 长期记忆, LangChain]
sources:
  - raw/09-archive/2026-08-02-AI 时代的“HTML 时刻”：一个被严重低估的知识标准 OKF - 贾克斯的平行世界.md
  - raw/01-articles/为什么越来越多人用OpenWiki？.md
last_updated: 2026-09-15
---

## 定义
LangChain 于 2026 年 7 月开源的命令行工具（Node.js 22+），扫描代码库后用 LLM 生成一套 Markdown Wiki。**OpenWiki 是 LLM Wiki 理念的第一个完整工程实现**——把代码库的结构、架构、依赖关系「编译」成一套 Agent 可以快速查阅的 Wiki，让 Agent 不用每次都从头翻代码，即「AI 编程 Agent 的长期记忆系统」。开源 5 天冲到 9K+ Star，后超 16,500 Star。MIT 协议。

官方定位：**"An agent reads your sources, synthesizes a linked Markdown wiki you own, and keeps it current on every change."**

## 关键信息

### 为什么出现：AI 编程的长期记忆缺口
很多团队用上 AI 编程工具后都遇到同一个瓶颈：**AI 的「短期记忆」够了，但「长期记忆」没有**。每次任务都是一次全新的开始，之前积累的理解完全浪费——你花时间让 AI 理解的项目架构，下个任务它完全不记得。

### 与传统 Wiki 的本质区别
传统 Wiki（Confluence、语雀）是写给人看的，读者是开发者，写作风格是散文式的。[[LLMWiki]] 的读者不是人，是 AI Agent。

**最反直觉、也最关键的设计决策：为 Agent 写文档，不是为人写文档。** 人类读文档能容忍模糊、能脑补上下文、能从散乱段落中提取信息；但 Agent 的上下文窗口有限，每一行无用信息都在消耗宝贵的 Token。所以输出不是供人类阅读的散文，而是**针对 LLM 上下文优化的结构化 Markdown**，每一页都经过精心组织让 Agent 快速定位到相关上下文。

### 三层核心架构
1. **代码仓库层**：只读不改，保留原始代码和 Git 历史
2. **Deep Agents 文档生成引擎**：基于 LangChain [[DeepAgents]] 构建的 Agent，负责扫描代码、分析架构、生成 Wiki，通过 Claims 机制保证每条事实有据可查
3. **结构化知识层**：`openwiki/` 目录下的 Markdown Wiki（架构页/模块页/集成页），每条事实放在 `openwiki/.claims/` 下溯源

### 四个设计要点
- **[[Claims溯源]] 机制**：每条事实性陈述关联一个 Claim，记录来自哪个文件的哪一行，LLM 总结错了可直接溯源验证
- **[[OKF]] 格式支持**：0.2 版全面支持 Google Open Knowledge Format，每个 Markdown 概念都带 YAML front matter，类型信息明确方便 Agent 解析
- **自动更新机制**：`openwiki --update` 刷新过时 Claims，保持 Wiki 与代码同步
- **多语言支持**：`--language <locale>` 生成其他语言文档，但代码和标识符保持原样

### 底层原理：Agent 驱动 + 确定性工程
不是「把代码丢给 LLM 让它自由发挥」，而是混合模式。`openwiki --init` 的五步流程：
1. **代码扫描**：扫描仓库结构，收集 Git 上下文（分支、提交历史、变更文件）
2. **架构分析**：Deep Agents 会话读取代码库，识别模块划分、依赖关系、调用链路、集成点
3. **Wiki 生成**：生成结构化 Markdown 页面（架构概览、模块说明、集成指南等）
4. **Claims 校验**：每条事实性陈述关联 Claim，记录来源文件和行号
5. **写入文件**：Wiki 写入 `openwiki/`，同时在仓库根的 `AGENTS.md` 和 `CLAUDE.md` 插入指针，让 AI 编程 Agent 知道「先读 Wiki 再干活」

**增量更新**：`openwiki --update` 不是从头重新生成，而是对比代码变更与 Wiki 中已有 Claims，只更新过时部分、重新校验受影响页面。核心价值：**Wiki 的维护成本随代码量线性增长，而不是指数增长**。

**CI 自动化**：提供 GitHub Actions、GitLab CI、Bitbucket Pipelines 示例工作流，每次代码提交自动 `--update` 并开 PR。**这意味着 Wiki 永远不会过时**——代码改了 Wiki 自动跟着改，不需要人工维护。

### 使用方式
```bash
npm install -g openwiki      # 需 Node.js 22+
openwiki --init              # 首次生成（引导选推理提供商/API Key/模型）
openwiki --update            # 增量更新 + 调和过时 Claims
openwiki visualize           # 本地交互式节点图（左树右阅读）
openwiki personal --init     # 个人知识库模式
```
Windows 用户建议用 npm 或 pnpm，bun 安装可能触发 better-sqlite3 原生编译（需 Visual Studio Build Tools）。个人知识库模式从本地 Git/Gmail/Notion/Web 搜索/Hacker News/X 摄取知识，存到 `~/.openwiki/wiki`。

生成后目录结构：
```
your-project/
├── openwiki/
│   ├── index.md          # 知识索引
│   ├── architecture.md   # 架构概览
│   ├── modules/          # 各模块说明
│   ├── integrations.md   # 集成点
│   ├── .claims/          # 事实溯源
│   └── INSTRUCTIONS.md   # Wiki 生成指令
├── AGENTS.md             # Agent 指令（自动更新指针）
└── CLAUDE.md             # Claude Code 指令（自动更新指针）
```

### 对比 RAG
| 对比维度 | 传统 RAG | OpenWiki（LLM Wiki） |
| --- | --- | --- |
| 知识组织 | 向量碎片 | 结构化 Markdown 页面 |
| 更新方式 | 每次查询重新检索 | 增量更新 Claims |
| 可审计性 | 弱（黑盒检索） | 强（Claims 溯源） |
| 知识积累 | 用完即弃 | 编译一次、持续复用 |
| Agent 友好度 | 需检索后拼接 | 直接读 Wiki |

**RAG 是「解释器模式」，每次执行都从头解析；OpenWiki 是「编译器模式」，编译一次、反复使用**（详见 [[编译器模式vs解释器模式]]）。

### 优点（十项）
1. 为 Agent 而生，不是为人而生——Token 消耗大幅降低
2. Claims 溯源，事实可验证
3. 自动更新，永不过时（三大 CI 平台）
4. 支持 12 种模型提供商（OpenAI/Anthropic/Bedrock/Gemini），可接任何 OpenAI 兼容网关，不锁定任何一家
5. 内置连接器丰富（Custom MCP、Notion、Slack、Gmail、X、Web Search、Hacker News、本地 Git）
6. [[OKF]] 格式，标准化输出
7. `openwiki visualize` 可视化节点图，人类也可浏览
8. 完全开源，MIT 协议
9. 与 AI 编程工具无缝集成（自动在 `AGENTS.md`/`CLAUDE.md` 插指针，Claude Code/Codex/OpenCode/Cursor 都能发现并查阅）
10. 个人知识库模式

### 缺点（五项）
1. 需要 Node.js 22+ 环境，老项目需额外安装
2. 编译过程消耗 Token，每次 `--init`/`--update` 都是完整 LLM 分析
3. 中文文档生成支持有限，中文质量可能不如英文
4. 生态仍在早期，社区插件和第三方集成还在发展中
5. 需要 Schema 设计能力——`openwiki/INSTRUCTIONS.md` 定义生成范围与质量标准，写得不好会导致 Wiki 组织混乱

### 适用场景
强烈推荐：大型代码库 AI 编程、多 Agent 协作项目（所有 Agent 共享同一套 Wiki 记忆）、团队知识沉淀、个人知识管理、CI/CD 自动化、快速上手陌生项目、对 Token 成本敏感的团队（编译一次反复使用长期省 Token）。需评估：一次性查询场景（RAG 更轻量）、Node 环境受限的项目。

### 与 OKF 生态的关系
OpenWiki 是快速采用 [[OKF]] 的上层应用：这些知识不必永远留在 OpenWiki 自己的系统中，可被其他兼容工具读取——体现「标准让生态围绕同一种知识产物独立生长」的价值。

## 关联连接
- [[摘要-openwiki-为什么越来越多人用]] — 来源（深度解析）
- [[摘要-okf]] — OKF 标准背景
- [[LangChain]] — 开源方
- [[DeepAgents]] — 底座引擎
- [[LLMWiki]] — OpenWiki 是 LLM Wiki 理念的第一个完整工程实现
- [[OKF]] — 采用的知识格式标准
- [[Claims溯源]] — 每条事实关联来源文件与行号
- [[编译器模式vs解释器模式]] — RAG vs OpenWiki 的本质差异
- [[长期记忆]] — Agent 的持久化上下文
- [[RAG]] — 被对比的解释器模式
- [[自生长知识库]] — 相近的知识组织模式
- [[WeKnora]] — 类似的 Wiki Mode 自动编译
- [[AGENTS-md]] — 自动插入指针的机制
- [[ClaudeCode]] / [[Codex]] / [[Cursor]] / [[OpenCode]] — 可发现并查阅 Wiki 的编程工具
