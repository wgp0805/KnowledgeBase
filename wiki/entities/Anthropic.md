---
title: "Anthropic"
type: entity
tags: [AI公司, 大模型开发商]
sources:
  - raw/01-articles/2026-09-03-顶模 Fable 5.1发布，到底强了多少？.md
  - raw/01-articles/2026-09-07-我帮企业配了两年数字员工，轮到自己却卡在了第一步.md
  - raw/01-articles/2026-09-19-Anthropic 优化 30 多个生物模型，蛋白质设计成本最高降 98%.md
  - raw/01-articles/2026-09-24-A社O社，坐不住了.md
  - raw/01-articles/2026-09-25-扎克伯格谈Muse：个人Agent必须从预训练开始设计，虚拟机、记忆和权限系统是巨头的全栈护城河.md
  - raw/01-articles/2026-09-30-Anthropic 严正警告：GLM-5.3 已具备高级网络攻击能力.md
  - raw/01-articles/2026-10-03-一年前说 PM 会被淘汰，现在 Anthropic 说：人人都得学会当 PM.md
last_updated: 2026-10-08
---

## 定义
人工智能公司，专注于开发安全、可靠、可解释的 AI 系统，是 Claude 系列模型的开发公司。

## 关键信息
- **主要产品**：Claude 系列大语言模型，包括 Fable、Mythos、Sonnet、Opus 等版本
- **最新发布**：Fable 5.1 和 Mythos 5.1 模型
- **定价策略**：Fable 系列定位高端，价格相对较高
- **技术特点**：模型在长任务编码、游戏生成等领域表现突出
- **安全理念**：Mythos 系列模型具有更严格的安全限制
- **《Building effective agents》建议**：先采用尽可能简单的方案，确有必要再增加复杂度；角色增加要等现有流程暴露出具体需要再判断（被 [[数字员工]] 落地方法论引用）

### Claude 封号风波与地区识别代码争议（2026-06 至 2026-08）
来自 [[摘要-codex重置的真正原因]]。2026-06-24 Anthropic 指控与阿里有关的操作者使用约 2.5 万个欺诈账户，与 Claude 进行了 2880 万次交互，用于蒸馏模型能力；6 月底中国开发者社区集中出现 Claude 账号被停用的反馈。之后 [[Claude]] Code 又被发现加入了未充分披露的地区识别与请求标记代码（相关分析涉及时区、代理设置等信息），Anthropic 工程师称这是防止账号转售和模型蒸馏的反滥用实验，并在争议出现后回滚。

这场风波究竟影响了多少普通用户，Anthropic 没有公布数字。但它构成了一个[[竞品迁移窗口]]——只要开发者开始担心"我的账号明天还能不能用"，替代产品的机会就来了。同期的 [[Codex]] 用连续额度重置承接了这波迁移需求（作者声明没有公开数据能证明新增用户来自 Claude）。

### 优化生物模型（2026-09-19）
Anthropic 让 [[Claude]] 用不到四周优化 30 多个生物研究开源模型，覆盖蛋白结构预测、蛋白设计、Protein Language Model 和基因组学。允许极小精度损失时平均提速约 4 倍，要求输出完全一致时平均接近 2 倍加速，并降低显存占用让大型分子系统可在单张 NVIDIA GPU 节点推理。Claude 开发了 FlashPairformer 自定义 kernel 专门加速 triangle attention 和 triangle multiplication（AlphaFold3/OpenFold3/Boltz-2 大量使用），相较 NVIDIA cuEquivariance 快 2.7-2.9 倍。蛋白设计成本从每靶点约 1 万美元降到约 150 美元。详见 [[摘要-anthropic优化生物模型]]。

### Claude Opus 5.5 发布与降价（2026-09-22）
Anthropic 发布 [[Opus]] 5.5（约一个半小时后 OpenAI 推出 GPT-6 Sol/Luna 应战，见 [[大模型价格战]]）。定价：输入/输出每百万 token 降至 4/20 美元，比 Opus 5 低 20%，算上完成任务所需 token 更少，典型任务整体成本比 Opus 5 低约 40%；在 Anthropic 公布的 9 项基准测试中超过三周前的 [[Fable 5.1]]，标价却只有 Fable 5.1 的四成（Anthropic 自己提醒实际差距比跑分小）。提升集中在编程、智能体、计算机使用、数学与科学推理，更擅长需要持续执行的开发任务。动因：Ramp 数据显示 Fable 5 上线一个月只占企业从 Anthropic 采购 token 的 6%，企业不再为最高档自动付费；Anthropic 年化收入 7 月底达 650 亿美元、估值破万亿并已秘密递交上市申请，付费采用率 43.8%（高于 OpenAI 的 39.8%），降价目标是提高留存、扩大部署。详见 [[摘要-a社o社价格战]]。

