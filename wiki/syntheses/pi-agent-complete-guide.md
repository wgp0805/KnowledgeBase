---
title: "Pi Agent 完全教程"
type: synthesis
tags: [pi-agent, 教程, Agent, 终端工具]
sources: []
last_updated: 2026-08-05
---

# Pi Agent 完全教程

## 一、概述与设计理念
Pi（pi-coding-agent，GitHub 70K+ Star，MIT 协议）是 Mario Zechner（badlogic）主导、后被 Earendil Inc.（Flask 作者 Armin Ronacher 的公司）收购的**极简终端 AI 编码 Harness**。

核心设计哲学与 Claude Code / Codex 完全相反：
- **系统提示词 <1000 Token**（Claude Code 约 14000），把上下文窗口留给代码和对话
- **默认仅 4 个核心工具**：`read` / `write` / `edit` / `bash`（另有 grep/find/ls 只读工具可启用）
- **不做功能，只给原语**：无内置 MCP、子 Agent、计划模式、权限弹窗——需要就自己用扩展装
- **完全透明**：每个工具调用、每次文件读写都实时展示，无黑箱
- **模型无关**：15+ 供应商任意切换，不锁死任何一家
- **核心仅 418 行 TypeScript**，通过 jiti 动态加载扩展（TS 免编译）

> 设计前提：前沿模型经过大量 RL 训练已理解"什么是编码代理"，harness 越轻越好，不需要过度指导模型。

相关背景见 [[PiAgent]]、[[摘要-pi-agent-core-principles]]。

## 二、环境要求与安装
- **Node.js >= 22.19.0**（低于此版本安装会报 EBADENGINE，且 `pi update` 会出现静默失败/卡死）
- 跨平台：Windows / macOS / Linux

```bash
# 推荐：npm 全局安装
npm install -g --ignore-scripts @earendil-works/pi-coding-agent

# Linux/macOS 一键安装器
curl -fsSL https://pi.dev/install.sh | sh

# 卸载
npm uninstall -g @earendil-works/pi-coding-agent
```

> 注意：`--ignore-scripts` 用于禁用依赖生命周期脚本，Pi 正常安装不需要 install 脚本。
> 旧版本包名为 `@mariozechner/pi-coding-agent`，现已迁移至 `@earendil-works` 作用域。

## 三、认证（两种方式）
在项目目录运行 `pi` 启动，然后：

**方式一：订阅登录（OAuth）**
```
/login
```
内置订阅登录支持：Claude Pro/Max、ChatGPT Plus/Pro（Codex）、GitHub Copilot、Google Gemini CLI 等。

**方式二：API Key**
```bash
# 启动前设环境变量
export ANTHROPIC_API_KEY=sk-ant-...
pi

# 或 /login 后选择 API-key Provider，key 存入 ~/.pi/agent/auth.json
```
凭据解析优先级：CLI `--api-key` 参数 > `auth.json` > 环境变量 > `models.json` 自定义 Provider key。

## 四、第一次会话
```bash
cd /path/to/project
pi
# 输入：Summarize this repository and tell me how to run its checks.
```
Pi 在**当前工作目录**运行，可以读写文件、执行命令。建议在 Git 管理的项目里使用（Git 是最简单的安全网）。

**文件引用与命令执行（编辑器内）：**
```
@README.md "Summarize this"     # @ 模糊搜索文件并作为上下文
!npm run lint                   # 执行命令，输出进入模型上下文
!!npm run lint                  # 执行命令，但输出不进上下文
```

## 五、项目上下文文件（AGENTS.md 体系）
Pi 启动时分层加载上下文文件（修改后 `/reload` 生效）：

| 文件 | 位置 | 作用 |
| --- | --- | --- |
| `AGENTS.md` | 项目根目录 + 父目录逐级向上 + `~/.pi/agent/AGENTS.md` | 项目规范/命令/安全规则，注入 system prompt |
| `CLAUDE.md` | 同上 | 兼容 Claude Code 的项目文件，同样加载 |
| `SYSTEM.md` | `.pi/SYSTEM.md`（项目）/ `~/.pi/agent/SYSTEM.md`（全局） | **整份替换**默认系统提示词 |
| `APPEND_SYSTEM.md` | `.pi/` 或 `~/.pi/agent/` | 追加到系统提示词末尾，优先级高于 AGENTS.md |

