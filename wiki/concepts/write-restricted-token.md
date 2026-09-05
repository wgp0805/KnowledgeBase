---
title: "write-restricted-token"
type: concept
tags: [Windows, 安全, 沙箱, Codex, ACL]
sources: [raw/01-articles/2026-08-23-codex windows平台中elevated sandbox机制学习 - 三国梦回.md]
last_updated: 2026-08-24
---

# write-restricted token

## 核心定义
Windows 中在普通 token 基础上派生的权限更低的令牌，操作系统对其进行的检查项更多。Codex 在 Windows 平台利用 write-restricted token 实现文件系统隔离。

## 工作原理
1. **SidsToRestrict 字段**：包含一个随机生成的 SID（安全标识符）
2. 由于系统上无任何目录对该 SID 有 ACE（Access Control Entry），默认无法写入任何目录
3. Codex 主动给 workspace 目录设置 ACE 允许该 SID 写入，实现只写指定目录
4. `.codex` 目录下的 `cap_sid` 文件记录哪个 SID 可修改哪个目录

## 两种模式
### 未提权沙箱
- token 颁发人仍是当前真实用户
- 具有上网能力（最大短板：无法控制网络访问）
- 只能通过设置 `HTTPS_PROXY` 为不可访问值限制 curl 等知名程序

### 提权沙箱
- token 颁发人改为 `CodexSandboxOffline`（不能上网）
- 防火墙限制 `CodexSandboxOffline` 不能访问任何外网 IP
- `CodexSandboxOffline` 默认无权读取用户文件夹，需单独修改 ACL
- `codex-windows-sandbox-setup.exe` 异步为常用目录添加 ACE

## 关联概念
- **Token（令牌）**：Windows 进程的权限凭证
- **ACE（Access Control Entry）**：访问控制条目
- **ACL（Access Control List）**：访问控制列表
- **SID（Security Identifier）**：安全标识符

## 关联连接
- [[elevated-sandbox]]
- [[沙箱]]
- [[Codex]]
- [[Windows]]
