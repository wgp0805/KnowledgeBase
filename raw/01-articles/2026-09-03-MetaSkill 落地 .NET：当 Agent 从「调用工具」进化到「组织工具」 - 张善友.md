---
title: "MetaSkill 落地 .NET：当 Agent 从「调用工具」进化到「组织工具」 - 张善友"
source: "博客园"
url: "https://www.cnblogs.com/shanyou/p/22817523"
date: "2026-09-03T14:17:00Z"
score: 0.65
tags: ["编程", "中文", "技术"]
auto_captured: true
---

# MetaSkill 落地 .NET：当 Agent 从「调用工具」进化到「组织工具」 - 张善友

> **来源**: 博客园  
> **链接**: https://www.cnblogs.com/shanyou/p/22817523  
> **抓取日期**: 2026-09-03  
> **相关性评分**: 0.65

> 一句话摘要：OpenSquilla 提出了 Meta Skill 的概念——把调度能力写进一份 SKILL.md；而 OpenClaw.NET 用 C# 把这件事做成了可审计、可治理、可上线的工程系统。这篇文章聊聊两者之间的那条路。

![MetaSkill架构图 \(1\)](https://img2024.cnblogs.com/blog/510/202609/510-20260903082314713-1750194087.png)

## 一、先回顾那个判断

[《Meta Skill 来了，Agent 正从「调用工具」变成「组织工具」》。](<https://mp.weixin.qq.com/s/5HjSZUIdwNUWT2xUUKo6Og>), 文章的核心观察很锐利：OpenSquilla 最值钱的东西，不是那智能路由动画，也不是省下来的 60%–80% Token，而是文档里的一句话——

> Agent 下一步要解决的问题，已经从「会不会调用工具」，变成了「会不会组织工具」。

Meta Skill 做的事情，是把「调度」这个脑力活从人的脑子里抽出来，写进一份 SKILL.md：哪些步骤并行、哪些串行、上一步的产出喂给哪个下游、这一步该用便宜模型还是贵模型。

Agent 从此有了一个「项目经理」。

文章还把 Meta Skill 的出现归结为三条线的交点：

  * **模型成熟** ——复杂多步骤编排指令的理解能力过关了，400 行的 SKILL.md 不再是天书；
  * **生态爆发** ——原子 Skill 多到一定程度，必然需要更高的抽象层来管理；
  * **成本优化** ——把「这一步用什么模型」的决策前置到 Skill 层，而不是运行时再试错。



三条线交汇之处，就是所谓的 **Skill 2.0** 。

这个概念我基本认同。但原文停留在「现象观察」层面。作为一个天天和 .NET 打交道的人，我更关心的是另一个问题：

**这套东西，能不能离开 Python 的试验田，走进真正讲究审计、治理、稳定性的工程环境？**

OpenClaw.NET 给出了答案。

## 二、OpenClaw.NET 是什么

OpenClaw.NET 是一个 NativeAOT 友好的 .NET Agent 运行时与网关（github.com/clawdotnet/openclaw.net），MIT 协议，面向想要本地/自托管 Agent 网关的 .NET 开发者。

它有 80+ 原生工具面、9 个渠道适配器（TG、Slack、Discord、邮件、Webhook 等）、原生支持 OpenAI/Claude/Gemini/DeepSeek/Ollama，以及一条从源码到 NativeAOT 发布产物的完整路径。

但真正让我感兴趣的，是它文档目录里那个不起眼的文件：

`docs/opensquilla-meta-skill-migration.md`

——一份 OpenSquilla 风格 Meta Skill 的**迁移与对齐说明** 。这份文档透露了一个事实：OpenClaw.NET 已经把 Meta Skill 的核心编排骨架完整实现了，而且是带着 1907 个测试全部通过的底气实现的。

## 三、MetaSkill 在 .NET 里长什么样

### 1\. 一份 SKILL.md，就是一张 DAG

在 OpenClaw.NET 里，MetaSkill 通过 `kind: meta` 声明，编排逻辑写在 `composition.steps` 里——这就是一张有向无环图（DAG）：

  * `depends_on` 声明步骤间依赖关系；
  * 加载时即做**失败优先（fail-fast）校验** ：重复步骤 ID、缺失依赖、自依赖、依赖环、非法路由目标，全部在执行前拦截。



破图不执行，而不是跑到一半再炸。这一条就很「工程」。

### 2\. 七种原子步骤

运行时支持七种编排节点类型（见 `docs/zh-CN/meta-skill-orchestration.md`）：

步骤类型 | 干什么  
---|---  
`agent` | 委派一个完整子 Agent（多轮推理 + 工具调用，成本最高）  
`skill_exec` | 以受校验的子进程方式执行脚本入口（entrypoint/args/cwd/parse_mode 都是一等契约）  
`tool_call` | 直接调用工具，完全绕过 LLM——确定性副作用成本最低  
`llm_chat` | 单次有界模型生成，不产生工具循环  
`llm_classify` | 约束分类——强制模型从 `output_choices` 闭集合返回恰好一个标签，配合 `routes` 决定 DAG 往哪边走  
`user_input` | 人在环路：暂停、等待输入、从会话检查点恢复  
`fan_out` | 动态步骤展开（v2.x 新增）：对 Jinja `iterable` 求值得到元素列表，按 `fan_out_template` 克隆子步骤，以 `fan_out_max_concurrency` 受控并发执行，最后按 merge mode（`concat` / `json_array` / `first` / `last`）合并——N 路并行搜索、批量工具调用的标配  
  
这张表最值得玩味的是「成本」列：七种类型按执行成本从低到高排列，计划编写者可以为每个步骤选择**最低成本的执行器** ，而不是默认起一个完整子 Agent——这正是智能路由思想在编排层的内化。

另一个容易被忽略的架构事实：整套 DAG 引擎在**双运行时** 间共享——原生 `AgentRuntime` 和 Microsoft Agent Framework 适配器 `MafAgentRuntime` 共用同一套计划校验、模板渲染（Jinja2.NET）、路由规划、checkpoint 和审计持久化，唯一差异是 LLM 调度路径（`CallLlmWithResilienceAsync` vs `IChatClient.GetResponseAsync`），且有等价测试保证两个运行时对同一计划产出完全一致的结果。

`user_input` 值得单独说一句。它把「问用户一个问题再继续」做成了带 checkpoint 的暂停/恢复机制，支持 `form`/`chat` 两种 clarify 模式、字段级类型校验、超时、取消和 `skip_if`。跨恢复边界的暂停痕迹会被完整保留——这对长程交互流程是刚需。

### 3\. 失败，也是图的一部分

这是我认为 OpenClaw.NET 做得最漂亮的一点：**失败不是异常，是图里的一等公民。**

  * `on_failure`：某步失败时激活替代分支，替代步骤的输出会镜像回主步骤 ID，下游依赖无感知；
  * `retry.max_attempts` \+ `retry.backoff_ms` \+ `timeout_seconds`：给工具和模型步骤划定有界执行；
  * `output_contract` / `output_schema`：对 JSON 中间产物做必填属性校验，下游步骤拿到的永远是自己期望的形状；
  * `final_text_mode: structured`：返回结构化执行信封，每个步骤带状态、耗时、失败码——自动化测试和日志分诊不需要再去解析自由文本。



对比一下：在 Python 世界里，这些东西通常散落在 try/except 和约定俗成的字符串解析里。而在这里，它们是**解析器和运行时双层校验的强类型契约** 。

### 4\. 治理：Meta Skill 不是跑起来就完事

如果说 OpenSquilla 的 Meta Skill 是一个「聪明的演示」，OpenClaw.NET 关心的是演示之后的事——**这东西进了生产环境谁负责** 。

它的答案是一整套治理面：

  * **元策略门控** （`SkillsConfig.MetaSkill.Enabled`）：Meta Skill 可以保持安装状态，但对模型提示索引隐藏、抑制路由提示、拒绝显式 `meta_invoke` 调用。想关就关，不用卸载。
  * **运行记录与审计** ：每次 Meta 运行都会持久化最小运行记录，配套 `openclaw skills meta-runs` 操作面——支持按运行过滤、逐步骤追踪、JSON 输出、**只预览不重放的 replay** 、以及**不执行任何工具和模型的 reconstruct 审计重建** 。
  * **提案生命周期** ：从暂停或失败的运行中派生候选提案（proposals），支持 accept / dismiss / rollback / change 的完整生命周期；同操作幂等、冲突操作拒绝，且所有变更动作要求 `OPENCLAW_OPERATOR_ID` 操作员边界——没有身份，免谈。
  * **准入质量门禁** ：提案接受前必须跑过 `opensquilla-authoring-v1` 结构化校验档案，覆盖 structure / trigger / runtime / safety 四组检查，失败时输出机器可读的 `gate.failedChecks`，通过时把门禁快照持久化下来供审计回溯。
  * **创建侧门槛** ：`openclaw skills create --proposal-draft` 生成 Meta Skill 提案草稿时就有阻断式质量门——低质量草稿直接被拒，返回 `proposal_draft_quality_gate_failed`。



一句话：**MetaSkill 在这里不是「写完就跑」的脚本，而是「提案 → 评审 → 门禁 → 落盘 → 可回溯」的受治理资产。**

## 四、我的理解：MetaSkill 的本质是投影

聊到这，说点自己的判断。我一直在实践 DDD、JSON-LD Ontology 和 MetaSkill 的融合。从这个视角看，MetaSkill 的本质其实是**一次投影** ：

> 把人脑里的领域工作流（SOP），投影成一份机器可执行的有向无环图。

这份 SKILL.md 既是一份操作手册，也是一份轻量本体：步骤是节点，`depends_on` 是边，`llm_classify` 是条件路由，`output_schema` 是节点间传递数据的「形状契约」——这和 JSON-LD 里用 Framing 约束图数据的形状，思路是同一个家族。

区别在于执行语义落在哪里。JSON-LD Framing 投影的是**数据** ，MetaSkill 投影的是**行为** 。而 OpenClaw.NET 干的事情，是给这份行为投影补上企业级运行时所需要的一切：fail-fast 校验、有界执行、失败替代、人在环路、审计重建、准入门禁。

还有一个耐人寻味的细节：OpenClaw.NET 在运行时预检里**禁止 Meta Skill 嵌套 Meta Skill** （meta → meta 组合会被直接拒绝）。乍一看是限制，细想是清醒——图论上这叫控制图的深度，工程上这叫防止复杂度失控。微服务的历史已经证明：无约束的组合能力，最后都会变成无人敢动的意大利面。

## 五、结语：两条路线的汇合

OpenSquilla 证明了概念：Agent 的瓶颈已经从「调用工具」转向「组织工具」。

OpenClaw.NET 证明了另一件事：这个概念可以离开演示视频，变成一个 NativeAOT 编译、1907 个测试守护、带完整审计和治理面的 .NET 运行时。

原文作者说，他第一次看到 Meta Skill 时「后背有点发凉」——因为行业的理解可能从此分叉。

我的感觉略有不同。真正让我警惕的不是 Meta Skill 本身，而是它揭示的那个趋势：

**未来值钱的不是会写提示词的人，也不是会调 API 的人，而是能把自己的领域工作流抽象成一张干净 DAG 的人。**

这张图画在哪里，反而不是最重要的——画在 Python 的 SKILL.md 里，或者画在 .NET 的 `composition.steps` 里，殊途同归。

重要的是，你脑子里有没有那张图。

* * *

### 参考资料

  * OpenSquilla GitHub 仓库：<https://github.com/opensquilla/opensquilla>
  * OpenClaw.NET GitHub 仓库：<https://github.com/clawdotnet/openclaw.net>
  * OpenClaw.NET MetaSkill 编排架构（中文）：`docs/zh-CN/meta-skill-orchestration.md`
  * OpenClaw.NET Meta Skill 迁移说明：`docs/opensquilla-meta-skill-migration.md`
  * 原文：《Meta Skill 来了，Agent 正从「调用工具」变成「组织工具」》：<https://mp.weixin.qq.com/s/5HjSZUIdwNUWT2xUUKo6Og>




---
> 原文链接: https://www.cnblogs.com/shanyou/p/22817523