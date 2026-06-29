---
title: "ClaudeCode"
type: entity
tags: [AI工具, Agent, Anthropic]
sources: [raw/01-articles/全网最全！60分钟全面掌握Claude Code~【附完整文档】.md, raw/01-articles/6条Claude Code实践中的经验与思考.md, raw/01-articles/腾讯面试官："为什么 Claude Code 不用 RAG 检索代码，而是 grep？"我："因为...我也不知道"，他沉默了。.md, raw/01-articles/ClaudeCode写SpringBoot代码竟然这么野？这4个Skill让我彻底服了！.md, raw/01-articles/直接让你的 Claude Code 效率拉满，Anthropic 官方神级插件开源了！-2026-06-02 09_14_35.md]
last_updated: 2026-06-02
---

## 定义
Anthropic 在 2025 年 2 月推出的、原本为编程而生、运行在终端的 Agent 程序，现已能泛用到任何知识工作。

## 关键信息

### 核心特性
- **本地运行**：直接读写本地文件、使用终端、执行命令
- **Harness 工程**：业界领先的 Agent harness 设计，同样大模型效果差别极大

### 权限模式
1. **Plan Mode（计划模式）**：不直接动手，先给计划等确认
2. **默认模式**：智能判断哪些操作需要确认
3. **Accept Edits**：改文件不问，跑命令会问
4. **危险模式**：`--dangerously-skip` 参数，一路绿灯（Anthropic 发现 97% 用户直接同意）

### 上下文管理
- `/compact`：压缩上下文，保留关键信息释放空间
- `/clear`：彻底清空上下文
- `/context`：查看上下文占比和各组件 token 消耗
- 上下文 >60% 时建议手动 /compact

### 记忆体系
1. **CLAUDE.md**（第一优先级，全部注入上下文）：全局级/项目级/文件夹级三层叠加
2. **Auto Memory**（第二优先级，按需注入）：后台 agent 记录 user/feedback/project/reference 四类
3. **自建参考文档**（渐进式披露）：按需加载的领域文档

### 高级扩展
- **Skill**：技能包，四类（领域知识/工作流/工具组合/最佳实践）
  - Thariq 的 9 类分类法：知识、验证、数据访问、自动化、脚手架、代码审查、部署、调试、运维
- **MCP**：外部服务转接头
- **CLI 工具**：命令行工具扩展
- **SubAgent**：子 agent 并行处理
- **Hook**：条件反射式自动触发器
- **插件（Plugin）**：Skill + SubAgent + Hook + MCP 打包
  - **[[claude-plugins-official]]**：Anthropic 官方开源的插件应用商店（GitHub 近 3 万 Star），已内置在 Claude Code 中，通过 `/plugin install` 命令零配置安装
  - 三类插件：LSP 语言服务（TypeScript/Python/Java/Go/C++ 等）、开发工作流（feature-dev、code-review、commit-commands）、外部工具集成（GitHub、GitLab、Figma、Linear、Playwright、Vercel、Sentry 等）
  - 插件目录结构：`.claude-plugin/plugin.json`（必填）+ 可选 `mcp.json`、`commands/`、`agents/`、`skills/`
  - **[[claude-code-setup]]**：项目级一键自动化配置工具，背后通过 [[claude-automation-recommender]] Skill 扫描项目并产出 MCP/Skill/Hook/Subagent/Slash Command 五大能力的差异化推荐清单，全程只读不动文件

### 社区最佳实践与工作流范式
- **[[claude-code-best-practice]]**（GitHub 57k+ Star）系统整理 Claude Code 生态：核心能力、热门功能、工作流、Skill/Agent 精选集、83 条实战 Tips
- **[[Command-Agent-Skill编排]]**：Command 触发 → Agent 扮演角色 → Skill 提供专业能力，系统工程化的核心模式
- **[[Research-Plan-Execute-Review-Ship]]**：先研究→再计划→再执行→再审查→交付，主流工作流项目（Superpowers/Spec Kit/OpenSpec 等）共用范式
- **[[跨模型工作流]]**：通过 Plugin/MCP/Router 三种机制与 Codex、Gemini、DeepSeek 等其他模型协同
- 实战 Tips 经典两条：CLAUDE.md 单文件 ≤ 200 行；`.claude/rules/*.md` 在每个会话自动加载

### Dynamic Workflows（动态工作流）
Claude Code 提供基于 JavaScript 的可执行脚本编排能力，用于在会话内动态驱动多 Agent 协作：

