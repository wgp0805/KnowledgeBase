---
title: "全 AI 开发前后端分离项目指南"
type: synthesis
tags: [AI编程, 前后端分离, Skill, 工作流, 工具选型, 工程纪律]
sources:
  - wiki/sources/摘要-springboot4-security7-vue3-best-practice.md
  - wiki/sources/摘要-superpowers-openspec-speckit对比.md
  - wiki/sources/摘要-OpenSpec规范驱动AI编程框架.md
  - wiki/sources/摘要-spec-superflow-融合工作流.md
  - wiki/sources/摘要-再见吧-codex.md
  - wiki/sources/摘要-claude-code-实战防搞炸.md
  - wiki/sources/摘要-codex-从原理到-java落地.md
  - wiki/sources/摘要-codex必装skill推荐.md
  - wiki/syntheses/harness-architecture-comparison.md
  - wiki/concepts/Skill.md
  - wiki/concepts/CLAUDE-md.md
last_updated: 2026-11-11
---

# 全 AI 开发前后端分离项目指南

> 适用场景：从 0 到 1 开发一个前后端分离项目，全程用 AI 辅助。核心原则：**先铺地基再动手，规范驱动而非许愿式提问，小步实现 + 强制验证，人守住三条终审边界。**

## 一、主驾驶：选一个 Harness

"Model + Harness = Agent"——同一模型换个 Harness，效果差别巨大（详见 [[harness-architecture-comparison]]）。推荐配置：

| 工具 | 定位 | 使用方式 |
|------|------|---------|
| [[ClaudeCode]] | Harness 业界标杆：权限/Hooks/子 Agent/Skill 生态最完整 | **主力**，整体推进 |
| [[Codex]] | "规划—改文件—执行验证—依据结果迭代"的工程 Agent | 复杂重构、多文件联动、Bug 排查 |
| [[TRAE]] | 代码生成快 | Codex 出方案，TRAE 按方案写代码 |

大项目并行：用 Claude Code 的 **Project（协调员拆 Thread）+ [[NestedSession]]** 让前后端任务并行。

技术栈基线可照 [[摘要-springboot4-security7-vue3-best-practice]]：Spring Boot 4 + Spring Security 7 + Vue3，JWT 无状态 + Redis 黑名单 + 双 Token（AT 30 分钟 / RT 7 天，详见 [[无感刷新Token]]）+ RBAC 五表（详见 [[rbac]]）+ Pinia/Axios 无感刷新 + v-permission。

## 二、地基：先写说明书，再让 AI 动手

### 1. AGENTS.md / CLAUDE.md（项目根目录）

只放三类内容（详见 [[摘要-再见吧-codex]]、[[CLAUDE-md]]）：
- **项目硬约定**：不能动哪些目录、接口必须保留什么字段、日志与敏感数据处理方式
- **工作习惯**：改前先读相关文件、只做当前最小改动、完成后自证验证
- **踩坑记录**：易错点、已知坑

约束：**≤200 行**；过长按前端/后端拆分 + 主文件留指针；**推荐 AGENTS.md**（Codex 等其他 Agent 也通用）。

### 2. 规范驱动框架（替代"丢需求等结果"）

| 工具 | 解决什么 | 适合 |
|------|---------|------|
| [[SpecKit]] | 定"项目宪法"（constitution/spec/plan/tasks 七阶段） | 绿地项目 |
| [[OpenSpec]] | 管每次变更生命周期（explore→propose→apply→archive） | 棕地/增量变更 |
| [[Superpowers]] | 强制工程纪律（14 Skill + 五阶段） | 执行纪律 |
| [[SpecSuperflow]] | OpenSpec + Superpowers 融合（9 Skill + 八状态机 + execution-contract） | 想要一体化 |

理想组合：**Spec-Kit 定宪法 → OpenSpec 管变更 → Superpowers 执行纪律**（详见 [[摘要-superpowers-openspec-speckit对比]]、[[摘要-spec-superflow-融合工作流]]）。

### 3. 权限与安全护栏

deny 规则硬拦（`rm -rf`、`git push --force`、读 `.env`）；Auto Mode 是辅助不是沙箱；Hooks 在 PreToolUse 拦危险命令、编辑后格式化、结束前跑测试（详见 [[摘要-claude-code-实战防搞炸]]）。

## 三、分阶段 Skill 清单

### 阶段 0：需求与规划
- OpenSpec explore/propose —— 对话理清需求，产出 proposal/specs/design/tasks
- grill-with-docs / triage / wayfinder（Matt 编排层）

