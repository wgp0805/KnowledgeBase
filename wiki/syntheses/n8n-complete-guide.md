---
title: "n8n 完整指南"
type: synthesis
tags: [n8n, 自动化, AI-Agent, 工作流, 低代码]
sources: [raw/01-articles/使用n8n搭建Agent项目笔记.md]
last_updated: 2026-05-25
---

# n8n 完整指南

## 一、n8n 是什么

n8n（发音为 "n-eight-n"）是一款**开源的工作流自动化平台**，类似于 Zapier、Make（原 Integromat）的开源替代品。它允许用户通过可视化拖拽界面或代码方式，将不同的应用程序、API 和服务连接起来，实现业务流程自动化。

**核心特点**：
- **开源免费**：可自托管，无供应商锁定
- **可视化编排**：拖拽式工作流编辑器
- **代码扩展**：支持 JavaScript/Python 自定义逻辑
- **AI 原生支持**：内置 AI Agent 节点，支持 LLM 集成

## 二、n8n 能用来干什么

### 典型应用场景

| 场景 | 示例 |
|------|------|
| **数据同步** | CRM ↔ ERP、数据库 ↔ 表格 |
| **通知自动化** | 订单状态变更 → 微信/钉钉/邮件通知 |
| **内容处理** | RSS → AI 摘要 → 自动发布到博客 |
| **客服自动化** | 用户提问 → AI 回答 → 工单创建 |
| **开发运维** | GitHub Webhook → 自动部署 → 监控告警 |
| **AI Agent** | 构建 RAG 知识库问答、多 Agent 协作 |

### 支持的集成

n8n 官方支持 **400+ 集成**，包括：
- **数据库**：MySQL、PostgreSQL、MongoDB、Redis
- **云服务**：AWS、GCP、Azure
- **SaaS**：Slack、Notion、Google Sheets、Airtable
- **AI/LLM**：OpenAI、Claude、Ollama、LangChain
- **开发工具**：GitHub、GitLab、Jira、Jenkins

## 三、n8n 解决了什么问题

### 1. 降低集成成本
传统方式需要为每个 API 编写代码，n8n 提供预置节点，配置即可使用。

### 2. 消除重复劳动
将手动、重复的业务流程自动化，释放人力。

### 3. 数据孤岛打通
连接不同系统，实现数据流转和业务协同。

### 4. AI 落地门槛降低
提供可视化 AI Agent 构建能力，非技术人员也能搭建智能工作流。

### 5. 供应商锁定规避
开源自托管方案，数据和逻辑完全可控。

## 四、未来发展前景

### 市场趋势
- **工作流自动化市场**预计 2027 年达到 180 亿美元
- **AI Agent** 成为行业热点，n8n 已原生支持
- 企业对**低代码/无代码**需求持续增长

### n8n 竞争优势
- **开源社区活跃**：GitHub 50k+ Star，持续迭代
- **AI 能力领先**：原生 AI Agent 节点，支持 RAG、Function Calling
- **企业版成熟**：提供 SSO、审计、权限管理等企业特性
- **融资充足**：获得大量投资，产品持续演进

### 潜在挑战
- 与 Zapier、Make 等成熟产品的竞争
- 企业级安全和合规要求
- 复杂场景下的性能优化

## 五、是否值得学习

**推荐学习**，理由如下：

| 维度 | 评估 |
|------|------|
| **就业需求** | 自动化/AI Agent 岗位需求增长 |
| **技能迁移** | 工作流思维适用于任何自动化场景 |
| **学习曲线** | 可视化界面，入门门槛低 |
| **社区支持** | 中文社区活跃，文档完善 |
| **职业发展** | 可向 AI Agent 架构师方向发展 |

## 六、详尽使用教程

### 6.1 安装部署

#### 方式一：Docker 部署（推荐）

```bash
# 创建数据卷
docker volume create n8n_data

# 运行容器
docker run -d \
  --name n8n \
  -p 5678:5678 \
  -v n8n_data:/home/node/.n8n \
  n8nio/n8n
```

访问 `http://localhost:5678` 即可使用。

#### 方式二：Docker Compose

```yaml
version: '3.8'
services:
  n8n:
    image: n8nio/n8n
    container_name: n8n
    ports:
      - "5678:5678"
    volumes:
      - n8n_data:/home/node/.n8n
    environment:
      - N8N_BASIC_AUTH_ACTIVE=true
      - N8N_BASIC_AUTH_USER=admin
      - N8N_BASIC_AUTH_PASSWORD=your_password
      - GENERIC_TIMEZONE=Asia/Shanghai

volumes:
  n8n_data:
```

#### 方式三：npm 安装

```bash
npm install n8n -g
n8n start
```

### 6.2 核心概念

#### 节点（Node）
工作流的基本单元，每个节点执行一个特定操作：
- **触发器节点**：工作流的起点（Webhook、定时、事件）
- **操作节点**：执行具体动作（HTTP 请求、数据库操作、AI 调用）
- **逻辑节点**：条件判断、循环、合并

