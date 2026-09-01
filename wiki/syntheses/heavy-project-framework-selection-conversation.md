---
title: "重型项目 AI 编程框架选型完整对话记录与最终方案"
type: synthesis
tags: [框架选型, OpenSpec, CodeGraph, MattPocock, GSDCore, SpecSuperflow, 重型项目, 棕地项目, 绝对主动权, 日志收集, MCP, 实操指南, 对话记录]
sources:
  - wiki/entities/OpenSpec.md
  - wiki/entities/CodeGraph.md
  - wiki/entities/MattPocock.md
  - wiki/entities/mattpocock-skills.md
  - wiki/entities/GrillMe.md
  - wiki/entities/GSDCore.md
  - wiki/entities/SpecSuperflow.md
  - wiki/concepts/delta-spec.md
  - wiki/concepts/流程税.md
  - wiki/concepts/强模型时代工作流选型.md
  - wiki/syntheses/openspec-brownfield-usage-guide.md
  - wiki/syntheses/openspec-bugfix-workflow.md
  - wiki/syntheses/openspec-archive-modify-and-token-tradeoff.md
  - wiki/syntheses/openspec-working-principle.md
  - wiki/syntheses/heavy-project-impact-analysis-and-planning.md
  - wiki/syntheses/optimal-framework-combination-heavy-project.md
  - wiki/syntheses/openspec-codegraph-usage-guide.md
  - wiki/syntheses/project-analysis-planning-tool-selection.md
  - wiki/sources/摘要-mattpocock-skills.md
  - wiki/sources/摘要-codegraph-deep-dive.md
  - wiki/sources/摘要-codegraph-mcp-gateway.md
  - wiki/sources/摘要-gsd-core-ai工作流.md
  - wiki/sources/摘要-superpowers-openspec-speckit对比.md
last_updated: 2026-08-28
---

# 重型项目 AI 编程框架选型完整对话记录与最终方案

> **定位**：本文是一次完整咨询对话的归纳总结，从初始需求到最终方案，记录了用户提问、框架对比、否决过程、最终选型、安装配置、实操方法的全过程。是 [[optimal-framework-combination-heavy-project]] 和 [[openspec-codegraph-usage-guide]] 的对话溯源。

## 一、对话背景与用户画像

- **用户环境**：重型棕地 Java 项目，集团下发需求，团队中有的用 AI 有的不用，需要混合协作
- **用户能力**：自己知道项目功能都是干什么的，但复杂需求来时怕人工分析有遗漏
- **核心诉求**：AI 帮忙全面分析制定方案，简单代码 AI 写，复杂逻辑自己写，对 AI 产出有绝对主动权

## 二、提问演进时间线

### Q1：初始需求——适合的框架推荐

**用户提问**：项目很重，团队 AI 使用水平参差不齐，没有 AI 相关框架。希望找到适合的框架，简单代码 AI 写，复杂需求自己完成。已用过 OpenSpec（个人使用），寻求类似框架推荐。

**回答**：推荐 spec-superflow（OpenSpec+Superpowers 融合）为首选，备选 OpenSpec+grill-me 极简组合。

**固化**：已记录日志，未单独保存 synthesis。

### Q2：OpenSpec 个人使用时同事代码更新后如何保持 spec 准确

**用户提问**：OpenSpec 个人使用时，同事不用 AI 改了代码，spec 怎么保持准确？

**回答**：核心是"拉取即核对"纪律 + Delta Spec 补录 + `/opsx:sync`。OpenSpec 的 spec 是静态文档，不会自动扫描代码变更，依赖人工诚实和手动补录。

**固化**：[[openspec-team-sync-personal-use]]

### Q3：结合项目给出需求规划方案最全面的工具

**用户提问**：希望结合现有项目进行分析、给出方案规划，哪个工具最全面？

**回答**：推荐 GSD Core（`/gsd-map-codebase` 主动分析代码库），是唯一有主动分析代码库能力的框架。

**固化**：[[project-analysis-planning-tool-selection]]

### Q4：SpecSuperflow 是不是电信内部插件

**用户提问**：SpecSuperflow 是电信内部的插件吗？

**回答**：不是。SpecSuperflow 是 MageByte-Zero 开发的开源项目（MIT 协议）。

