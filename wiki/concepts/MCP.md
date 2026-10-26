---
title: "MCP"
type: concept
tags: [AI, 协议, 外部服务]
sources: [raw/01-articles/40分钟学会Codex！"零基础"终级教程～【附完整文档】.md, raw/01-articles/全网最全！60分钟全面掌握Claude Code~【附完整文档】.md, raw/01-articles/用 Java 开发 AI 项目，太爽了！.md, raw/09-archive/JAVA中AI框架选型指南（2026）.md, raw/01-articles/Claude Code 最佳学习路线：从“手敲代码”到“指挥AI打工”，强的离谱！！.md, raw/09-archive/AgentScope入门指南.md, raw/01-articles/2026-08-02-MCP 第五版 × OpenClaw.NET：从协议升级到生态编排 - 张善友.md, raw/09-archive/为什么越来越多人用FastMCP？.md, raw/01-articles/2026-09-07-"GPT-6 Astra 正式登场"会怎样改变现有技术栈？.md, raw/09-archive/2026-09-15-让AI真正赋能企业（初探）.md, raw/01-articles/2026-09-15-只会搜关键词还不够，Agent 需要一套更聪明的本地搜索.md, raw/01-articles/2026-10-01-Claude Code + MCP，让一个空文件夹变成了能玩的 Unity 游戏 - 张善友.md]
last_updated: 2026-10-08
---

## 定义
Model Context Protocol，解决 AI 与外部工具、外部服务连接的转接头协议，让 Agent 能访问外部数据源和工具。

## 关键信息
- MCP 服务占用 token 较多，难以同时存储很多
- 轻量外部工具正转向 Skill，重量的转向 CLI
- 使用时需配置 MCP 服务器地址和认证信息
- 典型应用：NotebookLM 知识库接入、Figma 设计稿读取
- LangChain4j 支持 MCP 集成：SSE 在线调用（HttpMcpTransport）和本地 Stdio 调用（StdioMcpTransport）
- Java 通过 McpToolProvider 将 MCP 工具注入 AI Service
- Claude Code 率先发明 MCP，Codex 后续跟进支持
- DeepSeek TUI 也支持通过 MCP 服务器扩展智能体能力

### A2A 与 MCP 的关系
- A2A（Agent-to-Agent）与 MCP 互补：MCP 解决 Agent 与外部工具/服务的连接，A2A 解决 Agent 与 Agent 之间的协作
- Spring AI Alibaba 和 AgentScope-Java 同时支持 MCP 和 A2A 协议

### AgentScope 集成方式
AgentScope-Java 通过 `tools.json` 文件驱动 MCP 集成：

**tools.json 声明式配置**：
```json
{
  "mcpServers": {
    "github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": {
        "GITHUB_PERSONAL_ACCESS_TOKEN": "${env:GITHUB_TOKEN}"
      }
    }
  }
}
```

**三种传输协议**：
| 协议 | 适用场景 | 声明方式 |
| --- | --- | --- |
| **stdio** | 本地进程，最常见 | `command` + `args` |
| **sse** | 远程 HTTP SSE server | `url` + `headers` |
| **ws** | 双向 WebSocket | `url` + `headers` |

HarnessAgent 启动时自动扫描 `workspace/tools.json` 的 `mcpServers` 段，连接每个 Server，自动将工具注册到 Agent。也可以通过 Java 代码用 `McpServerConfig` + `ToolsConfig` 动态配置。

**常用 MCP Server**：server-github（GitHub 操作）、server-filesystem（文件系统读写）、server-postgres（数据库查询）、server-slack（消息发送）、server-puppeteer（浏览器自动化）

### MCP 第五版（2026-07-28）无状态化
- **核心变革**：会话从协议层被彻底删除，MCP 从有状态的双向协议变成无状态的请求-响应协议
- 旧握手 `initialize/initialized` 简化为每请求自包含协议版本与能力；移除 `Mcp-Session-Id` 粘性会话；状态外置到数据库/缓存；HTTP+SSE 长连接改为 Streamable HTTP
- **收益**：远程 MCP Server 可像普通 HTTP 服务一样部署到 Serverless、边缘节点或 Kubernetes；支持轮询负载均衡，天然适配 K8s；网关可直接通过 `Mcp-Method`/`Mcp-Name` 请求头路由，无需解析 JSON body，降低网关 CPU 开销
- **显式业务句柄**：跨调用状态（浏览器实例、购物车、审批流程）通过显式句柄传递（如 create_browser 返回 browser_id），状态属于业务而不属于连接
- **MRTR**：替代服务端反向请求客户端能力，客户端携带 inputResponses+requestState 重新发起原始请求，任意服务端实例可继续任务（见 [[MRTR]]）
- **扩展框架**：MCP Apps（提供交互式 HTML 界面）、Tasks（标准创建-查询-更新-取消任务接口）、JSON Schema 2020-12（$ref/oneOf/anyOf/allOf）
- 核心协议做小、扩展能力做标准（Unix 哲学）：核心只管「如何调用工具」，Apps 管「如何渲染界面」，Tasks 管「如何管理长任务」

