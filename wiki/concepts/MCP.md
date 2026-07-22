---
title: "MCP"
type: concept
tags: [AI, 协议, 外部服务]
sources: [raw/01-articles/40分钟学会Codex！"零基础"终级教程～【附完整文档】.md, raw/01-articles/全网最全！60分钟全面掌握Claude Code~【附完整文档】.md, raw/01-articles/用 Java 开发 AI 项目，太爽了！.md, raw/01-articles/JAVA中AI框架选型指南（2026）.md, raw/01-articles/Claude Code 最佳学习路线：从“手敲代码”到“指挥AI打工”，强的离谱！！.md, raw/01-articles/AgentScope入门指南.md]
last_updated: 2026-07-22
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
- [[摘要-claude-code-learning-roadmap]] — 来源（Claude Code 王者级外部连接能力）
- [[摘要-AgentScope入门指南]] — 来源（AgentScope MCP 集成实战）
