---
title: "TextToCad"
type: entity
tags: [开源项目, CAD, AgentSkill, 3D建模, ClaudeCode]
sources: [raw/09-archive/2026-10-16 - 最近逛GitHub，挖到3个给力的开源项目，第一个比较硬核。.md]
last_updated: 2026-10-19
---

## 定义
text-to-cad 是给 Claude Code、Codex 等 Agent 工具赋予 CAD 建模能力的开源项目（earthtojake/text-to-cad），把建模、查看、导出流程整理成**插件与 Skill**：用户用自然语言描述零件形状和尺寸，Agent 编写本地建模脚本再生成三维文件。面向机械专业学生、机器人比赛团队、硬件工程师、3D 打印爱好者。

## 关键信息
- **参数化工作流**：描述尺寸（整体尺寸/厚度/孔径/孔位）→ Agent 写建模脚本 → 生成三维文件；改需求=改参数重新生成，**模型源码保留**便于迭代
- **导出格式**：STEP（继续在 CAD 软件里加工）、STL 与 3MF（3D 打印）、GLB（三维展示）
- **配套查看器**：打开模型检查形状，再给 Agent 提修改要求
- 开源地址：github.com/earthtojake/text-to-cad

## 关联连接
- [[摘要-github三个开源项目-text-to-cad]] — 来源
- [[程序汪]] — 推荐作者
- [[ClaudeCode]] — 支持的宿主 Agent
- [[Codex]] — 支持的另一宿主 Agent
- [[AgentSkills]] — 能力载体
