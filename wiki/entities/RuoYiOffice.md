---
title: "RuoYiOffice"
type: entity
tags: [开源项目, 企业应用, 微服务, 办公一体化]
sources: [raw/09-archive/2026-11-12 - RuoYi Office：一套系统把 OA、CRM、ERP 全装进去.md, "raw/09-archive/太酷了，RuoYi Office：一套系统把 OA、CRM、ERP 全装进去.md"]
last_updated: 2026-11-24
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

### 技术底子与双部署形态（2026-11-24 实测，来源：[[摘要-ruoyi-office-agentos实测]]）
- **技术栈**：Java 17 + Spring Boot、MyBatis-Plus 持久层、[[Flowable]] 审批流程；PC 端 Vue 3 + TypeScript + Vben Admin；移动端 [[UniApp]] 一套代码出 H5/App/小程序；数据层 MySQL + Redis（缓存与分布式锁）+ MinIO/OSS
- **同一套业务代码支持两种部署**：团队小用单体（一个 Spring Boot 应用直接启动、无额外组件）；业务量上来按模块切微服务（[[SpringCloudGateway]] 统一入口 + [[Nacos]] 注册与配置 + [[RocketMQ]] 异步消息 + [[XXL-JOB]] 定时任务），组件按需启用而非一开始全装
- **审批分层**：Flowable 只管流程（轮到谁、下一步、退回哪），各业务模块只管自己的单据字段与业务状态；两者分开才能把各部门申请汇到同一张待办表
- **权限与待办同一套**：OA/人力/合同/CRM/ERP/项目/资产共用一个账号体系，菜单与数据按岗位权限收敛，待办列表混合展示资产领用、合同发起、费用报销等单据
- **业务模块**：官方列 21 个（OA 协同、HRM、CRM、ERP 进销存、WMS 仓储、合同与财务、项目与资产等）；项目模块用甘特图排期，资产看板给原值净值 + 分类环图 + 部门柱图

### AgentOS：可独立部署的智能体层（2026-11-24）
见 [[AgentOS]]。要点：[[SpringAI]] 接大模型 → [[OAuth2]] 单点登录取员工身份 → 调用平台已开放且审核上架的业务接口；[[SSE]] 把执行过程推进对话。实测会议预约中，**写入动作必须本人确认**（先弹确认卡再建单），确认卡绑定会话结构化参数（不让模型重猜、重试有稳定请求标识），模型运行时可在 Spring AI 与 [[AgentScope]] 之间切换而不影响上层业务能力。

### 版本口径差异（2026-11-12 首篇 vs 2026-11-24 实测）
两篇来源对同一产品的描述不完全一致，保留两说：
| 维度 | 2026-11-12 首篇（[[摘要-ruoyi-office一体化办公平台]]） | 2026-11-24 实测（[[摘要-ruoyi-office-agentos实测]]） |
| --- | --- | --- |
| 架构 | 基于 Spring Cloud Alibaba 微服务全家桶 | 单体 / 微服务**双模式**，组件按需启用 |
| 模块数 | 16 个已上线子系统 | 21 个业务模块 |
| 流程引擎 | 自研 BPM 引擎（仿钉钉/飞书 + BPMN 双设计器） | [[Flowable]] 负责流程流转 |
| 智能体 | AI 助手（多模型切换、公文/问答/导图） | 独立部署的 [[AgentOS]]（OAuth2 身份 + 业务接口调用 + 写操作确认） |

差异可能来自版本迭代与统计口径不同，非直接矛盾；使用前以官方版本对照（含商业版边界）为准。2026-04 才建仓、迭代快，重要项目先在非核心场景验证。

## 关联连接
- [[RuoYi]] — 若依母框架（本平台为其生态衍生）
- [[RuoYi-Vue-Plus]] / [[RuoYiAI]] — 若依生态同类衍生项目
- [[Nacos]] / [[RocketMQ]] — 微服务基座组件
- [[DeepSeek]] — 内置可切换模型之一
- [[MySQL]] / [[PostgreSQL]] — 适配数据库
- [[程序汪]] — 来源作者
- [[摘要-ruoyi-office一体化办公平台]] — 来源（2026-11-12 首篇）
- [[摘要-ruoyi-office-agentos实测]] — 来源（2026-11-24 实测，AgentOS 与双模式）
- [[AgentOS]] — 可独立部署的智能体层
- [[Flowable]] — 流程引擎
- [[UniApp]] — 移动端一套代码多端
- [[SpringAI]] / [[AgentScope]] — 可切换的模型运行时
- [[OAuth2]] — AgentOS 员工身份来源
- [[XXL-JOB]] / [[SpringCloudGateway]] — 微服务模式组件
