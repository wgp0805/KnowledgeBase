---
title: "Junie 配置国产模型操作指南"
type: synthesis
tags: [Junie, JetBrains, ACP, IntelliJIDEA, 国产模型, GLM, Qwen, DeepSeek, Kimi]
sources: []
last_updated: 2026-07-08
---

# 在 [[IntelliJIDEA]] / [[Junie]] 中配置国产模型 Agent

## 前提：理解 ACP 机制

[[IntelliJIDEA]]（2026.1+）原生支持 ACP（Agent Client Protocol）。IDE 中「AI agents」选项即 ACP 注册表——选一个 agent，IDEA 通过 `command + args` 拉起它的进程，用 stdio 通信。**API Key 配在 agent 侧，不在 IDEA 侧。**

国产模型接入有两条路径：①直接选用注册表里的国产模型 agent（推荐）；②通过 [[Junie]] 自身 BYOK 走 OpenRouter 中转。

## 方式 A：Qwen Code（推荐，最省事）

[[Qwen]] Code 自带 model provider 选择菜单，首次启动即可选国产模型，且官方有 [[IntelliJIDEA]] 集成文档。

**第 1 步：装 CLI**
```powershell
npm install -g @qwen-code/qwen-code
# 或官方安装器
irm https://qwen-code-assets.oss-cn-hangzhou.aliyuncs.com/installation/install-qwen-standalone.ps1 | iex
```

**第 2 步：在 IDEA 中接入**
1. 打开右侧 **AI Chat** 工具窗口
2. 点 **Add ACP Agent** → **Install**（选 Qwen Code）
   - 若已有别的 agent：在 Agents List 点 **Install From ACP Registry** → 选 Qwen Code
3. Qwen Code 出现在 AI Assistant 面板

**第 3 步：选模型（关键）**
首次在终端跑一次 `qwen`，弹出 provider 菜单：
- **Alibaba ModelStudio** → Coding Plan / Token Plan / Standard API Key（填阿里云 DashScope key）
- **Third-party Providers** → 内置 **DeepSeek、MiniMax、Z.AI（智谱 [[GLM]]）**、OpenRouter，填对应 API Key
- **Custom Provider** → 填本地 / 代理 / 任意 OpenAI 兼容端点

选完写入磁盘，IDEA 里的 Qwen Code agent 直接复用该配置。

## 方式 B：GLM Agent（智谱，纯 GLM Coding Plan）

**第 1 步：获取 API Key**
访问 https://z.ai/manage-apikey/apikey-list → 注册 → 创建 key

**第 2 步：装 agent**
```powershell
npm install -g glm-acp-agent@latest
```

**第 3 步：配置 Key**（二选一）
```powershell
# 方式一：交互式写入磁盘（推荐，永久生效）
glm-acp-agent --setup
# 方式二：环境变量
$env:Z_AI_API_KEY="你的key"
```
Key 写入 `~/.config/glm-acp-agent/credentials.json`（0600 权限）；环境变量优先级高于文件。

**第 4 步：在 IDEA 接入**
AI Chat → Add ACP Agent → 选 GLM Agent；或手动 **Configure ACP Agent**（AI Chat 右上角三点菜单）：
```json
{
  "agent_servers": {
    "glm": {
      "command": "glm-acp-agent",
      "env": { "Z_AI_API_KEY": "sk-..." }
    }
  }
}
```
可用模型：glm-5.1（默认）/ 5-turbo / 5v-turbo（多模态）/ 4.7 / 4.5-air。注意 GLM Agent 专为 Z.AI Coding Plan 设计，非通用开放平台 API 客户端。

## 方式 C：手动 Configure ACP Agent（接任意国产模型）

任意 ACP agent 都能通过 **Configure ACP Agent** 手动配。只要该 agent 支持 OpenAI 兼容 base URL，就能填国产模型端点。模板：
```json
{
  "agent_servers": {
    "my-agent": {
      "command": "qwen",
      "args": ["--acp"],
      "env": {}
    }
  }
}
```

## 其他内置国产 agent（注册表已收录，直接 Install）

| Agent | 厂商 | 装法 |
|-------|------|------|
| Kimi CLI | [[Kimi]] 月之暗面 | `npm i -g` 或下二进制，需 Moonshot API Key |
| Codebuddy Code | 腾讯云 | `npx @tencent-ai/codebuddy-code --acp` |

## 路径 ②：Junie 自身 BYOK（中转方案）

[[Junie]] BYOK 明确支持的 provider = Anthropic / OpenAI / Google / xAI / OpenRouter / Copilot，未直接列国产模型。变通：
- **走 OpenRouter 中转**：OpenRouter 聚合了 DeepSeek / [[Qwen]] / [[GLM]] 等，配一个 OpenRouter key 即可曲线使用
- 若 Junie 的 OpenAI provider 支持自定义 base URL，可填国产模型的 OpenAI 兼容端点（需在 Junie 认证页确认是否开放 base URL 字段）

## 选型建议

- 最省事：**装 Qwen Code → IDEA 里 Install → 首次选 DeepSeek/Z.AI**，全程不用碰 JSON
- 想用智谱 GLM：**GLM Agent + Z.AI Coding Plan Key**
- 已有 Junie 订阅想用国产模型：**OpenRouter 中转**

## 关联连接
- [[Junie]] — JetBrains AI coding agent
- [[IntelliJIDEA]] — IDE 集成宿主
- [[GLM]] — 智谱国产模型
- [[Qwen]] — 阿里通义国产模型
- [[Kimi]] — 月之暗面国产模型
- [[DeepSeek]] — DeepSeek 模型（Qwen Code 内置支持）
