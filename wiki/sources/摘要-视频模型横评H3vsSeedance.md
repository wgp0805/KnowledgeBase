---
title: "摘要-视频模型横评H3vsSeedance"
type: source
tags: [来源, 原始文件, 视频生成, 模型横评]
sources: [raw/01-articles/2026-08-25-烧掉500块实测H3、Seedance 2.0 fast，意外挖出了性价比之王（附全部提示词）.md]
last_updated: 2026-08-26
---

## 核心摘要
同一提示词、同一分辨率、同一平台下对 MiniMax H3 与 Seedance 2.0 fast 进行 8 场景横评（真人表演、宫斗短剧、视觉动效、TVC广告、科幻电影、特效渲染、游戏场景、动画打戏）。结果 Seedance 2.0 fast 整体更稳，指令遵循和镜头连贯明显优于 H3；H3 在视觉动效和广告场景各有优势。Seedance 2.0 fast API 价格 0.6 元/秒，与 H3 的 0.5 元/秒相近，性价比最高。

## 关键洞察
| 场景 | 胜者 | 说明 |
|------|------|------|
| 真人表演 | Seedance 2.0 fast | 指令遵循强，情绪变化连续细腻 |
| 宫斗短剧 | Seedance 2.0 fast | 电影感更强，H3 有塑料感 |
| 视觉动效 | H3 | 节奏卡点更带感 |
| TVC广告 | Seedance 2.0 fast | 故事感更强 |
| 科幻电影 | Seedance 2.0 fast | H3 黑洞劣质，AI味明显 |
| 特效渲染 | Seedance 2.0 fast | 光影处理到位，音效还原 |
| 游戏场景 | Seedance 2.0 fast | 更像 3A 大作，H3 像页游 |
| 动画打戏 | Seedance 2.0 fast | H3 易出慢动作，打斗偏弱 |
| **综合** | **Seedance 2.0 fast** | **性价比之王** |

- **Seedance 2.5** 是断档式领先，但非本次横评重点
- **H3 部署要求**：最低 80GB GPU，理想 4×H100/H200，整套约 150 万，API 反而更划算
- **Seedance 2.0 fast 特点**：约 2.0 性能 80%，15s 视频不到 1 分钟生成
- **H3 优势**：视觉特效、中文不乱码、广告场景

## 关联连接
- [[MiniMax]] — H3 模型厂商
- [[Seedance]] — 字节 Seedance 视频模型系列
- [[Seedance2.5]] — SOTA 级视频模型
- [[VideoGeneration]] — 视频生成技术
- [[TokenEfficiency]] — token 效指标（成本控制）
- [[PromptEngineering]] — 提示词工程（横评使用统一提示词）
- [[GPU]] — 硬件基础设施
