---
title: "Skill"
type: concept
tags: [AI, Agent, 技能扩展]
sources: [raw/01-articles/40分钟学会Codex！"零基础"终级教程～【附完整文档】.md, raw/01-articles/全网最全！60分钟全面掌握Claude Code~【附完整文档】.md, raw/01-articles/6条Claude Code实践中的经验与思考.md, raw/01-articles/Java开发栈Skills全面指南.md, raw/01-articles/JAVA中AI框架选型指南（2026）.md, raw/01-articles/2026-06-29-AI native Casebook 面向 AI Agent 时代的测试用例工程化工作流 - 虫师.md, raw/01-articles/Claude Code 最佳学习路线：从“手敲代码”到“指挥AI打工”，强的离谱！！.md]
last_updated: 2026-07-27
---

## 定义
Agent 的技能包，是人为沉淀的可复用方法、流程和工具组合，相当于 Agent 做某类具体任务的行动指南/操作手册。

## 关键信息

### 四类 Skill
1. **领域知识型**：专业领域的最佳实践和知识
2. **工作流型**：标准化的操作流程
3. **工具组合型**：多工具协同使用的模式
4. **最佳实践型**：编码规范、设计模式等

### Thariq 的 9 类分类法（Anthropic 内部经验）
1. **知识/参考类**：告诉 Claude 如何正确使用内部库、CLI 或 SDK
2. **验证类**：描述如何测试或验证代码是否正确
3. **数据访问类**：连接数据和监控系统
4. **自动化工作流类**：把重复操作压缩成一条命令
5. **脚手架类**：为代码库的特定模块生成框架样板
6. **代码审查类**：执行代码质量检查
7. **部署类**：拉取、推送、部署代码
8. **调试类**：接收症状，走多工具调查流程，输出结构化排查报告
9. **运维类**：执行例行维护和操作流程

### 设计理念
- 渐进式披露：只发元信息（名称+何时调用），Agent 按需读取完整内容
- 不占满上下文，比写进 CLAUDE.md/agents.md 更灵活
- 安装方式：放入对应 skills 文件夹

### 为什么重要
- 大模型不可能把所有领域最佳实践塞进训练数据
- Skill 把专业知识变成 Agent 按需调用的"外接大脑"
- 工业标准化规避模型幻觉，优秀 Skill 集成大量开发者经验
- 能用 Skill 尽量用，比自己用模糊语言描述效果好得多

### Matt Pocock 的两层调用架构（User-invoked vs Model-invoked）
[[MattPocock]] 的 `mattpocock/skills` 仓库提出了一种重要的 Skill 设计层次划分：

- **User-invoked（编排层）**：只能由用户亲手打出 /xxx 触发，职责是"编排 orchestrate"。包括 ask-matt、grill-with-docs、triage、implement、wayfinder 等
- **Model-invoked（纪律层）**：模型可自动调用，承载"可复用的纪律 discipline"。包括 prototype、diagnosing-bugs、tdd、domain-modeling、code-review 等
- **铁律**：User-invoked skill 可向下调用 Model-invoked skill，但 **User-invoked 之间互不调用**。这条单向边确保整条链永远从用户手里发起，不会让 agent 在编排层之间乱窜

这一架构的核心哲学是"**把 skill 当纪律，不当框架**"——skill 不该被供着，而是随时可替换、可组合、可 hack 的一次性纪律，与 GSD、BMAD、Spec-Kit 等"接管流程"的重量级框架形成根本分野。

### 创建方式

### Skill 生态与资源

#### 基础设施/中间件 Skills
- **Redis 官方 Agent Skill**：Redis 官方团队编写，确保 Agent 用"正确的方式"写 Redis 代码，涵盖数据结构选型、集群模式、连接池配置等
- **Antigravity Awesome Skills**（GitHub 38.9k Stars, 1,480+ Skills）：包含 database-designer、migration-architect、postgres-best-practices、mysql-best-practices、kafka-expert、message-queue-patterns、redis 等，安装方式 `npx antigravity-awesome-skills --claude`

