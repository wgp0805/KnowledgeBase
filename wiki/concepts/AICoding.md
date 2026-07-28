---
title: "AICoding"
type: concept
tags: [AI, 编程, 范式转变]
sources: [raw/01-articles/6条Claude Code实践中的经验与思考.md, raw/01-articles/再见吧 Codex 你到底还是输了！.md, raw/01-articles/同事："Claude Code都能自动写代码了，还要什么Spec Coding？" 我反问："屎山代码你来维护？".md, raw/01-articles/DeepSeek、Gemini、Qwen、Step 3.7 Flash实测，谁才是国产黑马？.md, raw/01-articles/Claude Code 最佳学习路线：从“手敲代码”到“指挥AI打工”，强的离谱！！.md]
last_updated: 2026-07-27
---

## 定义
AI 辅助编程范式，工程师角色从代码执行者转变为任务管理者，通过自然语言描述和任务拆分来指挥 AI 完成编程工作。

## 关键信息

### 范式转变
- **旧范式**：理解需求→想清楚实现→一行行写代码
- **新范式**：理解需求→拆分任务→定义目标→自然语言描述→与 AI 沟通管理→验收结果

### 六条核心经验（二师兄总结）
1. **能用插件尽量用**：工业标准化规避幻觉
2. **工程师需具备 Leader 能力**：任务管理+沟通+拍板+验收
3. **任务拆分越细越好**：减少幻觉空间和错误传递
4. **培养完全 AI Coding 感觉**：即使小修改也让 AI 做
5. **编程经验依旧重要**：需能判断 AI 方案利弊
6. **培养产品感觉**：行业 Know-How 和 Idea 判断力被放大

### 口号变迁
- 旧：`Talk is cheap. Show me the code.`
- 新：`Code is cheap. Show me the talk(prompt).`

### 高效工作流：别把 AI 当许愿池
[[摘要-再见吧-codex]] 提出了一套适用于所有 AI Coding 工具的 7 步工作流：
1. **阅读理解** — 先让 AI 阅读项目结构、架构、启动/测试/部署方式
2. **写计划** — 复杂任务先输出实现计划（理解什么、影响哪些模块、分几步、怎么验证、风险点）
3. **确认范围** — 确认影响文件和范围后再开始实现
4. **小步实现** — 只改当前步骤需要的文件，不顺手改无关代码
5. **验证** — 执行测试，认真看 diff，不只跑 happy path
6. **总结** — 回答 5 个问题：改了哪些文件？为什么改？做了什么验证？哪些没覆盖？需要人工确认什么？
7. **新会话** — 将总结带入新对话避免旧假设污染

#### 进阶实践：Plan 模式与 Prompt 结构
- **Plan 模式前置**：先让 AI 输出执行计划（改哪些文件、用什么方案、分几步完成），审完计划确认无误后再执行，避免推翻重来
- **Prompt 四要素结构**：背景（当前模块状态）+ 目标（用技术语言描述）+ 约束（不能动什么、兼容什么）+ 验收标准（什么算完成）
- **精确描述**：贴代码（接口定义、表结构、官方文档）比自然语言描述准确得多

### 多模型协作
- 至少保持两个 session：一个审核 role 一个执行 role，上下文占用低于 30%
- 利用不同模型能力差异做交叉验证，如 Codex 写代码 + Claude Code 审查
- 当 AI 开始"打补丁式"修 bug，让另一个模型重新审视架构，给出重构方案

### 人机分工原则
- **人负责**：目录结构、模块边界、数据流向、接口设计、架构决策
- **AI 负责**：在定好的框架内填充具体实现
- 警惕 AI 过度封装倾向（如把两个业务共同点封装成统一调度器）

### 模型选择：执行稳定性也是成本
[[摘要-step-3-7-flash-agent横评]] 提醒，Coding Agent 场景不能只看单次 Token 单价或 benchmark，而要把工具调用失败、代码错误返工、页面/报告二次整理和人工介入一起纳入总成本。文章将总成本拆成：`Token 成本 + 失败重试成本 + 人工介入成本`。因此，像 [[Step3Flash]] 这类单次价格不是最低、但工具调用稳定性较好的模型，在高频多轮任务中可能拥有更低的综合成本。

### AI 编码四大失败模式（Matt Pocock 分类）
[[MattPocock]] 在 `mattpocock/skills` 仓库中总结了 AI 编码中常见的四大失败模式，每一类都有对症的修复 skill：

| 失败模式 | 表现 | 修复 Skill | 引用的工程经典 |
|---------|------|-----------|--------------|
| **对不齐** | Agent 没做你想要的，你以为说清楚了，AI 理解的是另一回事 | /grill-with-docs（盘问对齐） | The Pragmatic Programmer："没人真的清楚自己想要什么" |
| **太啰嗦** | 20 个词说 1 个词的事，变量名长到读不完 | 共享语言（Ubiquitous Language）→ CONTEXT.md | DDD（Eric Evans）领域驱动设计 |
| **跑不起来** | 看着对，跑就崩，AI 修了又牵出新 bug | 反馈回路：/tdd + /diagnosing-bugs | The Pragmatic Programmer："反馈的速度就是你的速度上限" |
| **架构烂成泥** | AI 加速了编码，也加速了软件熵 | 每日投资设计：/to-spec + /improve-codebase-architecture | XP（Kent Beck）/ 软件设计哲学（Ousterhout） |

Matt 认为这四个模式中，**太啰嗦**和**跑不起来**最容易栽进去。解决"太啰嗦"的关键是在项目里先立一套共享语言（Ubiquitous Language），把冗长业务描述压成术语表放 CONTEXT.md，让 agent 命名一致、思考省 token。

### Claude Code 学习路线
[[摘要-claude-code-learning-roadmap]] 将 AI Coding 能力成长拆成三步：先会用 [[ClaudeCode]] 完成日常开发和 Debug，再用 [[CLAUDEmd]]、计划模式、Thinking Mode 与 [[Skill]] 做深度定制，最后通过 Subagents、[[MCP]] 和自动化流水线进入“指挥 AI 完成完整开发流程”的阶段。

## 注意事项
- 老旧项目和资金安全相关项目需更慎重
- 清晰有逻辑的表达能力成为竞争优势
- 版本管理是安全网（每步 commit + clear）
## 关联连接

- [[ClaudeCode]] — 核心实践工具
- [[Codex]] — 核心实践工具
- [[Agent]] — AI Agent 概念
- [[Skill]] — 技能扩展
- [[CLAUDEmd]] — 契约与指令
- [[ai-programmer-survival-guide]] — AI 时代程序员生存指南
- [[cognitive-offloading]] — 认知卸载风险
- [[摘要-AI-agent工具应该怎么使用]] — 来源
- [[OpenSpec]] — 规范驱动 AI 编程框架
- [[摘要-OpenSpec规范驱动AI编程框架]] — 来源
- [[摘要-step-3-7-flash-agent横评]] — 来源（Flash 模型在真实 Coding Agent 任务中的横评）
- [[摘要-claude-code-learning-roadmap]] — 来源（Claude Code 分阶段学习路线）
- [[Step3Flash]] — Agent 执行层模型案例
- [[AI就绪上下文包]] — AI 编程工作流中的上下文管理方式
- [[MattPocock]] — AI 编码四大失败模式分类提出者
- [[摘要-mattpocock-skills]] — 来源（四大失败模式与修复 Skill）
