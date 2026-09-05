---
title: "Hooks"
type: concept
tags: [Agent扩展, 自动化, 防护机制, 生命周期事件]
sources: [raw/01-articles/Anthropic 工程师总结的 9 条血泪经验.md, raw/01-articles/2026-08-28 - 面试官坏笑：“你都用ClaudeCode写代码半年了，怎么保证它不会执行危险命令？”，我：“CLAUDE.md”，面试官：“回去等通知吧！”.md]
last_updated: 2026-08-28
---

## 定义

Claude Code 的 Hooks 是一种**生命周期事件驱动的自动触发机制**：在会话开始、用户提交 Prompt、工具调用前后、权限决定、响应停止、上下文压缩等关键节点上，自动执行预先配置的 handler（脚本/HTTP/MCP/模型判断/subagent），用于把格式化、危险命令拦截、权限审计、通知等固定动作变成可审计、可阻断的硬约束。

**与 Prompt 约束的本质差异**：Prompt 提醒依赖上下文和模型记忆，无法保证每次生效；Hooks 是工作流里的"固定卡点"，通过自动触发、脚本审计和风险阻断保证动作发生，作用近似于 pre-commit / CI / lint-staged / CODEOWNERS / branch protection。

## 关键信息

### 配置位置（三个常用 settings 文件）

| 位置 | 作用范围 | 适合放什么 |
| --- | --- | --- |
| `~/.claude/settings.json` | 当前用户所有项目 | 个人通知、个人习惯 |
| `.claude/settings.json` | 当前项目，可提交仓库 | 团队共享规则、项目级安全限制 |
| `.claude/settings.local.json` | 当前项目本机私有 | 不适合提交的个人配置 |

官方还支持 managed policy、插件的 `hooks/hooks.json`，以及 skill 或 agent frontmatter 里的 hooks。

### 五类 Handler

| 类型 | 做什么 | 适合场景 |
| --- | --- | --- |
| `command` | 执行 shell command | 格式化、日志、安全拦截、通知 |
| `http` | 把事件 JSON POST 到一个 URL | 团队审计服务、远程通知、集中化策略 |
| `mcp_tool` | 调用已连接 MCP server 上的工具 | 复用现有 MCP 能力 |
| `prompt` | 用一次模型判断返回 yes/no 风格 JSON | 轻量判断，如 Stop 前检查任务是否完成 |
| `agent` | 启动带工具访问能力的 subagent 做验证 | 需要读文件、搜代码、跑命令的验证（experimental） |

**handler 与事件的兼容性**：
- `PreToolUse`、`PostToolUse`、`PermissionRequest`、`Stop` 等事件支持全部五种 handler
- `Notification`、`PreCompact`、`ConfigChange` 等事件不支持 `prompt` 和 `agent`
- `SessionStart`、`Setup` 只支持 `command` 和 `mcp_tool`

**选型原则**：能写成确定脚本的规则优先交给 `command`（可独立调试、易纳入代码审查）；结果需要进入团队服务用 `http`；已有可用 MCP 工具再选 `mcp_tool`；只有语义判断无法写成确定规则时才引入 `prompt` 或 `agent`。

### 常用生命周期事件

| 事件 | 触发时机 | 适合做什么 |
| --- | --- | --- |
| `SessionStart` | 会话开始或恢复时 | 注入动态上下文、加载环境、压缩后补规则 |
| `UserPromptSubmit` | 用户提交 Prompt 后，Claude 处理前 | Prompt 审计、轻量拦截、补动态上下文 |
| `PreToolUse` | 工具调用执行前 | 拦危险命令、保护敏感文件、修改工具输入 |
| `PermissionRequest` | 工具调用需要权限决定时 | 审计权限，或非常窄地自动批准 |
| `PostToolUse` | 工具调用成功后 | 格式化、记录日志、lint、补充上下文 |
| `Notification` | Claude Code 发送通知时 | 桌面通知、手机推送 |
| `Stop` | Claude 完成一轮响应时 | 完成通知、质量门禁、提醒继续处理 |
| `PreCompact` | 上下文压缩前 | 备份状态、阻止不合适的压缩 |
| `PostCompact` | 上下文压缩后 | 记录摘要、同步外部状态 |

