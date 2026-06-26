---
title: "Superpowers、OpenSpec、Spec-Kit 傻傻分不清楚"
source: "https://mp.weixin.qq.com/s/jLg9oC8Cn_S5XBoVgEk2Ug"
---
苏三 苏三说技术 *2026年6月25日 14:36*

大家好，我是苏三，又跟大家见面了。

最近想快速提升项目实战能力（包含多个AI项目），或者最近找工作，或者想学习AI的小伙伴，可以看看下面👇🏻的这个链接（或许真的能够帮到你）:

[推荐一个牛逼的RAG + MCP系统](https://mp.weixin.qq.com/s?__biz=MzkwNjMwMTgzMQ==&mid=2247538241&idx=1&sn=73d443e9a5ce6ee3317e97e5ce213d07&scene=21#wechat_redirect)

## 前言

最近这段时间，我的技术群几乎被三个名字刷屏了—— **Superpowers、OpenSpec、Spec-Kit** 。

这三个项目在GitHub上都是现象级的存在：Superpowers狂揽 **238K Star** ，Spec-Kit斩获 **115K+ Star** ，OpenSpec也有 **46K+ Star** 。

加起来快 **40万Star** ，这是什么概念？

Spring Boot整个生态加起来都没这么多。

但问题来了：

它们到底有什么区别？

我该用哪个？

今天这篇文章就专门跟大家一起聊聊这个话题，希望对你会有所帮助。

## 一、先说说“Vibe Coding”的坑

在正式介绍这三个工具之前，我们先花2分钟聊聊一个现象。

> 有些小伙伴在工作中可能遇到过这样的情况：你让AI帮你实现一个功能，它二话不说就开始写代码了。你只是让它加一个登录接口，结果它顺手把整个认证模块都重写了。你问它“测试过了吗”，它说“应该没问题”。你让它解释为什么这么改，它开始讲一堆听起来很合理、但你总觉得哪里不对的理由。

这就是现在很多AI编程工具的真实写照。

它们不是不会写代码，而是 **太容易跳步骤了** 。

需求还没问清楚，就开始实现；设计还没确认，就开始改架构；测试还没跑完，就宣布完成。

问题的根源是什么？

**AI代理缺乏结构化的工作流约束** 。

AI写代码的能力已经足够强了，但它没有“工程纪律”的概念。

它不知道写代码之前要先理解需求，不知道改代码之前要先写测试，不知道提交之前要先做Code Review。

三个工具应运而生，从不同角度解决这个问题：

- **Spec-Kit** 解决的是 **“按什么规矩干”** ——规范可执行化
- **OpenSpec** 解决的是 **“改了什么”** ——轻量规范管理
- **Superpowers** 解决的是 **“怎么干”** ——技能驱动工作流

## 二、Superpowers

给AI装上“工程纪律”。

### 2.1 它是什么？

Superpowers由开发者Jesse Vincent（GitHub: obra）打造，是一套 **AI编程代理技能框架与开发方法论** 。

一句话概括： **它不是在让AI更聪明，而是让AI更守规矩——像给AI请了一个“项目经理”，强制它先思考、再计划、后编码、再审查** 。

截至目前，Superpowers在GitHub上已积累 **238K Star、21.1K Forks** ，Anthropic官方插件市场安装量超过 **68万次** 。

它支持Claude Code、Codex CLI、Gemini CLI、Cursor、GitHub Copilot CLI等多种AI编程工具。

### 2.2 核心机制：14个Skill

Superpowers的核心是 **14个可组合的Skill** （技能），分为四大类：协作、测试、调试、元。

**最重要的几个Skill：**

**① brainstorming（头脑风暴）⭐ 最常用**

这是入口Skill。它的核心逻辑是： **未获得用户明确批准前，绝不允许AI动手写一行代码** 。

AI会像苏格拉底一样，一次只问一个问题，逐步澄清需求；帮你把模糊的想法变成清晰的设计；提出2-3种方案，分析权衡；最终产出设计文档。

**② subagent-driven-development（子代理驱动开发）⭐ 核心Skill**

为每个计划任务派发独立子代理，互相隔离上下文，防止污染。每个任务完成后经过 **两阶段审查** ：

- **F1：规格合规审查** ——是否违反设计文档？
- **F2：代码质量审查** ——风格、性能、安全、边界条件？

审查不通过则打回去重做。

**③ test-driven-development（强制TDD）**

强制遵循TDD的“红-绿-重构”循环：先写一个会失败的测试 → 用最少的代码让它通过 → 优化代码。

**④ requesting-code-review（代码审查）**

AI自动获取当前分支的git diff，逐文件进行审查，按严重程度报告问题。关键问题会阻止继续推进。

### 2.3 五阶段开发流程

Superpowers的核心，是给所有AI编码会话定死了一套 **五阶段的标准化开发流程** ：

![图片](assets/Superpowers%E3%80%81OpenSpec%E3%80%81Spec-Kit%20%E5%82%BB%E5%82%BB%E5%88%86%E4%B8%8D%E6%B8%85%E6%A5%9A/b177c8d14cfa1f9a39fd9e37f4a91fcc_MD5.png)

**任何代码产出，都必须走完这五步，一步都不能跳。**

### 2.4 优缺点

**优点：**

- 强制工程纪律，杜绝Vibe Coding
- 14个Skill覆盖完整开发生命周期
- 子代理隔离，防止上下文污染
- 两阶段审查，确保质量
- 跨平台兼容，不锁定具体AI工具

**缺点：**

- 刚性Skill可能限制AI的“自由发挥”
- 强制TDD可能增加初期开发时间
- 学习曲线：需要熟悉14个Skill的用法

## 三、OpenSpec

给AI编码加上“规格说明书”。

### 3.1 它是什么？

OpenSpec是Fission AI团队创建的 **AI原生规范驱动开发框架** 。

一句话概括： **它让AI编码工具按照一份结构化的规格文档来干活，而不是随心所欲地写代码** 。

OpenSpec的核心理念是四个词： **fluid、iterative、easy、built for brownfield** 。

它不追求“规范生成代码”，而是做一层轻量的规范管理。

截至2026年6月，OpenSpec在GitHub上已有 **56K+ Star** ，支持 [Node.js](http://node.js/) 20.19.0+。

它不绑定特定AI工具，可无缝融入现有开发流程，尤其适配已有项目（1→n）的功能迭代。

### 3.2 核心机制：增量规格系统

OpenSpec最核心的创新是 **Delta-Based Specs（增量规格）机制** 。

传统的规格文档有个致命问题：每次需求变更，要么重写整个文档，要么在旁边手动批注。OpenSpec用增量方式表达变更：

- **ADDED Requirements** —— 新行为追加到主规格
- **MODIFIED Requirements** —— 替换现有需求块
- **REMOVED Requirements** —— 删除需求块
- **RENAMED Requirements** —— 用FROM:/TO:格式改标题

这个设计对 **棕地项目（已有代码库的项目）** 特别友好。

你不需要一次性把所有需求写全，发现遗漏了就直接追加一个ADDED。

![图片](assets/Superpowers%E3%80%81OpenSpec%E3%80%81Spec-Kit%20%E5%82%BB%E5%82%BB%E5%88%86%E4%B8%8D%E6%B8%85%E6%A5%9A/327250175d0500218dd5077b74047923_MD5.png)

### 3.3 四个核心Skill

OpenSpec提供四个Skill，覆盖完整的开发周期：

| Skill | 别名 | 用途 |
| --- | --- | --- |
| openspec-propose | /opsx:propose | 提出新变更，生成proposal/design/specs/tasks |
| openspec-explore | /opsx:explore | 探索模式，理清需求和设计思路 |
| openspec-apply-change | /opsx:apply | 按 [tasks.md逐步实现](http://tasks.xn--md-pe1dj21dlyjg16b/) |
| openspec-archive-change | /opsx:archive | 完成后归档，合并规范 |

### 3.4 完整工作流示例

以下通过一个天气查询CLI工具的例子，展示OpenSpec的完整流程：

**第一步：提出变更**

```
/opsx:propose "创建一个简单的天气查询命令行工具"
```

OpenSpec会生成四个文件：

`              proposal.md            ` —— 回答Why/What/Impact：

```
## Why
在终端快速查看天气，不需要打开浏览器或手机。
## What Changes
- 新增 weather-cli 命令行工具
- 支持 weather <城市名> 和 weather --help
## Impact
- 新增文件：
            weather.py
          
- 无外部依赖（仅用 Python 标准库）
```

`specs/city-weather-query/             spec.md           ` —— 逐条描述功能需求：

```
## Requirement: 城市天气查询
系统应接受城市名并返回当前天气。
Scenario: 有效城市名
- WHEN 运行 weather London
- THEN 显示伦敦的天气
Scenario: 无效城市名
- WHEN 运行 weather xyzxyzxyz
- THEN 显示友好错误信息
```

`              design.md            ` —— 记录架构决策：

```
## Context
零依赖的命令行天气查询工具。
## Goals / Non-Goals
- Goals: 城市名查询、--help、错误处理、零依赖
- Non-Goals: 自动定位、GUI、持久化
## Decisions
- 使用 
            wttr.in
           API（免费、无需API Key）
- 只用Python标准库
```

`              tasks.md            ` —— 可执行的检查清单：

```
## 1. Core Implementation
- [ ] 1.1 实现天气查询函数
- [ ] 1.2 添加CLI参数解析
- [ ] 1.3 添加错误处理
## 2. Testing
- [ ] 2.1 测试有效城市名
- [ ] 2.2 测试错误处理
```

**第二步：审阅** ——生成完成后，人工审阅这些文件。在这个阶段修改成本最低——改几行Markdown比改代码快得多。

**第三步：执行变更** ——确认无误后，执行 `/opsx:apply` ，AI按照 [tasks.md逐步实现。](http://tasks.xn--md-pe1dj21dlyjg16b./)

**第四步：归档** ——完成后执行 `/opsx:archive` ，合并规范。

### 3.5 DAG工件依赖图

OpenSpec内部用了一个 **DAG（有向无环图）来管理工作流的依赖关系** 。

简单说，它会自动判断：先写proposal，再写spec，再写design，再写tasks——顺序不能乱，依赖不能跳。

### 3.6 优缺点

**优点：**

- **轻量级** ：无需API Key和MCP
- **增量规格** ：对已有项目特别友好
- **规范可追溯** ：每次变更都有完整的proposal→spec→design→tasks→archive闭环
- **不绑定特定AI工具** ：支持Cursor、GitHub Copilot、Claude Code等

**缺点：**

- **执行层面较弱** ：可以把“要做什么”说清楚，但不太能把“具体怎么做”推进得足够细
- **缺乏强制质量门禁** ：规范写好了，但AI执行时可能跳步骤
- **WHAT清楚，但HOW不够细**

## 四、Spec-Kit

让规范“可执行”。

### 4.1 它是什么？

Spec-Kit是 **GitHub官方出品** 的规范驱动开发工具包。

官方定位非常明确： **Spec-Driven Development flips the script on traditional software development. Specifications become executable, directly generating working implementations rather than just guiding them** 。

翻译过来： **规范不只是“指导文档”，而是可执行的——能直接生成工作代码** 。

Spec-Kit发布于2025年8月，截至2026年6月已斩获 **115K+ Star、10.2k Fork** ，是2026年GitHub上增长最快的AI工具类项目之一。

支持Claude Code、GitHub Copilot、Cursor、Gemini CLI等25+种AI代理。

### 4.2 核心机制：七阶段流水线

Spec-Kit的核心是 **七个阶段的规范驱动开发流程** ，每个阶段都有明确的输入输出，像工厂流水线一样：

![图片](assets/Superpowers%E3%80%81OpenSpec%E3%80%81Spec-Kit%20%E5%82%BB%E5%82%BB%E5%88%86%E4%B8%8D%E6%B8%85%E6%A5%9A/c0fb8ed9178ff863ef91c604bf755b5b_MD5.png)

**[constitution.md（宪法）](http://constitution.xn--md\(\)-dj9g429f/)** ：定义项目级别的治理原则——代码质量标准、测试规范、用户体验一致性要求、性能要求。

**[spec.md（规范）](http://spec.xn--md\(\)-dn0lt84a/)** ：描述具体功能的需求——用户故事、功能需求，不涉及技术栈（关注what和why）。

**[plan.md（计划）](http://plan.xn--md\(\)-ii9fr261a/)** ：技术实现方案——技术栈选择、架构设计、API契约。

**[tasks.md（任务）](http://tasks.xn--md\(\)-i95fh7q/)** ：可执行的任务清单——从计划中提取的具体任务、实现步骤。

### 4.3 安装与使用

**安装** （需要Python 3.11+和uv包管理器）：

```
# 安装uv
curl -LsSf 
            https://astral.sh/uv/install.sh
           | sh

# 安装Specify CLI
uv tool install specify-cli --from
```

**使用** ：在AI代理中通过斜杠命令触发各阶段：

```
/
            speckit.constitution
            # 定义项目宪法
/
            speckit.specify
                 # 描述功能规范
/
            speckit.plan
                    # 制定技术计划
/
            speckit.tasks
                   # 分解任务
/
            speckit.analyze
                 # 一致性检查
/
            speckit.implement
               # 执行实现
```

### 4.4 优缺点

**优点：**

- **GitHub官方背书** ：可靠性高，长期维护有保障
- **规范可执行** ：规范不只是文档，能直接生成工作代码
- **七阶段流水线** ：流程清晰，每一步都有明确输入输出
- **支持25+种AI代理** ：覆盖面广
- **项目宪法机制** ：从顶层约束AI行为

**缺点：**

- **学习曲线陡峭** ：七阶段流程需要时间掌握
- **偏重“绿field项目”** ：对已有代码库的适配不如OpenSpec自然
- **Python技术栈** ：CLI基于Python/uv，对Java开发者有一定门槛

## 五、一张图看懂三者差异

这是最核心的部分—— **它们到底有什么区别？**

![图片](assets/Superpowers%E3%80%81OpenSpec%E3%80%81Spec-Kit%20%E5%82%BB%E5%82%BB%E5%88%86%E4%B8%8D%E6%B8%85%E6%A5%9A/1c0e7b8002621c3779535a8ed27e5460_MD5.png)

用一句话总结：

- **Spec-Kit** 像一本详细的 **《装修规范手册》** ——告诉你什么能做、什么不能做
- **OpenSpec** 像 **便利贴系统** ——快速记录变更，灵活调整
- **Superpowers** 像 **专业施工队的工作流程** ——每一步都有检查点，确保质量

## 六、多维度对比

| 对比维度 | Superpowers | OpenSpec | Spec-Kit |
| --- | --- | --- | --- |
| **GitHub Stars** | **204K** | 48K+ | 109K+ |
| **核心定位** | 技能驱动工作流 | 轻量规范管理 | 规范可执行化 |
| **核心问题** | “怎么干” | “改了什么” | “按什么规矩干” |
| **核心机制** | 14个Skill + 五阶段流程 | 增量规格 + DAG依赖图 | 七阶段流水线 |
| **技术栈** | Markdown（跨平台） | TypeScript（ [Node.js）](http://node.js\)/) | Python（uv） |
| **适用项目** | 所有类型 | **棕地项目（已有代码库）** | 绿field项目 |
| **API Key要求** | 不需要 | 不需要 | 不需要 |
| **支持的AI工具** | Claude Code、Cursor、Codex、Gemini CLI等 | Cursor、Copilot、Claude Code等 | 25+种AI代理 |
| **学习曲线** | 中等 | 低 | 陡峭 |
| **开源协议** | MIT | 未知 | 未知 |
| **官方背书** | Anthropic官方插件市场认证 | 社区驱动 | **GitHub官方** |

## 七、到底该选哪个？

### 选Superpowers的场景

- **你需要AI严格遵循工程纪律** —— 强制TDD、强制Code Review、强制子代理隔离
- **你的任务复杂度高** —— 涉及多文件修改、需要子代理并行执行
- **你希望AI从“代码生成器”升级为“资深工程师”**
- **你不希望被特定AI工具锁定** —— Superpowers跨Claude Code、Cursor、Codex等通用

> 我自己的经验是： **Superpowers最适合那些“代码质量要求高、返工代价大”的项目** 。比如金融系统、核心业务模块、长期维护的项目。强制流程虽然前期慢一点，但后期几乎不需要返工。

### 选OpenSpec的场景

- **你已有代码库，需要持续迭代** —— OpenSpec的增量规格机制对棕地项目特别友好
- **你希望需求变更可追溯** —— 每次变更都有完整的proposal→spec→design→tasks→archive闭环
- **你团队需要多人协作** —— 规范文档让所有人都清楚“这次改了什么”
- **你希望轻量级、快速上手** —— 无需API Key和MCP

> OpenSpec最打动我的是 **增量规格的设计** 。在一个已经跑了三年的老项目上，你不可能花一个月把全部需求文档补全。OpenSpec允许你“边做边补”，每次只记录这次变更涉及的部分。这才是真实世界的工作方式。

### 选Spec-Kit的场景

- **你从零开始一个新项目** —— 绿field项目，七阶段流水线从头走一遍
- **你需要GitHub官方背书** —— 长期维护有保障
- **你希望规范直接生成代码** —— 不只是指导文档，而是可执行的
- **你的团队愿意投入时间学习标准化流程**

> Spec-Kit适合“从零到一”的项目。如果你的团队正打算启动一个新的大项目，而且愿意花时间把规范做扎实，Spec-Kit的七阶段流水线会让你少走很多弯路。但如果你面对的是一个已经跑了三年的老项目，Spec-Kit可能不如OpenSpec来得灵活。

### 最佳实践

**不要把它们当成“三选一”** 。

实际使用中，很多开发者发现这三个工具可以 **组合使用** ：

- **OpenSpec擅长管理WHAT** —— 需求、提案、spec生命周期和归档
- **Superpowers擅长管理HOW** —— 头脑风暴、深度设计、计划执行和代码Review
- **Spec-Kit擅长管理“按什么规矩”** —— 项目宪法、全局约束

有开发者基于这个思路，创建了 **Comet** —— 一个结合OpenSpec和Superpowers的Skill工具：

> “OpenSpec很适合管理需求、proposal、spec生命周期和归档。Superpowers很适合做头脑风暴、深度设计、计划执行和代码review。但我在真实使用时发现：只用OpenSpec，容易出现WHAT清楚但HOW不够细的问题；只用Superpowers，容易出现HOW很强但WHAT没有完整生命周期闭环的问题。”

**理想的工作流** ：用 **Spec-Kit** 定义项目宪法和全局约束 → 用 **OpenSpec** 管理每次变更的规格和归档 → 用 **Superpowers** 约束AI的执行纪律。

## 总结

回到最初的问题： **Superpowers、OpenSpec、Spec-Kit，到底该怎么选？**

我的建议是三步走：

**第一步：认清你的项目阶段**

- 新项目从零开始 → **Spec-Kit** 的七阶段流水线帮你打地基
- 已有代码库持续迭代 → **OpenSpec** 的增量规格机制更灵活
- 两者都有 → 考虑组合使用

**第二步：认清你的核心痛点**

- AI不守纪律、乱改代码 → **Superpowers** 的14个Skill强制流程
- 需求说不清、变更没记录 → **OpenSpec** 的增量规格管理
- 项目没规范、质量靠运气 → **Spec-Kit** 的七阶段流水线

**第三步：不要怕组合使用**

这三个工具 **不是互斥的** 。Spec-Kit定“规矩”、OpenSpec管“变更”、Superpowers管“执行”——它们各管一摊，完全可以一起用。

**一个参考的组合方案** ：

1. 用 **Spec-Kit** 的 `constitution` 定义项目宪法（一次性）
2. 每次新功能用 **OpenSpec** 的 `propose` 创建变更提案
3. 用 **Superpowers** 的 `brainstorming` 做需求澄清
4. 用 **Superpowers** 的 `subagent-driven-development` 执行开发
5. 用 **OpenSpec** 的 `archive` 归档变更

这样，你既有全局规范（Spec-Kit），又有变更追溯（OpenSpec），还有执行纪律（Superpowers）—— **三管齐下，AI编程才能真正从“碰运气”变成“按流程”** 。

### 开源地址

- **Superpowers** ： [https://github.com/obra/superpowers](https://github.com/obra/superpowers) （238K Star）
- **OpenSpec** ： [https://github.com/Fission-AI/OpenSpec](https://github.com/Fission-AI/OpenSpec) （56K+ Star）
- **Spec-Kit** ： [https://github.com/github/spec-kit](https://github.com/github/spec-kit) （115K+ Star）

最近想快速提升项目实战能力（包含多个AI项目），或者最近找工作，或者想学习AI的小伙伴，可以看看下面👇🏻的这个链接（或许真的能够帮到你）:

[推荐一个牛逼的RAG + MCP系统](https://mp.weixin.qq.com/s?__biz=MzkwNjMwMTgzMQ==&mid=2247538241&idx=1&sn=73d443e9a5ce6ee3317e97e5ce213d07&scene=21#wechat_redirect)