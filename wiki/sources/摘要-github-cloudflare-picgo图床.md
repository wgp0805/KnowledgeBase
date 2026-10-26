---
title: "摘要-github-cloudflare-picgo图床"
type: source
tags: [来源, 原始文件, 图床, GitHub, Cloudflare, PicGo]
sources: [raw/09-archive/2026-09-25-GitHub + Cloudflare + Picgo 搭建你的免费图床 - DominicKK.md]
last_updated: 2026-09-28
---

## 核心摘要

本教程用"GitHub 私有仓库 + Cloudflare Workers 反代 + PicGo（可选）"搭建稳定、私有、免费的图床，适用于个人博客、小型网站与文档系统。GitHub 侧创建私有仓库并生成访问令牌：推荐 Fine-grained token（Repository access 限定图床仓库，Permissions 给 Contents: Read and write + Metadata: Read-only，`github_pat_` 前缀只显示一次需立即保存），不推荐 classic token（需 repo + write:packages 全量权限）。Cloudflare 侧从 Hello World 模板创建 Worker 并替换为反代脚本：非根路径把请求拼到 `raw.githubusercontent.com` 并带上 `Authorization: token`，支持通过 URL `?token=` 或环境变量注入 GH_TOKEN/GH_NAME/GH_REPO/GH_BRANCH，缺失 token 返回 400，失败返回自定义（哈利波特主题伪装）错误页；根路径返回伪装页或按 URL/URL302 环境变量随机跳转，可用自有域名经 Cloudflare DNS 代理接入。PicGo 侧配置 GitHub 图床与仓库/分支/token，推荐 `rename-file` 插件按 `{y}/{m}/{d}{h}{i}-{rand:3}` 自动重命名避免冲突，并可与 Typora 内置 PicGo 集成实现写作时一键上传。

## 关联连接

- [[图床]] — 方案概念页
- [[PicGo]] — 上传客户端
- [[GitHub]] — 存储与 Fine-grained PAT
- [[Cloudflare]] — Workers 反代与 CDN
- [[摘要-域名]] — Cloudflare 相关的既有来源
