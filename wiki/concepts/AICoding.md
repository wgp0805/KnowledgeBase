---
title: "AICoding"
type: concept
tags: [AI, 编程, 范式转变]
sources: [raw/01-articles/6条Claude Code实践中的经验与思考.md]
last_updated: 2026-05-19
---

## 定义
AI 辅助编程范式，工程师角色从代码执行者转变为任务管理者，通过自然语言描述和任务拆分来指挥 AI 完成编程工作。

## 关键信息

### 范式转变
- **旧范式**：理解需求→想清楚实现→一行行写代码
- **新范式**：理解需求→拆分任务→定义目标→自然语言描述→与 AI 沟通管理→验收结果

### 六条核心经验（二师兄总结）
1. **能用插件尽量用**：工业标准化规避幻觉
2. **工程师需具备 Leader 能力**：任务管理+沟通+拍板+验收
3. **任务拆分越细越好**：减少幻觉空间和错误传递
4. **培养完全 AI Coding 感觉**：即使小修改也让 AI 做
5. **编程经验依旧重要**：需能判断 AI 方案利弊
6. **培养产品感觉**：行业 Know-How 和 Idea 判断力被放大

### 口号变迁
- 旧：`Talk is cheap. Show me the code.`
- 新：`Code is cheap. Show me the talk(prompt).`

### 注意事项
- 老旧项目和资金安全相关项目需更慎重
- 清晰有逻辑的表达能力成为竞争优势
- 版本管理是安全网（每步 commit + clear）

## 关联连接
- [[ClaudeCode]] — 核心实践工具
- [[Agent]] — AI Agent 概念
- [[Skill]] — 技能扩展
- [[CLAUDEmd]] — 契约与指令
- [[ai-programmer-survival-guide]] — AI 时代程序员生存指南
- [[cognitive-offloading]] — 认知卸载风险
