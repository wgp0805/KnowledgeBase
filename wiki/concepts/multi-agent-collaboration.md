---
title: "multi-agent-collaboration"
type: concept
tags: [AI, Agent, 协作模式, 全栈开发, 角色隔离, 代码评审]
sources:
  - raw/01-articles/Java开发栈Skills全面指南.md
  - raw/09-archive/LangChain4j 和 LangGraph4j，哪个更好？.md
  - raw/09-archive/multi-agent-collaboration.md
last_updated: 2026-08-06
---

## 定义

多 Agent 协作模式是一种将复杂任务拆分为多个专业化 AI Agent 角色，通过**文件显式交接、角色硬约束隔离、客观验收闭环**来协同完成开发工作的流程方法。本文档涵盖两种主流模式：Skill 驱动的全栈开发分工，以及 Planner/Coder/Reviewer 三角色协作框架。

---

## 模式 A：Skill 驱动的全栈开发分工

以领域技能（Skill）为粒度划分 Agent 角色，适合全栈项目的并行开发。

### 典型角色分配
| Agent 角色 | 职责 | 推荐 Skill |
| :---: | :--- | :--- |
| 数据库架构师 | 数据库设计、迁移规划 | database-designer + migration-architect |
| 后端开发者 | Spring Boot + MyBatis + Redis 实现 | spring-boot-engineer + 自定义 MyBatis Skill |
| 前端开发者 | Vue/React + UI 组件库开发 | Patterns.dev React/Vue Skills + web-design-guidelines |
| 安全工程师 | 安全漏洞扫描 | security-hardening |
| DevOps 工程师 | CI/CD、部署 | ci-cd-pipeline-builder |

### 标准全栈工作流
1. **数据库设计阶段**：database-designer + migration-architect
2. **后端开发阶段**：Spring Boot Skills + MyBatis/Redis Skills
3. **前端开发阶段**：Vue/React Skills + Tailwind/设计指 Skills
4. **API 集成阶段**：api-design-principles
5. **测试阶段**：tdd-mastery + 前端测试 Skills
6. **部署阶段**：ci-cd-pipeline-builder

### 核心价值
- **专业化**：每个 Agent 聚焦单一领域，Skill 深度更高
- **并行化**：多个 Agent 可同时工作，缩短开发周期
- **标准化**：整体流程统一编排，输出质量可预期

---

## 模式 B：Planner/Coder/Reviewer 三角色框架

一种通用的、不绑定具体项目的多 Agent 协作方法论文档，通过三个角色分工和文件交接机制来解决多 Agent 协作中的核心痛点。

### 三个核心痛点
1. **角色越界**——Planner 顺手写了实现，Coder 顺手改了架构，Reviewer 顺手改了代码
2. **靠对话协作**——agent 之间靠"记得刚才说过什么"传递信息，上下文一长就漂移丢失
3. **互相包容**——同源模型的多个子 agent 互相评审时倾向"互相放水"，评审形同虚设

### 核心思想
1. **不靠对话记忆协作，靠文件显式交接**。信息只通过磁盘上的 markdown 文件传递
2. **角色靠硬约束切分，不靠自觉**。每个角色定义里写死"不能做什么"，并用工具白名单做物理闸门
3. **闭环靠客观验收，不靠互相认可**。任务的完成判据是可独立核对的命令/断言全部通过

### 三角色定义

| 角色 | 职责 | 产出 | 不能做 |
|------|------|------|--------|
| Planner | 需求拆解、接口设计、验收标准 | `spec.md` | 写实现代码 |
| Coder | 按 spec 实现 + 测试 | 代码 + `impl.md` | 改架构、扩范围 |
| Reviewer | 对照 spec 评审 | `review.md` | 直接改代码 |

**关键：三角色利益不完全一致。** Planner 为"可执行性"负责，Coder 为"按 spec 落地"负责，Reviewer 为"挑出问题"负责。Reviewer 的 KPI 是发现问题，不是让任务通过。

### 角色定义模板的 7 个区块

| 区块 | 作用 | 写法要点 |
|------|------|----------|
| ① frontmatter（name/description/tools） | 给主 agent 的元信息 | description 写"什么时候用我"，tools 精确到能/不能 |
| ② 角色一句话定位 | 给子 agent 自己的身份证 | 一句话含"职责 + 对谁负责" |
| ③ 输入 | 明确"拿什么当依据" | 列上游产物 + 必读规范 |
| ④ 产出 | 固定产出文件名 + 章节骨架 | 让下游能机械解析 |
| ⑤ 硬约束 | 写死"不能做什么" | 每条可验证（"不写实现逻辑"优于"保持克制"） |
| ⑥ 工作步骤 | 把流程固化成步骤 | 含"读什么 → 干什么 → 交接给谁" |
| ⑦ 协作要点（可选） | 重申交接纪律 | 强调只走文件、规范唯一来源 |

### 项目目录骨架

```
项目根/
├─ <主 agent 指令文件>      # 如 CLAUDE.md / AGENTS.md
├─ docs/
│  └─ convention.md        # ★ 唯一规范来源
├─ <agents 配置目录>/       # 如 .claude/agents/
│  ├─ planner.md
│  └─ reviewer.md
└─ tasks/                  # ★ 消息总线
   ├─ README.md           # 交接契约说明
   └─ <编号>-<短描述>/
      ├─ spec.md          # Planner 产出
      ├─ impl.md          # Coder 产出
      └─ review.md        # Reviewer 产出
```

### 三个"唯一来源"原则
- 规范唯一来源 = 共享的 convention 文件
- 消息总线唯一通道 = `tasks/` 目录
- 闭环唯一判据 = `review.md` 结论"通过"（无 Blocker）

### 协作流程

```
Planner ──> spec.md
Coder   ──> 代码 + impl.md
Reviewer ──> review.md
            ├ 通过（无 Blocker）──> 任务关闭
            └ 不通过 ──> Coder 按 review.md 改 ──> 重新 review
```

### 跨工具 vs 单工具对照

| 维度 | 跨工具（如 Claude+Codex） | 单工具（同工具子 agent） |
|------|--------------------------|--------------------------|
| 隔离强度 | 高（不同工具天然物理隔离） | 中（靠子 agent 独立上下文） |
| 异构模型 | 天然异构（防包容加分） | 同源，需对抗 prompt 补偿 |
| 协作摩擦 | 两端规范要对齐 | 一端，无对齐成本 |
| 适合场景 | 真实项目、想体验多工具 | 学习协作机制、快速迭代 |

---

## 相关概念

- [[role-isolation]] — 角色隔离机制（工具白名单 + 硬约束）
- [[adversarial-review]] — 对抗性评审（防"互相包容"）
- [[subagent-driven-development]] — 子代理驱动开发
- skill-creator — 技能创建与封装机制（skill 名，非 wiki 页）
- [[Agent工作流编排]] — 状态图与多 Agent 流程编排方法论

## 关联连接
- [[摘要-多Agent协作开发框架]] — 三角色框架来源
- [[摘要-java-stack-skills-guide]] — Skill 分工模式来源
- [[摘要-langchain4j-langgraph4j-comparison]] — LangGraph4j 多 Agent 模式来源
- [[Agent]] — 基础概念
- [[ai-agent-skill]] — 技能封装机制
- [[Skill]] — Agent 技能定义
- [[ClaudeCode]] — 多 Agent 调度平台
- [[LangGraph4j]] — Java 多 Agent 工作流编排框架
