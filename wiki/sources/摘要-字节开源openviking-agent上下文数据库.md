---
title: "字节又开源了一个顶级Agent项目：OpenViking"
type: source
tags: [OpenViking, Agent, 上下文数据库, 记忆系统, 字节开源, MCP, 虚拟文件系统]
sources: [raw/01-articles/2026-09-13 - 字节又开源了一个顶级Agent项目！.md]
last_updated: 2026-09-14
---

# 摘要：字节开源Agent上下文数据库OpenViking

## 核心摘要
OpenViking是字节跳动开源的面向AI Agent的上下文数据库（GitHub 35K+ star），将记忆、资源、技能统一存放在viking://协议下的虚拟文件系统中。Agent可用ls、tree、find等熟悉操作浏览自己的上下文，内容写入时处理成L0摘要、L1概览、L2详情三层按需加载，支持跨会话记忆召回，并可接入Claude Code、Codex、Cursor等主流Agent。

## 关键要点
- OpenViking是面向AI Agent的开源上下文数据库，解决Agent"记不住事"的问题
- 记忆/资源/技能统一存放在viking://虚拟文件系统，Agent用ls/tree/find浏览上下文
- 内容三层处理：L0摘要、L1概览、L2详情，按需加载省token
- 目录递归检索：先定位得分最高目录再逐层下探，结果连同周边上下文一起返回
- 会话沉淀记忆：会话结束后异步把用户偏好和Agent经验写成长期记忆，跨会话自动召回
- 多Agent共用：通过插件、MCP、SDK接给Claude Code、Codex、Cursor等外部Agent
- 部署轻量：一条docker run把服务、控制台、VikingBot一起带起
- 记忆以明文文件落盘，看得见摸得着，可观察可管理

## 详细内容

### 核心特性
OpenViking把上下文当工程对象来对待，和查黑盒向量库不同，Agent用熟悉的文件系统操作浏览自己的上下文。

关键特性：
- **目录递归检索**：先定位得分最高的目录，再逐层下探，结果连同周边上下文一起返回
- **会话沉淀记忆**：会话结束后异步把用户偏好和Agent经验写成长期记忆，下次对话自动召回，跨会话不失忆
- **多Agent共用**：同一份记忆通过插件、MCP、SDK接给外部Agent，跨项目共用

### 安装部署
配置文件ov.conf包含四块：
- **server**：服务监听地址、端口、管理密钥、public_base_url
- **storage**：记忆和向量数据落盘位置（agfs和vectordb均用local后端）
- **embedding**：向量模型（走阿里云百炼OpenAI兼容接口，text-embedding-v4，1024维）
- **vlm**：多模态大模型（qwen3-vl-plus，负责生成摘要和理解内容）

部署命令：
```
docker pull ghcr.io/volcengine/openviking:latest
docker run --name openviking -p 1933:1933 -v /mydata/openviking:/app/.openviking -d ghcr.io/volcengine/openviking:latest
```

健康检查：curl http://192.168.3.101:1933/health 返回status:ok和healthy:true。

### Web Studio控制台
地址：http://192.168.3.101:1933/studio

首页仪表盘展示上下文数据量、Token用量、检索次数。左侧导航分工作区、活动、设置、资源四个区。

连接设置需填Root API密钥（管理操作）和用户API密钥（数据访问）。用户管理中新增用户后生成用户API密钥。

工作台分三栏：
- 左边：上下文树（user下放个性化记忆、resources放外部资源）
- 中间：浏览viking://目录内容
- 右边：会话区（终端和Agent两种模式切换）

Agent工具调用与左侧目录联动：操作了哪个viking://文件，点一下就能定位和打开。

### 跨会话记忆体验
1. 输入"记住我的职业：Java开发工程师"，Agent调用openviking_memory_commit写入记忆，返回Memory URI
2. 新会话中问"我的职业是什么"，Agent先调openviking_search检索记忆再回答
3. 终端模式执行/search 职业，列出命中资源/记忆/技能，每条带L0/L1/L2层级和相似度score
4. 上下文树可展开到user/macro/peers/macro/memories/profile.md，预览是明文"职业：Java开发工程师"

记忆以明文文件落盘，看得见摸得着。

### AI Agent接入支持
OpenViking不只给自家VikingBot用，记忆能力开放给主流Agent：
- 插件接入：Claude Code、Codex、OpenClaw
- MCP方式：TRAE、Cursor等
- SDK：Python、LangChain等

接入三步：启动自部署Server→跑安装脚本接入Claude Code→重启后即可使用。

### 项目地址
https://github.com/volcengine/OpenViking

## 关联连接
- [[OpenViking]]
- [[Agent记忆系统]]
- [[虚拟文件系统]]
- [[MCP]]
- [[ClaudeCode]]
- [[上下文管理]]
- [[字节跳动开源]]
