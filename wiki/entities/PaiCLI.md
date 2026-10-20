---
title: "PaiCLI"
type: entity
tags: [AI, CLI工具, Agent, 开源项目]
sources: [raw/09-archive/AI agent工具应该怎么使用.md, raw/09-archive/面试官皱眉："让你负责一个生产级 Agent，你会怎么设计？"，我上来就开始背 ReAct、Function Calling、Skills。面试官听完摇头。.md, raw/09-archive/DeepSeek 员工：DeepSeek V4 Pro 正式发布，Harness 也进入最后一个内测版本（附Agent面试题）.md, raw/01-articles/JD员工：同事觉得电脑太卡，我用Codex帮他修，结果不小心看到他正在写的辞职信还有已经到手的offer，该不该跟领导说呢（附Agent面试题）.md]
last_updated: 2026-10-20
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

### 模型工厂与 Provider 降级（2026-08-24 增补）
- 请求先发给默认 Provider，失败后按顺序尝试下一个（GLM、DeepSeek、Step、Kimi 等），每个 Provider 对应一个客户端实例，统一实现同一套模型调用接口
- 模型抽象层已封装 OpenAI 协议的 HTTP 调用、SSE 解析、错误处理、重试逻辑；接入新模型（如 [[OxAlpha]]）只需新增一个 Provider 实现，声明"与标准协议的差异"
- 针对免费预览模型下线的系统性降级：①换同模型的其他 Provider；②换同能力级别模型；③降能力保可用（切小尺寸模型并限制任务复杂度）——每级切换都记录日志、发告警，不让用户在不知情时被降级

### 五大工程挑战实战细节（2026-10-20 增补，详见 [[摘要-jd-codex辞职信-agent面试题]]）
以 PaiCLI 为背景的 5 道 Agent 面试题解答，是该页"上下文压缩/容错"章节的量化版：

- **上下文膨胀 + JVM 内存失控**：三档渐进式压缩——①单次工具输出超 32000 字符即把完整结果卸载到 `.paicli/tool-outputs/<session>/`，上下文只留路径 + 开头 2000/结尾 800 字符预览；②token 触阈值时把除最近 3 条外的旧 `tool` 消息正文替换为 `[已清理的旧工具结果]` 占位符（保留 `tool_call_id` 维持配对）；③逼近窗口上限（200k 窗口约 167k token 触发）才做摘要压缩，保留最近 3 个完整用户轮次，更早历史按 60000 字符分块生成含四要素的结构化摘要。网络出口用 Jackson 生成器直接把 JSON 语法树写进输出流（先写计数空流拿 Content-Length 再原样写出），1M token 场景单次请求堆分配从 90.5MB 降到 4.7MB
- **MCP 子进程守护**：stdio 读循环单行隔离解析（非 JSON 行进 200 行 stderr 环形缓冲区，读线程绝不退出），区分 `method` 字段防 ping 请求 ID 串号；`Process.onExit()` + 30 秒空闲 ping（连 2 次不回判卡死）；死后卸载工具、`ProcessHandle.descendants()` 整棵进程树先关 stdin 再叶子逆序终止、2 秒后强清，1s/2s/4s 指数退避重启，稳定运行 60 秒后崩溃计数清零，连续 3 次失败停止并提示手动排查；PID/时间戳/命令行写入 `~/.paicli/mcp-pids.json` 下次启动清理孤儿进程
- **工具并发纪律**：8 类只读工具最大 4 线程并发，写文件与命令工具严格串行；每轮执行前在 `~/.paicli/snapshots/` 独立影子 Git 仓库做 `PRE_TURN` 快照，恢复会话先 `restorePreTurn` 还原工作区再重跑本轮，保证磁盘与对话账本一致
- **会话状态恢复**：本地只追加 JSONL（`~/.paicli/history/raw/<session>.jsonl`），每次修改内存对话历史后追加 `view_checkpoint` 记录，`/resume` 时定位最后一条 checkpoint 还原压缩后基准视图再重放增量，一字不差恢复重启前上下文
- **防行为漂移**：安全策略/模式守则/项目 `PAI.md` 固定拼进系统提示词全量注入、不参与压缩；Plan 模式生成带依赖的 JSON 任务图，拓扑排序 + 环检测校验后作为外部进度看板；摘要压缩强制校验"当前目标与成功条件、用户要求与已确认决定、已完成工作及证据、未解决问题与下一步"四要素，缺一项先自动修复格式、再缺则放弃本次压缩；`write_file`/`edit_file` 后置钩子自动跑 JavaParser 语法诊断，最多 20 条 `[LSP 诊断注入]` 在下一轮注入，防止带着编译不过的代码继续跑

### 简历写法 v2（2026-10-20）
项目名"PaiCLI 终端与云端代码 Agent"，技术栈 Java 21 / Spring AI / OkHttp / JGit / JavaParser / SQLite / JSON-RPC 2.0（MCP）；核心职责五条：三档压缩 + 流式写出（90.5MB→4.7MB）、读写分离调度 + 影子 Git 快照回滚、MCP 子进程生命周期守护（指纹信任校验/环境变量白名单/心跳探测/指数退避）、bubblewrap/Seatbelt 沙箱 + JSONL 审计日志、防漂移体系 + 增量索引（1892 个源码全量索引 218.9s→128.7s，无改动校验 0.8s）

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
- [[摘要-ox-alpha模型与agent面试题]] — 来源（模型工厂降级与评测体系）
- [[摘要-jd-codex辞职信-agent面试题]] — 来源（五大工程挑战实战细节与简历写法 v2）
- [[OxAlpha]] — 面试题中演示接入的免费预览模型
- [[降级]] — Provider 级降级策略的概念基础
