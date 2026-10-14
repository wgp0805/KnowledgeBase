---
title: "摘要-workbuddy自动签到云端"
type: source
tags: [来源, WorkBuddy, 云端自动化, AirScript, 薅羊毛]
sources: ["raw/01-articles/2026-10-13-WorkBuddy 自动签到：不开机也能 7×24 白嫖 100 积分天！.md"]
last_updated: 2026-10-14
---

## 核心摘要
晓庄AI创业笔记针对"WorkBuddy 自动签到必须开电脑"的死穴，给出把签到彻底搬上云的方案：从桌面客户端登录态文件取出 refresh_token，存进金山文档表格 B1 单元格，用 AirScript 脚本在云端调接口签到（每次运行自动续期令牌并回写），再配定时任务每天执行。关机、出差、断网都能每天领 100 积分（连签第 7 天额外 1000），整套部署约 10 分钟、不花钱、不用服务器。文章同时逆向给出了 WorkBuddy 桌面端 v5.5.x 的刷新与签到接口细节，并提醒令牌等于账号钥匙、文档绝不能分享。

## 关键信息

### 现有签到机制与市面方案的坑
- 新版 WorkBuddy 每天打开一次客户端即默认自动签到（Buddy 加油站，直接显示"今日积分已领"，签到按钮已移除）；不开机就领不到
- 积分规则：每天签到 100 积分，连签第 7 天额外 1000；一个月 30 天开机 vs 只有 15 天开机差 1500 积分，低倍率模型下够白用很久
- 市面签到 Skill 的死穴：都建本地定时任务，只有客户端开着才能跑；"云端工作模式设定时任务"路线也不通——云端沙箱没任务时休眠，实测唤醒经常失败（八成是 bug）
- 上个月官方给登录态文件加了锁，"打开电脑读文件"老路也快堵死

### 四步实操（拿令牌 → 存表格 → 贴脚本 → 定时间）
1. **获取 refresh_token**：必须用电脑客户端（小程序/APP 不行）。新建任务选 GLM-5.3-Flash，发提示词让 AI 读取登录态文件（macOS：`~/Library/Application Support/CodeBuddyExtension/Data/Public/auth/workbuddy-desktop.info`；Windows：`%LOCALAPPDATA%\CodeBuddyExtension\Data\Public\auth\workbuddy-desktop.info`），只提取 `auth.refreshToken` 字段值（约 700 字符），完整输出禁止截断
2. **金山文档建表存令牌**：kdocs.cn 网页版微信扫码登录，新建空白表格；**B1 格子粘贴 refresh_token（漏一个字符后面全白搭），B2 留给脚本回写执行结果**
3. **部署 AirScript 脚本**：「效率」→「高级开发」→「AirScript 脚本编辑器」→ 新建脚本；「服务」→「添加服务」→「网络API」；粘贴 JS 保存后试跑
4. **创建定时任务**：「效率」→「高级开发」→「定时任务」，选脚本设每天 09:00（周末也别跳过，周末也能领）

### 脚本设计要点（逆向自 WorkBuddy 桌面端 v5.5.x）
- API 基址 `https://copilot.tencent.com`
- 刷新令牌：`POST /v2/plugin/auth/token/refresh`，头带 `X-Refresh-Token` / `X-Domain` / `X-Auth-Refresh-Source: plugin`，返回新 accessToken + refreshToken
- 签到：`POST /v2/billing/meter/daily-checkin`，`Authorization: Bearer`；`code=10001` 表示今日已签（幂等跳过）
- 连签状态：`POST /v2/billing/meter/checkin-activity-status`，返回 streak_days 与 total_credits
- **令牌自续期**：每次签到后把新 refreshToken 回写 B1，旧令牌仍可用作兜底，链条可长期运行
- **脚本幂等**：无论定时跑多少次，当天只会真正签一次
- AirScript 2.0 注意：写入单元格要用 `Value2` 属性，不能直接 `.Value =`
- 结果回写 B2（日期时间 + 签到结果 + 连签天数/累计积分）

### 安全提醒
- 整个文档不要分享给任何人——**令牌等于账号钥匙**
- 云服务器/GitHub Actions 也能跑，但对小白门槛高；金山文档免费、网页版、不用下客户端，是最省事路子

## 关联连接
- [[WorkBuddy]] — 签到对象产品
- [[AirScript]] — 脚本运行的云端能力
- [[金山文档]] — 脚本托管平台
- [[GLM-5.3-Flash]] — 提取 token 环节推荐的模型
- [[SkillHub]] — 市面签到 Skill 的分发地
- [[refresh-token-rotation]] — 令牌自续期的相关机制
- [[摘要-workbuddy-15技能推荐-10月]] — 早期版本自动领积分 Skill 的推荐来源
