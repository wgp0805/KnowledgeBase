---
title: "摘要-Claude-Code与Grok-Bot被拆开后"
type: source
tags: [来源, AI产品, Agent, 产品分析, 护城河]
sources: [raw/01-articles/2026-08-26-Claude Code 与 Grok Bot 被拆开后：AI Agent 真正难复制的是什么？.md]
last_updated: 2026-08-27
---

## 核心摘要
2026 年两起事件：3 月 31 日 Claude Code 2.1.88 发布资产误带内部调试文件，暴露约 2000 个文件、50 万行内部代码；8 月 11 日 Grok Bot 以 Early Beta 推出后，外部开发者依据 0.18.0 客户端 Source Map 重建运行层。两起事件降低了外界理解 AI Agent 的成本，却没有让成熟产品的全部价值随代码转移。作者提出复制 AI Agent 的四层框架（代码复制/功能复制/产品复制/商业复制）和"任务托付能力"五维度框架（完成/控制/验证/恢复/积累）。核心论点：源码可以复制产品的骨架，却不能直接复制用户为什么愿意把工作交出去；AI Agent 最深的护城河不是让竞争者看不见它怎样工作，而是即使代码、功能和结构已被看见，用户仍然更愿意把下一项工作交给它。

## 关键信息
- **Claude Code 事件**：发布打包失误，暴露内部架构/功能开关/产品指令/未上线功能方向；Anthropic 定性为人为失误，无客户数据或凭证受影响
- **Grok Bot 事件**：非官方重建项目，保留打包 Renderer，恢复运行代码，新增 Claude Code/Codex/OpenRouter 路由和本地 Docker 沙箱
- **四层复制框架**：
  1. 代码复制：任务循环/工具连接/上下文管理/权限判断/异常处理
  2. 功能复制：Memory/Skills/Routines/Sub-agents/MCP/浏览器终端操作/审批/后台任务
  3. 产品复制：任务完成率/稳定性/人工接管率/权限体验/验证恢复/工作流沉淀
  4. 商业复制：分发获客/账号计费/企业采购/部署运维/成本管理/合规/持续升级
- **任务托付能力五维度**：
  1. 完成能力：Agent 说完成 ≠ 任务真完成，要定义现实环境最终应发生什么、什么证据证明完成
  2. 控制能力：自主权通过任务逐步获得——读取→待审核草稿→范围清晰动作→有限自动化→无人值守
  3. 验证能力：同时降低执行成本和验证成本；从完整轨迹提取真正影响判断的证据
  4. 恢复能力：阻止错误和恢复错误是两套不同能力；可逆/可补偿/不可逆操作分层处理
  5. 积累能力：长期价值来自工作方法而非聊天记录；积累也要能查看/修改/删除/判断适用范围/发现过期
- **审批疲劳**：Anthropic 披露用户批准约 93% 权限请求；提示越多用户越难认真判断
- **Grok Bot 共享电脑**：一名用户所有 Bot 共享一台持久化云电脑，不应当成彼此隔离的安全边界
- **Claude Code 商业数据**：2026-02 年化收入运行率超 25 亿美元，企业贡献超一半收入
- **PM 五条建议**：发布资产纳入验收、用任务链路代替竞品名词对齐、PM 参与定义 Agent 评测、同时设计权限与恢复、衡量用户是否真正开始托付任务

## 关联连接
- [[ClaudeCode]] — 源码暴露事件主角
- [[GrokBot]] — 运行层被重建事件主角
- [[Anthropic]] — Claude Code 母公司
- [[TaskDelegationSystem]] — 本文核心概念，任务托付能力五维度
- [[SourceMap]] — 两起事件的技术载体
- [[AutoMemory]] — Claude Code 记忆能力
- [[Checkpoint]] — Claude Code 恢复能力
- [[Skills]] — Claude Code/Grok Bot 共有的流程沉淀
- [[Hooks]] — Claude Code 确定性护栏
- [[Subagent]] — Claude Code 子 Agent
- [[MCP]] — 模型上下文协议
- [[OpenRouter]] — Grok Bot 重建项目新增路由
- [[Codex]] — Grok Bot 重建项目新增路由
- [[Docker]] — Grok Bot 重建项目可选沙箱
- [[Axios]] — 报道 Claude Code 事件的媒体
- [[BorisCherny]] — Anthropic 首席工程师（关联 Claude Code 评测演进）