**固化**：即时回答未保存。

### Q5：重型项目怕遗漏——变更影响分析工具

**用户提问**：重型项目怕遗漏，改了代码发现影响其他代码要重构，新需求不知道怎么做，应该用什么？

**回答**：推荐 CodeGraph（`codegraph impact` 变更影响分析）+ GSD Core 组合工作流。CodeGraph 解决"改了才发现要重构"（事前影响分析），GSD Core 解决"新需求不知道怎么做"（需求到方案的引导流程）。

**固化**：[[heavy-project-impact-analysis-and-planning]]

### Q6：Matt Pocock 的 mattpocock-skills 能否满足需求

**用户提问**：Matt Pocock 这个东西能满足我的需求吗？

**回答**：只能满足一半。
- ❌ 变更影响分析：mattpocock-skills 没有影响分析能力，还是得靠 CodeGraph
- ✅ 新需求不知道怎么做：`/grill-with-docs` 需求澄清很合适
- 建议：用 Matt Pocock 替代 GSD Core 的需求讨论和执行流程（更轻量、保留控制权），但 CodeGraph 不可替代

**固化**：即时回答未保存。

### Q7：澄清真实需求——日志收集场景，不满意 GSD Core，要最优组合

**用户提问**（关键转折）：用日志收集场景讲清需求——集团要求收集 4 种日志（登录/权限/前端操作/前端数据流转），集团只给了采集文档，看了项目不知道该咋做。想用注解→发现字段拿不到→放弃→改拦截器。痛点是需求来了不知道怎么办，plan mode 直接实现代码还是不全面。同事有的用 AI 有的不用，AI 写的代码也要足够了解并有绝对主动权。GSD Core 不满意，需要最优框架组合。

**回答**：这是整个对话的转折点。提炼出 4 个硬约束：

| 约束 | 本质 |
|------|------|
| ① 需求来了不知道怎么做 | 需要需求拆解+技术方案探索引导 |
| ② 方案试错成本高 | 需要动手前先分析可行性 |
| ③ 绝对主动权 | 拒绝"框架接管流程"，要人主导+AI 辅助 |
| ④ 同事混合协作 | 产出物必须是人类可读的规范文档 |

**最终方案**：OpenSpec（规划）+ CodeGraph（影响分析）+ Matt Pocock Skills（执行纪律箱）

**否决理由**：
- GSD Core：接管流程，失去控制权 ❌
- SpecSuperflow：八状态机自动驱动，太重 ❌
- Matt Pocock 单独用：没有规划文档存档，同事看不到决策原因 ❌

**固化**：[[optimal-framework-combination-heavy-project]]

### Q8：两个工具的使用方法

**用户提问**：给我这两个工具（OpenSpec + CodeGraph）的使用方法。

**回答**：提供了完整的安装、命令、棕地补录、bug 修复、MCP 接入、配合工作流的实操指南。

**固化**：[[openspec-codegraph-usage-guide]]

### Q9：OpenSpec init 报错

**用户提问**：`openspec-cn init --tools opencode qoder codex claude` 报错。

**回答**：`--tools` 参数只接受一个值，多个工具要用逗号分隔（无空格）：`openspec-cn init --tools opencode,qoder,codex,claude`。`ExperimentalWarning` 只是 Node.js 实验性功能警告，不影响使用。

**固化**：即时回答未保存。

### Q10：基于 opencode 开发的工具能否用 opencode 配置

**用户提问**：我现在用的工具是基于 opencode 开发的，直接使用 opencode 可以吗？

**回答**：可以。`opencode` 是合法工具 ID，OpenSpec 会按 opencode 的目录约定生成 Skills 和 Commands。

**固化**：即时回答未保存。

### Q11：CodeGraph 怎么在 agent 中使用

**用户提问**：codegraph 这个东西怎么在 agent 中使用？

**回答**：通过 MCP 协议接入，三步：`codegraph init -i` 初始化索引 → 配置 mcp.json → agent 自动调用 6 个 MCP 工具。

**固化**：即时回答未保存。

### Q12：每次都要执行 codegraph serve --mcp 吗

**用户提问**：每次使用都要执行 `codegraph serve --mcp` 吗？

