---
title: "URule"
type: entity
tags: [规则引擎, Java, 可视化, Spring Boot]
sources: [raw/01-articles/Spring Boot + URule 实现可视化规则引擎.md]
last_updated: 2026-06-10
---

## 定义
URule 是一款 Java 平台的可视化规则引擎，支持在浏览器中直接编辑和测试规则，无需额外安装桌面工具。

## 关键信息
- **部署环境**：兼容 Windows、Linux、Unix 等各类操作系统
- **编辑模式**：纯浏览器可视化编辑，非开发人员也可参与规则配置
- **版本区别**：分为开源版和 Pro 版，Pro 版提供交叉决策表、Excel 导入、版本控制、知识包监控等高级功能
- **使用模式**：嵌入式模式、本地模式、分布式计算模式、独立服务模式
- **核心组成**：设计器部分（库文件 + 规则文件）+ 规则执行引擎

## 注解与 API

**`@Label` 注解**：用于 Java POJO 字段上，描述字段属性，实现 POJO 与变量库属性的自动映射。

**`@ExposeAction` 注解**：标记在 Spring Bean 方法上，使方法被动作库识别并可在规则中调用。

**`@ActionId` 注解**：为动作库中的方法指定唯一标识 ID。

**规则执行 API**：
```java
KnowledgeService knowledgeService = (KnowledgeService)
    Utils.getApplicationContext().getBean(KnowledgeService.BEAN_ID);
KnowledgePackage knowledgePackage = knowledgeService.getKnowledge("包路径");
KnowledgeSession knowledgeSession = KnowledgeSessionFactory.newKnowledgeSession(knowledgePackage);
knowledgeSession.insert(pojo对象);
knowledgeSession.fireRules();
```

## Pro 版特有功能
与开源版相比，Pro 版额外提供：交叉决策表、复杂评分卡、Excel 决策表导入、规则集模板保存加载、中文文件名支持、知识包推送与压缩、循环规则多单元支持、对象查找索引、短路计算、缓存支持、批量场景测试、知识包监控、版本控制、Spring Bean 热部署及技术支持。

## 关联连接
- [[摘要-Spring-Boot-URule-规则引擎]] — 来源文章
- [[SpringBoot]] — Spring Boot 集成方式
- [[规则引擎]] — 同类规则引擎：Drools、Aviator、EasyRules