AGENTS.md 写法建议（对应 [[CLAUDEmd]] 方法论）：
```markdown
# Project Instructions
## 技术栈
- TypeScript + Node.js 22，pnpm 管理依赖，vitest 测试
## 测试命令
- 全部测试：pnpm test
- 类型检查：pnpm typecheck
## 红线规则
- 禁止提交 .env 文件
- 不要运行生产环境迁移
```

**项目信任机制**：Pi 启动时若发现项目含 `.pi/settings.json` / `.pi` 资源 / 项目级 skills，会询问是否信任（写入 `~/.pi/agent/trust.json`）。信任后才会加载项目级设置与扩展。非交互模式用 `--approve`/`-a` 或 `--no-approve`/`-na` 控制。

## 六、配置文件体系
| 文件 | 位置 | 用途 |
| --- | --- | --- |
| `settings.json` | `~/.pi/agent/`（全局）/ `.pi/`（项目） | 模型、主题、压缩策略、重试等运行参数 |
| `models.json` | `~/.pi/agent/` | 自定义模型与 Provider（Ollama/vLLM/OpenAI 兼容等） |
| `auth.json` | `~/.pi/agent/` | API Key 与 OAuth 凭据（权限 0600） |
| `keybindings.json` | `~/.pi/agent/` | 自定义快捷键 |
| `sessions/` | `~/.pi/agent/` | 会话存储（树状分支） |

**settings.json 全局示例：**
```json
{
  "defaultProvider": "deepseek",
  "defaultModel": "deepseek-v4-pro",
  "defaultThinkingLevel": "high",
  "enabledModels": ["deepseek-*", "claude-sonnet-4-*", "kimi-k3*"],
  "theme": "dark",
  "compaction": { "enabled": true, "reserveTokens": 16384, "keepRecentTokens": 20000 },
  "retry": { "enabled": true, "maxRetries": 3, "baseDelayMs": 2000 }
}
```
- 项目 `.pi/settings.json` **覆盖**全局，嵌套对象合并而非整体替换
- `enabledModels` 定义 Ctrl+P 轮换的模型列表，支持通配符，务必设置否则切换体验差
- `thinkingBudgets` 可配置各级思考深度对应的 token 预算

**models.json 接入本地模型：**
```json
{
  "provider": { "ollama": {
    "baseUrl": "http://localhost:11434/v1",
    "api": "openai-completions",
    "apiKey": "ollama", "models": ["qwen3-coder"] } }
}
```
支持 Ollama / LM Studio / vLLM / OpenRouter 及任意 OpenAI/Anthropic/Google 兼容端点。

**auth.json 的三种取值方式：** 字面量 / 环境变量插值（`"$MY_KEY"`）/ shell 命令（`"!security find-generic-password -ws 'anthropic'"`，可从系统钥匙串读取避免明文）。

## 七、TUI 界面布局
- **Startup header** — 快捷键、已加载的上下文文件/模板/Skill/扩展
- **Messages** — 用户消息、助手响应、工具调用、工具结果、通知、扩展 UI
- **Editor** — 输入区；**边框颜色表示当前 thinking level**
- **Footer** — 工作目录、会话名、token/cache 用量、费用、上下文占用、当前模型

## 八、常用斜杠命令
| 命令 | 说明 |
| --- | --- |
| `/login` `/logout` | 管理 OAuth / API-key 凭据 |
| `/model` | 切换模型 |
| `/scoped-models` | 配置 Ctrl+P 轮换的模型 |
| `/settings` | 思考级别、主题、消息传递、传输方式 |
| `/resume` | 从之前会话选择 |
| `/new` | 开始新会话 |
| `/name <名>` | 设置会话显示名 |
| `/session` | 显示会话文件/ID/消息/token/费用 |
| `/tree` | 跳到会话任意位置继续（树状导航） |
| `/fork` | 基于某条历史用户消息创建新会话 |
| `/clone` | 复制当前活动分支到新会话 |
| `/compact [prompt]` | 手动上下文压缩，可带自定义指令 |
| `/copy` | 复制上一条助手消息 |
| `/export [file]` | 导出会话为 HTML/JSONL |
| `/import <file>` | 导入 JSONL 会话 |
| `/share` | 上传为私有 GitHub gist 并生成分享链接 |
| `/trust` | 保存项目信任决定 |
| `/reload` | 重载键位/扩展/Skill/提示词/上下文文件 |
| `/hotkeys` | 显示所有快捷键 |
| `/quit` | 退出 |

