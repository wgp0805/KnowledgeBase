---
title: "DeepSeek V4.1-Flash"
type: entity
tags: [DeepSeek, V4.1-Flash, 国产模型, Harness, 模型更新, 搜索API]
sources: [raw/01-articles/2026-09-16-DeepSeek-V4.1-Flash 的最佳 Harness 搭档，我觉得可能是 Claude Code.md, raw/01-articles/2026-10-12-从 0 到 1：Electron41 + Vite8 + OpenAI SDK 接入 DeepSeek-V4.1-Flash 桌面端AI系统 - yxybox.md, raw/01-articles/2026-10-17-DeepSeek V4.1 Flash 新版本：许愿式编程一键成真.md, raw/01-articles/2026-10-21 - 真正的 OpenAI！DeepSeek 开源内部推理框架 DeepInfer。.md]
last_updated: 2026-10-22
---

## 定义
DeepSeek-V4.1-Flash 是 [[DeepSeek-V4|DeepSeek V4]] 系列的升级版本，技术文件指出：大模型很少只跑在固定 Harness 里，不同脚手架的提示词/工具定义/上下文管理/交互协议都会影响结果。官方测试显示 DSH Minimal 模式反常识地优于 Standard 与 PTC，而 [[ClaudeCode|Claude Code]] 或 [[Codex]] 接 DeepSeek-V4.1-Flash 开箱即用接近峰值。

## 关键信息

### Harness 影响模型表现
DeepSeek 技术文件核心观点：
- 同一模型在不同 Harness 下表现差异巨大
- **DSH Minimal 模式** 在两项测试中都高于 Standard 和 PTC 模式（反常识：功能更多更复杂 ≠ 成功率更高）
- **Claude Code 或 Codex** 接 DeepSeek-V4.1-Flash，开箱即用水平接近峰值

### Space Invaders 横评（[[SimonWillison|Simon Willison]] 原题）
四种 Harness 综合排名：**① Claude Code 9.2 分 ② Pi Agent 8.9 分 ③ DSH 标准 8.7 分 ④ DSH 极简 7.2 分**

| Harness | 用时 | Token | TPS | 结果 |
|---------|------|-------|-----|------|
| Pi Agent | 36分09秒 | 9.7M tok | - | 完成 |
| DSH 标准 | 8分54秒 | 4.2M tok | 275 tok/s | 完成 |
| DSH 极简 | 40分04秒 | 1.5M tok | 295 tok/s | **失败** |
| Claude Code | 9分34秒 | 3.0M tok | 205.5 tok/s | 完成 |

### Claude Code 胜出原因
- 交付质量/代码准确率/工程完整性均第一
- 上下文管理极其精炼：仅用 Pi Agent 约 1/3 的 Token 和 1/4 的耗时拿到全场最优效果
- 最懂原版：街机竖屏/飞碟/掩体破损等细节齐全，外壳和数据面板专业
- 定位：生产级工业落地 ROI 最高标杆

### 各 Harness 适用场景
- **Claude Code**：生产级工业落地，ROI 最高
- **Pi Agent**：质量极致要求、成本耗时完全不敏感的探索性任务（Token 全场最高 9.7M）
- **DSH 标准模式**：交付时效要求极高、任务复杂度适中的日常高吞吐开发（275 tok/s 全场最快）
- **DSH 极简模式**：Token 极致压榨但有代价（省 84.5% Token，但缺乏全局视野，40 分钟全场最慢，最终失败）

## 关键启示
**如果你觉得某个模型不太好，或许可以换一个 Harness。** Harness 选择直接影响交付质量、Token 消耗、耗时、辅助使用友好度。

### 桌面客户端接入实证（2026-10-12，详见 [[摘要-electron41-vite8-deepseek桌面ai]]）
第三方开发者用 [[Electron]] 41 + [[Vite]] 8 + Vue 3 + OpenAI SDK 直接接入该模型做桌面 AI 对话客户端，说明其**接入门槛低到普通前端项目即可承载**：
- 通过 OpenAI 兼容端点 + `stream: true` 即可获得 SSE 流式输出，首字延迟 < 100ms
- `thinking: { type: 'enabled' | 'disabled' }` 开关控制深度思考；`reasoning_content` 字段返回思维链，可做可折叠推理面板
- `temperature` 0.4 偏确定性；未设 `max_tokens` 时非思考模式默认 8K、思考模式 64K
- 该项目已作为“桌面 AI 流式会话模板”对外售卖，反映该模型在个人开发者中的普及度