#### 工作流（Workflow）
由多个节点连接组成的自动化流程。

#### 凭证（Credential）
存储 API Key、OAuth Token 等认证信息。

### 6.3 创建第一个工作流

#### 示例：RSS 订阅 → AI 摘要 → 邮件通知

**步骤 1：添加 RSS 触发器**
1. 拖入 "RSS Feed Trigger" 节点
2. 配置 RSS URL：`https://example.com/feed.xml`
3. 设置轮询间隔：每 1 小时

**步骤 2：添加 AI 摘要节点**
1. 拖入 "OpenAI" 节点
2. 配置 API Key（在凭证管理中添加）
3. 设置 Prompt：`请用中文总结以下文章，不超过100字：{{ $json.content }}`

**步骤 3：添加邮件节点**
1. 拖入 "Send Email" 节点
2. 配置 SMTP 信息
3. 设置邮件内容：`AI 摘要：{{ $json.summary }}`

**步骤 4：连接节点并激活**
1. 拖拽连接三个节点
2. 点击右上角 "Active" 开关
3. 保存工作流

### 6.4 构建 AI Agent

#### 步骤 1：创建 Agent 工作流
```
触发器 → AI Agent → 响应输出
```

#### 步骤 2：配置 AI Agent 节点
1. 拖入 "AI Agent" 节点
2. 选择 Agent 类型：
   - **Conversational Agent**：对话式 Agent
   - **Tool Calling Agent**：工具调用 Agent
   - **ReAct Agent**：推理+行动 Agent

#### 步骤 3：添加工具（Tools）
为 Agent 添加能力：
- **HTTP Request**：调用外部 API
- **Code**：执行自定义代码
- **Vector Store**：RAG 知识库检索
- **Calculator**：数学计算

#### 步骤 4：配置记忆（Memory）
添加 "Window Buffer Memory" 节点，保持对话上下文。

#### 步骤 5：测试与部署
1. 使用 "Chat" 界面测试
2. 配置 Webhook 触发器
3. 部署到生产环境

### 6.5 RAG 知识库搭建

#### 架构
```
文档上传 → 文本分割 → 向量化 → 存储
用户提问 → 向量检索 → LLM 回答
```

#### 实现步骤

**步骤 1：准备向量数据库**
- 推荐使用 Qdrant（n8n 原生支持）
- Docker 部署：`docker run -p 6333:6333 qdrant/qdrant`

**步骤 2：创建文档处理工作流**
```
触发器 → 文档加载 → 文本分割 → Embedding → 向量存储
```

**步骤 3：创建问答工作流**
```
用户提问 → Embedding → 向量检索 → LLM 回答
```

**步骤 4：配置关键参数**
- Chunk Size：500-1000 tokens
- Overlap：50-100 tokens
- Top K：3-5 个相关文档

### 6.6 高级技巧

#### 错误处理
1. 添加 "Error Trigger" 节点
2. 配置重试策略
3. 设置告警通知

#### 循环处理
使用 "Split In Batches" 节点处理数组数据。

#### 条件分支
使用 "IF" 或 "Switch" 节点实现条件逻辑。

#### 子工作流
将复杂逻辑拆分为可复用的子工作流。

### 6.7 企业级部署建议

#### 安全配置
```bash
# 启用 HTTPS
N8N_PROTOCOL=https
N8N_SSL_CERT=/path/to/cert.pem
N8N_SSL_KEY=/path/to/key.pem

# 限制访问
N8N_BASIC_AUTH_ACTIVE=true
N8N_BASIC_AUTH_USER=admin
N8N_BASIC_AUTH_PASSWORD=strong_password
```

#### 性能优化
- 使用 PostgreSQL 替代 SQLite
- 配置 Redis 缓存
- 启用队列模式处理高并发

#### 监控告警
- 集成 Prometheus + Grafana
- 配置工作流执行告警
- 设置资源使用阈值

## 七、学习资源

| 资源 | 链接 |
|------|------|
| **官方文档** | https://docs.n8n.io |
| **社区论坛** | https://community.n8n.io |
| **GitHub** | https://github.com/n8n-io/n8n |
| **模板库** | https://n8n.io/workflows |
| **YouTube** | 搜索 "n8n tutorial" |

## 八、总结

n8n 是一款**功能强大、灵活可扩展的工作流自动化平台**，特别适合：
- 需要打通多个系统的企业
- 希望构建 AI Agent 的开发者
- 追求数据自主可控的团队

**学习建议**：
1. 从简单的数据同步场景入手
2. 逐步尝试 AI Agent 搭建
3. 参与社区交流，积累实战经验

## 关联连接

- [[摘要-使用n8n搭建Agent项目笔记]] — n8n AI 工作流搭建实践
- [[Agent]] — AI Agent 核心概念
- [[Docker]] — 容器化部署方式
- LLM — 大语言模型集成
- [[RAG]] — 检索增强生成技术
