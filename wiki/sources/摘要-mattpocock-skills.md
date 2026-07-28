---
title: "摘要-mattpocock-skills"
type: source
tags: [AI编程, Skill, 工程纪律, 开源工具]
sources: [raw/01-articles/Matt Pocock 那个 5 个月冲到 17 万 star 的 grill-me，作者自己却不用了，原因是这几个.md]
last_updated: 2026-07-27
---

## 核心摘要

本文介绍了 Matt Pocock 的 `mattpocock/skills` 仓库——一个 5 个月冲到 17 万 star 的 AI 编码 skill 集合。文章的核心论点是"把 skill 当纪律，不当框架"，与 GSD、BMAD、Spec-Kit 等"接管流程"的重量级框架形成对比。文章深入分析了 AI 编码的四大失败模式（对不齐、太啰嗦、跑不起来、架构烂成泥）及其对应修复 skill，提出了 User-invoked（编排层）与 Model-invoked（纪律层）的两层调用架构，并给出了中文团队的落地建议。

## 关键信息

### 核心设计哲学
- **Skill 是纪律，不是框架**：skill 不该被供着，而是随时可替换、可组合、可 hack 的一次性纪律
- **小、可改、可组合、跨模型**：基于工程基础，不接管流程控制权
- **与 GSD/BMAD/Spec-Kit 的根本分野**：后者"接管流程"让用户失去控制权，前者把控制权留给用户

### 四大失败模式与修复
| 失败模式 | 表现 | 修复 Skill | 引用的工程经典 |
|---------|------|-----------|--------------|
| 对不齐 | Agent 没做你想要的 | /grill-with-docs（盘问对齐） | The Pragmatic Programmer |
| 太啰嗦 | 命名冗长，代码膨胀 | 共享语言（Ubiquitous Language）→ CONTEXT.md | DDD（Eric Evans） |
| 跑不起来 | 看着对，跑就崩 | 反馈回路：/tdd + /diagnosing-bugs | The Pragmatic Programmer |
| 架构烂成泥 | 软件熵加速 | 每日投资设计：/to-spec + /improve-codebase-architecture | XP（Kent Beck）/ 软件设计哲学（Ousterhout） |

### User-invoked vs Model-invoked 两层架构
- **User-invoked（编排层）**：用户亲手打出 /xxx 触发，职责是"编排"。包括 ask-matt、grill-with-docs、triage、implement、wayfinder 等
- **Model-invoked（纪律层）**：模型可自动调用，承载"可复用的纪律"。包括 prototype、diagnosing-bugs、tdd、domain-modeling、code-review 等
- **铁律**：User-invoked skill 可调 Model-invoked skill，但 User-invoked 之间互不调用

### 推荐落地链
domain-model → to-prd → to-issues → tdd（规划→规范→工单→实现）

### 安装哲学
- **skills.sh**：可编辑副本，拷进项目可以改，适合团队定制
- **Claude Code Plugin**：只读、永远最新、订阅式，不修改

### 中文团队落地建议
- 先装三件套：grill-with-docs + /tdd + /code-review
- 共享语言在中文项目同样成立，把长业务描述压成术语表放 CONTEXT.md
- issue tracker 国内多用 GitHub 或本地文件

## 关联连接
- [[MattPocock]] — 仓库创建者，Total TypeScript 作者
- [[Skill]] — Skill 概念体系
- [[AICoding]] — AI 编码范式
- [[GSDCore]] — 同属 AI 编码工作流方案
- [[SpecKit]] — 同属规范驱动阵营
- [[TDD]] — 测试驱动开发实践
- [[code-review]] — 代码审查实践
- [[CLAUDEmd]] — 类似的元指令/规则注入思路