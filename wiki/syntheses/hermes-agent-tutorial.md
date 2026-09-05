---
title: "Hermes Agent 完整教程"
type: synthesis
tags: [AI, Agent, 教程, Hermes, 安装]
sources: [raw/09-archive/OpenClaw vs Hermes：万字深入讲解两大通用 Agent.md]
last_updated: 2026-06-08
---

# Hermes Agent 完整教程：安装、配置与使用

[[HermesAgent]] 是由 [[NousResearch]] 构建的开源自我进化 AI 智能体。它不是你关掉终端就失忆的聊天机器人——它有记忆、能学习、会沉淀经验。本文带你从零开始，30 分钟内完成安装到熟练使用。

## 一、Hermes Agent 是什么

Hermes Agent 是一个**通用 AI Agent 系统**，与 [[OpenClaw]] 属于同一大类，但工程重心完全不同：

| 维度 | Hermes Agent | OpenClaw |
|------|-------------|----------|
| 核心定位 | Self-improving AI agent | 本地优先个人 AI 助手 |
| 重心 | 学习型执行循环 | Gateway 控制面 |
| 技能体系 | 自动创建 + 自我改进 | 人工定义 + 治理加载 |
| 记忆系统 | SQLite + FTS5 + Honcho | 文件即记忆 |
| 安全 | 纵深防御（审批+隔离） | 信任模型 + 配置审计 |
| 技术栈 | Python 3.11 | Node.js / TypeScript |
| 渠道 | CLI + 6 个消息平台 | 25+ 渠道 + 设备节点 |
| 更适合 | 长期任务经验沉淀 | 多渠道个人助理 |

如果你的核心痛点是**Agent 每次任务都从零开始、不会积累经验**，Hermes 是最值得尝试的选择。

## 二、安装

### 前置条件

| 项目 | 要求 |
|------|------|
| 操作系统 | Linux / macOS / WSL2 / Android (Termux) |
| 内存 | 最低 4GB，推荐 8GB+ |
| 磁盘 | ~2GB 可用空间 |
| Git | 任意版本 |
| LLM 模型 | 至少 64K token 上下文窗口 |

> **Windows 用户**：推荐使用 WSL2。原生 Windows 支持处于早期测试版，可使用 PowerShell 安装。

### 一键安装

**Linux / macOS / WSL2：**

```bash
curl -fsSL https://hermes-agent.nousresearch.com/install.sh | bash
```

**Windows（原生，PowerShell 早期测试版）：**

```powershell
iex (irm https://hermes-agent.nousresearch.com/install.ps1)
```

安装程序自动处理：Python 3.11、Node.js、ripgrep、ffmpeg、仓库克隆、虚拟环境、全局 `hermes` 命令注册。

安装完成后重新加载 shell：

```bash
source ~/.bashrc   # 或 source ~/.zshrc
```

验证安装：

```bash
hermes --version
hermes doctor      # 运行诊断，确认环境完整
```

### 国内安装注意事项

如果直连 GitHub 超时，参考以下镜像方案：

**Git 镜像：**
```bash
git clone https://gitcode.com/GitHub_Trending/he/hermes-agent.git ~/.hermes/hermes-agent
```

**PyPI 镜像：**
```bash
export UV_INDEX_URL=https://mirrors.aliyun.com/pypi/simple/
```

**npm 镜像：**
```bash
npm config set registry https://registry.npmmirror.com
```

**Playwright 浏览器镜像：**
```bash
export PLAYWRIGHT_DOWNLOAD_HOST=https://npmmirror.com/mirrors/playwright
```

### 从 OpenClaw 迁移

如果你已有 OpenClaw 配置，首次运行 `hermes setup` 会自动检测并提示迁移。

```bash
hermes claw migrate              # 交互式迁移
hermes claw migrate --dry-run    # 预览迁移内容
hermes claw migrate --preset user-data   # 仅迁移用户数据（不含密钥）
```

## 三、配置模型提供商

安装完成后，最重要的步骤是配置 LLM 模型。

```bash
hermes model
```

交互式向导会引导你选择提供商。

### 推荐方案

| 方案 | 适合场景 | 配置方式 |
|------|---------|---------|
| **Nous Portal** | 新用户首选 | `hermes setup --portal`（OAuth 一键登录）|
| **OpenRouter** | 200+ 模型自由切换 | 粘贴 API Key |
| **Anthropic** | Claude 直连 | OAuth 或 API Key |
| **OpenAI** | GPT 系列 | API Key |
| **Ollama** | 本地免费离线 | 自定义端点 `http://127.0.0.1:11434/v1` |