**回答**：不需要。配置在 mcp.json 里后，agent 启动时自动拉起，agent 关闭时跟着结束。

**固化**：即时回答未保存。

### Q13：mcp.json 在什么位置

**用户提问**：mcp.json 这个在什么位置？

**回答**：对于 opencode，配置文件在 `C:\Users\w1217\.config\opencode\opencode.jsonc`。也可用 `codegraph install --yes` 自动配置。

**固化**：即时回答未保存。

### Q14：怎么让 agent 用 CodeGraph 根据 OpenSpec 规划文档搜索

**用户提问**：怎么直接告诉 agent 让 codegraph 执行搜索，根据 openspec 给出的规划文档？

**回答**：不需要手动指定。配好 MCP 后 agent 会自动判断何时调用。两种方式：
- 自然语言提需求："根据 design.md 分析要改的符号的影响面"→ agent 自动调 `codegraph_impact`
- 明确指示："读取 design.md，用 codegraph 分析里面要改的每个符号的影响面"

**固化**：即时回答未保存（本文归纳）。

## 三、最终方案总结

### 最优框架组合

| 工具 | 定位 | 解决的约束 | 核心命令 |
|------|------|-----------|---------|
| [[OpenSpec]] | 规划引擎（想清楚再动手+存档） | ①②③④ | `/opsx:explore` `/opsx:propose` `/opsx:apply` `/opsx:archive` |
| [[CodeGraph]] | 变更影响分析（动手前知道影响面） | ② | `codegraph impact <符号> --depth 2` |
| [[MattPocock]] Skills | 执行纪律箱（按需调用） | ③ | `/tdd` `/code-review` `/grill-with-docs` |

### 组合本质

> **OpenSpec 管"想清楚再动手"（规划+存档），CodeGraph 管"动手前知道影响面"（影响分析），Matt Pocock Skills 管"动手时的代码质量"（纪律箱）。三者都是工具，你按需调用，没有任何框架接管你的流程。**

### 完整工作流

```
新需求来了
    │
    ├─ 1. /opsx:explore                    # OpenSpec：探索需求怎么落地
    │
    ├─ 2. /opsx:propose                    # OpenSpec：生成规划工件
    │      → proposal.md / spec.md / design.md / tasks.md
    │
    ├─ 3. codegraph impact <符号>          # CodeGraph：分析改现有代码的影响面
    │      → agent 自动调用，或你用自然语言指示
    │
    ├─ 4. 【人工确认】                      # 你的绝对主动权
    │      → 审查 spec + design + 影响分析
    │
    ├─ 5. /opsx:apply                      # OpenSpec：按 tasks.md 逐项实现
    │      → 可选：/tdd 先写测试、/code-review 审查质量
    │
    └─ 6. /opsx:archive                    # OpenSpec：归档
         → 同事打开 design.md 就能看懂决策原因
```

### 安装配置

```bash
# 1. OpenSpec 中文版
npm install -g @studyzy/openspec-cn@latest
cd /your-project
openspec-cn init --tools opencode    # 多个工具用逗号分隔，无空格

# 2. CodeGraph
npm install -g @colbymchenry/codegraph
codegraph init -i                     # 初始化项目索引
codegraph install --yes               # 自动配置 MCP 到 opencode

# 3. Matt Pocock Skills（选装）
npx skills@latest add mattpocock/skills
# 选择：grill-with-docs, tdd, code-review
```

### CodeGraph MCP 配置

opencode 的配置文件位置：`C:\Users\<用户名>\.config\opencode\opencode.jsonc`

```jsonc
{
  "$schema": "https://opencode.ai/config.json",
  "mcp": {
    "codegraph": {
      "type": "local",
      "command": ["codegraph", "serve", "--mcp"],
      "enabled": true
    }
  }
}
```

配好后 agent 启动时自动拉起 `codegraph serve --mcp`，不需要手动执行。

### 让 agent 根据 OpenSpec 规划文档调用 CodeGraph

配好 MCP 后，agent 会自动判断何时调用 CodeGraph。两种触发方式：
- **自然语言**："根据 design.md 分析要改的符号的影响面" → agent 自动调 `codegraph_impact`
- **明确指示**："读取 design.md，用 codegraph 分析里面要改的每个符号的影响面"

