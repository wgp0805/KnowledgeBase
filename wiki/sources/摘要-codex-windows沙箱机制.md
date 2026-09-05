---
title: "摘要：Codex Windows平台elevated sandbox机制"
type: source
tags: [Codex, Windows, 沙箱, 安全, write-restricted-token, elevated-sandbox]
sources: [raw/01-articles/2026-08-23-codex windows平台中elevated sandbox机制学习 - 三国梦回.md]
last_updated: 2026-08-24
---

# 摘要：Codex Windows沙箱机制

## 核心主旨
拆解 OpenAI Codex Desktop 在 Windows 平台的沙箱机制，分为未提权沙箱（unelevated）和提权沙箱（elevated）两种模式。核心是利用 Windows 的 write-restricted token 实现文件系统隔离。

## 未提权沙箱（Unelevated Sandbox）
1. **write-restricted token**：在普通 token 基础上派生的权限更低的令牌，操作系统检查项更多。
2. **SidsToRestrict 字段**：包含一个 codex 随机生成的 SID。由于系统上无任何目录对该 SID 有 ACE（Access Control Entry），codex 默认无法写入任何目录。codex 主动给 workspace 目录设置 ACE 允许该 SID 写入，实现只写指定目录。
3. **cap_sid 文件**：`.codex` 目录下记录哪个 SID 可修改哪个目录。
4. **最大短板——无法控制网络访问**：token 颁发人仍是当前真实用户（如张三），具有上网能力。只能通过设置 `HTTPS_PROXY` 为不可访问值来限制 curl 等知名程序，但无法阻止不理会环境变量的程序。

## 提权沙箱（Elevated Sandbox）
1. **需要管理员权限**：创建专门的沙箱用户。
2. **codexSandboxUsers 用户组**：包含 `CodexSandboxOffline`（不能上网）和 `CodexSandboxOnline`（可上网）两个用户。
3. **防火墙规则**：限制 `CodexSandboxOffline` 不能访问任何外网 IP。
4. **write-restricted token 颁发人改为 CodexSandboxOffline**：因防火墙限制，该 token 无法上网。但 `CodexSandboxOffline` 默认无权读取用户文件夹，需单独修改各文件夹 ACL。
5. **codex-windows-sandbox-setup.exe**：异步在后台为 `C:\Program Files\` 等常用目录添加 `CodexSandboxOffline` 的 ACE，因文件多开销大。

## 关键概念
- **Token（令牌）**：Windows 进程的权限凭证
- **Restricted Token（受限令牌）**：派生的低权限令牌
- **write-restricted token**：限制写入能力的受限令牌
- **ACE（Access Control Entry）**：访问控制条目
- **ACL（Access Control List）**：访问控制列表
- **SID（Security Identifier）**：安全标识符

## 原始信息
- **来源**: 博客园 / 三国梦回
- **链接**: https://www.cnblogs.com/grey-wolf/p/22643567
- **参考**: https://openai.com/zh-Hans-CN/index/building-codex-windows-sandbox/
- **抓取日期**: 2026-08-23

## 关联连接
- [[Codex]]
- [[Windows]]
- [[沙箱]]
- [[write-restricted-token]]
- [[elevated-sandbox]]
- [[OpenAI]]
