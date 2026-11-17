---
title: "摘要-onlyoffice私有化与springboot接入实战"
type: source
tags: [来源, OnlyOffice, 私有化部署, API集成, SpringBoot]
sources: [raw/09-archive/为什么越来越多人用 OnlyOffice ？.md]
last_updated: 2026-11-17
---

## 核心摘要
苏三 2026-11-17《为什么越来越多人用 OnlyOffice？》的**同名异文**（同标题系列新篇，区别于已摄入的 9.4.0 轻量模式篇，详见 [[摘要-为什么越来越多人用onlyoffice]]），从企业在线编辑需求出发拆解 OnlyOffice 作为"文档编辑能力积木"的完整选型与接入：三条路（SaaS 数据出不了内网、商业 SDK 按人头收费、自研渲染成本高）走不通时，OnlyOffice 以私有化部署 + API 嵌入给出"第三选择"。版本三条线（社区版 AGPL v3 免费适合小团队/测试、企业版商业授权带管理面板、开发者版商业授权带白标换 Logo/主题/关于页），版本功能差异小、差的是授权/并发/品牌控制权。开发者四能力：①API 集成——后端生成 config JSON（文件类型/地址/权限/用户/回调）→ 前端加载 api.js → 保存回调三件事闭环，附 50+ 现成连接器（本质是 API 现成用法示例）；②私有化部署——本地/私有云/离线内网，Docker 一行跑起，JWT 必配（不设或弱密钥等于文档服务裸奔公网）；③协作内置——实时编辑（快速/严格双模式）、评论 @、版本历史对比回滚；④白标（开发者版核心差异，editorConfig.customization 换 Logo/主题色）。Spring Boot 3.4.5 + Java 17 完整实战：JWT 用 JDK HmacSHA256 手写（config 令牌与下载令牌权限分离，下载令牌带 fileId+purpose 15 分钟有效）；document.key 用"文件ID+版本号"策略（保存后版本号+1 自然产生新 key，复用旧 key 会导致协同错乱/缓存旧版本）；回调 status 1/2/4/6/7 处理表（2/6 下载保存、4 无修改返回成功、7 强保失败不覆盖）；落盘先写临时文件再原子替换（ATOMIC_MOVE）；离线 AI 需额外部署本地模型、非开箱即用。内容已并入 [[OnlyOffice]] 与 [[document-key机制]]。

## 关联连接
- [[OnlyOffice]] — 核心实体（增量更新）
- [[document-key机制]] — key 版本策略增量
- [[摘要-为什么越来越多人用onlyoffice]] — 同标题系列第一篇（9.4.0 轻量模式视角，非重复）
- [[摘要-springboot-onlyoffice-在线编辑]] — 既有集成摘要对照
- [[苏三]] — 来源作者
- [[JWT]] — 安全令牌机制
- [[SpringBoot]] — 接入框架
- [[Docker]] — 部署载体
