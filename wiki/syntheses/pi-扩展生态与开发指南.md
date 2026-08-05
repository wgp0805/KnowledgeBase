---
title: "Pi 扩展生态：现成扩展查找与开发规范"
type: synthesis
tags: [pi-agent, 扩展, 开发指南, Agent]
sources: []
last_updated: 2026-08-05
---

# Pi 扩展生态：现成扩展查找与开发规范

## 结论
Pi 已有成熟且丰富的扩展生态：官方 50+ 扩展示例 + 社区数千个 npm 包（keywords: pi-package）。不想开发可直接复制/一键安装；想开发遵循四层扩展系统（Skill / Prompt Template / Extension / Package），Extension 是能力核心（TypeScript 模块，jiti 加载免编译）。

## 一、四层扩展系统速查
| 层 | 形态 | 写起来要 | 能力边界 |
| --- | --- | --- | --- |
| Skill | Markdown（SKILL.md） | 5 分钟 | 按需投喂工作流给模型；不能跑代码、不能拦事件 |
| Prompt Template | Markdown（*.md） | 2 分钟 | 把常打的 prompt 变成 `/foo` 命令 |
| Extension | TypeScript 模块 | 30 分钟~几天 | 注册工具、拦 Agent loop、画 TUI、做 RPC |
| Package | npm/git 包 | 1 小时 | 把上面三层打包发布共享 |

## 二、现成扩展从哪里找（不用开发时）
1. **pi.dev/packages** — 官方 Package Catalog，按类型（extension/skill/prompt/theme）筛选，每条附 `pi install npm:xxx`
2. **npm 搜索**：`npmjs.com/search?q=keywords:pi-package`
3. **官方 examples**：`earendil-works/pi` 仓库 `packages/coding-agent/examples/extensions/`（50+ 可直接复制）
4. **Discord 社区** #pi-packages 频道

常用官方扩展示例（复制到 `~/.pi/agent/extensions/` 即自动加载）：
- 安全类：`permission-gate.ts`（危险命令确认）、`protected-paths.ts`（保护 .env/node_modules）、`confirm-destructive.ts`、`dirty-repo-guard.ts`、`sandbox/`
- 工作流类：`plan-mode/`（计划模式）、`subagent/`（子 Agent）、`git-checkpoint.ts`（每轮 Git 检查点）
- 功能类：`todo.ts`、`ssh.ts`（远程执行）、`tool-override.ts`、`qna.ts`、`status-line.ts`

常用社区 npm 包：
- `pi-mcp-adapter` — MCP 支持
- `pi-subagents` — 子 Agent（月下载 10 万+）
- `pi-web-access` — 网页搜索/抓取
- `pi-plan-mode`、`pi-lsp`、`pi-memory`、`@vtstech/pi-security`（命令/路径/SSRF 防护）
- `pi-marketplace` — 在 Pi 内搜索/审计/安装包（带安全审查）

管理命令：`pi install <src>` / `pi list` / `pi config`（启停资源）/ `pi update`。
⚠️ Pi 包以完整系统权限运行，装第三方包前务必审源码。

## 三、Extension 开发规范（核心）
- 入口必须 `export default function (pi: ExtensionAPI) { ... }`（可用 async 做一次性初始化）
- 放置位置：`~/.pi/agent/extensions/`（全局）/ `.pi/extensions/`（项目）/ `pi -e ./path.ts`（临时测试）
- 经 jiti 加载，**TypeScript 无需编译**；`/reload` 热重载
- 可导入包：`@earendil-works/pi-coding-agent`（类型）、`typebox`（参数 Schema）、`@earendil-works/pi-ai`、`@earendil-works/pi-tui`
- 注册接口：`pi.registerTool()`、`pi.on()`（生命周期事件）、`pi.registerCommand()`、`pi.registerShortcut()`、`pi.registerFlag()`、`pi.sendMessage()`
- 参数用 TypeBox Schema；字符串枚举用 `StringEnum`（Google API 兼容必需）
- 状态持久化：工具返回 `details` 字段 + `pi.appendEntry()`，保证会话 fork 时状态不丢
- 用户交互：`ctx.ui.select/confirm/input/notify/setStatus/setWidget/custom`（可画完整 TUI 组件）

