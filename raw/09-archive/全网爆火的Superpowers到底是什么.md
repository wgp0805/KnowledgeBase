---
title: "全网爆火的Superpowers到底是什么?"
source: "https://mp.weixin.qq.com/s/tzLUVq36CqWmE2uJyYdlpw"
---
苏三 苏三说技术 *2026年6月23日 08:44*

大家好，我是苏三，又跟大家见面了。

最近想快速提升项目实战能力（包含多个AI项目），或者最近找工作，或者想学习AI的小伙伴，可以看看下面👇🏻的这个链接（或许真的能够帮到你）:

[推荐一个牛逼的RAG + MCP系统](https://mp.weixin.qq.com/s?__biz=MzkwNjMwMTgzMQ==&mid=2247538241&idx=1&sn=73d443e9a5ce6ee3317e97e5ce213d07&scene=21#wechat_redirect)

## 前言

最近这段时间，我的技术群几乎被同一个话题刷爆了——“你装Superpowers了吗？”

打开GitHub一看， **204K Stars、18.2K Forks、68万+安装量** 。

一度登上GitHub Trending榜首，2026年初进入Anthropic官方插件市场后迅速爆发。

很多小伙伴跑来问我：“三哥，这个Superpowers到底是什么？为什么突然这么火？”

说实话，第一次看到这个项目的时候，我也挺好奇的。

一个插件而已，凭什么能拿到20多万Star？

深入研究之后，我才发现—— **它解决的不是“AI能不能写代码”的问题，而是“AI怎么好好写代码”的问题。**

今天这篇文章就专门跟大家一起聊聊这个话题，希望对你会有所帮助。

**最近建了几个AI技术交流群，扫描加我微信，备注：AI，即可进群交流和学习，获取AI最新咨询。**

![图片](assets/%E5%85%A8%E7%BD%91%E7%88%86%E7%81%AB%E7%9A%84Superpowers%E5%88%B0%E5%BA%95%E6%98%AF%E4%BB%80%E4%B9%88/120fc0032d790118e773ec1a67b88378_MD5.webp)

## 一、先说说AI编程的“野蛮生长”

在正式介绍Superpowers之前，我们先花2分钟回顾一下，现在的AI编程工具到底出了什么问题。

> 有些小伙伴在工作中可能遇到过这样的情况：你让AI帮你改一个小功能，结果它上来就改了五六个文件。你只是让它修一个bug，它顺手重构了一片代码。你问它“测试过了吗”，它说“应该没问题”。你让它解释为什么这么改，它开始讲一堆听起来很合理、但你总觉得哪里不对的理由。

这不是个例，这是现在大多数AI编程工具的真实写照。

它们不是不会写代码，而是 **太容易跳步骤** 了。

需求还没问清楚，就开始实现。

设计还没确认，就开始改架构。

测试还没跑完，就宣布完成。

Review还没做，就准备提交。

这种现象在圈子里有个专门的说法—— **Vibe Coding** （凭感觉编程）。

很多开发者刚开始用AI编程工具时，习惯性地把AI当成“代码生成器”——提个需求，等它吐代码，复制粘贴，完事。

这种方式在简单场景下还行，但一旦项目复杂起来，问题就全暴露了：

- 代码质量参差不齐
- 缺乏系统性的测试
- 调试困难，bug频发
- 代码难以维护

**说到底，这不是AI不够聪明的问题，而是AI缺乏工程纪律的问题** 。

我们缺的，从来不是一个能写代码的AI，而是一个 **能跟着资深工程师的规范流程走的AI** 。

## 二、Superpowers到底是什么？

好了，现在正式回答这个问题。

Superpowers由开发者Jesse Vincent（GitHub账号obra）打造，是一套 **AI编程代理技能框架与开发方法论** 。

它的核心目标只有一个： **把你的AI编码助手，从一个急于交差的“初级开发”，改造成一个严守开发纪律的资深软件工程师** 。

它不只是一个简单插件，更是一套 **强制AI遵循架构师标准的“铁律”** 。

### 2.1 一句话说清

**Superpowers不是让AI更聪明，而是让AI更守规矩——像给AI请了一个“项目经理”，强制它先思考、再计划、后编码、再审查** 。

或者说： **把软件工程的最佳实践，焊死在AI Agent上** 。

### 2.2 核心理念：Process over Prompt

Superpowers最核心的理念是四个单词： **Process over Prompt（流程大于提示词）** 。

什么意思呢？

传统的AI编程方式，依赖的是你写的 **提示词（Prompt）** ——你写得好，AI就干得好；你写得不好，AI就乱来。

这种方式高度依赖用户的水平，而且不可复制、不可规模化。

而Superpowers的方式是： **把资深工程师的思考和执行习惯，直接“编译”进AI的大脑** 。

不是让你手动写一堆长Prompt，而是 **把软件工程最佳实践全部封装成AI可自动执行的流程** 。

### 2.3 它到底是什么技术形态？

很多人第一次听说Superpowers，以为它是某种Claude的fine-tune版本，或者是一个专属的Agent框架。

**都不是。**

Superpowers的全部实现就是 **一套 [SKILL.md文件](http://skill.xn--md-zg3cw96f/)** 。

每个 [SKILL.md文件就是一套流程规范，用Markdown写成，任何人打开都能读懂。](http://skill.xn--md,markdown,-ht4sw5fnzavc33fhzvxl2bd6l4lo1xodvbc6bf07b42dm66dpi8brv3ast7bjdn144cgkplf4b./)

整个框架 **没有自己的运行时，不锁定模型，不依赖私有API** 。

它本质上是一套 **编码进文本的工程方法论** 。

这个设计让整个框架极度轻量：它不锁定你用哪个模型，不需要自己的运行时， **跨Claude Code、Cursor、Gemini CLI、GitHub Copilot CLI、Codex CLI都能工作** 。

![图片](assets/%E5%85%A8%E7%BD%91%E7%88%86%E7%81%AB%E7%9A%84Superpowers%E5%88%B0%E5%BA%95%E6%98%AF%E4%BB%80%E4%B9%88/bf4b0514b0979c5a69a067c5f83a7695_MD5.png)

## 三、14个核心Skill详解

Superpowers内置了 **14个核心Skill** （技能），分为四大类。

我挑几个最重要的给你详细拆解。

### 3.1 头脑风暴（Brainstorming）

这是入口Skill，也是 **最重要的一个** 。

它的核心逻辑是： **未获得用户明确批准前，绝不允许AI动手写一行代码** 。

工作方式是这样的：

- AI像苏格拉底一样，一次只问一个问题，逐步澄清需求
- 帮你把模糊的想法变成清晰的设计
- 提出2-3种方案，分析权衡
- 最终产出设计文档

**实战效果** ：有用户反馈说“前面花了两个小时被拷打需求，后面执行只用了10分钟，一遍过”。

### 3.2 编写计划（Writing Plans）

把设计拆成 **2-5分钟的细粒度任务** 。

每个任务包含：

- 精确的文件路径
- **完整的代码（禁止TBD/TODO占位符）**
- 验证命令

### 3.3 子代理驱动开发（Subagent-Driven Development）

这是Superpowers最核心、最强大的能力之一。

为每个计划任务 **派发独立子代理，互相隔离上下文，防止污染** 。

每个任务完成后经过 **两阶段审查** ：

- **F1：规格合规审查** ——是否违反设计文档？
- **F2：代码质量审查** ——风格、性能、安全、边界条件？

审查不通过则打回去重做，确保每个环节的质量。

### 3.4 并行子代理（Dispatching Parallel Agents）

当有多个互不依赖的任务时，派发多个子代理 **并行处理** ，大幅提升效率。适合同时修改多个独立模块的场景。

### 3.5 代码审查（Requesting Code Review）

AI自动获取当前分支的git diff，逐文件进行审查，按严重程度报告问题。

**关键问题会阻止继续推进** ，起到质量守门员的作用。

### 3.6 测试驱动开发（TDD）

Superpowers强制遵循 **TDD（测试驱动开发）** 的“红-绿-重构”循环：

- **RED** ：先写一个会失败的测试
- **GREEN** ：用最少的代码让它通过
- **REFACTOR** ：优化代码

### 3.7 系统化调试（Systematic Debugging）

遇到bug时不盲目乱改，而是 **系统化地定位根因** 。

### 3.8 完整的Skill列表

| 分类 | Skill名称 | 作用 |
| --- | --- | --- |
| **协作类** | brainstorming | 需求澄清，AI像苏格拉底一样提问 |
|  | writing-plans | 把设计拆成细粒度任务 |
|  | executing-plans | 按计划执行 |
|  | subagent-driven-development | 子代理隔离执行+两阶段审查 |
|  | dispatching-parallel-agents | 并行执行独立任务 |
|  | requesting-code-review | 自动发起代码评审 |
|  | receiving-code-review | 处理评审反馈 |
|  | using-git-worktrees | Git工作区隔离 |
|  | finishing-a-development-branch | 分支收尾 |
| **测试类** | test-driven-development | 强制TDD |
|  | verification-before-completion | 完成前验证 |
| **调试类** | systematic-debugging | 系统化调试 |
| **元技能** | writing-skills | 编写新Skill |
|  | using-superpowers | Superpowers激活恢复 |

## 四、安装与配置

### 4.1 环境准备

确保你已经安装并配置好Claude Code。

### 4.2 安装Superpowers

在Claude Code终端中执行以下命令：

```
# 步骤1：注册Superpowers市场源
/plugin marketplace add obra/superpowers-marketplace

# 步骤2：安装插件
/plugin install superpowers@superpowers-marketplace
```

安装完成后，输入 `/reload` 让skill生效。

### 4.3 验证安装

重启会话后，执行以下命令验证：

```
# 查看技能列表，确认superpowers存在
/find-skills

# 测试核心命令是否可用
/superpowers:brainstorm
```

如果看到Superpowers的相关命令，说明安装成功。

## 五、五阶段开发流程

Superpowers的核心，是给所有AI编码会话定死了一套 **五阶段的标准化开发流程** 。

任何代码产出，都必须走完这五步， **一步都不能跳** 。

![图片](assets/%E5%85%A8%E7%BD%91%E7%88%86%E7%81%AB%E7%9A%84Superpowers%E5%88%B0%E5%BA%95%E6%98%AF%E4%BB%80%E4%B9%88/88eabcbf86dbef96b54d4fea6f08bec1_MD5.png)

### 阶段1：头脑风暴

拿到需求但还不知道怎么设计方案时，执行：

```
/superpowers:brainstorm 设计一个高并发的秒杀系统
```

Superpowers会引导AI按照软件工程思维，从以下维度系统思考：

- 业务边界和核心痛点
- 技术选型和架构设计
- 潜在风险和应对措施
- 性能和可扩展性考量

**关键提示** ：不要直接跳到编码，先在头脑风暴阶段把方向理顺。

### 阶段2：方案设计

需求明确后，输出技术方案文档：

```
/superpowers:design 基于Spring Boot实现分布式任务调度系统
```

Superpowers会强制生成包含以下内容的方案文档：

- 系统架构图（Mermaid或PlantUML）
- 模块划分和职责定义

### 阶段3：编写计划

把设计拆成细粒度任务，每个任务包含精确的文件路径、完整代码和验证命令。

### 阶段4：执行开发

为每个计划任务派发独立子代理，互相隔离上下文。每个任务完成后经过两阶段审查。

### 阶段5：代码审查

AI自动获取git diff，逐文件审查，按严重程度报告问题。

## 六、底层原理

> 很多小伙伴可能会问：Superpowers不就是一套Markdown文件吗，有什么底层原理可谈？

如果你这么想，那就太小看这套框架了。

虽然它的实现确实只是一堆 [SKILL.md文件，但](http://skill.xn--md,-vu9djor61i/) **这套文件的设计和编排方式，才是真正的“底层原理”** 。

### 6.1 架构全景

先上一张全局架构图，让你对Superpowers的底层设计有一个整体认知：

![图片](assets/%E5%85%A8%E7%BD%91%E7%88%86%E7%81%AB%E7%9A%84Superpowers%E5%88%B0%E5%BA%95%E6%98%AF%E4%BB%80%E4%B9%88/c95b2fbe4512a73423629b466cdba791_MD5.jpg)

### 6.2 会话启动时序图

接下来，我们看看当一个Claude Code会话启动时，Superpowers内部发生了什么：

![图片](assets/%E5%85%A8%E7%BD%91%E7%88%86%E7%81%AB%E7%9A%84Superpowers%E5%88%B0%E5%BA%95%E6%98%AF%E4%BB%80%E4%B9%88/f1ab5a032140fe777241aa1a228b8469_MD5.png)

### 6.3 子代理执行时序图

当主会话需要派发子代理执行具体任务时，其内部机制如下：

![图片](assets/%E5%85%A8%E7%BD%91%E7%88%86%E7%81%AB%E7%9A%84Superpowers%E5%88%B0%E5%BA%95%E6%98%AF%E4%BB%80%E4%B9%88/9658351e0a7de4449c7247f271ebf7fc_MD5.jpg)

### 6.4 工作目录与隔离机制

Superpowers的子代理隔离机制，在文件系统层面是这样运作的：

![图片](assets/%E5%85%A8%E7%BD%91%E7%88%86%E7%81%AB%E7%9A%84Superpowers%E5%88%B0%E5%BA%95%E6%98%AF%E4%BB%80%E4%B9%88/0e89392d95cad9a05989a0489797aeb5_MD5.png)

### 6.5 设计取舍与已知问题

**设计取舍一：2000 tokens的引导注入**

Superpowers选择在会话启动时只注入2000 tokens的引导文档，而不是一次性加载所有Skill。

优点是：节省上下文，为后续任务留出空间；

缺点：子Agent需要额外的Hook来继承引导上下文。

**设计取舍二：强制流程 vs 灵活性**

强制五阶段流程让AI更守纪律，但也牺牲了一部分灵活性。

对于简单任务，这套流程可能显得“杀鸡用牛刀”。

**已知问题**

- **子Agent上下文继承不完整** ：SubagentStart Hook虽然会尝试重新注入引导文档，但有时会失败，导致子Agent跳过TDD约束
- **解决方案** ：遇到时手动触发 `using-superpowers` skill拉回正常轨道
- **官方预计** ： [v5.2.0将修复此问题](http://v5.2.xn--0-8g7a43z64ccq0a4k2do5d/)

## 七、优缺点

### 🌟 优点

**1\. 强制工程纪律，杜绝Vibe Coding**

Superpowers最核心的价值就是 **给AI套上工程纪律的护栏** 。不再凭感觉乱写，先规划再执行。

**2\. 14个Skill覆盖完整开发生命周期**

从需求澄清到方案设计，从任务拆解到代码执行，从测试驱动到代码审查—— **全流程覆盖** 。

**3\. 子代理隔离，防止上下文污染**

为每个任务派发独立子代理，互相隔离上下文。这在处理复杂项目时尤其重要。

**4\. 两阶段审查，确保质量**

每个任务完成后经过规格合规审查和代码质量审查。审查不通过则打回去重做。

**5\. 跨平台兼容**

一套开发规范，跨Claude Code、Cursor、Codex、Gemini CLI等多个平台通用。

**6\. 完全开源，可定制**

框架完全透明，你可以 **修改任何Skill来适配自己团队的规范** 。

**7\. 真实反馈极好**

用户普遍反映“代码质量提升明显，维护性变好，后期迭代轻松多了”。

### ⚠️ 缺点与注意事项

**1\. 子Agent上下文继承问题**

子Agent启动时不会自动继承引导上下文，有时会跳过TDD约束。需要手动触发 `using-superpowers` skill拉回来。

**2\. 强制流程可能增加初期开发时间**

例如，强制TDD可能增加初期开发时间，但能降低后期维护成本。

**3\. 学习曲线**

虽然Skill本身是Markdown写的，但要熟练使用所有14个Skill，还是需要一定的学习成本。

**4\. 刚性约束可能限制自由度**

刚性Skill可能限制AI的“自由发挥”，但能减少低级错误。

## 八、适用场景

### 强烈推荐使用的场景

| 场景 | 理由 |
| --- | --- |
| **复杂项目开发** | 子代理+新上下文窗口，适合中大型功能开发 |
| **团队协作项目** | 统一流程规范，避免每个人“调教AI”的方式不一样 |
| **需要生产级质量的项目** | 强制TDD+多轮Review，生产级质量大幅提升 |
| **长周期维护项目** | 代码质量提升明显，维护性变好，后期迭代轻松 |
| **多人协作+代码审查** | 自动代码审查+两阶段审查，质量有保障 |

### 不太适合的场景

| 场景 | 理由 |
| --- | --- |
| **极简单的单文件脚本** | 杀鸡用牛刀，流程反而拖慢速度 |
| **快速原型验证** | 流程约束可能影响探索速度 |
| **对AI自由度要求极高的场景** | 刚性Skill限制了AI的“自由发挥” |

## 九、与其他工具的对比

目前市面上还有另外两个热门方案： **GitHub官方的Spec-Kit** 和 **轻量级的OpenSpec** 。

| 对比维度 | Superpowers | Spec-Kit | OpenSpec |
| --- | --- | --- | --- |
| **GitHub Stars** | 204K | 82.5K | 34.5K |
| **核心定位** | 技能驱动工作流 | 规范可执行化 | 轻量规范层 |
| **实现方式** | 14个 [SKILL.md文件](http://skill.xn--md-zg3cw96f/) | 7阶段流水线 | 规范管理 |
| **灵活性** | 高（可修改Skill） | 中 | 高 |
| **学习曲线** | 中 | 陡 | 低 |

**简单来说** ：

- **Spec-Kit** ：规范不只是指导文档，而是可执行的——能直接生成工作代码
- **OpenSpec** ：做一层轻量的规范管理，让规范成为活文档
- **Superpowers** ：通过一组可组合的“技能”来约束代理行为

## 十、快速上手指南

如果你现在就想试试，这里是最快的上手路径：

**Step 1：安装**

在Claude Code终端执行：

```
/plugin marketplace add obra/superpowers-marketplace
/plugin install superpowers@superpowers-marketplace
/reload
```

**Step 2：验证**

```
/find-skills
```

**Step 3：开始使用**

拿到一个新需求时， **不要直接让AI写代码** 。先执行：

```
/superpowers:brainstorm 你的需求描述
```

让AI先帮你把需求问清楚、方案想明白，再开始写代码。

**Step 4：逐步深入**

熟悉brainstorm之后，逐步尝试其他Skill：

- `writing-plans` ：把设计拆成任务
- `subagent-driven-development` ：子代理执行
- `requesting-code-review` ：代码审查

## 总结

回到最初的问题： **Superpowers到底是什么？**

它不是让AI变得更聪明的“魔法药水”。

**它是一套给AI套上工程纪律的“铁律”** 。

它解决的不是“AI能不能写代码”的问题，而是 **“AI怎么写好代码”** 的问题。

AI写代码的能力已经足够强了。

问题在于， **它太急于交差，太容易跳步骤** 。

Superpowers做的，就是在需求和代码之间加了一层 **纪律屏障** 。

这层屏障非但不会拖慢你的进度，反而会通过 **提前规避返工，帮你省下大量时间** 。

如果你已经受够了AI写的“能跑但没法维护”的代码，不妨试试Superpowers。

它会让你重新相信： **AI真的可以像一个资深工程师一样写代码** 。

GitHub仓库： [https://github.com/obra/superpowers](https://github.com/obra/superpowers)

最近想快速提升项目实战能力（包含多个AI项目），或者最近找工作，或者想学习AI的小伙伴，可以看看下面👇🏻的这个链接（或许真的能够帮到你）:

[推荐一个牛逼的RAG + MCP系统](https://mp.weixin.qq.com/s?__biz=MzkwNjMwMTgzMQ==&mid=2247538241&idx=1&sn=73d443e9a5ce6ee3317e97e5ce213d07&scene=21#wechat_redirect)