## 九、键盘快捷键
| 操作 | 快捷键 |
| --- | --- |
| 打开模型选择器 | `Ctrl+L` 或 `/model` |
| 轮换模型（enabledModels） | `Ctrl+P` / `Shift+Ctrl+P` |
| 切换思考级别 | `Shift+Tab` |
| 中断当前操作 | `Escape` |
| 转向消息（打断并立即响应） | `Enter` |
| 排队消息（完成后追加） | `Alt+Enter` |
| 退出 | `Ctrl+C`（按两次） |

## 十、模型切换与思考级别
- 思考级别：`off` / `minimal` / `low` / `medium` / `high` / `xhigh` / `max`
- 策略建议：深度分析用强推理模型 + xhigh；日常轻量任务用 Flash 档模型省钱；长上下文场景用 Kimi 类大窗口模型
- 支持**对话中途切换模型**，thinking block 自动转换

## 十一、会话管理
- 所有会话以**树状分支**存储（单个文件），可用 `/tree` 跳转任意历史节点继续，`/fork` 从历史消息分叉
- `/session` 查看 token/费用，`/compact` 手动压缩，`/export`/`/share` 分享
- 启动参数：`pi -c`（继续最近会话）、`pi -r`（浏览历史会话）、`pi --name "任务名"`、`pi --session <path|id>`

## 十二、上下文压缩
- 默认自动压缩（settings 可配 reserveTokens / keepRecentTokens）
- `/compact [prompt]` 手动触发，可指定自定义压缩指令
- 压缩策略可通过扩展自定义（按主题/按代码感知/换总结模型）

## 十三、核心扩展体系（四层）
详见 [[pi-扩展生态与开发指南]]，此处给速查：

| 层 | 形态 | 定位 |
| --- | --- | --- |
| Skill | `SKILL.md` Markdown | 按需投喂的工作流能力包 |
| Prompt Template | `*.md` | 把常用 prompt 变成 `/name` 命令 |
| Extension | TypeScript 模块 | 注册工具/拦事件/画 UI/做 RPC |
| Package | npm/git 包 | 打包上面三层分发共享 |

### Skills 规范（Agent Skills 标准）
```
my-skill/
├── SKILL.md              # 必需：frontmatter + 指令
├── scripts/              # 辅助脚本
├── references/           # 按需加载的详细文档
└── assets/
```
frontmatter 字段：`name`（必需，小写字母数字连字符，≤64 字符）、`description`（必需，≤1024）、`license`、`compatibility`、`metadata`、`allowed-tools`（实验性）、`disable-model-invocation`。

加载位置：`~/.pi/agent/skills/`、`~/.agents/skills/`、项目 `.pi/skills/`、`.agents/skills/`（向上到 git 根）、包内 skills/。**渐进式披露**：system prompt 只注入名称与描述，完整指令按需 read。可通过 `/skill:name` 强制加载。
**兼容性**：可在 settings.json 里加 `"skills": ["~/.claude/skills", "~/.codex/skills"]` 直接复用 Claude Code / Codex 的 Skills。

### Extensions 规范
- 入口：`export default function (pi: ExtensionAPI) {...}`（可 async）
- 放置：`~/.pi/agent/extensions/`（全局）/ `.pi/extensions/`（项目）/ `pi -e ./x.ts`（临时测试）
- API：`pi.registerTool()`、`pi.on()`、`pi.registerCommand()`、`pi.registerShortcut()`、`pi.registerFlag()`、`pi.sendMessage()`、`pi.registerProvider()`
- 交互：`ctx.ui.select/confirm/input/notify/setStatus/setWidget/custom`
- 参数用 TypeBox Schema，字符串枚举用 `StringEnum`（Google API 兼容必需）
- 状态持久化：工具 `details` 字段 + `pi.appendEntry()`

