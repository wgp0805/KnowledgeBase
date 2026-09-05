---
title: "AgentBro"
type: entity
tags: [AI-Agent管理工具, macOS, 开源项目, Skill治理]
sources: [raw/09-archive/别再乱装skill了，这个开源项目教你如何有效管理Skill.md]
last_updated: 2026-07-29
---

## 定义

AgentBro 是由程序员追风（石人闯，GitHub: shirenchuang）自研并每日自用的 macOS 端 AI Agent 管理工具。它将原本分散在各个 Agent（Claude Code、Codex、ZCode、Trae、Qoder、豆包等）目录下的 Skill 集中治理，提供"中心库唯一事实源 + 软链接分发 + 技能包开关 + 扫描接管存量 + 冲突检测 + 测试包观察期 + 远程管理"的完整闭环能力。

## 关键信息

**核心架构原则：**
- **中心库是治理上的唯一事实源**：源码可留在个人 Git 项目，真正分发给 Agent 的关系只能从中心库出去
- **软链接分发**：个人 Git 项目 → 软链接导入中心库 → 软链接分发到各 Agent，修改源码即同步生效，需冻结快照时可复制导入
- **技能包即开关**：中心库当库存，技能包当开关。长期不用的不分发；偶尔用的留在对应技能包；生产环境只开稳定必要的最小集合
- **技能包非文件夹**：一个 Skill 可同时属于多个技能包（按来源、工作场景、稳定性分别组织），多包开启取并集，共同 Skill 只生效一次

**核心功能模块（11大 Case）：**
1. **自研 Skill 软链接分发**：解决多 Agent 同步更新难题
2. **中心库唯一事实源**：解决同一 Skill 在不同 Agent 版本不一致
3. **扫描接管存量**：扫描已安装 Agent 目录，把未管理的 Skill 放入待处理区，无冲突批量接管并替换为指向中心库的软链接
4. **同名冲突检测与决策**：扫描出同名冲突时单独标出，默认中心库版本优先，确认需并存才重命名，偶尔 Agent 版本更新则反向覆盖中心库
5. **技能包治理库存与生效**：中心库展示 Skill 库存、Agent 安装数、未管理数量；技能包按来源/场景/稳定性组织，生产仅开最小稳定集合
5. **社区 Skill 试用区**：新见 Skill 先进 `NiceTry-测试`，验证好用再进稳定 `NiceTry`；创作者批量 Skill 直接组成技能包（如 `anthropics/skills`），来源用途不混淆
6. **开发中 Skill 隔离**：不稳定 Skill 移入测试包（如 `SZ-内容创作-测试中`），调试时开启、正式任务关闭，避免误触发干扰调试
7. **多技能包引用同一 Skill**：技能包取并集，共同 Skill 只生效一次；关掉测试包后因创作者包仍生效；全关才真正失效
8. **公司/个人 Skill 隔离**：技能包生效状态按 Agent 独立管理，公司 Agent 只用公司包，个人 Codex 用个人包
9. **菜单栏快捷开关**：macOS 菜单栏点开即选 Agent、勾选技能包，马上生效，降低切换成本
10. **远程服务器统一管理**：维护共用远程服务器列表，可从 `~/.ssh/config` 导入；SSH 隧道（本地监听 7399）接收远程 Agent 事件；远程需装 `agentbro-remote`；本地可在本机/远程间切换管理环境
11. **诊断与 Hooks 管理**：远程连接后同一条 SSH 管道做 Agent 管理、诊断、Hooks 管理

**项目地址：** https://github.com/shirenchuang/agentbro

**当前规模（文中数据）：** 中心库 213 个 Skill，各 Agent 累计 244 份安装；一次扫描发现 86 个可接管 Skill 与 19 个同名冲突

**支持的 Agent：** Claude Code、Codex、ZCode、Trae、Qoder、豆包等

**作者：** 程序员追风（石人闯，微信公众号作者）

## 关联连接

- [[摘要-agentbro-skill-management]] — 来源摘要
- [[AgentBroRemote]] — 远程管理组件
- [[AgentBroMarket]] — 技能市场
- [[ClaudeCode]] — 支持的 Agent
- [[Codex]] — 支持的 Agent
- [[Skill]] — AI Agent 技能扩展机制
- [[SkillPackage]] — 技能包概念
- [[SkillCentralLibrary]] — 中心库概念
- [[SkillSoftLink]] — 软链接分发机制
- [[SkillScanTakeover]] — 扫描接管机制
- [[SkillConflictResolution]] — 同名冲突解决
- [[SkillTestPackage]] — 测试包观察期
- [[AgentSpecificSkillPackages]] — Agent 维度技能包隔离
- [[RemoteAgentManagement]] — 远程 Agent 管理
- [[ShirenChuang]] — 作者实体