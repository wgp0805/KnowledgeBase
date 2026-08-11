---
title: "摘要-京东-agent面试题"
type: source
tags: [京东, AI Agent, 面试题, 电商, AI Coding]
sources: [raw/01-articles/京东员工：实习生、应届生结合JoyCoder写的代码一坨屎，我Code Review的时候真是一口老血吐屏幕上，这种情况怎么办啊？（附Agent面试题）.md]
last_updated: 2026-08-11
---

## 核心摘要
文章由 [[沉默王二]] 撰写，以"京东员工吐槽实习生用 [[JoyCoder]] 写出的代码一团糟"为切入点，指出 AI Coding 只降低了"写完代码"的门槛、没有降低"写好代码"的门槛。随后介绍了 [[京东]] 的 AI 产品线（JoyAI-LLM Flash 基础大模型、JoyAI-Image-Edit 图像模型、[[JoyAgent]] 云平台与开源 JoyAgent-JDGenie），并完整展开一份"电商智能购物与履约 Agent"的面试题解答：含 AI Agent 与传统工作流/聊天机器人的区别、购物 Agent 模块设计、ReAct 与 Plan-and-Execute 选型、MCP 工具 Schema 设计、幂等与订单状态机防重复下单、库存实时校验与预占、提示词注入四层防御、采销 Agent 与 RAG/工具调用边界，最后给出可直接写进简历的 SmartCart 项目模板。核心方法论：高频标准流程走工作流、复杂场景走 Agent 的混合方案，以及"实时数据走工具调用、低频知识走 RAG"的判断标准。

## 关键信息
- 核心观点：AI Coding 降低"把代码写完"的门槛，但不降低"把代码写好"的门槛；Code Review 仍是质量防线
- 京东 AI 产品线：基础大模型 JoyAI-LLM Flash、图像模型 JoyAI-Image-Edit、具身大尺寸模型 JoyAI-RA、工业大尺寸模型 JoyIndustrial；护城河是"自营零售数据 + 仓储物流网络 + 供应链履约系统"×供应链智能体
- [[JoyAgent]]：京东云 AI Agent 平台，开源 JoyAgent-JDGenie 支持 ReAct 与 Plan-and-Execute，子 Agent、高并发 DAG、跨任务工作流记忆
- Agent vs 工作流 vs 聊天机器人：聊天机器人一问一答；工作流路径固定、响应快成本低；Agent 路径动态、自主规划调工具
- 京东智能客服 = 混合方案：物流/退换货高频流程走工作流，跨订单比价退差价等复杂场景走 Agent
- 购物 Agent 推荐 Plan-and-Execute：先拆搜索→比价→优惠→库存→下单 DAG，无依赖步骤并行，失败触发 replan
- MCP 工具 Schema：每个能力独立封装（搜索与下单必须分离），description 写给模型看、inputSchema 字段要有说明；写操作工具需用户确认
- 防重复下单：幂等键（user_id + session_id + sku_id hash）+ 订单状态机（pending→confirmed→paid）+ 人工确认兜底
- 库存一致性：下单前实时校验 + 乐观锁库存预占 15 分钟 + 售罄自动推荐替代商品（不直接结束）
- 提示词注入防御四层：入口净化（正则+黑名单）→ 上下文角色隔离（system/user/tool_result 分层）→ 工具权限分级（只读自由调、写入需确认）→ 出口内容安全过滤
- 采销 Agent：模型理解业务与编排，数值计算走后端规则引擎；大额补货人工审批、异常波动先告警
- RAG vs 工具边界：看数据实时性——低频知识（售后政策/商品规则/话术）走 RAG，实时数据（订单/物流/券余额/价格）走工具调用，常见为两者交叉比对
- 大促缓存：缓存 TTL 压到秒级，工具返回值带查询时间戳，展示前二次实时校验
- 离线评测 Golden Set 回归；在线评测关注任务完成率、对话轮数、工具调用成功率、用户满意度

## 关联连接
- [[京东]] — 文章主角企业
- [[JoyCoder]] — 京东 AI 编程工具
- [[JoyAgent]] — 京东 AI Agent 平台
- [[沉默王二]] — 作者
- [[ReAct_Agent]] — ReAct 模式
- [[Research-Plan-Execute-Review-Ship]] — Plan-and-Execute 范式
- [[MCP]] — 工具封装协议
- [[RAG]] — RAG 与工具边界
- [[智能客服Agent设计]] — 客服 Agent 架构
- [[提示词注入防御]] — 四层防御框架
- [[idempotency]] — 幂等防重复
- [[乐观锁]] — 库存预占机制
- [[Agent]] — Agent 核心概念