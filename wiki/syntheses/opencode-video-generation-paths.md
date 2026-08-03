---
title: "opencode-生成视频的三种途径"
type: synthesis
tags: [OpenCode, 视频生成, Skill, MCP, Remotion, AI编程]
sources:
  - raw/01-articles/分享8个codex必装的skill，让你的AI能力起飞！.md
  - raw/09-archive/Codex 从基础到进阶的10条实用技巧.md
  - raw/01-articles/最强AI设计智能体Lovart，保姆级入门教程（4000字长文）.md
last_updated: 2026-08-03
---

# opencode 生成视频的三种途径

> **核心问题**：[[OpenCode]] 本身是编程 Agent，内置工具只有 bash/edit/write/read/grep/webfetch 等，没有视频生成能力，那如何用它生成视频？

## 结论先行

opencode 自身**不直接出片**，而是作为编排者，通过三种扩展途径把视频能力"接进来"：

| 途径 | 原理 | 适合场景 | 可控性 | 出片方式 |
| --- | --- | --- | --- | --- |
| **1. Skill 扩展** | 安装视频生成 Skill，SKILL.md 引导调用外部工具 | 现成、傻瓜化 | 中 | 工具内部处理 |
| **2. bash + 编程框架** | bash 调用 [[Remotion]] 等"代码写视频"框架 | 程序员、可复现 | 高（逐帧逻辑） | 渲染 MP4 |
| **3. MCP 接入视频模型** | 配置 MCP 服务器，调用文生视频模型 API | 一句话出片 | 低 | 模型生成 |

## 途径一：Skill 扩展（最省事）

- 给 opencode 安装视频生成类 Skill，文件放项目 `.opencode/skills/` 即可被自动加载（opencode 官方兼容标准 SKILL.md 规范）。
- 知识库中提到的 [[HyperFrames]] 就是典型视频生成 Skill，见 [[摘要-codex必装skill推荐]]。
- 优点：无需写代码，对话里直接触发。

## 途径二：bash + Remotion（程序员首选）

- [[Remotion]] 是"用代码写视频"的 React 框架——像写组件一样写视频，渲染成 MP4。
- opencode 的 bash 工具可以直接执行 `npx remotion render`，配合 write 工具生成视频脚本代码。
- 这是 [[Codex]] 场景下的成熟做法，[[摘要-codex-97percent-技巧]] 明确提到"Remotion 做视频"。
- 优点：完全程序化、可复现、精确控制；缺点：需要写代码。

## 途径三：MCP 接入 AI 视频模型（纯 AI 生成）

- 在 `opencode.json` 的 `mcp` 字段配置视频生成服务，openode 把提示词/脚本交给模型。
- 可接 [[Sora]]（OpenAI 文生视频模型，见实体页），或 [[Lovart]] 推荐使用的 Seedance 2.0（见 [[摘要-最强AI设计智能体Lovart入门教程]]）。
- 优点：一句话出片；缺点：素材不受控，依赖模型能力与 API 成本。

## 选型建议

- 想要**完全程序化 / 可复现 / 精确逐帧** → 途径二（Remotion + bash）
- 想要**纯 AI 生成 / 低成本尝试** → 途径三（MCP 接 Sora / Seedance）
- 想要**现成傻瓜化 / 快速出片** → 途径一（HyperFrames 类 Skill）

## 关联连接

- [[OpenCode]] — 编排者本体
- [[HyperFrames]] — 视频生成 Skill
- [[Remotion]] — 代码写视频框架
- [[Sora]] — OpenAI 文生视频模型
- [[Lovart]] — AI 设计智能体，视频生成用 Seedance 2.0
- [[摘要-codex必装skill推荐]] — 来源（HyperFrames）
- [[摘要-codex-97percent-技巧]] — 来源（Remotion 做视频）
- [[摘要-最强AI设计智能体Lovart入门教程]] — 来源（Seedance 2.0）
- [[Skill]] — Skill 扩展机制
- [[MCP]] — MCP 协议
