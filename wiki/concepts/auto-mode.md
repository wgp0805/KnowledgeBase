---
title: "auto-mode"
type: concept
tags: [AI编程, 权限, Claude Code, 安全]
sources:
  - raw/09-archive/面试官坏笑：“你用ClaudeCode写代码，不怕它把项目搞炸？”，我：“怕，所以CLAUDE.md、权限和验证，一个都不能少。”.md
  - raw/09-archive/Agent 的权限模式（Permission Mode）了解吗？.md
  - "raw/09-archive/2026-10-25 - 刚刚，Claude自动模式将全球上线！OpenAI曝出最恐怖一幕.md"
  - "raw/09-archive/DeepSeek是如何防止提示词注入攻击的？.md"
last_updated: 2026-11-27
---

## 定义

Auto Mode 是 [[ClaudeCode]] 的权限自动模式，用独立分类器判断操作风险：低风险自动放行，高风险（下载执行陌生代码、发送敏感内容、生产部署、强推、直接 push 到 main）阻断或转人工确认。它解决的是"少点确认"，不负责隔离文件系统、网络和凭据。

## 关键信息

- 切换：CLI 中 Shift+Tab 切换权限模式；需账号/模型/provider/组织设置均满足才出现 auto
- 不提供安全沙箱，高风险任务仍需容器、临时账号、最小权限、deny 规则、[[Hooks]] 和人工 Review
- v2.1.142+ 忽略项目级 .claude/settings.json 中的 auto 设置，防止仓库自启 Auto Mode；应放用户级或组织 managed settings
- Bedrock/Vertex AI/Microsoft Foundry 等 provider 需额外设 CLAUDE_CODE_ENABLE_AUTO_MODE=1
- `--dangerously-skip-permissions` 不建议日常使用，除非文件系统/网络/凭据已隔离
- **分类器内部机制（2.1.210+，2026-10-14 补充）**：分类器默认跑在 Sonnet 5（不随 /model 变）；输入含用户消息、工具调用、CLAUDE.md，**剔除工具结果**（防网页/文件恶意指令）与 **Claude 自己的输出**（防说服分类器放行）；先输出单 token 快速判断，可疑再用思维链复核；连续拦截 3 次或累计 20 次自动暂停退回人工弹窗；正常操作误拦率 0.4%、越权放行率 17%（官方 "the honest number"）。详见 [[权限模式]]
- 2.1.284 起未手动配置权限模式时，终端交互会话默认进入 auto
- **全球默认化节点（2026-10-25 报道）**：报道称"下周起" Claude 全球默认开启自动模式——哪步能做、哪步不能做全凭另一个 AI 拍板；Anthropic 未公开拍板机制，依据是人类监工实测失效：1053 名付费测试者写代码中途注入危险命令，人拦 13.6% vs AI 拦 89%，连点 50+ 次弹窗后人类拦截率约 5%（详见 [[权限模式]]、[[摘要-claude-auto-mode监控逃逸]]）；OpenAI 的 [[多级AI监控]] 可作参考

### 与 DSH 自动审查模式的隔离范围对照（2026-11-26，详见 [[摘要-deepseek防提示词注入]]）

[[DeepSeekHarness|DSH]] 的 [[自动审查模式]] 与本页的 Auto Mode 分类器是**同一思路的两种实现**：都用独立模型在工具调用前判风险。差别在**给审查员喂什么上下文**：

| | Auto Mode 分类器 | DSH 自动审查模式 |
| --- | --- | --- |
| 剔除工具结果 | ✅ | ✅ |
| 剔除模型自身输出 | ✅ | ✅ |
| 剔除主 Agent 系统提示词 | ❌ 保留（含 CLAUDE.md） | ✅ 剔除 |
| 审查员可见 | 用户消息、工具调用、CLAUDE.md | 当前工作目录、用户指令、项目约束、调用参数、待审调用 |
| 风险分级 | 低风险放行 / 高风险阻断或转人工 | `low` 直接放行 / `medium` 需当前用户授权 / `high` 一律拒绝 |

DSH 的隔离面更彻底（连系统提示词都不给审查员看），代价是审查员对「主 Agent 被要求做什么」理解更少，更依赖调用参数本身的可判性。两者的**共同结论**是一致的：审查模型的输入必须**主动剥离可被污染的内容**，不能直接复用主 Agent 的上下文。

## 关联连接

- [[ClaudeCode]] - 所属工具
- [[CLAUDEmd]] - 配合的项目规范
- [[Hooks]] - deny 规则的补充拦截
- [[权限模式]] - 权限模式总概念
- [[code-review]] - 安全审查实践
- [[摘要-claude-code-实战防搞炸]] - 来源
- [[摘要-agent-permission-mode深度解析]] - 2026-10-14 分类器内部机制来源
- [[摘要-claude-auto-mode监控逃逸]] — 2026-10-25 全球默认化与监控审计来源
- [[监控逃逸]] — AI 监控被绕过的六条暗道
- [[多级AI监控]] — OpenAI 参考方案
- [[自动审查模式]] — DSH 侧同类实现（隔离范围更彻底）
- [[摘要-deepseek防提示词注入]] — 来源（隔离范围对照）
- [[提示词注入防御]] — 上位防御体系
- [[DeepSeekHarness]] — 对照实现所在框架