### 1017 版本更新（2026-10-17，详见 [[摘要-deepseek-v41-flash-1017]]）
- **版本号**：V4.1-Flash-1017，网页端/APP/API 同步变更；权重开源（HuggingFace/ModelScope `deepseek-ai/DeepSeek-V4.1-Flash-1017`）
- **性能–费用帕累托改进**：基准提升同时任务运行时间与输出长度同步缩短，在多个 Harness 下达新的帕累托最优；**重点适配 DeepSeek Harness、腾讯 [[CodeBuddy]]、[[WorkBuddy]]**（需 DeepSeek Harness 0.2.1-rc.1+）
- **许愿式编程**：基于自反馈的强化学习（RL）增强从零构建 3D 建模、游戏等完整项目能力——四例演示（故宫 3D 建模、网页赛车游戏、Godot 复刻《传送门2》、Valley of Ages）均少提示词、极短交互轮次完成（详见 [[许愿式编程]]）
- **Search/Fetch API 开放**：自研 AI 原生搜索引擎（千亿级网页索引，过滤 SEO 作弊/GEO 操纵/低质 AIGC）的两个接口对外开放，**5 元/千次**；当前在 DeepSeek Harness/Claude Code/Codex 走 Server 端工具调用暂不计费，**2026-11-01 00:00 起按次收费**

### 大规模推理部署实践（2026-10-21，详见 [[摘要-deepinfer-deepseek开源推理框架]]）
基于开源引擎 [[DeepInfer]] 的官方部署报告《DeepSeek V4.1 Flash 大规模推理部署实践》给出生产级数字：
- **单集群日吞吐 155 万亿 Tokens**，KV Cache 保留时间拉长至 **72 小时以上**
- **三阶段分离部署**：视觉编码器放最便宜的单卡、Prefill 放 8 卡做小规模专家并行、Decode 放 64~128 卡超节点做大规模专家并行（Wide-EP）+ EPLB 动态负载均衡
- **KV Cache 落盘**：基于自研 3FS 建约 100 PiB SSD 存储集群，峰值聚合读带宽 10 TiB/s，128 Token 分页块缓存全量写盘；SWA KVCache 只留内存约 180 秒、线上命中率超 98%，未命中时 SWA Bounded Replay 只重算最近 128 Token，使预填充在解码层的总计算量减少近一半
- **DSpark 置信度投机解码**：只把验证算力分给收益最高的前缀子集，相比固定验证 5 个 Token，线上吞吐提升 6%
- **零开销异步批调度**：GPU 执行第 N 步时 CPU 并行做第 N+1 步调度与第 N-1 步后处理，GPU 全程零空闲
- **批次无关确定性**：`DEEPINFER_BATCH_INVARIANT=1` 开启后，相同输入无论并发批次怎么变都产出相同结果，便于线上复现与评测

## 关联连接
- [[摘要-deepseek-v41-flash-1017]] — 2026-10-17 来源（1017 版本：帕累托改进、许愿式编程、搜索 API 开放）
- [[许愿式编程]] — 1017 版本支撑的开发方式概念
- [[CodeBuddy]] — 1017 点名优化的腾讯框架
- [[AgenticSearch]] — Search/Fetch 接口服务的场景
- [[摘要-deepseek-v4-1-flash-harness横评]] — 来源
- [[DeepSeek-V4]] — V4 系列
- [[DeepSeek]] — 母公司
- [[ClaudeCode]] — 最佳 Harness 搭档（综合第一）
- [[DeepSeekHarness]] — 官方 Harness（标准/极简模式）
- [[Pi]] — Pi Agent
- [[Codex]] — 官方提到开箱即用接近峰值的另一个 Harness
- [[SimonWillison]] — Space Invaders 测试原题作者
- [[Harness差异化]] — 概念页
- [[TokenEfficiency]] — 概念
- [[老章]] — 文章作者
- [[摘要-electron41-vite8-deepseek桌面ai]] — 来源（桌面客户端接入实证）
- [[Electron]] — 桌面客户端载体
- [[Vite]] — 构建工具
- [[SSE流式输出]] — 接入后的核心技术机制
- [[DeepInfer]] — 部署报告对应的推理引擎
- [[摘要-deepinfer-deepseek开源推理框架]] — 来源（大规模推理部署实践）
