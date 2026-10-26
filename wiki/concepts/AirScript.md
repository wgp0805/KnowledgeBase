---
title: "AirScript"
type: concept
tags: [云端自动化, 金山文档, 定时任务, 零成本]
sources: ["raw/09-archive/2026-10-13-WorkBuddy 自动签到：不开机也能 7×24 白嫖 100 积分天！.md"]
last_updated: 2026-10-14
---

## 定义
AirScript 是 [[金山文档]] 内置的云端脚本能力：在表格中通过「效率 → 高级开发 → AirScript 脚本编辑器」写 JS，配合「网络 API」服务调外部 HTTP 接口，再用「定时任务」按 Cron 触发——等于一块免费、免服务器、网页版即用的云端自动化运行时，关机/出差/断网都不影响执行。

## 关键信息
- **典型用例**：WorkBuddy 自动签到（详见 [[摘要-workbuddy自动签到云端]]）——B1 单元格存 refresh_token，脚本刷新令牌→签到→回写结果到 B2，定时任务每天 09:00 触发
- **部署门槛**：全程约 10 分钟、零成本、不用下载客户端、不用碰服务器（对比云服务器/GitHub Actions 对小白门槛过高）
- **工程要点**：
  - 写单元格要用 `Value2` 属性（AirScript 2.0 不能直接 `.Value =`）
  - 网络请求用 `HTTP.post(url, body, {headers, timeout})`
  - 脚本可设计幂等（当天已签自动跳过，定时任务重复跑无副作用）
  - 令牌自续期模式：每次运行把新 refreshToken 回写存储格，旧令牌兜底，长期免人工干预
- **安全边界**：表格即密钥容器——存令牌的文档绝不能分享；建议写入前评估"令牌泄露 = 账号钥匙拱手让人"的风险

## 关联连接
- [[摘要-workbuddy自动签到云端]] — 来源
- [[金山文档]] — 宿主平台
- [[WorkBuddy]] — 典型用例对象
- [[refresh-token-rotation]] — 令牌自续期的机制对照
- [[automations]] — 上位概念：Agent/系统定时自动化
- [[晓庄AI创业笔记]] — 方案作者
