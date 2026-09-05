---
title: "Cookie"
type: concept
tags: [Web, 客户端, 状态存储, 协议]
sources: [raw/09-archive/公司系统太多，能不能实现账号互通？.md]
last_updated: 2026-07-16
---

## 定义
Cookie 是 Web 应用中存储在客户端（浏览器）的小型数据片段，用于在多次请求间保持状态，是 Session 机制的默认实现方式。

## 关键信息
- **与服务器交互**：服务器通过 Set-Cookie 响应头设置 cookie，浏览器在后续请求中自动携带
- **JSESSIONID**：Java Web 应用中用于标识 Session 的 cookie 变量，存储在浏览器内存中（非硬盘）
- **跨域限制**：不同域名的系统无法共享 cookie，这是 SSO 需要中心化认证服务的根本原因
- **URL 重写**：当浏览器禁止 cookie 时，Web 服务器采用 URL 重写方式传递 SessionID（如 `sessionid=KWJHUG6JJM65HS2K6`）
- **安全性**：cookie 可被禁用、篡改，因此需要配合 HTTPS、HttpOnly、Secure 等安全属性

## 关联连接
- [[Session]] — SessionID 通过 cookie 传递
- [[SSO]] — 跨域 cookie 共享受限催生 SSO
- [[CAS协议]] — 中心化认证服务解决跨域问题
- [[摘要-sso-single-sign-on]] — 来源
