---
title: "Matt Pocock 那个 5 个月冲到 17 万 star 的 grill-me，作者自己却不用了，原因是这几个......"
source: "https://mp.weixin.qq.com/s/01pctmUOs9-nJU8dO_mp_A"
---
程序员追风 *2026年7月27日 22:00*

你让 AI 给项目加个权限控制，它唰唰改了四十多个文件，跑起来却报空指针。你让它修，它又牵出三个新 bug。你回头看它写的代码，变量名长得像绕口令，注释和代码说的是两回事。三个月后这个功能要改需求，你盯着那一团代码，根本不敢动。

这不是你一个人的问题。 **mattpocock/skills** 那个 5 个月冲到 17 万 star 的仓库，整本 README 就在掰扯这四类破事。

## 一、作者亲手撤下招牌 skill，不是打脸是点题

一个 17 万 star 的仓库，作者却把自己最火的 skill 从推荐位撤了。这事儿要放在别的网红项目上，早被骂成自相矛盾割韭菜了。

先抛规模参数。mattpocock/skills 创建于 2026-02-03，截至 2026 年 7 月中旬，star 数已经冲到 17 万+（170,525）。一个 5 个月大的仓库能拿到这个数字，在 AI 编码工具里属于现象级，但码哥得补一句时间锚，别写成绝对第一，它只是这个窗口期里最猛的那个。

170,525 这个具体数字，放在任何 AI 工具仓库里都是头部，但它涨得最猛的那段，恰恰是 Matt 开始公开劝人别把 grill-me 当默认推荐的那几个月。

