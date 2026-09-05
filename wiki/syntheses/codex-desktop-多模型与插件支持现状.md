---
title: "Codex 桌面版第三方模型与插件的支持现状"
type: synthesis
tags: [Codex, 多模型, 插件, cc-switch, Codex++]
sources: []
last_updated: 2026-08-05
---

# Codex 桌面版第三方模型与插件的支持现状

## 结论
Codex 桌面版对第三方模型与插件的支持是"半开放"的：cc-switch 这类配置工具绕不开桌面端 model picker 的显示问题，Codex++ 在模型列表上更稳定，而插件的高级能力被锁定在 ChatGPT 账号体系内。官方订阅是唯一开箱即用、无折腾成本的路径，但代价是只能用官方模型、接不了国产模型。

## 一、cc-switch 对 Codex 桌面版的多模型支持并不友好
- CC Switch 官方虽将 Codex 列入 7 个被管工具之一（支持 Codex CLI 与桌面端统一配置），但**桌面版的模型列表显示链路先天不顺**。
- GitHub farion1231/cc-switch 的 issue #3340 / #3605 / #4013 大量用户反馈"自定义模型在 Codex Desktop 的模型选择器里消失/为空"，需重启、清缓存甚至重装 Codex 才恢复。
- 直到 v3.16.5，CC Switch 才通过生成 `~/.codex/cc-switch-model-catalog.json` 让桌面端真正显示国产模型（MiMo / 豆包 / Qwen3-Coder / LongCat / MiniMax 等原生 Responses 供应商）。
- 注意边界：**不友好主要针对桌面版 App 的 model picker**，CC Switch 对 Codex CLI 的支持是稳定的。

## 二、插件功能：基础可用、高级受限
- Codex 桌面版支持四类插件：Chrome 扩展、MCP 服务器、Skills、第三方 App（GitHub / Slack / Gmail / Drive）。基础类（Chrome / MCP / Skills）API Key 模式也能跑。
- **高级插件受限**：依赖 ChatGPT 账号体系的第三方 App 插件需 OAuth 授权，官方文档明确"API Key 模式下某些功能可能不可用"，甚至安装时显示 "App unavailable"（openai/codex issue #16903）。

## 三、"不能使用 GitHub 插件市场"说法不准确
- Codex 的 marketplace 机制本身支持 GitHub 源，CLI 下 `codex plugin marketplace add owner/repo` 完全可用；官方文档支持仓库级/个人级 marketplace。
- 真正的坑是**桌面版 UI 添加 marketplace 有 bug**：openai/codex issue #21959 记录 Windows 上点 "Add marketplace" 只报通用错误 "Failed to add marketplace"、无诊断信息、会留脏状态，最终需用 CLI `codex plugin marketplace remove` 删掉重加才能解决。
- 准确表述：**CLI 能用、桌面 UI 有 bug、API 模式受账号体系限制**。

## 四、展示多模型列表：Codex++ 优于 cc-switch
- cc-switch issue #3340 评论区有用户直接实测对比："开启codex++显示模型，只用ccswitch不显示"、"我也装了c++模型显示正常"。
- Codex++（BigPizzaV3/CodexPlusPlus）通过外部 launcher + Chromium DevTools Protocol（CDP）注入脚本直接接管模型列表，比 CC Switch 走 `config.toml` 模型目录链路更稳。
- 二者定位不同：CC Switch 是**全局路由/配置管理器**（7 工具、50+ 预设、本地代理协议翻译、用量监控）；Codex++ 是**仅针对 Codex 桌面的增强器**（插件解锁、会话管理、中转注入、CDP 注入）。
- 选型：多工具、多密钥、需用量管控 + CLI 场景优先 CC Switch；仅用 Codex 桌面、侧重插件与会话优化优先 Codex++。

## 五、官方订阅是最省心但最受限的路径
- 官方订阅（ChatGPT Plus/Pro）下原生模型和插件都正常，无需折腾。
- 但官方订阅只能用官方模型，**接不了 DeepSeek、国产模型**——这正是大家使用 cc-switch/Codex++ 的初衷。
- 补充反例：官方订阅偶尔也有账号级 feature-flag bug（issue #16903 某 Plus 账号只显示 "Skills" 不显示 "Plugins"，需手动 `[features] plugins = true` 强开），属 OpenAI 侧偶发问题，非常态。

## 关键事实核对表
| 说法 | 验证结论 |
| --- | --- |
| cc-switch 对 Codex 桌面多模型不友好 | ✅ 正确（桌面 model picker 链路问题，v3.16.5 才补 model-catalog 修复） |
| 解锁插件可用但高级功能受限 | ✅ 正确（第三方 App 插件依赖 ChatGPT OAuth） |
| 不能使用 GitHub 插件市场 | ⚠️ 不准确（CLI 可用；实为桌面 UI 的 marketplace 添加 bug） |
| 展示多模型列表 codex++ 更好 | ✅ 正确（有用户实测对比佐证） |
| 官方订阅就没问题 | ✅ 基本正确（但受限于官方模型，偶有账号级 bug） |

## 关联连接
- [[Codex]] — 被讨论的目标产品
- [[ClaudeCode]] — 对标产品（插件市场/账号体系对比）
- [[MCP]] — 插件中的关键工具协议
- [[Skill]] — 插件携带的技能扩展
- [[摘要-codex-vs-claude-code-对比]] — Codex vs Claude Code 整体对比来源
- [[AI中转站]] — 同类"绕开官方账号接入国产模型"场景