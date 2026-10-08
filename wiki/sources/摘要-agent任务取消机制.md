---
title: "摘要-agent任务取消机制"
type: source
tags: [来源, 原始文件, Agent, 取消, 进程管理]
sources: ["raw/01-articles/2026-10-05 - 用户中途取消，Agent 任务怎么停下来？.md"]
last_updated: 2026-10-08
---

## 核心摘要
面试题拆解"用户中途取消，Agent 任务怎么停下来"，逐层给出工程正解：①断开请求是错的——只停掉可见输出，已启动的 Bash 命令还在跑、半截工具可能已改文件、下一轮请求会因缺 tool_result 被 API 拒绝，且按 Anthropic 计费规则中途断开照样收费；②取消信号要层层传递——全局变量 isCancelled 打不断等待中的网络请求也分不清停哪个 Sub-agent，杀进程会连会话一起杀；Claude Code 用 AbortController（Esc 按下后同一信号传给模型流式请求和每个工具，工具拿子信号，父取消子跟着取消、子取消不影响父），Codex（Rust）用 CancellationToken 同思路派生子 token；Agent Loop 还必须主动检查——流式输出中、每个工具执行前、重试等待间隙都要查信号（类比 Java `Future.cancel(true)` 只打中断标记、任务不检查就停不下来）；③正在执行的工具要杀整个进程组——只杀 shell 父进程留活子进程（npm run dev 的 Node 还占着端口）；SIGTERM 可捕获先清理、SIGKILL 强杀不可拦截：Codex 对一次性命令先 SIGTERM 等 50ms 再 SIGKILL，Claude Code 直接 SIGKILL 杀整棵进程树；Sub-agent 前台与主任务共用取消信号、后台的要单独停；④会话历史要补齐结果——每个 tool_use 必须紧跟 tool_result：Claude Code 给被打断的工具补"用户拒绝了这次操作"、文件修改不写入并停下等指令，Codex 下轮额外提醒 "aborted by user"（模型会先检查半截命令而不是假装没发生），Pi 跳过整条半截回答、无结果的统一补 "No result provided"；⑤只是想补充要求用 Steering——先把新消息排队，等当前这批工具执行完、下次调用模型前再注入（tool_use 与 tool_result 之间不能夹别的消息）：Pi 有 steer（本轮工具完后注入）与 followUp（Agent 正常停下才执行）两条队列，Claude Code 补充输入排队同轮提交，Ctrl+Enter 则立即发送、正在跑的 shell 转后台且模型能看到已有输出。

## 关联连接
- [[Agent任务取消]] — 本文核心概念
- [[steering]] — 执行中插话的控制机制
- [[AgentLoop]] — 必须主动检查取消信号的执行循环
- [[ClaudeCode]] — 取消实现的代表产品
- [[Codex]] — CancellationToken 实现对照
- [[Subagent]] — 子智能体的取消信号归属
