---
title: "PaiCLI"
type: entity
tags: [AI, CLI工具, Agent, 开源项目]
sources: [raw/09-archive/AI agent工具应该怎么使用.md, raw/09-archive/面试官皱眉："让你负责一个生产级 Agent，你会怎么设计？"，我上来就开始背 ReAct、Function Calling、Skills。面试官听完摇头。.md, raw/09-archive/DeepSeek 员工：DeepSeek V4 Pro 正式发布，Harness 也进入最后一个内测版本（附Agent面试题）.md]
last_updated: 2026-08-13
---

## 定义
PaiCLI 是开发者"二哥"（沉默王二）开源的终端 Agent 项目，类 Claude Code 的 AI 命令行工具，使用 Python 编写，GitHub 地址：https://github.com/itwanger/PaiCLI-Python。作为生产级 Agent 的典型案例，深度覆盖了 Agent 工程化的核心挑战。

## 关键信息
- 开发方式：全程使用 Codex 进行 AI 辅助编程
- 集成了阿里云 OCR 服务（通过 .env 中 ALIYUN_OCR_ENABLED 全局开关控制）
- 使用 JLine 交互库实现命令行交互界面
- 多模型协作开发流程：Claude Code 做需求拆解和审查，Codex 负责执行实现
- 每个功能均让 Codex 生成测试用例
- 技术栈：Java 21 + OkHttp + SQLite + JLine，未使用 Spring AI 等框架

### 三种运行模式
1. **ReAct 主循环**：经典的推理-行动循环模式，用于实时交互的短任务
2. **Plan-and-Execute**：先规划后执行，适合复杂任务（如多文件重构），通过 DAG 任务图按拓扑排序执行
3. **Multi-Agent Team**：多角色协作模式

三种模式共用一套工具注册表、记忆系统、安全审批、审计日志，是 Agent Harness 的核心设计挑战。

### Agent 完整流程（ReAct 模式）
1. **输入预处理**：本地路径展开、图片引用解析等
2. **长期记忆检索**：找出与当前输入相关的记忆注入系统提示词
3. **Prompt 组装**：分层拼接（静态层在前，动态层在后），利用 Prompt Caching 降低 API 成本
4. **ReAct 循环主体**：检查退出条件（Token 预算耗尽、连续相同工具调用、迭代上限等）→ 调用 LLM → 若返回 Function Calling 则执行工具（可并行）→ 结果追加到对话历史 → 继续决策
5. **输出格式化**：无工具调用时，将最终结果格式化为 HTML 返回

### 审批机制（HITL）
- write_file、execute_command 等高危工具执行前走 HITL 审批
- 路径检查器判断文件路径是否在允许范围内
- 命令检查器判断命令是否安全
- 审批策略分三档：auto（自动通过）、suggest（建议确认）、never（必须手动确认）
- 读操作不需要审批，直接执行
- 拒绝结果作为 tool_result 返回给模型，模型自行决定下一步（如换一种方式达成目标）

### Prompt 分层设计
PaiCLI 的 Prompt 共 9 层，前 4 层静态（身份定义、人格定义、模式指令、审批策略），利用 Prompt Caching 按最长公共前缀命中，前缀越稳定缓存命中率越高。

### 工具 Schema 约束
- 每个工具注册时带 JSON Schema，定义参数类型、必填项、取值范围
- 模型生成的工具调用参数必须通过 Schema 校验，不合规就拒绝执行
- MCP 工具的 Schema 需额外清洗：ref 展开、anyOf 拍平成最常用类型

### 容错与异常处理

#### LLM 层
- 重试 3 次，指数退避加随机抖动，退避基数 500ms，上限 30s
- 仅重试特定错误码：429（限流）、500/502/503/504（服务端异常）、408（超时）
- 400（参数错误）、401（认证失败）不重试
- 响应头带 Retry-After 时优先使用服务端建议的等待时间

