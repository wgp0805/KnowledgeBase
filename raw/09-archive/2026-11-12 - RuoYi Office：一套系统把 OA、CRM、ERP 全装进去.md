---
source_url: "https://mp.weixin.qq.com/s/HDJWskoUCt4oVUg1NPUjDA"
title: "RuoYi Office：一套系统把 OA、CRM、ERP 全装进去"
account: "我是程序汪"
published_at: "2026-11-12 11:36:39"
saved_at: "2026-11-12 11:55:01"
sync_id: "art_36b8295d2c2c4d94bf7e8f671dcd2aeb"
parse_status: "ok"
---

# RuoYi Office：一套系统把 OA、CRM、ERP 全装进去

** RuoYi Office：一套系统把 OA、CRM、ERP 全装进去**

中小企业上数字化系统，最烦的不是没钱，是**系统太多**。 考勤一套、客户一套、进销存又一套，每个系统单独付费，数据还互不相通，月底对账全靠表格搬运。 RuoYi Office 想干的事很简单：**一个平台，管好整个企业**。

![](assets/2026-11-12%20-%20RuoYi%20Office%EF%BC%9A%E4%B8%80%E5%A5%97%E7%B3%BB%E7%BB%9F%E6%8A%8A%20OA%E3%80%81CRM%E3%80%81ERP%20%E5%85%A8%E8%A3%85%E8%BF%9B%E5%8E%BB/3ec54a0900229a01b856f2c61603e1c9_MD5.png)

![](assets/2026-11-12%20-%20RuoYi%20Office%EF%BC%9A%E4%B8%80%E5%A5%97%E7%B3%BB%E7%BB%9F%E6%8A%8A%20OA%E3%80%81CRM%E3%80%81ERP%20%E5%85%A8%E8%A3%85%E8%BF%9B%E5%8E%BB/17b126d2c1bc386563e07735078b42f9_MD5.png)

![](assets/2026-11-12%20-%20RuoYi%20Office%EF%BC%9A%E4%B8%80%E5%A5%97%E7%B3%BB%E7%BB%9F%E6%8A%8A%20OA%E3%80%81CRM%E3%80%81ERP%20%E5%85%A8%E8%A3%85%E8%BF%9B%E5%8E%BB/f2d0492735d388f045a1be8f982ea2c6_MD5.png)

![](assets/2026-11-12%20-%20RuoYi%20Office%EF%BC%9A%E4%B8%80%E5%A5%97%E7%B3%BB%E7%BB%9F%E6%8A%8A%20OA%E3%80%81CRM%E3%80%81ERP%20%E5%85%A8%E8%A3%85%E8%BF%9B%E5%8E%BB/7954ed687319908f9fd249e42aa63fab_MD5.png)

**01 它是什么**

RuoYi Office 是基于 **Spring Cloud Alibaba 微服务 + Vue 3** 构建的中小企业办公一体化平台。 不是单机小系统，是正经的微服务架构：Gateway 网关、Nacos 注册中心、RocketMQ 消息队列，生产级那一套。 协议 **MIT，个人和企业 100% 免费商用**。

**02 功能覆盖到什么程度**

目前已上线 16 个子系统，基本把企业日常业务全覆盖了：

- OA 协同办公 ：用车、印章、会议室预约、企业云盘、通知公告
- HRM 人力资源 ：员工档案、入职、转正、调动、离职全生命周期
- CRM 客户管理 ：线索、客户、联系人、商机、合同、回款
- ERP 进销存 ：采购、销售、库存、产品、收付款
- EAM 资产管理 ：资产登记、领用、维修、报废全生命周期
- WMS 仓储 ：仓库、出入库、库存查询
- MALL 企业商城 ：商品、订单、营销活动、分销裂变
- AI 智能助手 ：对话、写作、绘图、知识库问答、思维导图
- BPM 流程引擎 ：仿钉钉/飞书设计器 + BPMN 双设计器
- 支付中心、数据报表、IoT 物联网、微信公众号、会员中心 等

规划中的还有项目管理、薪酬、考勤、绩效、财务报销，持续迭代中。

**03 三个值得说的点**

**一是流程引擎是重头。**标配**仿钉钉/飞书可视化设计器**，拖拽 10 分钟配好一条审批流。 会签、或签、转办、委派、加签、父子流程、超时审批这些硬功能全都有。 所有业务单据都和 BPM 打通，审批不用跨系统切来切去。

**二是 AI 不是摆设。**内置多模型切换：ChatGPT、通义千问、文心一言、DeepSeek、讯飞星火。 公文起草、邮件撰写、知识库问答、一键生成思维导图，办公场景是真能用的。

**三是微服务模块化。**16 个子系统各自独立部署，**用哪个启哪个**，不用为用不到的功能买单。 多租户 SaaS 模式，一套系统服务多家企业，租户数据完全隔离。 数据库适配 MySQL、PostgreSQL、Oracle、达梦、人大金仓，**信创环境也能上**。

**04 技术栈和上手成本**

环境要求：**JDK 17/21、MySQL 5.7+、Redis 5+、Node 18+、Maven 3.9+、Nacos 2.x**。 启动流程：导入 SQL → 起 Nacos → 后端  `mvn clean install`  打包启动 → 前端  `pnpm install && npm run dev` 。

说几句实在话：

- 优点 ：功能覆盖全、微服务架构正规、双流程设计器、AI 内置、协议宽松
- 要注意 ：微服务全家桶， 环境依赖多，上手门槛比单体项目高 ，Nacos、RocketMQ 都得自己部署
- 项目是基于芋道 yudao 生态衍生，代码量大， 建议先看在线演示再决定是否部署

**适合谁**

10-500 人规模的中小企业想一套系统打通办公、人事、销售、仓储的，或者开发团队想基于微服务做企业级二开的，都值得去演示环境点一圈。

在线演示：ruoyioffice.com/web/admin，账号 admin / admin123。 仓库地址：Gitee 搜 **yqzy1688/ruoyi-office**。

---
原文链接：https://mp.weixin.qq.com/s/HDJWskoUCt4oVUg1NPUjDA
