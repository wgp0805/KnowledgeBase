---
title: "摘要-claude-code-pi-tool设计原则"
type: source
tags: [来源, 原始文件, Tool设计, ClaudeCode, Pi, Agent面试]
sources: [raw/09-archive/Claude Code 和 Pi Agent 中 Tool 的设计原则。.md]
last_updated: 2026-10-20
---

## 核心摘要
沉默王二从 Claude Code、Pi 源码与 Anthropic 官方指南提炼 Agent Tool 设计原则，反驳"封装函数+写清 JSON Schema 就够"的思路——大模型生成合法参数的能力远比想象差（Claude Code 源码注释直接承认这点）。核心分三层：**入口（工具选择）**——工具不是越多越好，Pi 只默认开放 read/bash/edit/write 四个核心工具并让模型用 bash 执行 ls/rg/find（预训练语料见得多反而最准），Claude Code 用"Bash 禁用 find/grep/cat/sed 强制分流专用工具"+"MCP/低频工具延迟加载（ToolSearch 按需拉取）"治理几十个工具的选错率；**入口（参数防护）**——从接口设计上杜绝错误（路径强制绝对路径），参数静默兼容（edits 数组传成字符串先包装再校验、数字带引号静默转数字）+ 前置拦截（Edit 三道关卡：必须先 Read、Read 后文件被改则拒绝、old_string 多处匹配则拦截，报错信息像提示词一样指导模型）；**出口（执行与输出）**——读写分离并发控制（只读工具打包并发最多 10 个，遇写操作立刻串行；Pi 按真实路径加锁）、首尾差异化截断（read 头部截断提示传 offset，bash 尾部截断保末尾报错，超 5 万字符落盘只回预览并冻结结果保 Prefix Caching）、人机视图分离（edit 返回 content 只给模型、details diff 只给终端渲染，省 Token）。权限边界绝不能交给模型判断，必须在工具代码内按真实身份拦截。

## 关联连接
- [[ClaudeCode]] — 工具设计实践方一
- [[Pi]] — 工具设计实践方二（极简 4 工具）
- [[ToolCalling]] — 相关概念
- [[ToolSearch]] — 延迟加载机制
- [[Anthropic]] — 设计原则出处
- [[沉默王二]] — 作者
