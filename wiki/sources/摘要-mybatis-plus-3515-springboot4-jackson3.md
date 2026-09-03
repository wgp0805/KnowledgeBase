---
title: "摘要-mybatis-plus-3515-springboot4-jackson3"
type: source
tags: [来源, 原始文件, MyBatisPlus, SpringBoot4, Jackson3]
sources: [raw/01-articles/MyBatis-Plus 3.5.15 已全面支持 Spring Boot 4.0 及 Jackson 3.0.md]
last_updated: 2026-09-03
---

## 核心摘要
MyBatis-Plus 3.5.15 版本更新重点支持 Spring Boot 4.0 和 Jackson 3.0。Spring Boot 4 项目需使用 `mybatis-plus-spring-boot4-starter`，与 Boot 2/3 Starter 名称不同、自动配置不兼容。Jackson 3 将核心包从 `com.fasterxml.jackson` 迁移到 `tools.jackson`，对应新增 `Jackson3TypeHandler` 替代原有的 `JacksonTypeHandler`。文章还详细说明了升级时的常见坑：Starter 选错、JSON 处理器版本不匹配、`factoryBeanObjectType` 报错（需显式指定 mybatis-spring 4.0.0）等。

## 关联连接
- [[MyBatisPlus]] — 增强工具主体
- [[SpringBoot]] — 框架升级支持
- [[Jackson]] — JSON 处理库
- [[Jackson3TypeHandler]] — Jackson 3 类型处理器
- [[autoResultMap]] — 实体配置要点
