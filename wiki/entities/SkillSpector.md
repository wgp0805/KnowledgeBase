---
title: "SkillSpector"
type: entity
tags: [开源工具, NVIDIA, Agent技能, 安全扫描]
sources: [raw/09-archive/2026-10-06-盘点 20 个 9 月份 GitHub 上顶顶顶的开源项目。.md]
last_updated: 2026-10-08
---

## 定义
SkillSpector 是 NVIDIA 开源的 Agent Skill 安全扫描工具，在安装第三方 Agent 技能前检查仓库、压缩包、目录或单个文件，寻找提示注入、数据外传、危险代码和权限相关风险，2026 年 9 月月增约 3500 Star。

## 关键信息
- **检查对象**：仓库、压缩包、目录、单个文件
- **风险类型**：提示注入、数据外传、危险代码、权限相关风险（例如技能说明里夹带"向外部地址上传本地文件"的指令）
- **输出**：报告含风险等级、问题位置和建议，再决定怎样处理
- **定位**：适合放进第三方技能安装前的检查流程；报告中的问题仍需结合具体文件和行为判断
- **GitHub**: <https://github.com/nvidia/skillspector>
- **月增 Star**: 约 3500（2026-09）

## 关联连接
- [[摘要-20个9月github热门开源项目]] — 来源
- [[AgentSkill安全扫描]] — 该文提炼的概念
- [[ai-agent-skill]] — 被扫描的对象机制