### FastMCP：MCP 生态事实标准
- FastMCP 是建立在 MCP 协议之上的 Python 框架，占所有语言 70% 的 MCP 服务器份额，GitHub 25.5k Star（vs 原生 SDK 405 Star），2024 年 1.0 并入官方 MCP Python SDK
- 用 `@mcp.tool`/`@mcp.resource`/`@mcp.dependency` 装饰器把协议底层细节封装成 Pythonic API，Schema/验证/文档自动生成
- 三大支柱：Servers（包装 Python 函数为 MCP 工具/资源/提示词）、Clients（连接任意 MCP 服务器）、Apps（交互式 UI）
- 企业级方案 Prefect Horizon 提供 SSO/RBAC/审计/可观测性
- 详见 [[FastMCP]]、[[摘要-为什么越来越多人用FastMCP]]

### GPT-6 Astra 时代的远程 MCP（2026-09-07）
- GPT-6 Astra 的 [[ResponsesApi]] 承载远程 MCP 调用
- Astra 支持 [[ToolSearch]] 和 [[Skills]]：需要时再加载工具定义与能力说明，避免一次塞进上下文
- 这会影响 Agent 框架：纯粹做工具转发的中间层价值下降；留下来的部分是企业连接器/流程规则/可观测性/权限控制/异常恢复
- 详见 [[摘要-GPT-6-Astra改变技术栈]]

### MCP 作为员工 AI 项目的发布协议（2026-09）
来自 [[摘要-让AI真正赋能企业初探]]。**企业 Agent 中枢** 的核心机制就是把通用能力（用户、基础数据、权限、三方工具）通过 MCP 协议开放给所有员工 AI。每个员工 AI 发布的项目可以在企业 Agent 中枢中**开放自己的 MCP 服务**，供其他员工的 AI 调用，形成"AI 内循环"。通用测试 Agent 前置——只跑基础安全，不改业务逻辑。详见 [[Agent中枢]]。

### MCP 作为本地搜索基础设施的接入层（2026-09）
来自 [[摘要-zvec-grep-本地搜索基础设施]]。zvec-grep 通过 `zg install` 自动发现已装的 Agent（Codex/Claude Code/Cursor/OpenCode/Qoder）并配好 MCP，CLI 和 Agent **共享同一份索引**。Agent 不必再重复建索引，本地搜索从"命令"升级为"面向 Agent 工作流的基础设施"。详见 [[ZvecGrep]]。

### MCP 与 Skill 的上下文开销权衡（2026-10）
来自 [[摘要-claude-code-mcp-unity游戏]]。实测经验：**Skill 每次调用只占约 8 个 token**、按需加载平时不占上下文，而 **MCP 工具开销重得多且始终挂在 prompt 里**（不管用不用）——上下文窗口装多了 AI 智能明显下降。工程建议：优先用 Skills 而非 MCP 工具、把用不到的 MCP 工具（Gmail、Calendar 等）统统禁掉、任务之间 `/clear`；"薄服务器+动态注册"模式的 GameDev-MCP-Server 一份代码同时服务 Unity/Godot/Unreal 三引擎，是 MCP 服务器复用的范本（见 [[UnityMCP]]）。

## 关联连接
- [[Agent]] — MCP 所属概念
- [[ClaudeCode]] — MCP 发明者
- [[DeepSeekTUI]] — MCP 支持者
- [[Skill]] — 替代/互补方案
- [[LangChain4j]] — MCP Java 实现
- [[A2A]] — 互补协议
- [[SpringAI_Alibaba]] — 双协议支持
- [[AgentScope_Java]] — 双协议支持
- [[HarnessAgent]] — AgentScope MCP 自动集成
- [[MRTR]] — 第五版多轮往返机制
- [[OpenClawNET]] — 第五版编排层实践
- [[FastMCP]] — MCP 生态事实标准 Python 框架
- [[GPT-6]] — Astra 支持远程 MCP
- [[ResponsesApi]] — Astra 唯一支持接口
- [[ToolSearch]] — 按需加载工具
- [[Skills]] — 按需加载能力说明
- [[摘要-claude-code-learning-roadmap]] — 来源（Claude Code 王者级外部连接能力）
- [[摘要-AgentScope入门指南]] — 来源（AgentScope MCP 集成实战）
- [[摘要-mcp-v5-openclaw-net]] — 来源（MCP 第五版 × OpenClaw.NET）
- [[摘要-为什么越来越多人用FastMCP]] — 来源（FastMCP 占 70% MCP 服务器份额）
- [[摘要-GPT-6-Astra改变技术栈]] — 来源（Astra 远程 MCP 支持）
- [[摘要-让AI真正赋能企业初探]] — 来源（员工 AI 项目通过 MCP 发布）
- [[摘要-zvec-grep-本地搜索基础设施]] — 来源（zg 通过 MCP 接入 Agent）
- [[Agent中枢]] — 企业 Agent 架构范式
- [[ZvecGrep]] — 通过 MCP 接入 Agent 的本地搜索
- [[UnityMCP]] — MCP 驱动游戏开发的实践案例
- [[摘要-claude-code-mcp-unity游戏]] — 来源（MCP 与 Skill 上下文开销权衡）
