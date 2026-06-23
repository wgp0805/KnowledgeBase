---
title: "Web-access"
type: entity
tags: [实体, Skill, 浏览器控制]
sources: [raw/01-articles/分享8个codex必装的skill，让你的AI能力起飞！.md]
last_updated: 2026-06-23
---

## 定义
Web-access 是一个 Codex Skill，当官方 Chrome 插件不可用时，通过 Chrome DevTools Protocol (CDP) 控制真实浏览器，实现网页操作、截图、滚动、读取动态加载内容等功能。

## 关键信息
- **核心功能**：操控用户自己的 Chrome 或 Edge 浏览器，支持登录态访问
- **技术原理**：基于 Chrome DevTools Protocol (CDP)
- **使用前提**：需要打开浏览器远程调试开关
  - Edge: `edge://inspect/#remote-debugging`
  - Chrome: `chrome://inspect/#remote-debugging`
- **适用场景**：动态内容网页、需要登录的页面、浏览器自动化流程

## 关联连接
- [[摘要-codex必装skill推荐]] — 来源
- [[Codex]] — 所属 AI 工具
- [[Skill]] — 技能扩展机制
- [[Agent-Reach]] — 相似 Skill