### 阶段 1：架构与数据模型
- 后端架构 Skill（可自写 `backend-architect`）—— 分层、路由、依赖注入
- database-designer / migration-architect（Antigravity Awesome Skills）—— 表设计、迁移
- postgres/mysql-best-practices —— 索引、JSONB、约束
- GitNexus —— 代码知识图谱，先看懂结构再改

### 阶段 2：后端实现
- Spring Boot 专属 Skill（见 [[spring-skill-usage-guide]]）
- 自定义 MyBatis-Plus Skill —— `@TableName/@TableLogic`、LambdaQueryWrapper、分页、Service 模板
- Redis 官方 Agent Skill —— 数据结构选型、集群、连接池、穿透/雪崩
- **TDD**（Model-invoked 纪律）—— 先测试后实现
- **code-review** —— 提交前 AI 审查

### 阶段 3：前端实现
- **frontend-design**（Anthropic 官方）—— 高质感 UI、Tailwind 设计系统、Anti-patterns
- VercelLabs（react-best-practices / web-design-guidelines）
- PatternsDev（Vue/JS 设计模式）
- shadcn-ui —— 组件库

### 阶段 4：联调与测试
- backend-api-test-suite —— 接口回归
- Casebook —— 测试用例工程化
- 浏览器控制 Skill（Web-access 类）—— E2E 与截图验证

### 阶段 5：安全与权限
- saas-auth-rbac-security —— JWT/限流/密钥管理/支付验签幂等
- 双 Token 无感刷新（[[无感刷新Token]]）+ RBAC 按钮级权限（[[rbac]]）

### 阶段 6：部署与交付
- 部署类 Skill —— Dockerfile/Compose、CI、环境变量
- context-doctor —— 上下文健康检查

### 贯穿全程
- **Skill Creator** —— 把项目专属规范沉淀为 Skill
- Humanizer-zh —— 去 AI 味（文档/注释）

## 四、纪律：7 步工作流 + 三条边界

**7 步工作流**（详见 [[摘要-再见吧-codex]]）：

```
阅读理解 → 写计划 → 确认范围 → 小步实现 → 验证 → 总结 → 新会话
```

- 复杂任务先让 AI 输出：要理解什么 / 影响哪些模块 / 分 3-7 步 / 每步怎么验证 / 哪里易错
- Bug 修复给日志与复现步骤，**不预猜原因**
- "收工了"五问：改了什么？为什么？验证了什么？漏了什么？哪里要人工确认？→ 写回 AGENTS.md
- 小步提交 + Worktree 隔离多实例

**三条终审边界**（必须由人决策，详见 [[摘要-codex-从原理到-java落地]]）：
1. 架构选型
2. 复杂核心业务
3. 安全敏感代码（权限/加密/支付）

原则：**提交者对 AI 生成代码负责**；敏感数据不进公共服务。

## 五、最小起步清单（6 个，跑通再加）

1. `AGENTS.md`（硬约定 + 踩坑）
2. OpenSpec 或 SpecSuperflow（规划层）
3. 后端架构 + MyBatis-Plus（自写，贴合 ORM）
4. TDD + code-review（纪律层，防失控核心）
5. frontend-design（前端质感）
6. Skill Creator（沉淀经验为资产）

## 六、Skill 使用三原则（详见 [[Skill]]）

- description 写**触发条件**（"当用户要求 X 时使用"），不是功能介绍
- 主体 **≤200 行**，细节拆 `references/`（渐进式披露）
- 项目规范进项目级 `.claude/skills/`，个人偏好进 `~/.claude/skills/`

## 关联连接

- [[摘要-springboot4-security7-vue3-best-practice]] — 前后端分离技术栈基线
- [[摘要-superpowers-openspec-speckit对比]] — 三大规范工具组合策略
- [[摘要-OpenSpec规范驱动AI编程框架]] — 规范驱动四阶段
- [[摘要-spec-superflow-融合工作流]] — 融合工作流
- [[摘要-再见吧-codex]] — 7 步工作流与 AGENTS.md 写法
- [[摘要-claude-code-实战防搞炸]] — 权限/Hooks/验证三位一体
- [[摘要-codex-从原理到-java落地]] — Java 落地与三条终审边界
- [[摘要-codex必装skill推荐]] — Skill 生态推荐
- [[harness-architecture-comparison]] — Harness 选型
- [[Skill]] — 技能机制与反模式
- [[CLAUDE-md]] — 项目记忆文件
- [[NestedSession]] — 多会话并行
- [[无感刷新Token]] — 双 Token 续期
- [[rbac]] — 权限模型
- [[spring-skill-usage-guide]] — Spring Skill 组合策略
- [[claude-code-增强框架对比]] — 增强框架横向对比
- [[openspec-brownfield-usage-guide]] — 棕地项目 OpenSpec 用法
