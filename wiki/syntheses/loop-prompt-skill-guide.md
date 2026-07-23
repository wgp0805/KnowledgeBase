---
title: "loop-prompt-skill-guide"
type: synthesis
tags: [Loop, Prompt, Skill, Agent, 最佳实践]
sources: [raw/01-articles/Loop Engineering 实战指南.md, raw/01-articles/Prompt 已死，Loop当立？先看完这5个生产级坑再决定.md, raw/01-articles/老奶奶看完都会写 Skill，这可能是全网最接地气的 Skill 教程.md]
last_updated: 2026-07-23
---

# Loop / Prompt / Skill 三者区别与最佳实践

## 一、三者区别

| 维度 | 提示词（Prompt） | Skill | Loop |
|------|-----------------|-------|------|
| **本质** | 一次性指令，说完就没了 | 常驻的操作说明书（SKILL.md） | 自动化循环执行系统 |
| **比喻** | 临时喊一嗓子"帮我倒杯水" | 冰箱上贴的纸条"客人来了先倒水" | 自动运转的工厂流水线 |
| **生命周期** | 单次对话有效 | 常驻，遇到相关任务自动触发 | 持续运行直到停止条件满足 |
| **编写者** | 用户即时输入 | 开发者沉淀的最佳实践 | 开发者设计循环规则 |
| **复杂度** | 低，几句话搞定 | 中，几十到几百行 Markdown | 高，需设计三文件体系 |
| **复用性** | 低，每次重写 | 高，安装后自动生效 | 中，按需启动/停止 |

**核心关系**：Prompt 是"临时告诉 AI 怎么做"；Skill 是"把重复要求固化下来"；Loop 是"让 AI 自己持续跑"。

## 二、最小可用实践：用 /loop 构建命令行备忘录

### 目标
5 分钟内体验 `/loop` 的完整逻辑——AI 自动逐轮构建，每轮只做一件事，你确认后继续。

### 步骤

#### 1. 创建空目录和宪法（CLAUDE.md）

```bash
mkdir /d/demo-loop && cd /d/demo-loop
```

创建 `CLAUDE.md`：

```markdown
# 项目宪法

## 任务
用 Python 写一个命令行备忘录工具，支持：
1. 添加备忘录   `python todo.py add "内容"`
2. 列出所有     `python todo.py list`
3. 删除一条     `python todo.py del <id>`

## 规则
- 每次只做一件事
- 做完更新 STATE.md
- 等待我确认后再继续
```

#### 2. 创建状态文件（STATE.md）

```markdown
# 循环状态

## 已完成
- (暂无)

## 待完成
- [ ] 1. 创建项目结构和 todo.py 脚手架
- [ ] 2. 实现 add 命令
- [ ] 3. 实现 list 命令
- [ ] 4. 实现 del 命令
- [ ] 5. 跑一遍验证所有功能正常

## 下一步
- 创建项目结构
```

#### 3. 创建技能卡（SKILL.md）

文件位置：`.claude/skills/demo-todo/SKILL.md`

```markdown
---
name: demo-todo
description: 命令行备忘录工具开发循环。当用户说"开始"、"跑循环"、
  "继续"、"执行下一步"时使用。
---

# 备忘录开发循环

## 怎么做
1. 读 STATE.md 了解当前进度
2. 从待完成列表取最顶上的一项执行
3. 执行完后更新 STATE.md（移到已完成）
4. 报告做了什么，问用户是否继续
```

#### 4. 启动循环

```bash
cd /d/demo-loop
/loop
```

#### 5. 体验流程

**第一轮**：AI 读取 STATE.md，看到"创建项目结构"，自动创建 `todo.py` 基础框架，更新 STATE.md，询问是否继续。

输入 `y` 进入下一轮。AI 实现 add 命令，更新状态，再问。再输入 `y`，实现 list 命令……

**切换到 L3 无人值守模式**（第三轮后如果信任 AI）：

```
/loop 自动执行，不需要我确认。每轮汇报结果就行。
```

### 三、核心原理

| 你学会的 | 对应概念 |
|---------|---------|
| 项目先立规矩再干活 | CLAUDE.md = 宪法 |
| 用文件记录进度，不靠对话记忆 | STATE.md = 记忆 |
| 把重复流程封装成可复用指令 | SKILL.md = 技能卡 |
| 每步确认，可控迭代 | L2 分诊模式 |
| 信任后让 AI 自动跑 | L3 无人值守 |

### 四、关键命令速查

| 你想做什么 | 输入 |
|-----------|------|
| 启动循环 | `/loop` |
| 指定范围 | `/loop 只做前端部分，暂不碰后端` |
| 指定目标 | `/goal 完成所有 CRUD API 且测试通过` |
| 查看进度 | `/read STATE.md` |
| 暂停循环 | 直接说"暂停"或 Ctrl+C |
| 切换方向 | "先做状态流转，优先级管理后面再做" |
| 无人值守 | `/loop 自动执行，做完汇报` |

### 五、支持的 Agent 工具

| 工具 | Prompt | Skill | Loop | 特点 |
|------|--------|-------|------|------|
| **Claude Code** | ✅ | ✅ | ✅ | Query Loop 异步生成器，CLAUDE.md + SKILL.md + /loop |
| **Codex** | ✅ | ✅ | ✅ | AGENTS.md + SKILL.md + Automations/Goals |
| **OpenCode** | ✅ | ✅ | ✅ | 开源替代，兼容 SKILL.md，20+ 种 Hook 事件 |
| **ECC** | ✅ | ✅ | ✅ | 增强框架，47+ Agent + Skill + Hook |
| **Superpowers** | ✅ | ✅ | ❌ | 14 核心 Skill，强制工程纪律 |
| **MiMoCode** | ✅ | ✅ | ✅ | 目标驱动自主循环，支持 max-mode 并行评估 |
| **Kaku** | ✅ | ✅ | ✅ | 双面板同时运行 Claude Code + Codex |
| **DeepSeekTUI** | ✅ | ✅ | ⚠️ | Plan/Agent/YOLO 三种模式 |

### 六、生产环境五大坑

1. **生成和验证必须硬隔离**：builder 有写权限，checker 只能读
2. **编排器必须原样转发失败信息**：不要自己解读，完整转发
3. **必须有明确的停止规则**：最多几轮、什么情况下停止
4. **状态必须落地**：写在 STATE.md 而非对话里
5. **目标必须可验证**："所有测试通过"是合格目标，"做好"不是

## 关联连接
- [[LoopEngineering]] — 循环工程方法论
- [[Skill]] — 技能扩展机制
- [[提示词工程]] — Prompt 工程四大技巧
- [[ClaudeCode]] — Claude Code 平台
- [[Codex]] — Codex 平台
- [[摘要-loop-engineering-guide]] — 方法论来源
- [[摘要-loop-engineering-pitfalls]] — 生产实践来源
- [[摘要-胖虎-skill教程]] — Skill 编写教程
- [[ECC]] — 增强框架
- [[Superpowers]] — 强制工程纪律框架