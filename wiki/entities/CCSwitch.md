---
title: "CC Switch"
type: entity
tags: [AI编程工具, 供应商切换, 配置管理, 开源工具]
sources: [raw/09-archive/替代 CC Switch，这个项目已经斩获 20K Star！.md]
last_updated: 2026-10-27
---

## 定义

CC Switch（GitHub: farion1231/cc-switch）是管理 Claude Code、Codex、Gemini CLI 等 AI 编程工具供应商配置的桌面工具：把各家工具的配置收在一个窗口，点一下即可切换供应商而无需手改配置文件；附带本地路由、熔断、MCP 与 Skills 面板、会话管理、云同步。

## 关键信息

- **配置写回事故（旧版缺陷）**：旧版保存供应商配置的方式是**整份复制**——加一个供应商就把当时的配置全量快照入库，切换时整份写回；此后手改的 settings.json 内容（状态栏配置、13 个 hooks、`enabledPlugins`、`extraKnownMarketplaces`、`permissions.deny` 拒绝规则）会在某次切换时被旧快照静默覆盖丢失，还会冒出陌生环境变量
- **3.16.5 的保护与残留坑**：切换写回前按用户实时 settings.json 重新收取公共部分（hooks/enabledPlugins/env）存进通用配置，免得下次切换静默丢失；但该保护**只对开启了通用配置的供应商生效**——未开启的供应商仍写回整份旧快照（作者踩坑：库里唯一没开的恰好是 DeepSeek）
- **4.0 修复**：写回改为**只替换少数几个字段**，写入前还会检查文件是否被别处修改过；同时新增类似 magpie 的模型聚合模式
- **对 Codex 桌面版**：模型列表面板显示链路先天不顺，桌面 model picker 问题多（v3.16.5 起用 `cc-switch-model-catalog.json` 缓解），详记于 [[codex-desktop-多模型与插件支持现状]]；对 Codex CLI 支持是稳定的
- **定位对比**：多工具、多密钥、需用量管控+CLI 场景优先 CC Switch；多供应商多账号重额度调度选 [[Magpie]]。本知识库相关检索见 [[codex-desktop-多模型与插件支持现状]] 与 [[CCGUI]]（后者支持 cc-switch 凭证兼容）

## 关联连接

- [[摘要-magpie替代cc-switch]] — 来源（写回事故与 magpie 对比）
- [[Magpie]] — 对比与替代对象
- [[ClaudeCode]] — settings.json 写回事故的主角工具
- [[Codex]] — 桌面版 model picker 问题工具
- [[Gemini]] — 被管理的 CLI 之一
- [[LLM网关]] — 同领域概念（本地路由/协议翻译）
- [[CCGUI]] — 支持 cc-switch 凭证兼容的 JetBrains 插件
- [[codex-desktop-多模型与插件支持现状]] — 相关综合分析