> 模型要求：**至少 64K token 上下文窗口**。大多数云端模型（Claude、GPT、Gemini、Qwen、DeepSeek）都满足。

### 提供商容灾链

在 `~/.hermes/config.yaml` 中配置：

```yaml
fallback_providers:
  - provider: openrouter
    model: anthropic/claude-sonnet
  - provider: ollama
    model: gemma4
```

主提供商宕机时自动切换。

## 四、第一次对话

```bash
hermes            # 经典 CLI
hermes --tui      # 推荐：现代化 TUI 界面
```

启动后你会看到欢迎横幅，显示当前模型和可用工具。输入任何问题即可。

### 常用 CLI 命令

| 命令 | 功能 |
|------|------|
| `hermes` | 启动交互式 CLI |
| `hermes --continue` / `-c` | 恢复上次会话 |
| `hermes model` | 切换 LLM 提供商和模型 |
| `hermes tools` | 配置启用哪些工具 |
| `hermes config set` | 设置单个配置项 |
| `hermes doctor` | 诊断问题 |
| `hermes update` | 更新到最新版本 |

### 会话中斜杠命令

| 命令 | CLI | 消息网关 |
|------|-----|---------|
| 新对话 | `Ctrl+N` | `/new` |
| 重试 | `Ctrl+Z` | `/retry` |
| 撤销 | `Ctrl+Shift+Z` | `/undo` |
| 查看用量 | `/usage` | `/usage` |
| 浏览技能 | `Ctrl+S` | `/skills` |
| 中断 | `Ctrl+C` | `/stop` |

## 五、消息网关：连接聊天平台

Hermes 通过消息网关运行 Telegram、Discord、Slack、WhatsApp、Signal 等多个平台机器人。

### 配置网关

```bash
hermes gateway setup
```

交互式向导会引导你选择平台并输入凭证。

### Telegram 设置

