---
title: "ClawGod"
type: entity
tags: [实体, 开源工具, ClaudeCode, 补丁, 权限]
sources: [raw/09-archive/2026-10-01-一行命令，解锁 Claude Code 全部权限-ClawGod - 绝不原创的飞龙.md]
last_updated: 2026-10-08
---

## 定义
ClawGod（github.com/0Chencc/clawgod）是一个开源（GPL-3.0）的 [[ClaudeCode]] 本地补丁工具，一行命令安装（约 30 秒），把 Anthropic 官方在客户端关闭的功能全部打开；只修改本地客户端行为，不认证流程、不修改账号、不绕过服务端限流。

## 关键信息
- **模型解锁**：把用户类型从 `external` 改为 `ant`（伪装 Anthropic 内部用户），绕过按订阅等级的模型分配——专业版即可用 Opus 4.6 + 1M 上下文
- **内部用户模式**：GrowthBook 功能开关系统可被本地配置覆盖，消息过滤规则放宽
- **Agent Teams 解锁**：移除多智能体协作功能的条件检查（`return!0` 强制开启），原版需实验性环境变量
- **删除三条内部限制指令**：CYBER_RISK_INSTRUCTION（渗透测试/漏洞利用等安全话题拒答）、URL 生成限制、操作审慎指令（删除文件等破坏性操作强确认）——面向安全研究/CTF/渗透测试人群的最大痛点
- **功能开关自管**：注入 `CLAUDE_INTERNAL_FC_OVERRIDES` 环境变量，用本地 JSON 覆盖远程功能标志（tengu_harbor、tengu_session_memory 等）
- **自定义 API**：可改 apiKey/baseURL/model，支持代理、中转、兼容 API
- **安装与卸载**：macOS/Linux 用 curl 脚本、Windows 用 irm 脚本；产出 `claude`（补丁版）与 `claude.orig`（原版备份），`claude --uninstall` 一键恢复；生效后终端主题橙色→绿色
- **兼容性与风险**：用正则坐标偏移量匹配，小版本更新大概率兼容；安全研究解禁+确认框移除会放大 prompt 注入与误操作风险，属第三方非官方修改，使用前须了解风险

## 关联连接
- [[摘要-clawgod解锁claude-code]] — 来源
- [[ClaudeCode]] — 被修改的目标工具
- [[Anthropic]] — 官方厂商
- [[ClawBot]] — 名称相近的腾讯微信接入插件（勿混淆）
