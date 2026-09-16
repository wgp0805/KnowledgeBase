---
title: "GitHub"
type: entity
tags: [代码托管, DevOps, 开源]
sources: [raw/01-articles/搞定 OAuth 2.0 第三方登录，So Easy !.md]
last_updated: 2026-09-16
---

## 定义
GitHub 是全球最大的代码托管和协作开发平台，基于 Git 版本控制系统，提供代码托管、Pull Request、Issues、Actions（CI/CD）等功能。

## 关键信息
- 代码托管：支持公开/私有仓库
- 协作开发：Pull Request、Code Review、Branch Protection
- CI/CD：GitHub Actions 自动化工作流
- 项目管理：Issues、Projects、Milestones
- 社区：开源项目托管、Star/Fork/Watch 机制
- GitHub Pages：静态网站托管
- GitHub Copilot：AI 代码补全工具

### OAuth 2.0 第三方登录支持
GitHub 官方支持基于 OAuth 2.0 的第三方登录，详见 [[摘要-oauth2-第三方登录]]。

**三个核心 URL**
- `https://github.com/login/oauth/authorize` — 认证服务器（授权请求）
- `https://github.com/login/oauth/access_token` — 令牌服务器（换取 access_token）
- `https://api.github.com/user` — 资源服务器（获取用户信息）

**配置流程**
1. 进入 GitHub Setting → Developer settings → OAuth Apps → New OAuth App
2. 填写回调地址（需与后端接口匹配）
3. 获取 `Client ID` 和 `Client Secret`

**登录流程**
1. 后端生成 state 防 CSRF（见 [[State-CSRF防护]]）
2. 重定向到 GitHub 授权页面
3. GitHub 重定向回本站，携带 code（10 分钟过期）和 state
4. 校验 state 匹配
5. POST code + client_id + client_secret 换 access_token
6. GET /user 携带 token 获取用户信息

## 关联连接
- [[Git]] — 底层版本控制系统
- [[Gitee]] — 国内同类平台
- [[GitLab]] — 自托管竞品
- [[CI-CD]] — GitHub Actions 实现
- [[ClaudeCode]] — 可集成 GitHub
- [[OAuth2]] — 支持的第三方登录协议
- [[QQ互联]] — 对比的第三方登录平台
- [[State-CSRF防护]] — OAuth 登录中的 CSRF 防护
- [[摘要-用Qoder提交PaiAgent到GitHub]] — 记录使用 Qoder CLI 为 PaiAgent 项目添加…
- [[摘要-域名]] — 记录在阿里云国际版和 CloudFlare 上对白嫖域名进行…
- [[摘要-oauth2-第三方登录]] — 来源（OAuth 2.0 第三方登录实战）