## 四、Package 发布规范
```json
{ "name": "my-pi-pack", "keywords": ["pi-package"],
  "peerDependencies": { "@earendil-works/pi-coding-agent": "*" },
  "pi": { "extensions": ["./extensions"], "skills": ["./skills"], "prompts": ["./prompts"] } }
```
- 核心包放 `peerDependencies`（不要 bundle）；普通依赖放 `dependencies`
- 分发：`npm publish` 或 `git tag v1.0.0`
- 安装：`pi install npm:xxx` / `pi install git:github.com/user/repo`；`-l` 为项目级安装

## 五、起步路径（实操建议）
1. 复制官方 `hello.ts` 到 `~/.pi/agent/extensions/`，`/reload` 验证加载
2. 参照 `permission-gate.ts` 改一个自己的工具
3. 复杂功能读社区 `pi-mcp-adapter`（~250 行）与 `pi-subagents` 源码学模式
4. 发布前 `pi -e .` 本地测试，再 `npm publish`

## 六、工作开发推荐安装清单
### 第一档：必装（安全底线，Pi 默认 YOLO 全靠它们兜底）
- `permission-gate.ts`（官方）— 危险命令（rm -rf、sudo 等）执行前弹确认
- `protected-paths.ts`（官方）— 禁止写入 .env、.git/、node_modules/ 等敏感路径
- `dirty-repo-guard.ts`（官方）— 有未提交 Git 变更时阻止切换/清理会话，防丢代码
- `@vtstech/pi-security`（社区）— 命令/路径/SSRF 三合一综合防护，可顶替上面官方零散方案
- `sandbox/`（官方，可选但强烈建议）— OS 级沙箱，配合 Docker/VM 使用

### 第二档：强烈推荐（补齐开发工作流）
- `plan-mode/`（官方）— 只读探索 + /plan 计划模式，先规划再执行
- `subagent/`（官方）或 `pi-subagents`（社区更成熟）— 子 Agent 分解复杂任务
- `git-checkpoint.ts`（官方）— 每轮自动 stash 检查点，改坏了随时恢复
- `pi-mcp-adapter`（社区）— MCP 接入：数据库/浏览器/API 等外部工具
- `todo.ts`（官方）— 待办列表工具 + /todos 命令

### 第三档：按需选装
- `pi-marketplace` — 最先装它，之后在 Pi 内搜索/审计/安装其他包（带安全审查）
- `pi-web-access` — 网页搜索与内容抓取
- `@narumitw/pi-lsp` — LSP 诊断注入
- `pi-memory` / `@vtstech/pi-long-term-memory` — 跨会话持久记忆
- `status-line.ts` / `custom-footer.ts` — 状态栏（Git 分支、token 用量）
- `ssh.ts` — 远程服务器开发
- `qna.ts` — 把问题提取进编辑器方便追问

### 安装命令速记
```bash
# 官方 examples：复制到全局扩展目录（/reload 热加载）
cp .../permission-gate.ts ~/.pi/agent/extensions/
# 社区包：一行安装
pi install npm:pi-mcp-adapter
pi install npm:pi-marketplace
# 管理
pi list    # 查看已装
pi config  # 启停扩展/skill
```
> 提醒：扩展只是"闸门"，沙箱是"围墙"。即使装了全套安全扩展，也建议在 Docker/VM 沙箱里跑 pi 做开发。

## 关联连接
- [[PiAgent]] — 扩展所属的 Agent 框架实体
- [[Skill]] — 四层扩展系统最轻的一层
- [[Agent]] — 扩展能力的作用对象（循环管控）
- [[MCP]] — pi-mcp-adapter 接入的外部工具协议
- [[OpenCode]] — 同类可扩展 Agent 工具（对比参考）
- [[ContextEngineering]] — 扩展可定制的上下文压缩
- [[trace-turn]] — 扩展可拦截的生命周期事件背景