不需要记 CodeGraph 命令名，agent 会自动选择对应工具。

## 四、选型否决记录

| 框架 | 否决原因 | 否决阶段 |
|------|---------|---------|
| [[GSDCore]] | 接管流程，失去控制权，用户明确不满意 | Q7 |
| [[SpecSuperflow]] | 八状态机自动驱动，太重 | Q7 |
| Matt Pocock 单独用 | 没有规划文档存档，同事看不到决策原因 | Q7 |
| spec-superflow（初始推荐） | 用户后续澄清需求后修正 | Q7 |

## 五、关键认知沉淀

1. **"不知道怎么做"的根因是缺乏结构化探索**，不是缺乏流程管控 → OpenSpec explore 解决
2. **"方案试错成本高"的根因是动手前没分析可行性**，不是流程不够重 → OpenSpec design.md + CodeGraph impact 解决
3. **"绝对主动权"的对立面是"框架接管流程"** → 必须选工具箱型而非流水线型 → OpenSpec 人工确认门 + Matt Pocock 纪律箱解决
4. **"同事混合协作"要求产出人类可读文档** → 只有 OpenSpec 的 spec 文档满足 → GSD Core 的内部状态不满足
5. **CodeGraph 通过 MCP 接入后 agent 自动调用**，不需要手动跑命令，配置一次即可
6. **OpenSpec 的 spec 是静态文档不会自动扫描代码**，依赖人工诚实和手动补录（delta spec + sync）

## 六、产出物索引

本次对话产出的 synthesis 页面：

| 页面 | 内容 | 对应提问 |
|------|------|---------|
| [[openspec-team-sync-personal-use]] | OpenSpec 个人使用时同事代码更新后的 Spec 同步策略 | Q2 |
| [[project-analysis-planning-tool-selection]] | 结合项目分析的需求规划工具选型（GSD Core 首选，后被修正） | Q3 |
| [[heavy-project-impact-analysis-and-planning]] | 重型项目两大痛点：CodeGraph + GSD Core 组合（后被修正） | Q5 |
| [[optimal-framework-combination-heavy-project]] | **最终方案**：OpenSpec + CodeGraph + Matt Pocock Skills | Q7 |
| [[openspec-codegraph-usage-guide]] | OpenSpec 和 CodeGraph 完整使用指南 | Q8 |
| 本文 | 完整对话记录与归纳总结 | 全部 |

## 关联连接

- [[optimal-framework-combination-heavy-project]] - 最终方案（本文是其对话溯源）
- [[openspec-codegraph-usage-guide]] - 完整使用指南（本文是其对话溯源）
- [[heavy-project-impact-analysis-and-planning]] - 前一版方案（已修正）
- [[project-analysis-planning-tool-selection]] - 前一版选型（已修正）
- [[openspec-team-sync-personal-use]] - OpenSpec 同事代码同步策略
- [[OpenSpec]] - 规划引擎
- [[CodeGraph]] - 变更影响分析
- [[MattPocock]] - 执行纪律箱作者
- [[mattpocock-skills]] - 执行纪律箱仓库
- [[GrillMe]] - 需求澄清 skill
- [[GSDCore]] - 被否决的方案
- [[SpecSuperflow]] - 被否决的方案
- [[delta-spec]] - 增量变更机制
- [[流程税]] - 避免重流程的理论依据
- [[强模型时代工作流选型]] - 分层加载方法论
- [[openspec-brownfield-usage-guide]] - 棕地项目使用方案
- [[openspec-bugfix-workflow]] - bug 修复流程
- [[openspec-archive-modify-and-token-tradeoff]] - 归档修改与 token 权衡
- [[openspec-working-principle]] - OpenSpec 工作原理
- [[摘要-mattpocock-skills]] - Matt Pocock skills 来源
- [[摘要-codegraph-deep-dive]] - CodeGraph 深度解析
- [[摘要-codegraph-mcp-gateway]] - CodeGraph 多项目网关
- [[摘要-gsd-core-ai工作流]] - GSD Core 来源
- [[摘要-superpowers-openspec-speckit对比]] - 三大框架对比
- [[MCP]] - CodeGraph 接入协议
- [[ClaudeCode]] - 承载平台
- [[OpenCode]] - 承载平台
