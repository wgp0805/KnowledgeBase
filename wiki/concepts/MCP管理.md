---
title: "MCP管理"
type: concept
tags: [概念, MCP, 管理, 技术]
sources: [raw/01-articles/2026-09-01-DeepSeekHarness-MCP-Manager 一款DSH超好用的MCP管理跟Skills管理插件 - xxxyz.md]
last_updated: 2026-09-01
---

## 定义
对MCP（Model Context Protocol）服务器进行管理的功能，包括服务器的新增、删除、启用、停用、重启等操作。

## 关键信息
- 管理项目级与全局配置
- 支持stdio和streamable-http两种传输方式
- 提供服务器健康检查（实时工具数与loader阶段）
- 支持备份/恢复（JSON导出/导入）
- 宿主注册4个mcp_manager_*工具，模型可直接查询与操作MCP服务

## 关联连接
- [[摘要-DeepSeekHarness-MCP-Manager插件]] — 来源文章
- [[DeepSeekHarness]] — 插件所属的Agent平台
- [[Skills管理]] — 插件的另一核心功能
- [[MCP]] — 相关协议
