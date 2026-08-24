---
title: "elevated-sandbox"
type: concept
tags: [Windows, 安全, 沙箱, Codex, write-restricted-token]
sources: [raw/01-articles/2026-08-23-codex windows平台中elevated sandbox机制学习 - 三国梦回.md]
last_updated: 2026-08-24
---

# Elevated Sandbox（提权沙箱）

## 核心定义
OpenAI Codex Desktop 在 Windows 平台的提权沙箱机制。需要管理员权限，通过创建专门的沙箱用户和防火墙规则，解决未提权沙箱无法控制网络访问的短板。

## 实现机制
1. **codexSandboxUsers 用户组**：包含两个用户
   - `CodexSandboxOffline`：不能访问外网
   - `CodexSandboxOnline`：可以访问外网
2. **防火墙规则**：限制 `CodexSandboxOffline` 不能访问任何外网 IP
3. **write-restricted token 颁发人改为 CodexSandboxOffline**：因防火墙限制，该 token 无法上网
4. **ACL 修改**：`CodexSandboxOffline` 默认无权读取用户文件夹，需单独修改各文件夹 ACL
5. **异步设置**：`codex-windows-sandbox-setup.exe` 在后台为 `C:\Program Files\` 等常用目录添加 ACE

## 与未提权沙箱的对比
| 维度 | 未提权沙箱 | 提权沙箱 |
|------|-----------|---------|
| 权限要求 | 普通用户 | 管理员 |
| token 颁发人 | 当前真实用户 | CodexSandboxOffline |
| 网络访问 | 无法控制（短板） | 可通过防火墙限制 |
| 文件权限 | 继承用户权限 | 需单独修改 ACL |

## 关联连接
- [[write-restricted-token]]
- [[沙箱]]
- [[Codex]]
- [[Windows]]
