---
title: "摘要-gpt6-tripo-清明上河图3d游戏"
type: source
tags: [来源, 原始文件, 3D, AI游戏, Tripo, GPT-6]
sources: [raw/09-archive/2026-09-18-从 Demo 到3D游戏，GPT-6 加 Tripo 把清明上河图“整活”了！.md]
last_updated: 2026-09-20
---

## 核心摘要
作者用 GPT-6 Astra 调度 Tripo 生成人物与道具，再用 Three.js 搭场景，把《清明上河图》网页 Demo 做成有剧情动画、互动人物和收集任务的 3D 游戏。Tripo 是 3D 基座模型，可直接把文字/图片变成生产级 3D 资产，P2.0 模型秒级完成人物建模，支持 API/CLI/Codex 插件三种调用方式，自带绑骨、idle 待机动画、动画重定向和自动分件能力。工作流为"GPT-6 Astra 总指挥 + Tripo 生成 GLB 资产 + Three.js 搭场景 + frontend-design 技能做界面"。量产技巧：把人物生成过程打包成 Skill 作为 3D 配方复用、用动画重定向迁移动作、拆解成 5 个并行进程分批验收。虹桥场景一次做出 45 个人物，配音用豆包 Seed-TTS 2.0。

## 关联连接
- [[Tripo]] — 3D 基座模型
- [[GPT-6]] — 总指挥模型
- [[Three.js]] — 游戏场景搭建
- [[Blender]] — 早期建模工具（对比）
- [[Codex]] — Tripo 插件接入
- Seed-TTS — 配音模型
- Seedream5.0 — 人物平面三视图生成
- [[动画重定向]] — 批量动作迁移
- [[绑骨]] — 一键骨骼绑定
- [[鲸选AI]] — 作者