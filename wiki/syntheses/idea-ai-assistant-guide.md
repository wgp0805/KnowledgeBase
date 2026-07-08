---
title: "IntelliJ IDEA AI Assistant 能力全貌与配置指南"
type: synthesis
tags: [IntelliJIDEA, Junie, ACP, AIAssistant, 代码补全, JetBrains]
sources: []
last_updated: 2026-07-08
---

# [[IntelliJIDEA]] AI Assistant 能力全貌与配置指南

## 一、能力概览：两套独立机制

[[IntelliJIDEA]] 的 AI 生态分两大块，二者互不干扰：

1. **AI Chat / Agent mode** —— 多步任务（修 bug、实现功能、重构、审查 PR、写测试），走 [[ACP]]
2. **代码补全 inline completion** —— 单行/多行提示，走 JetBrains AI 服务或第三方插件

## 二、AI Chat / Agent mode（走 ACP）

由 [[Junie]]（JetBrains 出品的 AI coding agent）驱动，LLM 无关，可自带模型也可用 JetBrains 账号 [[Junie]]。

### 三条运行通道 [[Junie]]
- **终端 CLI**：独立 `junie` 命令，交互式输入任务
- **IDE 内集成**：IDEA 等 JetBrains IDE 的 AI Assistant agent mode
- **CI/CD pipeline**：通过 GitHub Action 自动响应 issue / PR / CI 失败

### ACP 机制本质
[[IntelliJIDEA]]（2026.1+）原生支持 ACP（Agent Client Protocol）。IDE 中「AI agents」选项即 ACP 注册表，IDEA 通过 `command + args` 拉起本地进程（通常即 CLI 工具），用 **stdio** 与之通信，**API Key 配在 agent 侧而非 IDEA 侧** [[junie-国产模型配置指南]]。

严格说 ACP 是"用 stdio 对话的进程协议"，agent 不一定非得是 CLI——任何能用 `command + args` 拉起、走 stdio 的程序都行，但实际注册表里都是 CLI 工具。

### 配置国产模型 agent
详见 [[junie-国产模型配置指南]]，三种方式：
- **方式 A（推荐）**：Qwen Code，自带 provider 菜单，首次可选 DeepSeek / [[GLM]] / MiniMax
- **方式 B**：GLM Agent，纯 Z.AI Coding Plan
- **方式 C**：手动 Configure ACP Agent，接任意 OpenAI 兼容端点

ACP 注册表已收录的国产 agent：GLM Agent、Kimi CLI、Qwen Code、Codebuddy Code [[Junie]]。

### 认证与模型来源 [[Junie]]
- JetBrains 账号 OAuth / Junie API Key
- BYOK：Anthropic / OpenAI / Google / xAI / OpenRouter / Copilot
- 国产模型可经 OpenRouter 中转 [[junie-国产模型配置指南]]

## 三、代码补全（不走 ACP）

> ⚠️ **本地知识库中无代码补全机制记录**，以下为通用知识，需以 JetBrains 官方文档为准。

代码补全与 ACP 是**两套独立机制**，互不影响：

| 能力 | 机制 | 配置位置 |
|------|------|----------|
| AI Chat / agent mode | ACP 注册表 | AI Assistant → AI agents |
| 代码补全 inline completion | JetBrains AI 补全服务 / 第三方插件 | Settings → Tools / Plugins |

### 无 JetBrains AI 订阅也能用代码补全

走第三方插件（IDEA Plugins 市场安装）即可，登录取 Key 后启用：

| 插件 | 收费 | 说明 |
|------|------|------|
| 通义灵码（阿里） | 免费 | 国产，中文友好 |
| CodeGeeX（智谱） | 免费 | 国产 |
| Codeium | 免费 | 个人版免费 |
| Supermaven | 免费版 | 补全速度快 |
| GitHub Copilot | 付费 | 需 Copilot 订阅 |
| Amazon Q | 免费 | 原 CodeWhisperer |

装好插件后即可在 IDEA 用对应补全，与 ACP / [[Junie]] 完全互不干扰。

## 四、选型建议

- 要多步任务 / agent 能力：配 [[Junie]] 或 ACP 国产 agent（见 [[junie-国产模型配置指南]]）
- 只要代码补全、又不想付费：装通义灵码 / Codeium 插件
- 两者可共存：**ACP 管 chat，第三方插件管补全**，互不冲突

## 知识缺口

本地知识库当前缺失以下内容，建议后续补充：
- JetBrains AI 订阅的具体档位与对应能力（免费/Pro/Enterprise）
- 代码补全 inline completion 的官方配置路径（2026 版 Settings 菜单细节）
- JetBrains 自家补全模型与第三方插件补全的质量对比

## 关联连接
- [[IntelliJIDEA]] — IDE 集成宿主
- [[Junie]] — JetBrains AI coding agent
- [[junie-国产模型配置指南]] — ACP 配置国产模型操作步骤
- [[Qwen]] — 阿里通义国产模型
- [[GLM]] — 智谱国产模型
- [[Kimi]] — 月之暗面国产模型
- [[DeepSeek]] — DeepSeek 模型（Qwen Code 内置支持）
