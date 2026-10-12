---
title: "Agent幻觉"
type: concept
tags: [Agent, 幻觉, 可靠性, 治理]
sources: [raw/01-articles/2026-10-10 - Agent 出现幻觉怎么治理？.md]
last_updated: 2026-10-12
---

## 定义
Agent 幻觉指幻觉进入 Agent 执行流程后"从说错变成做错"的现象：模型的幻觉表现为错误的工具调用、错误的上下文压缩、错误的长期记忆检索、未完成却宣称完成的执行步骤，以及多 Agent 协作中被下游当作事实的错误结论。2025 年 9 月中国科学院信息工程研究所牵头、联合南洋理工大学及中国人民大学等十几家机构发表的论文《LLM-based Agents Suffer from Hallucinations》按发生阶段将其分为**推理、执行、感知、记忆、通信**五类。

## 关键信息
- **五类分类（论文）**：推理幻觉（凭记忆编造）、执行幻觉（表现得好像已完成某步骤，实际没有）、感知幻觉、记忆幻觉（不经核对就相信自己的记忆，用上过时/编造/混淆的内容）、通信幻觉（下游 Agent 把上游 Agent 的幻觉当成事实继续推理）
- **治理总思路**：只有一条——让 Agent 执行的每一步都去真实环境核对一遍，把错误当作工具结果交还给模型，让模型自己改正
- **工具调用治理**：调用不存在的工具返回 "Tool xxx not found"；参数经 TypeBox（TypeScript 的 JSON Schema 定义与校验库）校验，失败时把出错字段路径和原始参数发回并打 isError 标记，模型下一轮重新发起调用（[[ArminRonacher|Armin 的 Pi]]）
- **文件编辑治理**：Claude Code 的 Edit 要求 old_string 在文件里一字不差且只出现一次；Codex apply_patch 对不上原文报 "Failed to find expected lines"；Pi 的 edit 每次从磁盘重新读取校验真实内容——**模型可以记错，但磁盘上的文件不会错**
- **压缩（短期记忆）治理**：Pi 的压缩提示词要求摘要保留准确的文件路径/函数名/报错信息，而"读过改过哪些文件"由代码从工具调用记录提取并附在摘要后，原始对话保存在会话文件可回溯；Claude Code 压缩后从磁盘重新读取最近读写过的最多 5 个文件并重新注入 CLAUDE.md，只在对话里交代的指令可能丢失，故官方建议把长期规则写进 CLAUDE.md
- **长期记忆治理**：Codex 读取记忆的提示词写明 "Memory is not proof of current behavior"（记忆不能证明现状），易变且核实成本低的事实先核实再回答；Claude Code 在记忆文件里记录写入时间
- **执行幻觉治理**：①用确定性检查代替模型自我判断——Claude Code Stop hook 在结束前跑测试，未通过返回 block 让其继续修改（为防无限循环最多 8 次），与 Harness 五要素中 Evaluation"只认客观物证"一致；②验证的人不能是干活的人——用上下文全新的 Sub-agent 只看 diff 与验收标准做审查，但审查者被要求找问题时通常也会报几个问题，意见不能照单全收；③涉钱操作最后一步交给确定性代码校验（如退款不得超过实付金额，写死在代码里）
- **通信幻觉治理**：Agent 之间传递结论必须附证据（文件路径、行号、命令原始输出），让下游能自己核对，而不是只接收一句"已经修好了"
- **核心隐喻**：记忆只是线索，磁盘上的内容才是证据

## 关联连接
- [[摘要-agent-hallucination-governance]] — 来源
- [[幻觉]] — 模型侧的上位概念
- [[AI幻觉]] — 相邻概念
- [[Tool幻觉]] — 五类中工具调用侧的具体表现
- [[零幻觉]] — 治理目标的相邻概念
- [[ClaudeCode]] — old_string、Stop hook、压缩重读、Sub-agent 审查的实践方
- [[Codex]] — apply_patch 原文匹配与记忆提示词原则
- [[ArminRonacher]] — Pi Agent 的作者，其 Pi 是文中的治理样板
- [[PiAgent]] — 同名框架的区分说明
- [[AgentHarness]] — Harness 五要素中的 Evaluation 原则
- [[Subagent]] — 全新上下文审查者模式
- [[Hooks]] — Stop hook 确定性检查
- [[error-feedback-self-healing]] — 错误回灌自愈
- [[AgentMemory]] — 记忆幻觉所依附的记忆机制
- [[Agent上下文管理]] — 压缩环节的治理对象
