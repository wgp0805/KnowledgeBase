---
title: "AI编程助手总在失忆？试试这个开源记忆层AgentMemory"
type: source
tags: [AgentMemory, AI编程, 记忆层, MCP, 开源, Agent, Claude Code, Cursor, OpenViking]
sources: [raw/01-articles/2026-09-09-AI 编程助手总在“失忆”？试试这个开源记忆层 AgentMemory.md]
last_updated: 2026-09-14
---

# 摘要：AI编程助手总在"失忆"？试试开源记忆层AgentMemory

## 核心摘要
AgentMemory是一款开源记忆层项目（GitHub 28k Star），解决AI编程助手跨会话失忆问题。它通过hooks捕获会话中的提示词、工具调用、文件访问、命令执行结果，经压缩、索引后形成可检索记忆，在新会话开始时注入相关上下文。采用四层记忆模型，支持BM25关键词检索、向量语义检索和图关系检索，通过MCP和REST API让多个Agent共享同一记忆服务。

## 关键要点
- 定位：Agent的持久化记忆层（捕获→整理→检索→注入），解决跨会话失忆
- GitHub 28k Star，项目地址：https://github.com/rohitg00/agentmemory
- 通过hooks自动捕获：提示词、工具调用、文件访问、命令执行结果、错误信息
- 四层记忆模型：从零散工具调用记录逐步整理成稳定项目知识
- 三种检索方式：BM25关键词检索（无模型依赖）、向量语义检索（需embedding）、图关系检索
- MCP负责Agent调用记忆服务，hooks负责自动采集会话信息——两者缺一不可
- 支持多Agent共享：Claude Code、Cursor、Codex CLI、OpenCode、Gemini CLI
- 后端运行在iii-engine之上（非简单数据库，是运行时和基础设施层）
- 与OpenViking区别：agentmemory=工作记忆层，OpenViking=上下文管理系统
- Windows部署仍有门槛：需手动下载iii.exe或用WSL2/Docker Desktop

## 详细内容

### 解决的问题
AI编程助手单次会话表现不错，但会话结束后丢失上下文。第二天继续时，Agent需重新扫描项目、重新确认认证方案、重新询问技术选型原因。CLAUDE.md/.cursorrules等文件需手动维护、易过时、检索能力有限。

### 工作流程
1. **捕获：** 通过hooks记录工具调用、文件读取、命令执行的原始观察
2. **记忆：** 压缩、索引，提炼值得长期保留的事实、决策和工作方式（非全文搬运）
3. **召回：** 新会话开始时，只注入与当前项目和问题相关的内容
4. **注入：** 通过MCP/REST API提供给Agent

### 四层记忆模型
项目README将记忆整理为四个层级（适合软件开发场景）：
- 单次工具调用只是局部动作（读文件、执行命令）
- 有价值的内容需多个动作组合才能看出（bug根因、实现选择、测试边界）
- 零散记录逐步整理成稳定项目知识
- 提供版本关系、来源追踪、过期处理、相似记忆提示

注意："像人脑一样按遗忘曲线自动管理记忆"是产品设计类比，非真正复现人类记忆机制。

### 三种检索信号
| 检索方式 | 适用场景 | 依赖 |
|----------|----------|------|
| BM25关键词 | 文件名、函数名、库名、错误信息 | 无模型依赖 |
| 向量语义 | 表达不同但含义相近的问题 | embedding模型（本地Xenova/all-MiniLM-L6-v2） |
| 图关系 | "某决策和哪些文件/模块/问题有关" | 知识图谱能力 |

### MCP vs hooks（易混淆）
- **MCP：** 让Agent调用记忆服务（保存/搜索/查看历史），解决"能不能用记忆工具"
- **hooks：** 在会话生命周期中自动采集信息，解决"工作过程能不能被记录"
- 只接通MCP→只能手动保存查询；想要自动记录→还需安装插件/hooks

Claude Code插件安装：
```
/plugin marketplace add rohitg00/agentmemory
/plugin install agentmemory
```

### 与OpenViking的区别
| 项目 | 定位 | 范围 |
|------|------|------|
| agentmemory | Agent的持久化记忆层 | 会话捕获、记忆整理、检索、自动注入 |
| OpenViking | Agent的上下文管理系统 | 文档、资料、技能、记忆统一为虚拟文件系统 |

- "每次开始编码都要重新解释项目"→agentmemory更直接
- "统一管理大量文档、技能、项目资料"→OpenViking覆盖面更广

### iii-engine
agentmemory后端运行在iii-engine之上。
- 官方定位：用Worker、Function、Trigger三个抽象组合和观察服务
- 提供：状态存储、消息流、任务触发、Worker管理、可观测能力
- 理解为agentmemory的运行时和基础设施层（非简单数据库）
- 用户无需单独搭建PostgreSQL、Redis、Express、pm2、Prometheus
- 代价：增加对iii生态的依赖

### 安装与部署
```
npx -y @agentmemory/agentmemory@latest
```
首次启动进入交互式向导：选择Agent→配置模型提供商→决定全局命令→启用MCP/hooks/技能。

本地服务端口：http://localhost:3113

**Windows注意：** 需手动下载iii.exe，或用WSL2/Docker Desktop。Linux/macOS可由npm包自动处理iii-engine安装。

### 模型配置
支持多种模型提供商，也支持Ollama、LM Studio、vLLM等OpenAI兼容接口的本地服务。"OpenAI"是协议兼容选项，非只能用OpenAI模型。配置文件：`~/.agentmemory/.env`

### 核心价值与风险
**最值得关注：** 把记忆变成相对完整的工程管线（捕获→压缩→索引→召回），重点是召回质量和记忆治理。

**Agent长期记忆需解决的三个问题：**
1. 什么内容值得记住
2. 什么内容应该在什么时候被召回
3. 错误、过时或敏感内容如何被删除

**风险：** 记忆保存越多未必越好，旧方案/临时判断/错误总结长期注入会误导Agent。需定期清理错误信息，谨慎开启自动采集。

## 关联连接
- [[AgentMemory]]
- [[OpenViking]]
- [[MCP协议]]
- [[AI编程助手]]
- [[Agent记忆层]]
- [[iii-engine]]
- [[ClaudeCode]]
- [[跨会话记忆]]
