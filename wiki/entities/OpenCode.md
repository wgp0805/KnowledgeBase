---
title: "OpenCode"
type: entity
tags: [AI, 开源, 编码助手, Agent]
sources: [raw/09-archive/ECC使用教程.md, raw/01-articles/OpenCode架构演进剖析.md]
last_updated: 2026-08-10
---

## 定义
OpenCode 是开源 AI 编程助手，支持事件驱动 Hook 系统和 SubAgent，是 Claude Code 的开源替代方案。相比 Claude Code 在插件系统和钩子事件上更强大。2.0 时代通过渐进式重构（v1.17.x→v1.18.x）完成了 Desktop 从单体到模块化工作空间的架构升级。

## 关键信息

### 与 Claude Code 的对比
| 特性 | Claude Code | OpenCode |
|------|------------|----------|
| 钩子事件类型 | 8 种 | 20+ 种 |
| 自定义工具 | 通过 hooks 模拟 | 6 个原生工具 |
| Skill 格式 | SKILL.md | SKILL.md（兼容） |
| 插件 API | 有限 | 更丰富的插件 API |

### 独有优势
- **file.edited** 事件：文件编辑后自动触发（Claude Code 无此事件）
- **lsp.client.diagnostics** 事件：LSP 诊断后触发
- **原生自定义工具**：run-tests、check-coverage、security-audit
- **精细 Skill 权限控制**：按 agent 设置不同的 skill 访问权限

### 安装 ECC
```bash
npm install -g opencode-ecc
# 或
npm install -g ecc-universal  # 通用包
```

### 配置文件
- 项目级：`opencode.json`
- 全局：`~/.config/opencode/opencode.json`
- Agent 定义：`AGENTS.md`
- Agent 引用：`@planner`、`@code-reviewer`

### 2.0 开发者生态（Desktop v2，详见 [[摘要-opencode-架构演进剖析]]）
- **插件 API**：导出函数返回 Hook 对象扩展功能；Hook 事件域含 command/file/lsp/message/permission/session/tool；`tool()` 可注册自定义工具
- **Skill 系统**：`SKILL.md` 定义可复用指令集；放 `.opencode/skills/`（项目级）或 `~/.config/opencode/skills/`（全局级）；通过 `opencode.json` 的 `skills:{name: allow/ask/deny}` 做权限控制；Agent 内置 `skill` 工具加载执行
- **SDK（@opencode-ai/sdk）**：sessions（create/prompt/command/shell）、files（find.text/find.files/read）、结构化输出（format: json_schema）

### 2.0 架构演进要点
- **UI 单体→模块化**：Session UI（v1.17.13）、Command Palette（v1.17.15）、Review Panel（v1.17.14）、Model Picker（v1.17.13）独立模块化，Home 冷启动时间显著降低（v1.18.0）
- **Prompt Input v2**（v1.18.2）：重写提高可靠性
- **标签页系统**：标签页作为"一等公民"，作用域限定单窗口、循环切换、导航与重开（v1.17.11-14）
- **Session Snapshots**（v1.17.11）：会话快照与回滚控制，出错一键恢复
- **Session Search**（v1.18.3）：command palette 直接搜索历史会话
- **MCP 深度集成**（v1.17.10-14）：server 配置 UI 化、Code mode adapter、可折叠 server sections——MCP 作为一等公民
- **多模型自适应思考**：模型特定系统提示 + 自适应推理控制（Claude Sonnet 5 / Kimi 等）
- **UI/UX 哲学**：从"命令行工具的图形化包装"转向"完整开发工作空间"，大量采用[[渐进式披露]]（渐进式公开，默认简洁按需展开）
- **兼容迁移**：新旧界面设置切换 → 完成迁移保留升级处理 → 逐步移除旧代码
- **技术债务修复**：默认禁止 subagent 嵌套（v1.18.2）、WSL 加载修复（v1.18.3）

### 衍生项目
- **[[MiMoCode]]** — 小米基于 OpenCode 构建的 AI 编程 Agent，保留全部核心能力（多 Provider、TUI、LSP、MCP、插件），扩展了持久化记忆、子智能体编排、目标驱动自主循环、Compose 工作流和自进化能力

## 关联连接
- [[ECC]] — 增强框架（同时支持 Claude Code 和 OpenCode）
- [[MiMoCode]] — 基于 OpenCode 的衍生项目
- [[ClaudeCode]] — 对比平台
- [[Agent]] — Agent 核心概念
- [[Hooks]] — 钩子系统（OpenCode 事件更丰富）
- [[Skill]] — 技能扩展机制
- [[MCP]] — OpenCode 深度集成协议
- [[渐进式重构]] — 2.0 架构演进的指导方法论
- [[渐进式披露]] — UI 设计哲学
- [[FeatureToggle]] — 新旧界面切换的支撑机制
- [[WSL2]] — 跨平台支持改进
- [[摘要-ECC使用教程]] — 来源
- [[摘要-mimo-code发布]] — MiMo Code 来源
- [[摘要-opencode-架构演进剖析]] — 2.0 架构演进来源
