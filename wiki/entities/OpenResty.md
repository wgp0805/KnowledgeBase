---
title: "OpenResty"
type: entity
tags: [Nginx, Lua, 反向代理, 网关, 开源]
sources: [raw/09-archive/2026-10-28 - Cloudflare正式开源Nginx替代品：Pingora.md]
last_updated: 2026-10-29
---

## 定义
OpenResty 是基于 [[Nginx]] 与 LuaJIT 的 Web 平台，把 Nginx 扩展成一个可用 Lua 脚本编程的网关/应用服务器，由 [[章亦春]] 创建。它在工程史上是"Nginx 如何获得可编程性"这一问题的第一代主流答案。

## 关键信息

### 技术路线
- **宿主**：Nginx（C 实现，成熟稳定，生态与运维经验充足）
- **扩展语言**：Lua / LuaJIT，通过各阶段钩子（access、content、log 等）嵌入业务逻辑
- **定位**：用脚本语言获得可编程性，而不是替换 Nginx 本体

### 与 [[Pingora]] 的路线对照
| 维度 | OpenResty | Pingora |
|------|-----------|---------|
| 策略 | 在成熟 C 代码上叠脚本层 | 用 Rust 重写代理本体 |
| 可编程性 | Lua 脚本 | Rust 代码 + filters/callbacks |
| 成熟度 | 多年生产验证，运维经验丰富 | pre-1.0，API 不稳定 |
| 内存安全 | 依赖 C 层与 Lua 边界 | 语言级保证 |
| 批评对方的核心论点 | —— | 用 Rust 写解释型网关是"退步" |

### 与本文的关联
[[章亦春]]（OpenResty 作者、曾参与 Cloudflare 架构工作）对 Cloudflare 开源 Pingora 的评价是本知识库记录该事件时的重要反方观点：他认为这不是技术跃迁，而是新工程师"搞不定" Nginx 后的重造轮子，并指出用 Rust 实现解释型网关在抽象层次上是倒退。

## 关联连接
- [[Nginx]] — 宿主服务器
- [[章亦春]] — 创建者
- [[Pingora]] — 同场景的竞争路线（Rust 重写）
- [[Cloudflare]] — 争议事件的发生地
- [[反向代理]] — 所属技术类别
- [[摘要-cloudflare开源pingora]] — 来源
