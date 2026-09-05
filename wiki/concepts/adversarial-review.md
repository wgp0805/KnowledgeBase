---
title: "adversarial-review"
type: concept
tags: [AI, Agent, 代码评审, 质量保障]
sources: [raw/09-archive/multi-agent-collaboration.md]
last_updated: 2026-08-06
---

## 定义

对抗性评审（Adversarial Review）是一种通过**对抗性 prompt + 盲审流程 + 独立验证**来防止同源 AI Agent 互相"放水"的代码评审机制。Reviewer 的 KPI 是"发现问题"，而不是"让任务通过"。

## 关键信息

### 防"互相包容"的四层机制

1. **客观验收闸门**：验收标准 = 可独立执行的命令 + 退出码/输出断言，Reviewer 自己跑，不采信 Coder 自证
2. **盲审**：Reviewer 先看 spec + 代码独立下结论，再看 Coder 的 impl.md 对照
3. **对抗性 prompt**：默认立场是怀疑，通过需主动举证，举证不足 = Blocker
4. **异构模型 / 红队**：Coder 与 Reviewer 用不同厂商模型，或加红队 reviewer 只挑 Blocker

### 对抗性 Prompt 模板

```markdown
## 硬约束
1. 不直接改代码，只提问题和建议。
2. 问题必须给 <文件:行> + 修改建议。
3. 默认立场是怀疑：通过需要你主动为每条验收标准找到独立证据
   （自己跑命令 / 读断言），找不到证据就标 Blocker"未独立验证"，
   不得采信 impl.md 的自述作为通过依据。
4. impl.md 的"验证情况/遗留疑问"是 Coder 的辩词，参考但不作豁免依据。
5. 不为评审而评审，没问题不硬凑。
```

### 同源模型互相包容的根源

1. **训练偏好同源**——同一家模型倾向礼貌、配合、肯定
2. **共情偏差**——Reviewer 看到 Coder 解释"环境受限/已尽力"会代入对方视角放松标准
3. **确认偏置**——倾向于找"符合"而非"违反"的证据
4. **责任稀释**——知道"反正还能退回重改"，放水成本低

## 关联连接

- [[multi-agent-collaboration]] — 所属框架
- [[role-isolation]] — Reviewer 隔离（有 Bash 无 Edit）
- [[subagent-driven-development]] — 子代理双裁决审查
- [[摘要-多Agent协作开发框架]] — 来源