作者 Matt Pocock 不是蹭热度的网红。他是 Total TypeScript 的作者，TypeScript 教育圈的老面孔，还运营着 [aihero.dev，newsletter](http://aihero.dev,newsletter/) 大概 6 万开发者订阅。这种人撤自己最火的 skill，不会是手滑。

决策背景写在 [aihero.dev/skills-grill-me](http://aihero.dev/skills-grill-me) 那篇博客顶部的更新声明里，原话是，「I stopped using /grill-me for coding. I now recommend /grill-with-docs when you want to align a plan with your codebase before implementation.」现在更进一步，默认推荐 **domain-model** 作为规划起点。

表面看这是打脸。你一个 17 万 star 的招牌 skill，自己不用了，凭什么让别人用。

但码哥读完整个仓库，反而觉得这一撤点破了 AI 编码的正确姿势。

**skill 不是供起来的框架，是随时该被替换、被 hack、被组合的一次性纪律。**

谁把一个 skill 供着不放，谁就还没真正学会用它。当纪律的意思很具体，你今天用 grill-with-docs 对齐，下周发现 domain-model 更顺手，就换，不纠结，不念旧。整篇文章，就绕着「把 skill 当纪律，不当框架」这个立场转。

这八个字，是它跟 GSD、BMAD、Spec-Kit 最根本的区别。

## 二、它到底是什么，跟那些「接管流程」的框架差在哪

先把仓库说清楚，它到底是个啥，又为什么和那些「接管流程」的框架不是一路货。mattpocock/skills 的简介就一句，「Skills for Real Engineers. Straight from my.claude directory.」README 里 Matt 的定位更直白，「My agent skills that I use every day to do real engineering - not vibe coding.」翻译过来，这是他每天真实在用的工程纪律，不是玩具。

Matt 是谁前面说了，他的反框架立场也写得毫不客气。原文是，「Approaches like GSD, BMAD, and Spec-Kit try to help by owning the process. But while doing so, they take away your control and make bugs in the process hard to resolve.」

这句话是本文的核心对立轴。 **GSD** 、BMAD、Spec-Kit 这类重量级框架，思路是「我帮你把整套流程接管了」。听起来省心，代价是你的控制权被拿走了，流程本身出了 bug 你还很难修，因为你是被流程裹挟的那个人。

mattpocock/skills 走的是反面。设计哲学原文，「These skills are designed to be small, easy to adapt, and composable. They work with any model. They're based on decades of engineering experience.」小、可改、可组合、跨模型、基于工程基础。

你可能会说，又一个 AI 编码 skill 集合罢了，star 高不代表什么，社区里每月都有新套装冒出来，三个月后谁还记得。这个怀疑码哥完全理解，17 万 star 里水分和跟风从来不少。

但是，你翻完它的失败模式分类和分层设计，会发现它不是在堆功能，是在把几十年的工程纪律翻译成 agent 能执行的指令。光是这一点，就和那些「装上去就全自动」的框架拉开了身位。

![图片](assets/Matt%20Pocock%20%E9%82%A3%E4%B8%AA%205%20%E4%B8%AA%E6%9C%88%E5%86%B2%E5%88%B0%2017%20%E4%B8%87%20star%20%E7%9A%84%20grill-me%EF%BC%8C%E4%BD%9C%E8%80%85%E8%87%AA%E5%B7%B1%E5%8D%B4%E4%B8%8D%E7%94%A8%E4%BA%86%EF%BC%8C%E5%8E%9F%E5%9B%A0%E6%98%AF%E8%BF%99%E5%87%A0%E4%B8%AA/116d0a4b93c594af944fe4f6a8c7f5f2_MD5.png)

mattpocock/skills 全景图：Engineering/Productivity 两大类 × User-invoked/Model-invoked 两种调用层，代表 skill 一一列出

仓库里的 skill 分两大块，Engineering（代码向）和 Productivity（通用工作流）。按调用方式又能切成两层，这一刀是全文最关键的洞察，后面单独开一章讲。先记住一点，它不要求你全装，也不要求你按某个固定顺序走。

## 三、4 大失败模式，每个都有对症的修复

这部分是工程师最容易直呼「就是这样」的地方。Matt 把 AI 编码的翻车现场归成四类，每一类配一个修复 skill，还特意引了工程经典书。码哥一个一个拆。

1\. 对不齐。The Agent Didn't Do What I Want。你以为你说清楚了，AI 理解的是另一回事。修复叫 grilling session（盘问），非代码场景用 **/grill-me** ，带共享语言加 ADR 用 /grill-with-docs。引的是 The Pragmatic Programmer 那句，「No-one knows exactly what they want.」没人真的清楚自己想要什么，所以得盘问，得对齐，不能指望一句话把需求交代明白。

2\. 太啰嗦。The Agent Is Way Too Verbose。20 个词说 1 个词的事，变量名长到读不完。修复是共享语言，也就是 **ubiquitous language** ，落在 **[CONTEXT.md](http://context.md/)** 里。

引的是 Eric Evans 的《领域驱动设计》。Matt 给了个真例子，把「课程某 section 里的 lesson 被 materialize（在文件系统里获得位置）」压成一个领域词，「materialization cascade」。好处很实在，变量、函数、文件命名一致，代码库更好导航，agent 思考还更省 token。这事儿内建在 /grill-with-docs 里，README 里 Matt 说这可能是「the single coolest technique in this repo」。

3\. 跑不起来。The Code Doesn't Work。看着对，跑就崩。修复是反馈回路，静态类型、浏览器访问、自动化测试，核心是 red-green-refactor，先写失败测试再修。对应 skill 是 **/tdd** 和 **/diagnosing-bugs** （reproduce → minimise → hypothesise → instrument → fix → regression-test）。引的还是 The Pragmatic Programmer，「The rate of feedback is your speed limit.」反馈的速度就是你的速度上限。

4\. 架构烂成泥。We Built A Ball Of Mud。agent 加速了编码，也加速了软件熵。修复是每天投资设计。skill 是 /to-spec（改代码前先问你动了哪些模块）和 /improve-codebase-architecture（建议每几天跑一次救架构）。引 Kent Beck 的《XP》，「Invest in the design of the system every day.」再引 Ousterhout 的《软件设计哲学》，「The best modules are deep.」

![图片](assets/Matt%20Pocock%20%E9%82%A3%E4%B8%AA%205%20%E4%B8%AA%E6%9C%88%E5%86%B2%E5%88%B0%2017%20%E4%B8%87%20star%20%E7%9A%84%20grill-me%EF%BC%8C%E4%BD%9C%E8%80%85%E8%87%AA%E5%B7%B1%E5%8D%B4%E4%B8%8D%E7%94%A8%E4%BA%86%EF%BC%8C%E5%8E%9F%E5%9B%A0%E6%98%AF%E8%BF%99%E5%87%A0%E4%B8%AA/16ecd2cacf9a3eab4f7edf8fab37ed0b_MD5.png)

AI 编码 4 大失败模式与对应修复 skill：对不齐→grill-with-docs、太啰嗦→ CONTEXT.md 共享语言、跑不起来→tdd+diagnosing-bugs、架构烂→to-spec+improve-codebase-architecture

四个模式里，码哥见过最多人栽在 ② 和 ③。把「用户在下单后 15 分钟没付款订单进待关闭释放库存」这种长句甩给 agent，它每次都重新翻译一遍，命名能乱到亲妈不认。。。你不在项目里先立一套共享语言，就别怪 agent 写出来的代码像拼凑的。

## 四、两种安装哲学，先想清楚你要哪种

实操部分来了，仓库给了两条安装路子，哲学完全不同，选错会很别扭。

第一条， [skills.sh，30](http://skills.sh,30/) 秒装完，拿到的是可编辑副本。

```
npx skills@latest add mattpocock/skills
```

装完在 agent 里跑一次 /setup-matt-pocock-skills，它会问你三件事，用哪个 issue tracker（GitHub / Linear / 本地文件），triage 用什么标签，文档存哪里。

第二条，Claude Code 插件，只读、永远最新、订阅式。

```
/plugin marketplace add mattpocock/skills
/plugin install mattpocock-skills@mattpocock
```

嫌打命令麻烦，shell 里也行。

```
claude plugin marketplace add mattpocock/skills
claude plugin install mattpocock-skills@mattpocock
```

然后每仓库跑一次 /setup-matt-pocock-skills。Codex 和其他遵循 Agent-Skills 标准的 agent， [skills.sh](http://skills.sh/) 安装器已经支持，原生 Codex 插件还在路线图上。

官方一句话总结了两种哲学的差异。 [skills.sh](http://skills.sh/) copies the skills into your project so you can hack on them and make them your own。The plugin keeps them as a read-only, always-current bundle you don't edit。前者把 skill 拷进项目，你可以改，改成自己的。后者是只读、常新的打包，你别动。

![图片](assets/Matt%20Pocock%20%E9%82%A3%E4%B8%AA%205%20%E4%B8%AA%E6%9C%88%E5%86%B2%E5%88%B0%2017%20%E4%B8%87%20star%20%E7%9A%84%20grill-me%EF%BC%8C%E4%BD%9C%E8%80%85%E8%87%AA%E5%B7%B1%E5%8D%B4%E4%B8%8D%E7%94%A8%E4%BA%86%EF%BC%8C%E5%8E%9F%E5%9B%A0%E6%98%AF%E8%BF%99%E5%87%A0%E4%B8%AA/e1c14d8bff74c94c3f8224432fcb6a73_MD5.png)

两种安装哲学对比： skills.sh 可编辑副本 vs Claude Code plugin 只读订阅，维度覆盖可修改性、更新方式、适用人群和安装命令

码哥的判断先放这。

**没有两全其美的策略。**

想把它改造成团队规范，就选 [skills.sh；只想蹭一套靠谱默认、跟着作者迭代，就选](http://skills.xn--sh;,-nw3c158opkbw1a031a5tntthompuu4ebxza5o0bp3b6vl4ucz2kdqap68j4l8a/) plugin。别一边用 plugin 一边手痒去改，也别用 [skills.sh](http://skills.sh/) 却从不维护，那两份都白费。码哥的观察，团队刚上手先用 [skills.sh](http://skills.sh/) 更稳，因为你迟早要改一两个 skill 去适配自己的 issue 流程和标签体系；等全组跑顺了，再切成 plugin 跟着上游走，反而省维护。

## 五、User-invoked 和 Model-invoked，这是全文最关键的一刀

前面说仓库按调用方式切两层，这一刀值得单开一章，因为它解释了为什么这套东西不会变成另一个失控框架。

**User-invoked** ，用户调用。只能你亲手打出 /xxx 触发，职责是「编排 orchestrate」。这一类包括 ask-matt（路由，帮你选该用哪个 skill）、grill-with-docs、triage、improve-codebase-architecture、setup-matt-pocock-skills、to-spec、to-tickets、implement、wayfinder，Productivity 那边有 grill-me、handoff、teach、writing-great-skills。

**Model-invoked** ，模型调用。模型可以自动调用，承载「可复用的纪律 discipline」。这一类有 prototype、diagnosing-bugs、research、tdd、domain-modeling、codebase-design、code-review（两轴审查，Standards 加 Spec，跑成并行子 agent 互不污染）、resolving-merge-conflicts，Productivity 那边是 grilling（grill-me / grill-with-docs 背后那个复用循环）。

铁律原文，「A user-invoked skill may invoke model-invoked skills, but never another user-invoked one.」编排层能调纪律层，但编排层之间不互调。

举个具体例子，你打 /implement，它内部去调 /tdd、/code-review 这些纪律层，但 /implement 永远不会去调另一个编排层的 /to-spec。这条单向边，让整条链永远从你手里发起，不会自己长出新入口让 agent 乱窜。

![图片](assets/Matt%20Pocock%20%E9%82%A3%E4%B8%AA%205%20%E4%B8%AA%E6%9C%88%E5%86%B2%E5%88%B0%2017%20%E4%B8%87%20star%20%E7%9A%84%20grill-me%EF%BC%8C%E4%BD%9C%E8%80%85%E8%87%AA%E5%B7%B1%E5%8D%B4%E4%B8%8D%E7%94%A8%E4%BA%86%EF%BC%8C%E5%8E%9F%E5%9B%A0%E6%98%AF%E8%BF%99%E5%87%A0%E4%B8%AA/64f00af9b9d487ac4f9ba377770cbde4_MD5.png)

User-invoked 编排层 vs Model-invoked 纪律层：编排层只能由你打 /xxx 触发、互不调用；纪律层可被模型自动调用；编排层可单向调用纪律层

这铁律解决了一个真问题。很多框架失控，是因为上层编排互相打架，你调我我调你，最后没人说得清当前到底在哪个状态。

码哥见过团队用重框架，状态机互相跳转，debug 时要先搞清自己在哪个节点，纯属内耗。mattpocock/skills 把编排权留在你手里，纪律沉淀在模型可复用的层里，层次干净。你只管打 /xxx，剩下的纪律让 agent 自己按规矩跑。

这一刀，才是它和「接管流程」框架的分水岭。

## 六、把整套东西焊进你自己的工作流

光知道有哪些 skill 不够，得串成链才能真正用起来。官方现在推荐的规划链是 domain-model → to-prd → to-issues → tdd。这条链把「想清楚」和「做对」用 skill 焊死了，而不是靠你记性。

README 里还有一条更完整的落地链，码哥整合一下给你用。

对齐，用 /grill-with-docs 或 domain-model，先把需求和代码库对齐。出规格，用 /to-spec，把意图落成可验证的规格。

拆工单，用 /to-tickets，每个工单声明阻塞边（blocking edge），谁依赖谁写清楚。实现，用 /implement，它在预先约定的接缝处驱动 /tdd，提交前用 /code-review 收尾。定期救架构，用 /improve-codebase-architecture，每几天跑一次，别等烂透了再救。

举个具体例子，你接一个「导出报表」的需求。先 /grill-with-docs 把「报表」「导出」「分页」这几个词在 [CONTEXT.md](http://context.md/) 里定死，agent 之后不再把导出一会儿叫 dump 一会儿叫 export。再 /to-spec 落成规格，/to-tickets 拆成「数据源查询」「格式渲染」「分页接口」三个工单，标注后者阻塞前者。/implement 在每个工单的接缝处驱动 /tdd，红测试先写，绿了再提交，/code-review 两轴过一遍。两周后你感觉架构有点散，跑一次 /improve-codebase-architecture，它只给建议不擅自改。

![图片](assets/Matt%20Pocock%20%E9%82%A3%E4%B8%AA%205%20%E4%B8%AA%E6%9C%88%E5%86%B2%E5%88%B0%2017%20%E4%B8%87%20star%20%E7%9A%84%20grill-me%EF%BC%8C%E4%BD%9C%E8%80%85%E8%87%AA%E5%B7%B1%E5%8D%B4%E4%B8%8D%E7%94%A8%E4%BA%86%EF%BC%8C%E5%8E%9F%E5%9B%A0%E6%98%AF%E8%BF%99%E5%87%A0%E4%B8%AA/a7cdf139250d9f97f3b3aebe0d992e6a_MD5.png)

mattpocock/skills 推荐落地工作流：对齐 → 出规格 → 拆工单 → 实现(驱动 tdd + code-review) → 定期救架构

grill-me 现在的定位也清楚了，当你只想要一次纯粹的高压盘问、还不需要完整 domain-model 流程时用它。它没被删，只是从「默认推荐」退到了「特定场景工具」，这正印证了开头的立场，skill 该被替换、被降级、被组合，而不是供着。

## 七、中文项目、国内团队怎么落地

最后给码哥读者一份能直接抄的落地清单，单独成章是因为国内团队的坑和老外不一样。

从哪几个开始。别一次全装。先装 grill-with-docs（对齐加共享语言）加 /tdd 加 /code-review 这三件套，跑顺了再加 to-spec、to-tickets、implement。

为什么先这三件套而不是别的。

grill-with-docs 治的是「对不齐」，tdd 治的是「跑不起来」，code-review 治的是「写完没人卡」。三个正好覆盖最高频的翻车点，等这套节奏你了然于胸，再去碰 to-spec、to-tickets、implement 这种重编排的，才不会一上来就被一堆 skill 晃晕。

共享语言在中文项目同样成立。把冗长业务描述压成术语表放 [CONTEXT.md，agent](http://context.md,agent/) 命名、导航、省 token 全受益。

举个中文业务的类比，把「用户在下单后 15 分钟内未支付则订单进入待关闭状态并释放库存」压成一个领域词，「超时释单」。四个字，agent 从此统一口径，不用每次重新翻译那句长话。码哥提醒一句，术语表不是写完就完，得有人值守，业务词变了 [CONTEXT.md](http://context.md/) 得跟着改，否则 agent 又回到各说各话。

issue tracker 国内多用 GitHub 或本地文件，Linear 用得少，setup 时按实际选，别照抄官方默认。

选安装方式。想改造成团队自己的规范，上 [skills.sh](http://skills.sh/) 可编辑副本；只想蹭一套靠谱默认、跟着作者更新，上 plugin。

一句话立场收在这。

**把它当「纪律工具箱」用，不要当「接管一切的框架」用。**

这正是它跟 GSD、BMAD、Spec-Kit 的根本分野，也是 Matt 撤下 grill-me 真正想告诉你的事。

## FAQ

**Q1** mattpocock/skills 和 Spec-Kit、GSD 到底选哪个？ A 看你要控制权还是省心。GSD/Spec-Kit 帮你接管流程，代价是失控难修；mattpocock/skills 把纪律拆小、可组合，控制权在你。码哥的判断，团队流程还没稳定的，先用这种不接管的，等纪律内化再考虑更重的框架。

**Q2** grill-me 被撤了，我还能用吗？ A 能用，只是不再是默认推荐。它现在定位是「纯粹高压盘问」的场景工具，不需要完整 domain-model 流程时用。Matt 没删它，是把它从推荐位降级，这正是 skill 该有的样子。

**Q3** 中文项目用 [CONTEXT.md](http://context.md/) 共享语言，agent 真能懂吗？ A 能，而且收益比英文项目更明显。中文业务描述往往更长更绕，压成术语表后，agent 命名一致、思考省 token。关键是术语得全组统一，写进 [CONTEXT.md](http://context.md/) 让每个 session 都读得到。

**Q4** [skills.sh](http://skills.sh/) 和 plugin 能混用吗？ A 不建议。 [skills.sh](http://skills.sh/) 是可编辑副本，plugin 是只读订阅，混用会导致同一 skill 两份来源、版本对不上。选一个跟到底。

**Q5** Codex 用户现在能用吗？ A [skills.sh](http://skills.sh/) 安装器已支持 Codex 及其他遵循 Agent-Skills 标准的 agent，原生 Codex 插件还在路线图上。先用 [skills.sh](http://skills.sh/) 装。

## 总结

码哥的判断就一句，17 万 star 是现象，真正值钱的是它把「小、可改、可组合」写进了每个 skill 的基因里。你把它当框架供着，它迟早变成又一个吃灰的插件；你把它当纪律箱随手抽，它才真帮你写出能改的代码。

顺手点个星标，码哥后面写 AI 编码工作流的长文你还能翻出来。

下一篇码哥打算扒一下 domain-model 这个被 Matt 推上规划起点的 skill，从源码看它怎么把需求盘成领域模型。

身边要是有人正在 AI 编码框架里选型，把这篇甩给他，少走半年弯路。

 **![图片](assets/Matt%20Pocock%20%E9%82%A3%E4%B8%AA%205%20%E4%B8%AA%E6%9C%88%E5%86%B2%E5%88%B0%2017%20%E4%B8%87%20star%20%E7%9A%84%20grill-me%EF%BC%8C%E4%BD%9C%E8%80%85%E8%87%AA%E5%B7%B1%E5%8D%B4%E4%B8%8D%E7%94%A8%E4%BA%86%EF%BC%8C%E5%8E%9F%E5%9B%A0%E6%98%AF%E8%BF%99%E5%87%A0%E4%B8%AA/000659fdef65615a176821139f9416c4_MD5.webp)**你在看吗****