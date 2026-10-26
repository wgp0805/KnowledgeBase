---
title: "DeepSeek"
type: entity
tags: [AI模型, 大语言模型, 中国公司]
sources: [raw/01-articles/2026-09-03-腾讯内测Cheso，一个专做 PPT 的 AI Agent，实测有吓到我.md, raw/01-articles/2026-09-23-开多个 Agent 后 Claude Code 账单翻了 4 倍，一个配置解决了 - 码哥字节.md, raw/09-archive/2026-10-03-DeepSeek为什么要16000张卡？.md, raw/09-archive/2026-10-06-deepseek拟人形象大战，究竟在吵什么.md, raw/01-articles/2026-10-21 - 真正的 OpenAI！DeepSeek 开源内部推理框架 DeepInfer。.md]
last_updated: 2026-10-22
---

## 定义
中国AI公司开发的大语言模型，是Cheso集成的多个AI模型之一。

## 关键信息
- **开发公司**：DeepSeek
- **产品类型**：大语言模型
- **集成平台**：Cheso演示文稿生成工具
- **技术定位**：为Cheso提供AI能力支持

### Anthropic 兼容端点与 Claude Code 分层接入（2026-09）
来自 [[摘要-claude-code-多agent账单分层路由]]。DeepSeek 提供 Anthropic 兼容 API 端点（`https://api.deepseek.com/anthropic`，**末尾不能加 `/v1`**），Claude Code 改 `ANTHROPIC_BASE_URL` + 模型级别变量即可接入：
- **deepseek-v4-pro[1m]**：主 Agent（Opus/Sonnet 级），`[1m]` 后缀解锁 1M 上下文，不加只有 200K
- **deepseek-v4-flash**：子 Agent（Haiku 级），价格 $0.14/$0.28，比 Claude Haiku 4.5 便宜一个数量级
- **兼容性边界**：端点暂不支持 image/document 内容块（截图类任务拿到空白且无报错）；模型名写错时**静默 fallback 到 v4-flash 不报错**，需去控制台核对实际调用模型

### 16000 张昇腾卡的两本账（2026-10-03，详见 [[摘要-deepseek-16000张卡]]）
- **采购**：华为给 DeepSeek 的产能约 16000 张卡（按梁文锋算法≈4000 张英伟达卡，做不了下一代模型但够帮华为跑通生态）；彭博社报道其计划在乌兰察布 1GW 数据中心部署至少 16 万颗昇腾 950DT
- **价格观**：梁文锋 2026-07 交流会称华为卡"贵百分之一百、两百都无所谓"——两本账里芯片价格排不到前头，多掏钱换的是"确定拿到卡"的时间与确定性
- **国产替代逻辑**：不是"国产更好"而是"英伟达买不到"，前提脆弱但当下成立
- **开源解后半截（2026-09-30）**：六组件对齐昇腾（含 DeepGEMM-Ascend、DeepEP-Ascend），把训练用的每个 TileLang 算子在昇腾重做一遍，适配一个算子从按周按月变成换编译器后端——"三年前解的是芯片能不能跑，现在解的是能不能排上"
- **买与送一套动作**：一边买华为卡，一边把工具链开源给所有芯片厂，多几家能出卡它就多几个拿货的地方

### 开源生产级推理基础设施（2026-10-21，详见 [[摘要-deepinfer-deepseek开源推理框架]]）
DeepSeek 把"支撑自家线上亿级流量"的推理基础设施首次完整开源，这是其开源策略从"底层零件"升级为"整车生产线"的标志：
- **[[DeepInfer]]**：生产级推理引擎，基于 vLLM 演进并吸收 SGLang / TensorRT-LLM 思路；原生兼容英伟达 SM100 架构 GPU 与华为 [[昇腾]] 950 NPU。基于该框架的 [[DeepSeek-V4.1-Flash]] 单集群日吞吐 155 万亿 Tokens，KV Cache 保留时间达 72 小时以上；开源不到 24 小时 GitHub Star 破 1.46 万
- **[[DeepSeekRecipe]]**：Rust 编写的生产级 Token 编解码组件，统一 Chat Completions / Responses / Messages 三种协议，破解"私有化部署权重一样但深度思考与工具调用不如官方 API 稳定"的病根（协议转换 + 分词处理）
- **社区评价**："这才是真正的 OpenAI，就像村民免费向你分享了核聚变技术"——与此前开源 FlashMLA / DeepGEMM / DeepEP / TileLang 的"散装零件"形成对比
- **战略一致性**：与"买华为卡同时把工具链开源给所有芯片厂"的动作一致——开源解的是后半个问题，让更多芯片厂能出卡

### 拟人形象大战（2026-10-06，详见 [[摘要-deepseek拟人形象大战]]）
- **鲸鱼娘是社区去中心化产物**：DeepSeek 横空出世之初 DeepSeek 娘形象即出现（与 ChatGPT 娘、Kimi 娘、豆包看板娘并存），经御姐版/萌妹版/2D/3D 多版本互相吸收迭代，"吃白饭的蓝色大肥鱼"逐渐获社区公认；男版形象则只是个人画师作品——争论本质是个人作品与社区共识的差异
- **引爆点**：男版一方提出"软色情擦边"指责后，经历网文大战、二游大战的男性社区跳过论证流程直接对抗，核心诉求是社区文化主权（"我们创造的世界，凭什么要接受你的擦边审核"），详见 [[AI拟人形象]]

## 关联连接
- [[摘要-deepseek-16000张卡]] — 来源（16000 张卡与开源工具链）
- [[昇腾]] — 采购的国产芯片
- [[华为]] — 卡的供应方
- [[中芯国际]] — 制造产能瓶颈
- [[TileLang]] — 开源组件的语言层
- [[摘要-腾讯内测cheso一个专做ppt的ai-agent]] — 来源
- [[Cheso]] — 集成平台
- [[DeepSeek-V4]] — 分层路由使用的模型系列
- [[ClaudeCode]] — 兼容端点的主要接入方
- [[模型路由]] — 分层路由概念
- [[摘要-claude-code-多agent账单分层路由]] — 来源（Anthropic 兼容端点实战）
- [[摘要-deepseek拟人形象大战]] — 来源（拟人形象社区战争）
- [[AI拟人形象]] — 拟人形象概念
- [[卢诗翰]] — 战争复盘的作者
- [[摘要-deepseek多模态模型上线]] — 来源（V4-Flash-Vision 多模态上线）
- [[DeepInfer]] — 开源的生产级推理引擎
- [[DeepSeekRecipe]] — 开源的生产级 Token 编解码组件
- [[摘要-deepinfer-deepseek开源推理框架]] — 来源（推理基础设施开源）