进阶事件还包括：`Setup`、`InstructionsLoaded`、`ConfigChange`、`CwdChanged`、`FileChanged`、`SessionEnd`、`SubagentStart`、`SubagentStop`、`TaskCreated`、`TaskCompleted`、`WorktreeCreate`、`WorktreeRemove`、`Elicitation`、`ElicitationResult`、`StopFailure` 等。

### 输入输出契约

- **输入**：事件上下文以 JSON 传入（`command` 走 stdin，`http` 作为 POST body）。公共字段：`session_id`、`transcript_path`、`cwd`、`permission_mode`、`hook_event_name`；工具事件还带 `tool_name` 和 `tool_input`。建议用 `jq` 解析。
- **退出码**：
  - `exit 0` + stdout 是符合 schema 的 JSON → 按字段处理决策（如 `allow`/`deny`/`ask`/`defer`）
  - `exit 2` → 阻断工具调用（多数事件），但 `PermissionRequest` 不接受 `exit 2`，必须通过 `decision` 对象返回
  - `exit 1` → **最容易踩的坑**：stdout 为空/普通文本/JSON 校验失败时，对多数事件只是非阻断错误，流程会继续
- **stdout 纪律**：要返回 JSON 时 stdout 只放 JSON，调试信息写 stderr 或日志文件，否则容易遇到 `JSON validation failed`。

### 多 Hook 并行与合并

同一事件下多个 Hook 命中时并行执行，全部跑完再合并结果：
- 一个 Hook 返回 deny 不会阻止旁边 Hook 写日志/发 HTTP/改文件
- `PreToolUse` 多决策合并时采用**更严格**的结果
- 多个 Hook 同时改同一个工具输入时，最后生效的是最后完成的那个（不稳定，应避免）
- `command` Hook 以当前用户权限运行 shell，能访问/修改/删除用户有权限的文件，接入第三方脚本前必须先看懂并单独测试

### 三个最小可用示例（推荐接入顺序）

**1. Notification（低风险，先配）** — Claude 需要授权时弹通知：
```json
{
  "hooks": {
    "Notification": [
      { "matcher": "permission_prompt",
        "hooks": [{ "type": "command",
          "command": "osascript -e 'display notification \"Claude Code needs your attention\" with title \"Claude Code\"'" }] }
    ]
  }
}
```

**2. PostToolUse（自动化收益）** — 改完文件自动格式化：
```json
{
  "hooks": {
    "PostToolUse": [
      { "matcher": "Edit|Write",
        "hooks": [{ "type": "command",
          "command": "jq -r '.tool_input.file_path' | xargs npx prettier --write" }] }
    ]
  }
}
```
Java 项目应换成 `spotlessApply`/`google-java-format`，Python 用 `ruff format`，贴着项目现有工具走。

**3. PreToolUse（安全底线）** — 拦截危险命令和敏感文件（`.claude/hooks/guard.sh`）：
```bash
#!/usr/bin/env bash
set -euo pipefail
input="$(cat)"
tool="$(jq -r '.tool_name // empty' <<<"$input")"
command="$(jq -r '.tool_input.command // empty' <<<"$input")"
file="$(jq -r '.tool_input.file_path // empty' <<<"$input")"

if [[ "$tool" == "Bash" ]] && [[ "$command" =~ rm[[:space:]]+-rf|chmod[[:space:]]+-R[[:space:]]+777 ]]; then
  echo "Blocked risky shell command: $command" >&2
  exit 2
fi

if [[ "$tool" == "Edit" || "$tool" == "Write" ]]; then
  case "$file" in
    *.env|*.env.*|*/.env|*/.git/*|*id_rsa*|*id_ed25519*)
      echo "Blocked sensitive file edit: $file" >&2
      exit 2 ;;
  esac
fi
exit 0
```

