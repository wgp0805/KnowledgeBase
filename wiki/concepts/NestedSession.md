---
title: "NestedSession"
type: concept
tags: [概念, ClaudeCode, 多Agent, 会话管理, 并行]
sources: [raw/09-archive/Claude(Code)桌面APP，保姆级全攻略，一期视频精通.md]
last_updated: 2026-11-11
---

## 定义

Nested Session（嵌套会话）是 Claude 桌面端的多会话管理机制：主会话（父 Session）把可并行任务拆成多个**子会话**，子会话独立读取代码、修改文件、运行测试，完成后向父会话汇报。它形态上类似 [[Subagent]]（子代理），但**每个子会话在会话列表中可见、各自做了什么一目了然**，因此被认为将逐步取代 Sub Agent。

## 关键信息

### 工作方式

```
主 Session
 ├─ 子 Session 1（查 A 州天气）
 ├─ 子 Session 2（查 B 州天气）
 ├─ 子 Session 3（查 C 州天气）
 └─ 汇聚结果 → 主会话整合输出
```

- 父会话负责拆解任务与汇总结果，子会话各自独立执行
- 子会话的过程信息不挤占主对话，卡住的任务可进子会话看完整上下文
- 会话间可列出/读取/发消息/重命名/归档
- 支持 `Detach to top level`：把子 Session 提升为与主 Session 平级

### 与 Sub Agent 的差异

| 维度 | Sub Agent | Nested Session |
|------|-----------|----------------|
| 可见性 | 过程多为黑盒，只见最终结果 | 每个子会话可见、状态一目了然 |
| 管理 | 由主 Agent 内部调度 | 会话列表可直接查看/干预 |
| 定位 | 内部执行单元 | 一等公民的会话对象 |
| 趋势 | 逐步被替代 | 官方主推方向 |

### 配套能力（详见 [[摘要-claude桌面app全攻略]]、[[ClaudeCode]]）

- **三态侧边栏**：Needs input / Working / Completed 分组
- **并行启动**：Start all 一键并行
- **Worktree 隔离**：同仓库并发改动用 Git Worktree 隔离，避免互相覆盖
- **主动跟进卡片**：发现范围外问题时弹 Do it here / Start（另开会话）

### 设计动机

多 Agent 并行后，稀缺资源从"推理速度"转向"**开发者注意力**"——嵌套会话把"一组并行 Agent"的状态显性化，让人能快速判断该介入哪个会话，而不是在黑盒里猜。

## 关联连接
- [[摘要-claude桌面app全攻略]] — 来源
- [[ClaudeCode]] — 所属产品
- [[Subagent]] — 被逐步取代的旧机制
- [[subagent-driven-development]] — 子代理编排方法论（无独立页则见 [[multi-agent-collaboration]]）
- [[multi-agent-collaboration]] — 多 Agent 协作上位概念
- [[Worktree]] — 并行代码隔离
- [[子Agent编排]] — 编排能力对照