## 十四、非交互模式（自动化）
| 模式 | 命令 | 场景 |
| --- | --- | --- |
| Interactive | `pi` | 日常 TUI |
| Print | `pi -p "query"` | 脚本集成，输出纯文本 |
| JSON | `pi --mode json "..."` | 结构化事件流，管道处理 |
| RPC | `pi --mode rpc` | JSON over stdin/stdout，嵌入其他应用 |
| SDK | `createAgentSession()` | 直接嵌入 Node.js 应用 |

SDK 核心：`createAgentSession({ cwd, agentDir, model, thinkingLevel, tools, customTools, resourceLoader })` + `SettingsManager.create()` / `SessionManager.inMemory()`。OpenClaw 即基于此集成。

## 十五、安全与沙箱
- **默认 YOLO 模式**：无权限确认弹窗，`rm -rf` 说干就干。必须配合：
  1. 安全扩展：permission-gate、protected-paths、dirty-repo-guard（见 [[pi-扩展生态与开发指南]]）
  2. 沙箱：官方 `sandbox/`（@anthropic-ai/sandbox-runtime）、Docker、VM、Gondolin 微 VM、OpenShell
- **项目信任**机制（见第五节）隔离未信任项目的资源
- 第三方 Package 以完整系统权限运行，安装前务必审源码

## 十六、CLI 参考速查
```bash
pi [options] [@files...] [messages...]
# 模型：--provider、--model、--api-key、--thinking、--models（Ctrl+P 列表）、--list-models
# 资源：-e/--extension、--skill、--prompt-template、--theme（均可重复）、--no-* 禁用
# 其他：--system-prompt、--append-system-prompt、--ui-mode、-a/--approve、-na/--no-approve
# 包：pi install/remove/list/update/config
```

## 十七、工程化最佳实践（结合知识库）
- **先写 AGENTS.md**：技术栈、测试命令、红线规则（对应 [[CLAUDEmd]] 与 [[摘要-ai大模型学习路线]]）
- **计划先行**：装 plan-mode 扩展，先输出实现计划再动手
- **小步提交**：git-checkpoint 扩展，每轮自动检查点可回滚
- **多模型分工**：强推理切 Claude、长上下文切 Kimi、轻量用 DeepSeek 省钱
- **上下文治理**：定期 `/compact`，配置 compaction 策略（对应 [[ContextEngineering]]）
- **安全三件套**：permission-gate + protected-paths + 沙箱（扩展是闸门，沙箱是围墙）
- **团队共享**：项目级 `.pi/` 配置提交到仓库，Skills 放共享目录
- 完整扩展安装清单见 [[pi-扩展生态与开发指南]] 第六节

## 十八、常见坑
1. Node 版本 < 22.19 导致安装/更新异常 → 升级 Node
2. 默认无权限控制 → 务必装安全扩展 + 沙箱
3. 无 plan/subagent/MCP → 别裸用，先装扩展补齐
4. `enabledModels` 不设置 → Ctrl+P 轮换遍历所有模型体验差
5. 改完 AGENTS.md 忘记 `/reload` → 新规则不生效
6. 上下文文件修改后需重启或 /reload
7. 第三方包安全风险 → 审源码再用

## 关联连接
- [[PiAgent]] — 核心实体与原理
- [[摘要-pi-agent-core-principles]] — Agent = 大模型 + 工具集 + 执行循环
- [[摘要-pi-agent-production-guide]] — 生产落地三大工程难题
- [[pi-扩展生态与开发指南]] — 扩展体系与工作开发推荐清单
- [[CLAUDEmd]] — AGENTS.md 写作方法论
- [[ContextEngineering]] — 上下文压缩策略
- [[trace-turn]] — Trace/Turn 术语与生命周期钩子
- [[error-feedback-self-healing]] — 错误自愈机制
- [[Agent]] — Agent 核心概念
- [[MCP]] — 外部工具协议（pi-mcp-adapter）
- [[OpenCode]] — 同类成熟可扩展 Agent 工具（对比参考）
- [[ClaudeCode]] — 对标产品