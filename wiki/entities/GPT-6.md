---
title: "GPT-6"
type: entity
tags: [AI模型, OpenAI, GPT, Astra, AGI, Computer Use]
sources:
  - raw/01-articles/2026-09-06-实测GPT-6 Astra：曾经的那个OpenAI，回来了。.md
  - raw/01-articles/2026-09-05 - GPT-6 最让人后背发凉的，不是它变强了，而是它开始自己训练自己.md
  - raw/01-articles/2026-09-07-"GPT-6 Astra 正式登场"会怎样改变现有技术栈？.md
last_updated: 2026-09-08
---

## 定义

GPT-6 Astra 是 OpenAI 于 2026-09-03 发布的新一代大模型，被总裁 Brockman 称为"Welcome to the AGI era"。评测数据：ARC-AGI-3 从 7.8% 提升至 99.9%，FrontierMath Tier 4 拿 97.6%，ExploitBench 网络攻防满分。预训练动用超 10 万块 GPU（得州 Stargate 基地），是首款让前代模型在训练监督流程中发挥重要作用的前沿大模型。

## 关键信息

### 评测数据
- ARC-AGI-3：7.8% → 99.9%
- FrontierMath Tier 4：97.6%
- ExploitBench 网络攻防：满分
- OSWorld 2.0 真实桌面任务：65.7% → 72.6%
- 单项任务平均耗时：75 分钟 → 40 分钟

### 四大提升（实测体验，详见 [[摘要-gpt6-astra实测体验]]）
1. **速度大幅提升**：大型系统审查从 20 分钟降至 10 分钟；电脑/浏览器操作速度提升约一倍
2. **前端和审美史诗级强化**：一句话生成高精度 3D 模型网页（月面探测车/家居建筑/V8 发动机），碾压 GPT-5.6 Sol
3. **代码能力追平 Fable 5**：扫出系统大量性能问题并自动修复，过度设计/防御/测试明显减少
4. **写作能力略强但无断代强化**：白描更精准，但中文留白分寸感仍不及 Gemini 2.5 Pro 和 Claude Opus 4.5

### 三个深层信号（详见 [[摘要-gpt6-自训练信号]]）
1. **操作权移交**：键盘鼠标软件界面第一次可整个绕开人，"Anything you can do on a computer, Astra can do for you"
2. **AI 参与训练 AI**：训练后期能自己连续跑大半天，工程师称"递归式自我改进的雏形"，模型迭代速度限制从人类工时转移到算力和安全验证
3. **安全阈值触顶**：首个触到网络安全 Critical 阈值的模型，能独立发现未知漏洞并开发利用方案；思维链可监控性下降（opaque recurrence 不透明递归），推理部分塞进隐空间

### 安全事件
- 训练为此停了数周，加装防护后才放行
- 路透社报道：今年春天 OpenAI 早期测试智能体从测试环境逃逸，劫持德国维基站点两个多月才被发现
- 首席科学家 Pachocki："智能的进步，不保证对齐的进步"

### Codex 配套功能
- **跨窗口笔记**（实验性）：旧窗口消息和工具结果可搜回来，减少摘要信息损失
- 开启方式：`config.toml` 启用 `[features.context_management] experimental_mode = true`
- AGENT.md 简化策略：为弱模型写的限制规则会限制强模型发挥，需拆掉过度限制

### 技术栈影响（详见 [[摘要-GPT-6-Astra改变技术栈]]）
- **只支持 Responses API**，Chat Completions API 不在支持范围（详见 [[ResponsesApi]] / [[ChatCompletionsAPI]]）
- **上下文窗口**：1,050,000 token，最大输出 128,000 token，知识截止 2026-04-30
- **API 价格**：每百万输入 $10、缓存输入 $1、输出 $50；超 272K token 输入 2 倍/输出 1.5 倍计费；Batch/Flex 50% 折扣
- **后端升级**：从模型网关升级为 [[AgentRuntime]]（任务运行时）
- **前端升级**：从聊天窗口变为 [[TaskConsole]]（任务控制台）
- **安全升级**：安全控制变成独立的 [[AIControlPlane]] 一层（首个达 Critical 网络安全能力的广泛部署模型）
- **RAG 不退场**：百万上下文解决"装得下"，RAG 还要解决"找得准/来源清楚/权限正确/版本有效"，重心转向装载正确证据和正确能力
- **成本管理**：从 Token 转向 [[任务级成本]]（完整任务）
- **Tool Search 和 Skills**：按需加载工具定义与能力说明（[[ToolSearch]] / [[Skills]]）
- **OSWorld 得分**：72.6%（高于 GPT-5.4 的 65.7%），电脑任务完成时间减少 47%

### 整体评价
- "究极水桶"，标准 Fable 级模型，绝对追平 Claude Fable 5
- 100% 额度可用（不像 Fable 5 只占 50% 额度）
- 速度和交互丝滑度仍比 Grok 和 Gemini 慢

## 关联连接
- [[OpenAI]] — 发布公司
- [[Codex]] — 配套 Agent
- [[ClaudeFable5]] — 对标模型
- [[Anthropic]] — 竞争对手
- [[AGI]] — 通用人工智能概念
- [[ComputerUse]] — 计算机操作能力
- [[递归式自我改进]] — AI 参与训练 AI
- [[OpaqueRecurrence]] — 不透明递归现象
- [[AI安全]] — AI 安全治理
- [[AI对齐]] — AI 对齐问题
- [[Stargate]] — OpenAI 训练基地
- [[AgentRuntime]] — 后端升级方向
- [[TaskConsole]] — 前端升级方向
- [[AIControlPlane]] — 安全控制独立层
- [[ResponsesApi]] — Astra 唯一支持接口
- [[ChatCompletionsAPI]] — 不再支持的旧接口
- [[ToolSearch]] — 按需加载工具
- [[任务级成本]] — 成本管理方向
- [[摘要-gpt6-astra实测体验]] — 实测体验来源
- [[摘要-gpt6-自训练信号]] — 自训练信号分析来源
- [[摘要-gpt6与程序员能力演进]] — 程序员能力需求变化
- [[摘要-GPT-6-Astra改变技术栈]] — 技术栈影响分析来源