### 排查清单

Hook 没生效时按以下顺序排查：
1. 运行 `/hooks` 确认配置已加载并挂在预期事件上
2. 把脚本从 Claude Code 拿出来单独运行（用 `printf` 喂 JSON 测试退出码）
3. 记录 Claude Code 实际传入的事件数据到 stderr/日志文件（排查后删除，勿提交）
4. 一次只启用一个 Hook（多 Hook 并行时只看最终表现难定位）

常见症状对照：`/hooks` 看不到 → 检查 settings 位置和 JSON 格式；已注册不触发 → 检查事件和 matcher；脚本报错但工具仍继续 → 是否误用 `exit 1` 或拦截未放 `PreToolUse`；Claude 不停继续 → `Stop` Hook 缺退出条件；每次都跑 formatter → matcher 省略或太宽；`claude -p` 异常 → 不要依赖 `PermissionRequest`，改用 `PreToolUse`。

### 安全边界

- 命令黑名单只能识别已写进去的形式，`/bin/rm`、`find -delete` 等变体可能绕过
- 高风险操作应同时结合：路径限制 + 权限配置 + Hooks + Sandbox + CI + 人工 Review
- `PermissionRequest` 自动批准必须收窄 matcher 和输入条件，避免全局放行；删除文件、操作生产、读取凭证、外部 API 写数据继续交人确认
- `Stop` Hook 必须写好退出条件，否则来回重复（连续阻断 8 次后 Claude Code 强制结束本轮）

## 知识冲突（历史记录）

> 2026-05-28 旧版 [[摘要-anthropic-engineer-skills]] 曾将 Hooks 描述为「只在 Skill 被调用时生效、会话结束就消失」的 Skill 内嵌机制。
> 2026-08-28 经 [[摘要-claude-code-hooks-防危险命令]] 基于 Claude Code 官方文档 Hooks reference 核实，该描述不准确：Hooks 是生命周期事件驱动的独立机制，与 Skill 是并列概念。
> 经用户决策，已用新知识覆盖旧描述，旧来源保留作为历史参考。

## Hooks 与 Skills 的分工

| 维度 | Hooks | Skills |
| --- | --- | --- |
| 触发方式 | 生命周期事件自动触发 | Claude 判断相关时加载，或用户手动 `/skill-name` |
| 核心价值 | 让固定动作稳定发生 | 给 Claude 增加某类能力或流程知识 |
| 适合场景 | 格式化、危险命令拦截、权限审计、通知、日志、质量门禁 | 代码审查流程、部署 SOP、故障排查、资料检索、复杂任务 |
| 对模型判断的依赖 | 低（尤其 `command`） | 更高，Claude 需理解并执行 skill 指令 |
| 是否适合阻断 | 适合（`PreToolUse`/`UserPromptSubmit`/`Stop`） | 不适合作为硬拦截 |
| 常见风险 | matcher 太宽、脚本慢、自动批准过度 | 描述不清、触发不准、流程太长 |

两者可接在同一条工作流上：**Skill 规定代码审查要检查什么，Hook 负责在文件修改后运行 formatter、在危险命令执行前拦截、在响应结束前检查是否留下测试结果。**

## 关联连接
- [[ClaudeCode]] — Hooks 的运行平台
- [[Skill]] — 与 Hooks 并列的扩展机制
- [[摘要-claude-code-hooks-防危险命令]] — 来源（程序汪基于官方文档的实战教程）
- [[摘要-anthropic-engineer-skills]] — 历史来源（已被新知识覆盖）
- [[CLAUDEmd]] — Prompt 约束的载体，与 Hooks 形成软约束 vs 硬约束对比
- [[PreToolUse]] — 工具执行前事件（安全拦截核心）
- [[PostToolUse]] — 工具执行后事件（格式化收尾）
- [[PermissionRequest]] — 权限决定事件
- [[SessionStart]] — 会话开始事件
- [[Stop]] — 响应停止事件
- [[PreCompact]] — 上下文压缩前事件