1. 在 [@BotFather](https://t.me/BotFather) 创建机器人，获取 Token
2. 运行 `hermes gateway setup` 选择 Telegram
3. 粘贴 Bot Token
4. 可选：限制只有你的账号能访问（配置 `allowed_users`）

### 启动网关

```bash
hermes gateway           # 前台运行（测试用）
hermes gateway install   # 安装为持久服务（后台运行）
```

### 网关命令（消息平台通用）

| 命令 | 功能 |
|------|------|
| `/new` | 开始新对话 |
| `/model` | 切换模型 |
| `/retry` | 重试上一轮 |
| `/undo` | 撤销上一轮 |
| `/skills` | 浏览技能 |
| `/usage` | 查看用量 |
| `/stop` | 中断当前工作 |
| `/compress` | 压缩上下文 |

## 六、技能系统：Agent 的自学能力

Hermes 最独特的功能——**过程记忆**系统。Agent 完成复杂任务后，自动将成功路径沉淀为技能文档，下次做同类任务时直接复用。

### 技能自动创建

当你给 Agent 一个复杂任务时：
1. Agent 执行任务并记录关键步骤
2. 系统提示 Agent：是否应将此流程保存为技能？
3. Agent 创建 `SKILL.md` 文件，描述任务、步骤、工具调用和注意事项
4. 下次遇到类似任务，Agent 自动加载对应技能

### 技能管理

```bash
# 在会话中查看所有技能
/skills

# 手动创建/编辑技能
# 技能文件位于 ~/.hermes/skills/
```

技能预置 26 个类别：research、software-development、data-science、devops、mlops 等，兼容 agentskills.io 开放标准。

### 最佳实践

- 完成复杂任务后，检查 Agent 是否创建了技能
- 定期 review 技能文件，修剪过时或错误的内容
- 对高频重复任务，可以手动编写初始技能模板

## 七、记忆系统

Hermes 的记忆分三层：

| 层级 | 内容 | 特点 |
|------|------|------|
| 会话记忆 | 当前对话上下文 | 仅维持于当次会话 |
| 持久记忆 | 跨会话的事实和偏好 | 自动累积到 MEMORY.md + USER.md |
| 技能记忆 | 成功任务的解决方案模式 | SQLite + FTS5 全文检索，可搜索可复用 |

### 存储架构

- **SQLite + FTS5**：会话数据以 WAL 模式存储，支持全文检索
- **Honcho**：跨会话用户建模，构建长期用户画像
- **Source tag 过滤**：按来源（cli、telegram、discord 等）过滤搜索结果

## 八、Cron 定时任务

Hermes 内置 cron 调度器，可按任意时间表自动执行任务。

```bash
# 添加定时任务
hermes cron add "每天早上8点发送天气报告" "0 8 * * *"

# 列出任务
hermes cron list

# 删除任务
hermes cron remove <task_id>
```

任务结果可自动投递到已配置的任何平台（Telegram、Discord 等）。

## 九、MCP 集成

Hermes 支持 [[MCP]]（Model Context Protocol），可连接 GitHub、数据库、Stripe 等外部服务。

在 `~/.hermes/config.yaml` 中配置：

```yaml
mcp_servers:
  github:
    command: npx
    args: ["-y", "@modelcontextprotocol/server-github"]
    env:
      GITHUB_PERSONAL_ACCESS_TOKEN: "ghp_your_token"
  filesystem:
    command: npx
    args: ["-y", "@modelcontextprotocol/server-filesystem", "/home/user/projects"]
```

MCP 配置支持：工具过滤（include/exclude）、超时设置、连接超时、禁用 prompts/resources。

## 十、安全

Hermes 的安全体系采用**纵深防御**策略：

- **命令审批**：终端命令、文件写入等默认需人工确认，超时自动拒绝
- **容器隔离**：Docker / SSH / Daytona 等后端隔离执行环境
- **凭据过滤**：防止 API Key 等敏感信息泄露到上下文
- **注入扫描**：检测 Prompt 注入风险
- **NixOS 模式**：`ProtectSystem=strict` 命名空间隔离

## 十一、执行后端

Hermes 支持 6 种终端后端，可在 `config.yaml` 中切换：

```yaml
terminal.backend: docker   # Docker 隔离
terminal.backend: ssh        # 远程服务器执行
terminal.backend: local      # 本地直接执行
```

- **Local**：本机直接执行，性能最好
- **Docker**：容器隔离，安全性最高
- **SSH**：远程服务器执行
- **Daytona / Modal**：Serverless 按需启动，闲时几乎零成本
- **Singularity**：HPC 环境

## 十二、Windows 安全部署方案

在 Windows 上运行 Hermes 的正确分层隔离架构如下：

```
Windows 本机
  └─ WSL2（Hyper-V VM 隔离）
       ├─ Local 后端 → Hermes 在 WSL2 内直接运行
       │    ├─ 文件系统限制在 WSL2 ext4 分区
       │    └─ 可通过 /mnt/c 读写 Windows 文件（需注意）
       └─ Docker 后端（namespace 隔离）
            ├─ Playwright/Chromium 浏览器正常运作
            ├─ 无法访问 Windows 本机（除非显式挂载）
            └─ rm -rf / 只炸容器，不影响 WSL2 和 Windows
```

### 推荐方案：WSL2 + Docker 后端

1. **安装 WSL2**（如已安装可跳过）：
   ```powershell
   # PowerShell（管理员）
   wsl --install -d Ubuntu
   ```

2. **在 WSL2 中安装 Hermes**：
   ```bash
   curl -fsSL https://hermes-agent.nousresearch.com/install.sh | bash
   ```

3. **配置 Docker 后端**：
   ```yaml
   # ~/.hermes/config.yaml
   terminal:
     backend: docker
     docker_image: "nikolaik/python-nodejs:python3.11-nodejs20"
     docker_mount_cwd_to_workspace: false  # 不挂载宿主机目录
     container_persistent: true
   ```

Playwright/Chromium 在 Docker 容器内完全可用。Hermes 安装脚本会在容器镜像中预装浏览器依赖。唯一注意事项是共享内存大小：

```yaml
# ~/.hermes/config.yaml
terminal:
  backend: docker
  docker_extra_args:
    - "--shm-size=2g"  # 加大共享内存，防止 Chromium 崩溃
```

### 安全层级对比

| 部署方式 | 可损坏 Windows | 可损坏 WSL2 | 浏览器可用 | 推荐场景 |
|---------|:------------:|:----------:|:---------:|---------|
| 原生 Windows (local) | ✅ 可能 | N/A | ✅ | 快速试用（不推荐生产） |
| WSL2 (local) | ❌ VM 隔离 | ✅ 可能 | ✅ | 日常使用 |
| WSL2 + Docker | ❌ VM 隔离 | ❌ 容器隔离 | ✅ | **生产推荐** |
| WSL2 + Docker + 无 `/mnt` | ❌ 完全隔离 | ❌ 完全隔离 | ✅ | 最高安全 |

### /mnt/c 文件访问控制

WSL2 默认自动挂载 Windows 的 `C:\` 到 `/mnt/c`。如果担心 Hermes 通过 `/mnt/c` 触及 Windows 文件：

```bash
# 创建 /etc/wsl.conf 防止自动挂载
sudo tee /etc/wsl.conf << EOF
[automount]
enabled = false
EOF

# 重启 WSL2
wsl --shutdown
```

配合 Docker 后端后，容器内部默认不挂载 `/mnt/c`，即使 WSL2 有访问权限，容器内的 Agent 也接触不到。

### 浏览器操作的容器内安全

```yaml
# config.yaml
terminal:
  backend: docker
  docker_image: "nikolaik/python-nodejs:python3.11-nodejs20"
  # 浏览器在容器内运行 — 进程隔离 + 容器 namespace 隔离
  # 即使浏览器被利用，攻击面仅限于容器内
  docker_forward_env: []  # 不传环境变量到容器
  container_cpu: 1
  container_memory: 5120
```

浏览器操作流程：

```
用户请求"打开网页" → Docker 容器 → Playwright 启动 Chromium → 网页渲染在容器内
                                                                    ↓
                                                              结果(截图/HTML)返回
                                                                    ↓
                                                              容器销毁/重置 → 痕迹全清
```

### 总结

```bash
# Windows 安全部署三步走
# 1. 装 WSL2（VM 隔离）
wsl --install -d Ubuntu

# 2. 在 WSL2 里装 Hermes
curl -fsSL https://hermes-agent.nousresearch.com/install.sh | bash

# 3. 切 Docker 后端（容器隔离）
hermes config set terminal.backend docker
```

每一层隔离都独立运作，浏览器在 Docker 内容器正常工作，Windows 本机不受任何影响。

## 十三、常见问题

### "Model context too small" 错误

Hermes 要求模型至少 64K 上下文。本地模型需要显式设置：
```bash
ollama run gemma4 --ctx-size 65536
```

### `hermes: command not found`

重新加载 shell：`source ~/.bashrc`

### API key not set

运行 `hermes model` 重新配置提供商，或直接设置：
```bash
hermes config set OPENROUTER_API_KEY sk-or-xxx
```

### 网关无法连接

先运行 `hermes doctor` 诊断，再检查网络和 Token 配置。

### 国内网络问题

模型服务商选择参考：

| 提供商 | 国内直连 | 推荐度 |
|--------|---------|--------|
| DeepSeek | 直连，速度快 | 首选 |
| Kimi/Moonshot | 直连 | 推荐 |
| 阿里通义千问 | 直连 | 推荐 |
| MiniMax 国内 | 直连 | 推荐 |
| Anthropic/OpenAI | 需代理 | 有代理可用 |

## 十四、快速参考卡片

### 安装后第一件事

```bash
# 1. 配置模型
hermes setup --portal   # 推荐：Nous Portal 一键配置

# 2. 运行诊断
hermes doctor

# 3. 开始聊天
hermes --tui
```

### 日常命令速查

```bash
hermes                  # 启动聊天
hermes --continue       # 恢复上次会话
hermes model            # 切换模型
hermes gateway          # 启动消息网关
hermes cron add         # 添加定时任务
hermes update           # 升级版本
```

### 配置文件位置

- 主配置：`~/.hermes/config.yaml`
- 环境变量/密钥：`~/.hermes/.env`
- 技能目录：`~/.hermes/skills/`
- 会话存储：`~/.hermes/state/`（SQLite + FTS5）
- 持久记忆：`~/.hermes/MEMORY.md`、`~/.hermes/USER.md`

## 十五、总结

Hermes Agent 是 2026 年最值得关注的开源 AI Agent 之一。安装只需 60 秒，学习曲线平缓——从 CLI 对话开始，逐步添加消息网关、MCP 服务器和 cron 任务。其自我进化的技能系统意味着你的 Agent 会随着时间积累价值，而不是每个会话都从零开始。

> Hermes 更关心的问题是：**当它完成了一个复杂任务以后，这段经验会不会消失？下次做同类任务，它能不能少试错？**

上手路线图：

```
安装 → 配置模型 → 首次对话 → 网关（Telegram等） → 体验自动技能创建 → cron定时任务 → MCP扩展
```

## 关联连接

- [[HermesAgent]] — 实体页面
- [[NousResearch]] — 开发团队
- [[OpenClaw]] — 同类竞品对比
- [[MCP]] — 模型上下文协议
- [[Ollama]] — 本地模型运行
- [[Agent]] — AI Agent 核心概念
