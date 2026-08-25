---
title: "摘要-agent-skills-普通人教程-龙叔"
type: source
tags: [来源, Agent Skills, Claude Code, skill-creator, 教程]
sources: [raw/01-articles/2026-08-24-火爆全网的 Agent Skills，普通人到底该怎么用？-- 详细教程 - 程序员龙叔.md]
last_updated: 2026-08-25
---

## 核心摘要
程序员龙叔分享面向普通人（非技术人员、新手小白）的 Agent Skills 构建教程。核心方法论：用嘴说就能搞定，全程不用碰代码、不用搞配置。流程为：①进入 Claude Code 交互终端 → ②输入「帮我安装 skill-creator」→ ③描述需求让 AI 把开源项目（如 ImageMagick、yt-dlp）打包成 Skill → ④测试调用。文章强调「任何会重复 3 次及以上的、或任何可复用的能力，都建议 Skill 化」，并演示了图片格式转换压缩、视频下载（yt-dlp，143k star）两个完整案例。

## 关键信息
- **核心观点**：任何会重复 3 次及以上的能力，都建议抽象成技能 Skill 化
- **构建四步法**：进 CC → 装 skill-creator → 描述需求封装开源项目 → 测试
- **开源项目挖掘**：不知道用什么开源项目时，直接问 AI「在 Github 上有没有针对 XX 需求比较好的项目，请给出项目名称、地址、点赞数」
- **案例一**：ImageMagick 图片格式转换/压缩 Skill
- **案例二**：yt-dlp（143k star，支持 YouTube/B 站/抖音/小红书等 1000+ 网站）视频下载 Skill，15 秒下载小红书视频
- **查看已装 skills**：在 Claude Code 中输入 `/skills`
- **适用工具**：Claude Code、OpenCode、Codex、Antigravity、Coze 2.0 等主流 AI 工具

## 关联连接
- [[SkillCreator]] — Claude Code 元技能创建工具
- [[ClaudeCode]] — Anthropic 终端 AI Agent
- [[AgentSkills]] — Agent 技能生态
- [[GitHub]] — 开源项目来源
