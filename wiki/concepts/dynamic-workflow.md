---
title: "dynamic-workflow"
type: concept
tags: [AI Agent, 工作流编排, 代码即配置, MiMo Code]
sources: [raw/01-articles/小米版Claude Code正式发布，这次开源能给到夯.md]
last_updated: 2026-06-11
---

## 定义
Dynamic Workflow 是用代码替代自然语言编排复杂 AI Agent 工作流的方案。主 Agent 生成 JavaScript 脚本，在隔离沙箱中确定性执行，通过 `agent()` 派出 Sub-agent，通过 `parallel()` 和 `pipeline()` 控制并发。

## 关键信息
- **问题本质**：传统 Skill 用自然语言写编排逻辑 → 自然语言模糊、可遗忘、不可验证 → 复杂流程中系统性失效（上下文压缩吞掉步骤、模型跳过环节、分支重试靠模型判断而非代码保证）
- **解决思路**：编排逻辑从自然语言变为代码（JavaScript），在隔离沙箱中确定性执行
- **兼容性**：兼容 Anthropic Dynamic Workflow 核心语义
- **扩展能力**：
  - `workflow()` 允许脚本调用其他脚本，编排逻辑可复用和组合
  - 每个 `agent()` 调用的结果同步落盘，进程中断后可恢复
  - 沙箱内可直接读写文件
- **Skill vs Workflow**：Skill 是用自然语言写的 SOP，Workflow 是用代码写的 SOP

### Claude Code Dynamic Workflows（Anthropic 官方实现）
- **设计范式**：代码即编排（Code-as-Orchestration），图灵完备
- **核心 API**：`agent()` / `pipeline()` / `parallel()` / `phase()` / `budget`
- **安全机制**：运行时 Node.js 沙箱约束（无文件系统/网络）
- **状态恢复**：会话级 checkpoint + resume
- **适用场景**：快速审查 PR、多维度研究分析、一次性探索性分析

### 与 OpenClaw.NET MetaSKILL 对比
| 维度 | Claude Code Workflows | OpenClaw.NET MetaSKILL |
|---|---|---|
| **编排语言** | JavaScript（图灵完备） | YAML（声明式，非图灵完备） |
| **表达力** | 极高：循环、条件、try-catch | 中等：DAG + 条件路由 + fan_out |
| **安全门禁** | 运行时沙箱 | 三步 tool_allowlist + capabilities + policy |
| **审计持久化** | 会话内 | 持久化 + CLI 查询 |
| **人机交互** | 无原生暂停点 | `user_input` 检查点 |
| **Token 预算** | `budget` 全局变量 | 4 层超时保护 |
| **部署方式** | Claude Code CLI 会话 | .NET Gateway 服务器 |
| **最适合** | 探索性、一次性、程序员驱动 | 生产级、可审计、长期维护 |

两者互补：用 Workflows 做原型和探索，模式稳定后用 MetaSKILL 模板固化。

## 关联连接
- [[MiMoCode]] — 所属产品
- [[max-mode]] — 计算主题的并行机制
- [[goals]] — 计算主题的串行机制
- [[AgentHarness]] — Harness 计算主题
- [[Skill]] — 自然语言 SOP 对比
- [[摘要-mimo-code发布]] — 来源
- [[ClaudeCode]] — Workflows 所属平台
- [[OpenClaw]] — MetaSKILL 所属项目
- [[meta-skill]] — 元技能概念（声明式编排）
- [[摘要-Claude-Code-Workflows-vs-MetaSKILL]] — 来源
