---
title: "Agnes"
type: entity
tags: [AI产品, 图像生成, 视频生成, MCP, 生图]
sources: [raw/09-archive/2026-09-29-我用 WorkBuddy + Agnes一句话生成短视频，没花一分钱.md]
last_updated: 2026-10-08
---

## 定义
Agnes 是提供图像生成与图生视频能力的 AI 平台，提供免费档额度，可通过 `agnes-ai MCP` 连接器接入 WorkBuddy 等 Agent 工具，是"零成本 AI 短视频流水线"中唯一吃外部资源但走免费档的环节。

## 关键信息
- **接入方式**：在连接器官方页信任 `agnes-ai MCP`、填入自己的 Agnes 免费档密钥（免费档即可）
- **免费档限制**：需串行调用、段与段间隔 ≥30 秒，否则会撞 429 限流；WorkBuddy 可自动写批处理脚本一次排队多段挂着等
- **能力分工**：出图与图生视频；旁白（edge-tts）、备用生图（混元 Hy Image 3.5）、剪辑合成（ffmpeg 本地）均不依赖 Agnes
- **短板**：中文文字准确度明显弱于混元 Hy Image 3.5，文字要求高的画面建议用混元备用方案；配音能力早期被作者评价为"不太好用"（后由 edge-tts 替代）

## 关联连接
- [[摘要-workbuddy-agnes-短视频]] — 来源
- [[WorkBuddy]] — 接入 Agnes 的宿主工具
- [[AI视频生成]] — 所属技术领域
- [[腾讯混元]] — 备用生图方案的开发方