#### 工具层
- 单个工具执行失败不中断整体流程，失败消息作为 tool_result 追加到对话历史
- 并行执行的多个工具，总超时 90 秒

#### Agent 层
- 检测到连续相同的工具调用就强制退出
- Plan 模式下，任务执行中途失败：进度不到一半则重新规划，进度过半则保留已完成部分继续推进

### 上下文压缩策略
- Map-Reduce 分片摘要：旧消息每 5 条一组切片 → 独立生成摘要 → 合并为整体摘要
- 压缩后保留"摘要 + 最近 3 轮完整对话"
- 压缩前进行事实提取，将跨会话稳定事实写入长期记忆

### 记忆系统设计
- 不使用向量数据库，而是关键词匹配检索（规模小，毫秒级响应）
- 时间衰减加权：24 小时从满分衰减到半分
- 重要信息三层过滤：排除临时任务 → 排除推测 → 保留持久信号

### 指数退避重试
- 默认最多 3 次，间隔 500ms → 1s → 2s，上限 30s
- 加 20% 随机抖动，支持 Retry-After 头
- 区分可重试和不可重试错误类型

### 模型路由模块（2026-08-13 增补）
- 支持 7 个供应商的动态切换，运行时通过 `/model` 命令手动切换，也可根据任务类型自动路由
- 路由策略：规划/代码审查/复杂推理（连续推理 3 步以上、嵌套参数/多可选字段 schema）走 Pro；文件读写/格式化/简单补全/单步工具调用走 Flash
- 降级兜底：高峰期 Pro 限流时自动降级到 Flash，保证任务不中断
- 上下文拼接模块：系统提示和工具定义拼在最前面，记忆紧跟其后，用户消息和工具结果放尾部（配合 Prompt Caching）

### Better Harness 审计工具（2026-08-13 增补）
PaiCLI 的 Better Harness **不是 Agent 产品**，而是评估 Agent 干活质量的审计工具，与 [[Harness|DeepSeek Harness]]（Coding Agent 产品）是不同概念。执行器并行启动三个取证通道：

1. **会话证据通道**：从对话记录提取去标识化元数据（工具调用次数、模型切换记录、任务生命周期信息）
2. **项目配置通道**：扫描仓库里的测试、CI 文件和交付约束
3. **配置通道**：检查 Skill 配置、MCP 设置和记忆入口

最终按五个维度打分，检查 Agent 干活质量。详见 [[BetterHarness]]。

### 简历写法参考
文章给出了 PaiCLI 的简历包装示例（项目名 CodeMate，2026.03–2026.05）：
- 技术栈：Java 21、JLine、JavaParser、SQLite、JGit、Ollama、Jieba
- ReAct + Plan-Execute 双模式，Planner/Worker/Reviewer 多 Agent 协作
- ripgrep + JavaParser AST + Ollama Embedding + Jieba + BM25 混合检索，千行级代码块 P90 延迟 94ms
- 短期/长期记忆，Map-Reduce 摘要压缩，SQLite 持久化 + BM25 + 向量检索
- SWE-bench Multilingual + Harbor 构建 43 个真实 Issue 测试集，Pass@1 达 62.8%（修复 27 个）

## 关联连接
- [[Codex]] — 核心开发工具
- [[ClaudeCode]] — 代码审查工具
- [[PaiAgent]] — 同作者的 AI Agent 平台项目
- [[摘要-AI-agent工具应该怎么使用]] — 来源
- [[摘要-生产级Agent设计]] — 来源（面试题详解）
- [[摘要-deepseek-v4-pro-发布-harness-内测]] — 来源（V4 Pro 发布 + Better Harness 审计工具）
- [[BetterHarness]] — PaiCLI 的 Agent 质量审计工具
- [[ResponsesApi]] — V4 Pro/Flash 正式版支持的有状态 API
- [[context-compression]] — 上下文压缩策略
- [[指数退避重试]] — API 重试机制
- [[渐进式披露]] — Skill 按需加载机制
- [[沉默王二]] — 项目作者
