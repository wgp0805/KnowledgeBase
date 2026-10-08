---
title: "摘要-mybatisplus-pro-crud自动化"
type: source
tags: [来源, 原始文件, MyBatisPlus, Java, CRUD]
sources: [raw/01-articles/2026-10-02 - 为什么越来越多人用 MybatisPlus Pro？.md]
last_updated: 2026-10-08
---

## 核心摘要
苏三介绍基于 MybatisPlus 抽取增强的 **MybatisPlus Pro**：核心是继承一个 `BaseController<S extends IService<T>, T>`，增删改查、分页、列表、排序、条件查询全部开箱即用，创建完整 CRUD 的 Controller 只需一行继承代码，相比原生 MyBatis 工作量减少 80% 以上。实现靠两块基础设施：`ApprenticeUtil` 工具类（驼峰↔下划线互转 + Java 反射提取实体非空字段自动生成 QueryWrapper，"给什么字段查什么字段"零代码条件查询）与 BaseController（内部调用 IService 的 save/updateById/removeById/getById/list/page）。底层原理：Spring 启动时 MapperProxyFactory 对 BaseMapper 做 JDK 动态代理，SqlInjector 为通用方法自动生成 MappedStatement 注入 Configuration，MybatisPlusInterceptor 拦截器链承载分页/乐观锁/多租户。缺点：三表以上关联 Wrapper 反而更绕、通用方法默认 `SELECT *` 有性能隐患、字符串字段名是魔法值（推荐 LambdaQueryWrapper）、复杂 SQL 可读性差。选型建议：适合中小型/后台管理/单表 CRUD 主导项目；交易支付、复杂报表、需逐条审 SQL 的系统应回归手写 XML。文中注明 MybatisPlus Pro 有两种理解：社区基于 MP 的二次封装方案（本文重点，项目地址 gitee.com/nirui-gitee/mybatis-plus-pro）与官方迭代中的 Pro 级特性。

## 关联连接
- [[MybatisPlusPro]] — 文中主角
- [[MyBatisPlus]] — 所增强的基础框架
- [[MyBatis]] — 最底层 ORM 框架
- [[苏三]] — 作者
