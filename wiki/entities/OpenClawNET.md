---
title: "OpenClawNET"
type: entity
tags: [实体, AI Agent, 开源项目, MCP]
sources:
  - raw/09-archive/2026-08-02-MCP 第五版 × OpenClaw.NET：从协议升级到生态编排 - 张善友.md
  - raw/09-archive/2026-09-27-当 AI Agent 遇到 Nacos：OpenClaw.NET 集成入门 - 张善友.md
last_updated: 2026-09-28
---

## 定义
OpenClaw.NET 是 OpenClaw 的 .NET 生态版本，定位为「MCP 生态编排层」：当单个 MCP Server 变成「迷你 SaaS」时，OpenClaw.NET 成为这些 SaaS 之间的编排操作系统，通过 PR #196（csharp-sdk v2.0）全面拥抱 MCP 第五版协议。

## 关键信息
- **架构六层组件**：
  - **Gateway**：无状态路由与协议翻译（Mcp-Method/Mcp-Name 请求头路由、缓存语义、OTel 链路追踪、OAuth/OIDC 鉴权、限流审计、协议协商）
  - **MetaSkill**：工具编排与状态传递（显式句柄即 DAG 数据令牌）
  - **TokenHub**：计量与审计（每个句柄可追踪、计费、审计）
  - **Harness**：异步任务与中断恢复（MRTR 的 input_required 状态持久化，用户响应后重新调度到任意 Worker）
  - **OpenSandbox**：安全界面渲染（MCP Apps 沙箱 iframe 环境）
  - **DDI Registry**：契约治理（JSON Schema 2020-12 注册/版本化）
- **MCP 第五版适配要点（PR #196）**：
  - 协议协商优先 `server/discover`，404/-32601 回退 initialize
  - 支持 Streamable HTTP、每请求携带 Mcp-Method/Mcp-Name/Mcp-Protocol-Version 请求头
  - 实现 `/apps/mcp/{appId}` 代理端点（MCP Apps 正式扩展）
  - Tasks 扩展：任务句柄模型与 Harness 工作流实例 ID 同构
  - JSON Schema 2020-12：支持 $ref/oneOf/anyOf/allOf；工具缺失 inputSchema 时跳过而非崩溃；AllowRelaxedInputSchemaValidation 兼容开关
- **状态哲学**：无状态 Gateway × 有状态 Harness——获得 Serverless 弹性 + 有状态工作流可靠性

### Nacos 集成：零 LLM 调用的确定性工具管线（2026-09，来源：[[摘要-openclaw-net-nacos集成]]）
- **三层职责**：Nacos 3.2.4 AI 管理中心决定"存在什么、谁可见"（元数据/端点/版本/工具开关）；`NacosMcpRouter`（.NET global tool，ONNX 本地向量检索，不依赖外部 LLM）决定"如何被发现与连接"（search → add → use）；OpenClaw 运行时决定"何时、以何身份、经何审批执行"（确定性排序、有界缓存、熔断、审计回放）
- **Agent 声明**：skill 文件里只写 `capability_ref`（`provider: nacos`、`binding: dynamic|static`、`intent: task_description + keywords`）+ `tool_args`，发现与参数填充由 `AgentRuntime` / `MafAgentRuntime` 的同一条 capability 路径完成
- **协议防腐层**：Router 返回的是"自然语言包裹 JSON 的散文信封"，解析收敛到单一契约文件并有测试钉住，同一套 adapter 同时兼容 Python 版与 .NET 版 Router
- **缓存与世代**：TTL 300 秒、容量 1024、FIFO 驱逐；缓存键 `provider.Id:generation:binding:intentKey`，Nacos 配置一变世代 +1，旧键失效、在途解析晚到写不进新缓存，过期返回 `capability_stale_binding` 重试
- **熔断**：同一目标（安全域+provider+世代+Server+工具）连续失败 3 次熔断 30 秒，成功一次复位；被策略阻止（Blocked）的失败不计入；熔断器容量满时冷却中的不驱逐
- **失效事件**：Nacos 长轮询 → 内容 SHA-256 比对 → 发布 CapabilityChange → 缓存全量清空（正确性优先于命中率）
- **安全模型**："A tool handle, never permission to execute." 能力解析与执行被包装成 `resolve_capability` 工具，先过 OpenClawToolExecutor 治理链（审批、hooks、审计、工具策略）；userId/sessionId 随 MCP 请求 `Meta` 字段传给 Router；缓存命中后复检策略，动态绑定丢弃缓存重解析、静态绑定执行期拒绝；注册表元数据不等于真实能力
- **上手**：`dotnet tool install --global NacosMcpRouter`；Console API 默认 `127.0.0.1:8080` 不可覆盖；在 Nacos 控制台关闭某工具后运行时应在数秒内完成失效并拒绝调用

## 关联连接
- [[OpenClaw]] — 所属项目
- [[MCP]] — 核心协议
- [[MRTR]] — 协议新机制
- [[meta-skill]] — 编排引擎
- [[AgentHarness]] — 任务引擎
- [[摘要-Claude-Code-Workflows-vs-MetaSKILL]] — MetaSkill 编排对比
- [[摘要-mcp-v5-openclaw-net]] — 来源
- [[摘要-openclaw-net-nacos集成]] — Nacos 集成篇来源
- [[Nacos]] — 注册中心与 AI 管理中心
- [[AI Registry]] — Nacos 侧治理模块
- [[张善友]] — 两篇文章的作者