- **设计范式**：代码即编排（Code-as-Orchestration），编排逻辑是图灵完备的 JavaScript 代码
- **运行环境**：Claude Code CLI 会话内，Node.js 沙箱（无文件系统/网络访问）
- **触发方式**：用户调用 `/workflow` 或使用 Workflow 工具
- **核心 API**：
  - `agent(prompt, {schema})` — 生成子 Agent 执行特定任务，支持 JSON Schema 输出校验
  - `pipeline(items, stage1, stage2, ...)` — 流式多阶段处理，无同步屏障
  - `parallel(thunks)` — 并行执行多个任务，有同步屏障
  - `phase('Verify')` — 进度分组显示
  - `budget.remaining()` — Token 预算感知
  - 支持 `isolation: 'worktree'` 隔离并行修改
- **适用场景**：快速审查 PR、多维度研究分析、一次性探索性分析
- **与 OpenClaw.NET MetaSKILL 对比**：Workflows 灵活度高适合探索，MetaSKILL 安全审计完善适合生产

### Spring 生态专属 Skill
- **核心理念**：Claude Code 的上限完全取决于装了什么 Skill
- **搭载专属 Spring Skill 后**：变身「资深Spring架构师」，懂 Spring Boot 4.x、Spring Framework 7.x 最新规范、企业级工程最佳实践、测试闭环、AI Agent 调度
- **四大 Spring Skill 项目**：
  - [[dr-jskill]]：企业级项目脚手架技能（JHipster作者新作）
  - [[agent-skill-java-spring-framework]]：强制使用 Spring 最新 API 规范
  - [[sivalabs-agent-skills]]：统一 AI 技能封装规范
  - [[spring-testing-skills]]：自动生成全套测试用例

### 交互方式
- @文件引用、图片拖拽、斜杠命令（/help /model /btw /simplify 等）
- `!` 前缀进入 bash 模式
- Ctrl+B 后台运行命令
- Mac: Option+Enter 换行，Windows: Ctrl+Enter 换行

### 代码搜索方式（Agentic Search）
- 使用 **Glob + Grep + Read** 三工具组合，而非 RAG
- 早期版本曾用 Voyage Embedding RAG，后全面替换为 Agentic Search
- 三个工具均 `isConcurrencySafe = true`，可并行执行
- Grep 底层为 ripgrep，中型仓库搜索约 200ms
- LLM 自身充当 Reranker，多轮迭代式搜索

### 实践经验（二师兄总结）
1. 能用插件/Skill 尽量用，工业标准化规避幻觉
2. 工程师需具备 Leader 能力（拆分任务→描述→管理→验收）
3. 任务拆分越细越好，减少幻觉空间
4. 培养完全 AI Coding 感觉
5. 编程经验依旧重要，需判断 AI 方案利弊
6. 培养产品感觉，行业 Know-How 被放大

## 关联连接
- [[摘要-60分钟全面掌握Claude-Code]] — 来源
- [[摘要-6条Claude-Code实践经验与思考]] — 来源
- [[Codex]] — 对标产品
- [[Anthropic]] — 所属公司
- [[Agent]] — 核心概念
- [[CLAUDEmd]] — 指令系统
- [[AutoMemory]] — 自动记忆
- [[Skill]] — 技能扩展
- [[SkillCreator]] — 元技能创建工具
- [[meta-skill]] — 元技能概念
- [[摘要-为什么Claude-Code不用RAG检索代码]] — 来源
- [[摘要-claude-code-springboot-skills]] — 来源（Spring Skill 实战）
- [[摘要-claude-code-plugins-official]] — 来源（官方插件市场开源）
- [[摘要-claude-code-setup-plugin]] — 来源（一键配置插件）
- [[摘要-claude-code-best-practice]] — 来源（57k+ Star 最佳实践仓库）
- [[claude-code-setup]] — 官方一键配置插件
- [[claude-automation-recommender]] — 配置推荐 Skill
- [[claude-plugins-official]] — 官方插件市场
- [[claude-code-best-practice]] — 社区最佳实践仓库
- [[Command-Agent-Skill编排]] — 工作流核心架构
- [[Research-Plan-Execute-Review-Ship]] — 五阶段开发范式
- [[dynamic-workflow]] — 动态工作流概念
- [[跨模型工作流]] — 多模型协同范式
- [[AgenticSearch]] — 代码搜索范式
- [[Ripgrep]] — Grep 底层工具
- [[BorisCherny]] — 首席工程师
- [[Thariq]] — 工程师，分享 Skills 使用经验
- [[Cursor]] — 对比产品（混合检索）
- [[MCP]] — 外部服务协议
- [[AICoding]] — AI 编程范式
- [[Greptile]] — 开发者工具公司
- [[spring-skill-usage-guide]] — Spring Skill 使用时机与组合策略
- [[摘要-Claude-Code-Workflows-vs-MetaSKILL]] — 来源
