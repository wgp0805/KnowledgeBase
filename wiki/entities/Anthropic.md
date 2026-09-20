---
title: "Anthropic"
type: entity
tags: [AI公司, 大模型开发商]
sources:
  - raw/01-articles/2026-09-03-顶模 Fable 5.1发布，到底强了多少？.md
  - raw/01-articles/2026-09-07-我帮企业配了两年数字员工，轮到自己却卡在了第一步.md
  - raw/01-articles/2026-09-19-Anthropic 优化 30 多个生物模型，蛋白质设计成本最高降 98%.md
last_updated: 2026-09-20
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
Anthropic 让 [[Claude]] 用不到四周优化 30 多个生物研究开源模型，覆盖蛋白结构预测、蛋白设计、Protein Language Model 和基因组学。允许极小精度损失时平均提速约 4 倍，要求输出完全一致时平均接近 2 倍加速，并降低显存占用让大型分子系统可在单张 NVIDIA GPU 节点推理。Claude 开发了 [[FlashPairformer]] 自定义 kernel 专门加速 triangle attention 和 triangle multiplication（[[AlphaFold3]]/OpenFold3/Boltz-2 大量使用），相较 NVIDIA cuEquivariance 快 2.7-2.9 倍。蛋白设计成本从每靶点约 1 万美元降到约 150 美元。详见 [[摘要-anthropic优化生物模型]]。

## 关联连接
- [[摘要-顶模-fable-51发布到底强了多少]] — 来源
- [[摘要-codex重置的真正原因]] — 来源（封号风波与迁移窗口）
- [[摘要-anthropic优化生物模型]] — 来源（优化生物模型）
- [[Claude]] — 旗下产品，账号被停用事件的主体
- [[竞品迁移窗口]] — 风波带来的替代机会
- [[AlibabaCloud]] — 涉及欺诈账户指控的关联方
- [[Fable 5.1]] — 旗下模型
- [[Mythos 5.1]] — 旗下模型
- [[FlashPairformer]] — 自定义 kernel
- [[AlphaFold3]] — 被优化模型
- [[摘要-数字员工落地第一步]] — Building effective agents 建议被引用