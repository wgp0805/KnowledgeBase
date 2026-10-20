---
title: "摘要-jd-codex辞职信-agent面试题"
type: source
tags: [来源, 原始文件, Agent面试题, PaiCLI, 多租户]
sources: [raw/01-articles/JD员工：同事觉得电脑太卡，我用Codex帮他修，结果不小心看到他正在写的辞职信还有已经到手的offer，该不该跟领导说呢（附Agent面试题）.md]
last_updated: 2026-10-20
---

## 核心摘要
沉默王二以"用 Codex 帮同事修电脑意外看到辞职信"的职场分寸感话题开篇（结论：看破不说破），随后介绍京东 AI 布局（言犀 JoyAI 系列大模型、JoyCoder、JoyAgent 与开源 JoyAgent-JDGenie），主体是 5 道 Agent 工程面试题的深度解答，全部以 PaiCLI 与"派聪明"两个项目为实战背景：① 最大工程挑战——上下文膨胀与 JVM 内存失控，三档渐进式压缩（超 32000 字符工具输出卸载落盘、旧 tool 消息占位清理、逼近窗口时结构化摘要）+ Jackson 流式写出请求体，1M token 场景单次请求堆分配从 90.5MB 降到 4.7MB；② 多租户隔离——知识库 (file_md5,user_id,chunk_id) 复合唯一键 + KNN 预过滤注入权限、Redis Lua 令牌桶租户配额 + 后台任务预留 30% 在线令牌、沙箱从路径守卫/环境变量清洗到 Firecracker 微虚拟机分级；③ 千级沙箱资源池——预热池+休眠池+冷镜像三级结构、会话亲和 + 闲置 60 秒自动冻结（cgroup freezer + 内存增量转储）；④ 会话状态恢复——对话历史 MySQL+Redis 双写 / 本地 JSONL view_checkpoint、带心跳租约的租约状态机、幂等键与影子 Git PRE_TURN 快照防副作用重放；⑤ 长周期行为漂移——目标约束固定注入系统提示词不参与压缩、JSON 任务图拓扑校验、摘要四要素结构校验、编辑后 JavaParser 语法诊断注入。附 PaiCLI 简历写法。

## 关联连接
- [[PaiCLI]] — 面试题主要实战项目
- [[京东]] — 京东 AI 布局介绍
- [[JoyAgent]] — 京东 Agent 平台
- [[多租户隔离]] — 面试题 2 核心概念
- [[沙箱]] — 沙箱资源划分与隔离
- [[上下文压缩]] — 三档渐进式压缩
- [[沉默王二]] — 作者
- [[Agent面试题]] — 题目所属系列
