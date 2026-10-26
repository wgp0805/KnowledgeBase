---
title: "Agent任务取消"
type: concept
tags: [Agent, 取消, 中断, 进程管理, 信号, AbortController]
sources: ["raw/09-archive/2026-10-05 - 用户中途取消，Agent 任务怎么停下来？.md"]
last_updated: 2026-10-08
---

## 定义
Agent 任务取消的完整工程方案：不是断开请求，而是**取消信号层层传递 + Agent Loop 主动检查 + 杀掉整个进程组 + 会话历史补齐结果**四位一体；若用户只是想中途补充要求而非取消，则走 Steering 排队注入。

## 关键信息
- **为什么断开请求不够**：只停可见输出，已启动的 Bash 还在跑、半截工具可能已改文件、下轮请求因缺 tool_result 被 API 拒绝、按 Anthropic 计费规则照样收费
- **信号传递**：全局变量 isCancelled 无法打断等待中的网络请求、多 Sub-agent 分不清停谁；杀进程会连会话一起杀。Claude Code 用 **AbortController**（Esc 同一信号传给模型流式请求与每个工具，工具持子信号：父取消子跟取消、子取消不影响父），Codex（Rust）用 **CancellationToken** 层层派生子 token
- **Agent Loop 主动检查点**：流式输出过程中、每个工具执行之前、重试等待的间隙——不检查就停不下来（类比 Java `Future.cancel(true)` 只打中断标记，任务不检查标记线程停不了）
- **杀进程组**：只杀 shell 父进程不够（npm run dev 的 Node 子进程还占端口），进程组=父进程+派生子进程要整组停。SIGTERM（可捕获、先清理）vs SIGKILL（强制、不可拦截）：Codex 先 SIGTERM 等 50ms 再 SIGKILL，Claude Code 直接 SIGKILL 杀整棵进程树
- **Sub-agent 归属**：Claude Code 前台 Sub-agent 与主任务共用取消信号（Esc 一起停），后台 Sub-agent 用独立信号需单独结束
- **会话历史处理**：每个 tool_use 必须紧跟 tool_result。Claude Code 给被打断的工具补"用户拒绝了这次操作"（文件修改不写入）；Codex 下轮提醒 "aborted by user" 让模型先检查半截命令；Pi 跳过整条半截回答、无结果统一补 "No result provided"
- **Steering（补充而非取消）**：新消息先进队列，等当前这批工具执行完、下次调用模型前再注入——tool_use 与 tool_result 之间不能夹别的消息。Pi 两条队列：steer（本轮工具完注入）/ followUp（Agent 正常停下执行）；Claude Code 补充输入排队同轮提交，Ctrl+Enter 立即发送、shell 转后台且模型可见已有输出

## 关联连接
- [[摘要-agent任务取消机制]] — 来源
- [[steering]] — 中途插话的互补机制
- [[AgentLoop]] — 需要检查取消信号的执行循环
- [[ClaudeCode]] — AbortController 实现方
- [[Codex]] — CancellationToken 实现方
- [[Subagent]] — 取消信号的层级传递对象
- [[Agent]] — 上位概念
