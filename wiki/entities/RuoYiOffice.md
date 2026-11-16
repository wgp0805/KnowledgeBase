---
title: "RuoYiOffice"
type: entity
tags: [开源项目, 企业应用, 微服务, 办公一体化]
sources: [raw/09-archive/2026-11-12 - RuoYi Office：一套系统把 OA、CRM、ERP 全装进去.md]
last_updated: 2026-11-16
---

## 定义
RuoYi Office 是基于 Spring Cloud Alibaba 微服务 + Vue 3 构建的中小企业办公一体化开源平台（MIT 协议，个人和企业 100% 免费商用，基于芋道 yudao 生态衍生，Gitee：yqzy1688/ruoyi-office），目标"一个平台管好整个企业"，解决中小企业考勤/客户/进销存多系统割裂、数据不通、月底表格搬运对账的痛点。

## 关键信息
- **16 个已上线子系统**：OA 协同（用车/印章/会议室/云盘/公告）、HRM 人力资源（员工全生命周期）、CRM（线索/客户/商机/合同/回款）、ERP 进销存、EAM 资产、WMS 仓储、MALL 企业商城（分销裂变）、AI 智能助手、BPM 流程引擎、支付中心、数据报表、IoT 物联网、微信公众号、会员中心等；规划中还有项目管理、薪酬、考勤、绩效、财务报销
- **BPM 流程引擎（重头）**：仿钉钉/飞书可视化设计器 + BPMN 双设计器，拖拽约 10 分钟配一条审批流；会签、或签、转办、委派、加签、父子流程、超时审批齐全；所有业务单据与 BPM 打通，审批不跨系统
- **AI 助手**：内置多模型切换（ChatGPT、通义千问、文心一言、[[DeepSeek]]、讯飞星火），公文起草、邮件撰写、知识库问答、一键生成思维导图
- **微服务模块化**：Gateway 网关 + Nacos 注册中心 + RocketMQ 消息队列的生产级架构，16 子系统独立部署"用哪个启哪个"；多租户 SaaS 模式租户数据完全隔离；数据库适配 MySQL、[[PostgreSQL]]、Oracle、达梦、人大金仓（信创环境可上）
- **环境要求**：JDK 17/21、MySQL 5.7+、Redis 5+、Node 18+、Maven 3.9+、Nacos 2.x；启动流程：导入 SQL → 起 Nacos → `mvn clean install` → 前端 `pnpm install && npm run dev`
- **客观提醒**：微服务全家桶环境依赖多、上手门槛高于单体项目；代码量大，建议先看在线演示（ruoyioffice.com/web/admin，admin/admin123）再决定部署

## 关联连接
- [[RuoYi]] — 若依母框架（本平台为其生态衍生）
- [[RuoYi-Vue-Plus]] / [[RuoYiAI]] — 若依生态同类衍生项目
- [[Nacos]] / [[RocketMQ]] — 微服务基座组件
- [[DeepSeek]] — 内置可切换模型之一
- [[MySQL]] / [[PostgreSQL]] — 适配数据库
- [[程序汪]] — 来源作者
- [[摘要-ruoyi-office一体化办公平台]] — 来源
