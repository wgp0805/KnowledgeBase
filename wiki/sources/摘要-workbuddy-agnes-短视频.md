---
title: "摘要-workbuddy-agnes-短视频"
type: source
tags: [来源, 原始文件, WorkBuddy, 短视频, AI视频生成]
sources: [raw/01-articles/2026-09-29-我用 WorkBuddy + Agnes一句话生成短视频，没花一分钱.md]
last_updated: 2026-10-08
---

## 核心摘要
作者用 WorkBuddy 当"总导演"、Agnes 管画面、ffmpeg 本地收尾，跑通了外部成本约等于零的高质量短视频流水线，整条链路分七步：①文案 → 脚本/分镜表；②先生成主角人物立绘并配"形象锁定卡"写死长相服装气质（一张图锁全片角色一致，是流水线里性价比最高的动作，不锁则八段画面主角八张脸）；③edge-tts 免费旁白并拿逐字时间戳；④Agnes 图生视频（唯一吃外部资源的环节，走免费档，需串行调用、段间隔 ≥30 秒防 429 限流；备用方案是 WorkBuddy 内置混元 Hy Image 3.5 免费生图，5-10 积分/张，中文文字准确度明显强于 Agnes）；⑤ffmpeg setpts 按旁白时长拉伸对齐画面，原则是"音频优先、画面让路"；⑥烧入双层字幕（底部词级同步台词 + 顶部金色人名条）；⑦concat 滤镜八段合成一次编码成片。成本账：旁白 0 元、人物图 0 元、动图 Agnes 免费档、合成 ffmpeg 本地，一条片外部成本约等于 0，只付出时间。该能力在 WorkBuddy 中以零依赖自定义技能 `free-short-drama`（github.com/ZOORO-NEW/free-short-drama）打包，所有写作/分镜/形象/配音方法论内嵌，一句话即可触发全自动串联；前提是信任 `agnes-ai MCP` 连接器并填入自己的 Agnes 免费档密钥。不装技能也可把七步流程直接贴给 WorkBuddy 分步执行，只是不能一句话全自动。

## 关联连接
- [[WorkBuddy]] — 流水线的"总导演"
- [[Agnes]] — 图生视频环节的外部免费档模型
- [[AI视频生成]] — 所属技术领域
- [[腾讯混元]] — 备用生图模型 Hy Image 3.5 的开发方
