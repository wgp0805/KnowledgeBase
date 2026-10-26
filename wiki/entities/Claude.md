---
title: "Claude"
type: entity
tags: ["Anthropic", "AI-Agent"]
sources: [raw/01-articles/2026-09-19-Kimi向左，Claude、GPT向右.md, raw/01-articles/2026-09-19-Anthropic 优化 30 多个生物模型，蛋白质设计成本最高降 98%.md, "raw/09-archive/2026-10-25 - 刚刚，Claude自动模式将全球上线！OpenAI曝出最恐怖一幕.md"]
last_updated: 2026-10-26
---

# Claude

Claude 是 Anthropic 的 AI 产品线，包含模型层（Opus/Sonnet）、CLI 层、Harness 层（Claude Code）、Agent 层。不同形态体验差距大：网页版、APP、CLI、Agent 各有定位。

## 封号风波与地区识别争议（2026-06 至 2026-08）

来自 [[摘要-codex重置的真正原因]]。2026-06-24 [[Anthropic]] 指控与阿里有关的操作者使用约 2.5 万个欺诈账户与 Claude 进行 2880 万次交互以蒸馏模型能力，6 月底中国开发者社区集中出现 Claude 账号被停用的反馈。之后 Claude Code 又被发现加入了未充分披露的地区识别与请求标记代码（涉及时区、代理设置等信息），Anthropic 工程师称是防止账号转售与模型蒸馏的反滥用实验，并在争议出现后回滚。此事件构成一个[[竞品迁移窗口]]，详见 [[Anthropic]] 与 [[竞品迁移窗口]]。

## 产品合并路线（2026-09-16）

Claude 把独立 Chat 和 Cowork 合并成一个 Claude，在做减法。与 [[ChatGPT]]（OpenAI 7 月把 Codex App 并入新版 ChatGPT 桌面应用）形成对比，而 [[KimiCode]] 还在做加法。详见 [[摘要-kimi向左claude-gpt向右]]。

## 优化生物模型（2026-09-19）

Anthropic 让 Claude 用不到四周优化 30 多个生物研究开源模型，开发 FlashPairformer 自定义 kernel 加速 triangle attention，蛋白设计成本最高降 98%。详见 [[摘要-anthropic优化生物模型]]。

## 自动模式全球默认开启（2026-10-25 报道）

报道称"下周起" Claude 将全球默认开启 [[auto-mode]]：从"每走一步弹窗问允许"转为哪步能做、哪步不能做全凭另一个 AI 拍板。Anthropic 的两大依据（AI 产出人类审不过来；1053 名付费测试者实测人类拦截率仅 13.6%、AI 89%、弹窗疲劳后约 5%）见 [[Anthropic]]；Anthropic 未披露拍板机制，OpenAI 的 [[多级AI监控]] 可作参考。与 [[auto-mode]] 已记载的"Claude Code 2.1.284 起未手动配置时交互会话默认 auto"属同一趋势的产品级/全球默认化节点，详见 [[摘要-claude-auto-mode监控逃逸]] 与 [[监控逃逸]]。

## 关联连接
[[Anthropic]], [[Opus]], [[Claude-Code]], [[CLI]], [[沉默王二]], [[竞品迁移窗口]], [[摘要-codex重置的真正原因]], [[摘要-kimi向左claude-gpt向右]], [[摘要-anthropic优化生物模型]], [[ChatGPT]], [[KimiCode]], [[FlashPairformer]], [[auto-mode]], [[权限模式]], [[多级AI监控]], [[监控逃逸]], [[摘要-claude-auto-mode监控逃逸]]
