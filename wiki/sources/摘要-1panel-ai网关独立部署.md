---
title: "摘要-1panel-ai网关独立部署"
type: source
tags: [来源, 原始文件, AI网关, 1Panel]
sources: [raw/01-articles/2026-09-18-37K Star 的 GitHub 开源项目开放 AI 网关，10 人团队免费用.md]
last_updated: 2026-09-20
---

## 核心摘要
1Panel（37K Star 的开源 Linux 服务器管理工具）开放了 AI 网关的独立部署能力，10 人及以下团队可免费使用。网关能集中管理各家模型（如 DeepSeek、腾讯云 TokenHub）的原始密钥，给成员分配权限、按任务分配模型、查看每人调用用量并据此调整配额。调用关系为"团队 AI 应用 → 1Panel AI 网关 → 云端/本地模型"。支持两种部署方式：已用 1Panel 的团队从应用商店安装，或通过官方 Docker 镜像独立部署（`docker run` 启动，日志查看临时密码，建议内网访问 + HTTPS 反向代理）。

## 关联连接
- [[1Panel]] — 开源 Linux 服务器管理工具
- [[AI网关]] — 集中管理多模型密钥/权限/配额
- [[LLM网关]] — 相关概念
- [[逛逛GitHub]] — 作者