### 扎克伯格眼中的追赶对象（2026-09）
SemiAnalysis 7 月文章认为 Meta 最有可能追上 [[OpenAI]] 与 Anthropic；扎克伯格在访谈中承认 Llama 4 偏离预期后需重建方法，并把 Anthropic 与 OpenAI 并列为要追赶的前沿实验室。详见 [[摘要-扎克伯格谈muse-全栈护城河]]。

### 对智谱 GLM-5.3 的网络安全评估（2026-09-30）
Anthropic 发布对 [[智谱]] [[GLM-5.3]] 的网络安全评估：五个月前 Anthropic 首次实现自主开发端到端漏洞利用的 Claude Mythos Preview 通过 Project Glasswing 限制性开放（已帮可信防御者发现超 1 万个漏洞），如今同等能力已扩散到 GLM-5.3，且后者发布时缺少有效护栏——欺骗性提示/预填思考 token/abliteration 可使恶意任务参与比例分别达 64%/92%/100%，相同攻击对保留护栏的 Claude 模型全部无效。Anthropic 据此主张：防御者应获得与攻击者至少同等强的前沿模型，政府应对强能力模型开展独立安全测试，呼吁开放权重模型开发者设置适当护栏。详见 [[摘要-anthropic-glm53网络安全评估]]。

### 人人都得学会当 PM（2026-09-10 Lenny and Friends Summit 对谈）
来自 [[摘要-anthropic-人人都得学会当pm]]。Ami Vora 与 Mike Krieger（年初转 IC）在对谈中的要点：
- **PM 定义不变、节奏剧变**：产品始终是"人的问题"与"可用技术"之间的桥；技术从五年一变变成两个月一变，要"人的一侧盯住不放，技术的一侧保持新鲜眼光"
- **AI 没取消 PM，换掉了最贵的部分**：过去贵在做之前想清楚，现在贵的是信息不足时做判断、在岔路中持续推进、把并行实验收拢成产品
- **Mike 的亲身改口**：转 IC 后曾以为 Claude 能顶 PM，被 PM lead 提醒后发现客户/安全/协作等"胶水连接工作"仍需有人负责，一周后承认"你是对的"；Claude 目前还不是 convenor（召集人），但"不是因为做不到，大概只是还没打开那个设置"
- **团队方法**：frame the chaos（给混乱搭框架）+ 清晰的 DRI；实验称 bet、每个 bet 有 lead 决定加码或收掉；多押几注找到 PMF 后再收拢成一个产品
- **产品主张**：做 agent-native 与 malleable software，先建 primitives 底层（详见 [[Agent原生软件]]）
- **边界提醒**：这是模型公司的内部视角——Anthropic 有 foundations 团队统一底层、有实验室把项目停放进 eval harness 等新模型，多数公司没有这种余量

## 关联连接
- [[摘要-anthropic-人人都得学会当pm]] — 来源（PM 角色对谈）
- [[Agent原生软件]] — Mike 提出的 agent-native/primitives 设计观
- [[产品经理角色]] — 对谈讨论的角色概念
- [[摘要-顶模-fable-51发布到底强了多少]] — 来源
- [[摘要-codex重置的真正原因]] — 来源（封号风波与迁移窗口）
- [[摘要-anthropic优化生物模型]] — 来源（优化生物模型）
- [[摘要-a社o社价格战]] — 来源（Opus 5.5 降价与价格战）
- [[摘要-扎克伯格谈muse-全栈护城河]] — 来源（被 Meta 视为追赶对象）
- [[摘要-anthropic-glm53网络安全评估]] — 来源（GLM-5.3 网络安全评估与护栏主张）
- [[Opus]] — Opus 5.5 所属模型系列
- [[大模型价格战]] — Opus 5.5 参与的行业现象
- [[Claude]] — 旗下产品，账号被停用事件的主体
- [[竞品迁移窗口]] — 风波带来的替代机会
- [[AlibabaCloud]] — 涉及欺诈账户指控的关联方
- [[Fable 5.1]] — 旗下模型，被 Opus 5.5 反超
- [[Mythos 5.1]] — 旗下模型
- FlashPairformer — 自定义 kernel
- AlphaFold3 — 被优化模型
- [[摘要-数字员工落地第一步]] — Building effective agents 建议被引用
- [[ComputerUse]] — Opus 5.5 强化的计算机使用能力