---
title: "253k Superpowers 和 60k OpenSpec 被融合了！spec-superflow 工作流登上热榜"
source: "https://mp.weixin.qq.com/s/AU_bsGCKijCH-4cFT5S3sA"
---
程序员追风 *2026年7月13日 22:00*

大模型写代码最大的事故，不是它不会写，而是它在你没想清楚的时候就开始动手，以及在你已经想清楚之后还是动手太随意。

这两个问题，开源社区其实各自有答案。OpenSpec 解决第一个，Superpowers 解决第二个。但现实是，绝大多数团队只装了一个，或者两个都装了却没人手动把它们串起来。

于是Github 有一个「自包含的工作流 owner」，把两者的核心引擎源码级吸收进同一个插件，用一个 8 状态机加 1 个执行契约桥接层，把「想清楚」和「做对路」钉死在同一条流水线上。它叫 spec-superflow。

spec-superflow 已经在 GitHub 开源，MIT 协议。如果你也被 AI 写代码的失控点折磨过，建议直接装上试试，源码就在仓库里，架构、契约模板、状态机都看得见。

仓库地址在这里，点个 Star 支持一下。 [https://github.com/MageByte-Zero/spec-superflow](https://github.com/MageByte-Zero/spec-superflow)

## 站在哪两个巨人肩膀上

先把两位主角说清楚，后面才好讲融合。

### superpowers，一套「纪律优先」的 Agent 方法论

superpowers（作者 obra，目前 [v6.1.1）不是单个提示词，而是一整套面向编程智能体的可组合技能加启动引导。它的核心理念只有一句话，Discipline](http://v6.1.xn--1\),-s18d9bvj13ff7kcc68gs8bui1d2sy37dy4jfin53og1fcpjb5dea34ou33rqfop5e1u2bp4bx1l2yhga2769f042d.xn--,discipline-km8q762d7bt92on9okyan20hnye5w5ez6knp8i/) over vibes，用纪律代替感觉。

它内置 14 个技能，每个技能都是一个带 YAML frontmatter 的 [SKILL.md，靠](http://skill.xn--md,-je0k/) `description` 里的触发条件被 Agent 按需加载。几个关键角色你一定眼熟。

`using-superpowers` 是元技能，也是入口网关。它有一条近乎霸道的规则，哪怕你认为某技能只有 1% 的概率适用，也必须调用它。它在每次会话启动时，被各平台（Claude Code、Cursor、Codex、Copilot CLI 等）的 hook 注入首条消息，变成「正在遵守」的元规则。

`brainstorming` 是创意工作前的强制门禁，一次只问一个问题，给出两到三个方案并推荐，写设计文档到 `docs/superpowers/specs/` ，而且有硬门禁，设计没被批准前禁止任何实现动作。

`test-driven-development` 有一条铁律，没有先写失败测试就写的生产代码必须删除重来，RED 到 GREEN 再到 REFACTOR。

`subagent-driven-development` （SDD）把每个任务派给一个全新的实现子 Agent，每步做 spec 合规加代码质量双裁决，用 `.superpowers/sdd/             progress.md           ` 进度台账抵抗上下文压缩丢失。

`systematic-debugging` 要求先找根因再修，连续三次修复失败就要质疑架构。 `verification-before-completion` 更狠，声明完成前必须在本条消息里真正跑过验证命令并读到输出，把「声称完成」视为一种不诚实。

这套东西的精髓，是它不靠「请你守规矩」的愿望式提示，而是用行为塑形文档去约束 Agent。superpowers 关心的是 Agent 怎么 behave，它的产物是 specs 和 plans 文件，它自己既是规格的作者，也是执行者。

### OpenSpec，一套「规格驱动」的开发系统

OpenSpec（包名 @fission-ai/openspec，目前 [v1.5.0）的定位是「AI-native](http://v1.5.xn--0\)ai-native-li3j6085au89abg7aiv6c/) system for spec-driven development」，一句话心智模型是 agree first, then build confidently，先对齐，再自信地构建。

它解决的是「需求只活在聊天记录里、不可靠、不可追溯」的问题。人和 AI 之间，加一层轻量的约定层（agreement layer）。

它最漂亮的设计是 delta spec。变更里不重写整个规格，只写差异，用 ADDED、MODIFIED、REMOVED、RENAMED 四类区块表达。天然适配存量代码，支持并行变更互不冲突，归档时干净合并进主规格。

默认工作流叫 spec-driven，是一条 artifact 依赖图，proposal 到 specs 到 design 到 tasks，最后 apply。规格和变更文档是 Markdown，配置和 schema 是 YAML，主规格目录 `openspec/specs/` 是事实来源，变更提案放 `openspec/changes/` ，归档落 `openspec/changes/archive/` 。

它还是 agent-friendly 的，多数命令支持 `--json` 输出，有指令注入机制，能直接被 AI 消费。更夸张的是它给 30 多个 AI 编程客户端生成 skill 或 command 文件，Claude Code、Cursor、Codex、Copilot、Kimi、Pi 都不在话下。前置只要 [Node.js](http://node.js/) 20.19.0 以上，用 `npm install -g @fission-ai/openspec` 就能装。

吃透这两位主角后，你会发现一个尴尬的事实。

OpenSpec 让 AI 必须先写规划工件才能动代码，但它管不了执行阶段。superpowers 在执行阶段铁律森严，但它自己也是规划工件的作者和执行者，没把规划层和实现层用一份契约死死钉住。

一个是「想清楚」的专家，一个是「做对路」的教练。可大多数团队，要么只请了一位，要么两位都请了却没人负责把他俩的手牵到一起。

## 设计理念：源码级融合，不是简单并列

spec-superflow 官网文档里有一句我很喜欢的话，它是 source-level fusion, not side-by-side installation，源码级融合，不是简单并列。

这是它和「装两个插件」最本质的区别。它不让你去分别装 OpenSpec 和 superpowers，再把两者手工串起来，而是把两者的核心引擎，源码级吸收进同一个插件。

从 OpenSpec 借来的是规划侧的引擎，Schema、验证、解析。Requirement、Scenario、Delta、Change、Spec 的类型定义，从 proposal 里解析 `## Why` 、 `## What Changes` 与 delta 区块，校验 spec 必须含 SHALL 或 MUST 以及 `#### Scenario:`，实现验证时按 Completeness、Correctness、Coherence 三维度比对 diff 和 spec。

从 superpowers 借来的是执行侧的纪律，TDD 铁律、SDD 子代理驱动、根因调试、代码审查三级严重度、完成前验证。

但光借不够，融合的真正难点在于，怎么把「规划」和「执行」焊成一条流水线。spec-superflow 在这里独创了两样东西。

一样是 contract-builder 桥接层。它把四份规划工件自动压缩成一份 [execution-contract.md，作为规划到实现的唯一交接层（Guarded](http://execution-contract.xn--md,\(guarded-nm8qrxn0c10ek3quoal95bcy3a2xcu89cp07e1unc52i/) Handoff）。没有这份契约，或者契约没被批准，就不准进入实现。

另一样是 8 状态路由引擎，由 workflow-start 这个入口技能承载。它把规划状态机和执行状态机统一成一条显式状态机，并且阻止一切非法跳转。

![图片](assets/253k%20Superpowers%20%E5%92%8C%2060k%20OpenSpec%20%E8%A2%AB%E8%9E%8D%E5%90%88%E4%BA%86%EF%BC%81spec-superflow%20%E5%B7%A5%E4%BD%9C%E6%B5%81%E7%99%BB%E4%B8%8A%E7%83%AD%E6%A6%9C/65194fc249d50b14bc950e6189b1bc06_MD5.png)

spec-superflow 模块架构

所以你说它是站在巨人肩膀上，一点不夸张。但它不是把巨人搬过来摆着，而是把巨人的肌肉拆下来，重新长进自己身体里，再补上巨人们没空做的那块连接组织。整个插件自包含，零运行时依赖，仅 TypeScript 作为 devDependency，不需要你再装 OpenSpec 或 superpowers。

![图片](assets/253k%20Superpowers%20%E5%92%8C%2060k%20OpenSpec%20%E8%A2%AB%E8%9E%8D%E5%90%88%E4%BA%86%EF%BC%81spec-superflow%20%E5%B7%A5%E4%BD%9C%E6%B5%81%E7%99%BB%E4%B8%8A%E7%83%AD%E6%A6%9C/755a668f548f541be4f4197d05dc13c0_MD5.png)

spec-superflow 融合能力矩阵

## 架构设计：模块、组件、数据流

spec-superflow 的代码分两层，一层是嵌入式 TypeScript 引擎，一层是基于技能的工作流层。

### 底座，再实现的 OpenSpec 引擎

`src/` 目录下是它重新实现的 OpenSpec 引擎，编译进 `dist/` 。 `schema/` 里定义 Requirement、Scenario、Delta、Change、Spec， `parsing/` 里是正则解析器， `validation/` 里是校验器。注意，它用的是正则解析，没有引入 Zod 这类运行时校验库，这正是它零运行时依赖的代价与底气。

校验规则很硬。 [proposal.md](http://proposal.md/) 的 `## Why` 不能少于 50 个字符。 [spec.md](http://spec.md/) 每个 Requirement 必须含 SHALL 或 MUST，且至少一个 `#### Scenario:` 块。实现验证时把 diff 和 spec、design 比对，按 Completeness、Correctness、Coherence 三维度判定。

### 中层，9 个核心技能

`skills/` 目录下是 9 个技能，每个技能对应状态机里的一个阶段加一套指令集。

`workflow-start` 是入口，做内容级状态检测、8 状态路由、阻止非法跳转。它读的是工件内容，不是文件时间戳，所以你关掉会话再打开，它能准确判断自己停在哪一步。

`need-explorer` 负责探索，一次一问加方案对比加推荐，把方向失控掐死在萌芽。

`spec-writer` 产出 proposal、specs、design、tasks 四份工件，且由 Schema 引擎实时验证。

`contract-builder` 是独创桥接层，解析引擎自动提取四份工件，压缩成 [execution-contract.md。](http://execution-contract.md./)

`build-executor` 是执行核心，TDD 铁律加 SDD 子代理驱动加 Review Gate 三重纪律。

`bug-investigator` 走四阶段根因分析，三次修复失败必须质疑架构。 `code-reviewer` 做结构化审查，问题分 Critical、Important、Minor 三级。 `release-archivist` 负责验证收口加归档加风险总结。 `spec-merger` 把 delta spec 智能合并回主规范，专门防规范腐烂。

### 数据流，一次完整跑通

把上面的组件连起来，端到端是这样走的。

你说「帮我加一个权限控制」，workflow-start 作为唯一入口先做内容级状态检测，路由到正确的技能。进入 exploring，need-explorer 会问你，要 RBAC 还是 ABAC，粒度多大。确认完进入 specifying，spec-writer 产出四份工件，Schema 引擎当场验证格式。进入 bridging，contract-builder 自动提取，生成 [execution-contract.md。](http://execution-contract.md./)

到这里，会出现整个流程里唯一一次人工介入，契约批准（DP-3）。不批准，不许写一行业务代码。

批准后进入 executing，build-executor 按 TDD 到 SDD 到 Review Gate 的顺序推进。遇到 bug 强制进 debugging，由 bug-investigator 走根因分析，不允许随便试试。收口由 release-archivist 验证加归档，最后 spec-merger 把 delta spec 同步回主规范，防止规范腐烂。

![图片](assets/253k%20Superpowers%20%E5%92%8C%2060k%20OpenSpec%20%E8%A2%AB%E8%9E%8D%E5%90%88%E4%BA%86%EF%BC%81spec-superflow%20%E5%B7%A5%E4%BD%9C%E6%B5%81%E7%99%BB%E4%B8%8A%E7%83%AD%E6%A6%9C/7cfe619a5bcd86ba1ffc04c7cdba6d75_MD5.png)

spec-superflow 端到端数据流

![图片](assets/253k%20Superpowers%20%E5%92%8C%2060k%20OpenSpec%20%E8%A2%AB%E8%9E%8D%E5%90%88%E4%BA%86%EF%BC%81spec-superflow%20%E5%B7%A5%E4%BD%9C%E6%B5%81%E7%99%BB%E4%B8%8A%E7%83%AD%E6%A6%9C/80c960a2d69b8d9324cf3030e7db14ac_MD5.png)

spec-superflow 八状态机

它还有两条快速路径。hotfix 是改动不超过两个文件、不引入新模块时，可以跳过完整规划工件，但仍必须先生成一份最小 [execution-contract.md](http://execution-contract.md/) 并完成 DP-3。tweak 是不超过四个文件、纯配置或文档修改时，直接编辑。

你看，哪怕是小修小补，那道契约硬墙也始终立着。

## 使用方式：装好，说一句话就够了

spec-superflow 不是单一平台插件，而是多平台、单一源。同一套 skills、scripts、docs、templates、hooks，通过各平台 manifest 和安装器分发到 17 个客户端。

### 安装

以 WorkBuddy 为例，一句话搞定。

```
npx spec-superflow@latest install-workbuddy
```

本地调试可以用绝对路径，先预览再装。

```
node /绝对路径/spec-superflow/scripts/
            spec-superflow.mjs
           install-workbuddy --local /绝对路径/spec-superflow
ssf install-workbuddy --dry-run
```

Claude Code 走插件市场。

```
/plugin marketplace add MageByte-Zero/spec-superflow
/plugin install spec-superflow@spec-superflow
```

Cursor 用户直接跑安装器。

```
npx spec-superflow@latest install-cursor
```

全局 CLI 也行， `npm install -g spec-superflow` 之后用 `ssf` 命令，比如 `ssf validate <dir>` 校验工件， `ssf state <sub> <dir>` 看状态。

### 启动

装好之后，对 Agent 说一句话就能拉起整套流水线。

```
用 workflow-start 开始
```

新功能开发时，你说「加一个 SSO 登录」，AI 会先问清 SAML、OIDC、账号体系、Provider 这些，跑完四份规划工件加一份执行契约加 DP-3 审批，才写第一行业务代码。

恢复旧变更就说「继续上次的工作流」，不确定当前状态就说「帮我看看现在该干什么」，workflow-start 会在路由前先扫描 overlay 告诉你下一步。

### 可选配置

项目根目录放一个 `              spec-superflow.config.json            ` ，可以为不同执行角色配置模型。

```
{
  "models": {
    "mechanical": "vendor-small",
    "standard": "vendor-standard",
    "strong": "vendor-strong",
    "review": "vendor-review"
  }
}
```

机械性修改用便宜小模型，架构和最终审查用最强模型。只读解析一个 profile 的命令是 `ssf config --resolve-model mechanical` ，它只解析本地配置，不调 API，也不切当前会话模型。

## 价值主张：为什么不直接用两个框架

讲到这，价值已经藏在架构里了，我把它摊开说。

第一，它用一面硬墙把两个失控点隔开，而不是让你分别装两个工具。需求澄清到工件沉淀，Schema 引擎验证格式，执行契约桥接，TDD 加 SDD 加 Review Gate 三重纪律强制执行，验证收口，delta spec 同步防腐烂，一气呵成。

第二，规划白写的问题被根治。很多团队 proposal、design 写了也白写，AI 执行照样跑偏。 [execution-contract.md](http://execution-contract.md/) 是规划到实现的唯一交接层，规划一旦锁定，执行就被关进契约的笼子里。

第三，自包含、零运行时依赖。上游两个工具都偏重，团队往往不愿引入两个插件。spec-superflow 一个插件全包，没有运行时负担。

第四，规范防腐烂。spec-merger 强制把 delta spec 合并回主规范，避免「规格写完一次就腐烂」这个棕地项目最常见的痛。

第五，可审计、可重放、可证明。每个变更留下五份正式工件加 checkpoint 历史，三个月后回看为什么这么写一目了然。workflow-start 内容级重放会话，恢复时自动判断处于哪个状态。

第六，也是它相对两个上游最实在的工程卖点，跨 17 个平台零迁移成本。今天用 Claude Code，明天换 Cursor，后天切 Trae，同一套工作流原样带走，skills、scripts、hooks 自动部署。

它最适合大型功能开发、多人协作、长期维护、需要 TDD 加 Review Gate 的棕地项目。一次性脚本、纯咨询问答这类场景，就别请它出山了。

从「AI 写完再修」到「AI 一次写对」，这才是规格驱动加执行纪律真正值钱的地方。

---

spec-superflow 已经在 GitHub 开源，MIT 协议，目前已有 380+ Star。如果你也被 AI 写代码的失控点折磨过，建议直接装上试试，源码就在仓库里，架构、契约模板、状态机都看得见。

仓库地址在这里，求点个 Star 支持一下。

[https://github.com/MageByte-Zero/spec-superflow](https://github.com/MageByte-Zero/spec-superflow)

---

**转发给正在学 AI 开发的朋友** ，少走弯路 🚀

 **![图片](assets/253k%20Superpowers%20%E5%92%8C%2060k%20OpenSpec%20%E8%A2%AB%E8%9E%8D%E5%90%88%E4%BA%86%EF%BC%81spec-superflow%20%E5%B7%A5%E4%BD%9C%E6%B5%81%E7%99%BB%E4%B8%8A%E7%83%AD%E6%A6%9C/000659fdef65615a176821139f9416c4_MD5.webp)**你在看吗****