#### 前端开发 Skills
- **[[PatternsDev]]**：58 个前端设计模式 Skills（React 18 个、Vue 3 个、JavaScript 29 个），安装方式 `npx skills add PatternsDev/skills --skill <skill-name>`
- **[[VercelLabs]]**：高安装量前端 Skills，react-best-practices（148,900+ 安装）、web-design-guidelines（112,700+ 安装）、composition-patterns（48,400+ 安装）等
- **TailwindCSS/shadcn-ui** 相关：Anthropic 官方 `frontend-design` Skill 包含 Tailwind 设计系统指示，Google Labs 发布 `shadcn-ui` Skill

#### 全栈综合 Skills 仓库
- **Jeffallan/claude-skills**：66 个全栈 Skills，涵盖 React、Vue、TypeScript、Node.js、Python、数据库、DevOps、AI/ML
- **alirezarezvani/claude-skills**：129 个 Skills（51 Core + 78 POWERFUL），支持 Cursor、Aider、Kilo Code、OpenCode 等平台

#### 自定义 Skill 开发
可以为项目编写专属 Skill，示例：
- **MyBatis-Plus Skill**：封装 Mapper 继承、Service 层、@TableName/@TableLogic、LambdaQueryWrapper、分页配置等规范
- **Redis 项目 Skill**：封装 Key 命名规范（{module}:{business}:{id}）、Spring Data Redis + Lettuce、Redisson 分布式锁、缓存穿透/雪崩防护等

### Java AI 框架中的 Skill 实现
多个 Java AI 框架原生支持 Skill 机制，均遵循 Agent Skills 规范：
- **LangChain4j**：FileSystemSkillLoader 加载 Skill 目录，Tool Mode / Shell Mode 双模式
- **Spring AI Alibaba**：SkillRegistry + SkillsAgentHook，渐进式披露
- **AgentScope-Java**：SkillRepository 多后端（Git/Nacos/MySQL/文件），自学习闭环
- **Solon AI**：最完善，20个预置技能 + CliSkill（兼容Claude Skills生态）/RestApiSkill/ToolGatewaySkill/Text2SqlSkill

Tool 与 Skill 的区别：Tool 是功能型（执行原子操作），Skill 是知识型（包含指令/SOP/上下文）。Skill 可以包含多个 Tool 调用和决策逻辑。

## 关联连接
- [[Agent]] — Skill 所属概念
- [[ClaudeCode]] — Skill 发明者
- [[Codex]] — Skill 支持
- [[SkillCreator]] — 元技能创建工具
- [[meta-skill]] — 元技能概念
- [[Thariq]] — 9 类分类法提出者
- [[AICoding]] — AI 编程实践
- [[摘要-anthropic-engineer-skills]] — 9 类分类法来源
- [[spring-skill-usage-guide]] — Spring Skill 使用时机与组合策略
- [[摘要-java-stack-skills-guide]] — 来源
- [[PatternsDev]] — 前端 Skills 合集
- [[VercelLabs]] — 前端 Skills 发布者
- [[multi-agent-collaboration]] — 多 Agent 协作模式
- [[Skill_Registry]] — 技能注册中心
- [[SolonAI]] — Skill 系统最完善的框架
- [[摘要-java-ai框架选型指南-2026]] — 来源
- [[Casebook]] — 将测试设计方法沉淀为 Agent 技能包的案例
- [[摘要-casebook-ai-native-testcase-workflow]] — 来源（Casebook 中的 .agents/skills 用法）
- [[摘要-claude-code-learning-roadmap]] — 来源（Claude Code 白银级定制能力）
- [[MattPocock]] — User-invoked vs Model-invoked 两层架构提出者
- [[摘要-mattpocock-skills]] — 来源（Skill 作为纪律而非框架的设计哲学）
