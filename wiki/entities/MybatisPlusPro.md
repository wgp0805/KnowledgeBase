---
title: "MybatisPlusPro"
type: entity
tags: [实体, ORM, MyBatisPlus, Java, CRUD]
sources: [raw/09-archive/2026-10-02 - 为什么越来越多人用 MybatisPlus Pro？.md]
last_updated: 2026-10-08
---

## 定义
MybatisPlus Pro 是在 [[MyBatisPlus]] 基础上"只做增强不做改变"的增强工具：在 MP 已经消灭 Mapper 层代码的基础上，继续消灭 Service 层与 Controller 层的重复代码——只需继承一个 `BaseController`，增删改查、分页、列表、排序、条件查询全部开箱即用，让开发者只关注核心业务逻辑。文中注明其有两种理解：社区基于 MP 的二次封装方案（本文重点，项目地址 gitee.com/nirui-gitee/mybatis-plus-pro）与 MybatisPlus 官方迭代中新增的 Pro 级特性。

## 关键信息
- **两大基础设施**：①`ApprenticeUtil` 工具类——驼峰↔下划线互转 + Java 反射提取实体非空字段自动生成 QueryWrapper（"给什么字段查什么字段"，零代码条件查询）；②`BaseController<S extends IService<T>, T>`——集成 add/update/delete/detail/list/page 六个通用接口，内部调用 IService 对应方法
- **代码量收益**：一个完整 CRUD 模块的 Controller 只需一行继承，相比原生 MyBatis（XML+Mapper+Service+ServiceImpl+Controller）工作量减少 80% 以上；所有模块风格统一，新人零学习成本
- **底层原理**：Spring 启动时 MapperProxyFactory 对 BaseMapper 做 JDK 动态代理；SqlInjector 为通用方法自动生成 MappedStatement 注入 Configuration（免 XML 的原因）；MybatisPlusInterceptor 拦截器链承载分页、乐观锁、多租户等增强；save 方法按主键是否为 null 自动决定 insert/updateById
- **优点**：开发效率指数级提升、代码风格统一、零 XML、分页插件内置、非侵入式（复杂 SQL 仍可回退原生 Mapper XML）
- **缺点**：三表以上关联 Wrapper 比 SQL 还绕；通用方法默认 `SELECT *` 有性能隐患；字符串字段名是魔法值（推荐 LambdaQueryWrapper 方法引用）；复杂条件构造器生成的 SQL 不直观难调优
- **选型**：适合中小型快速迭代、后台管理系统、单表 CRUD 占 80% 以上的项目、小团队统一风格；不推荐交易/支付/高并发订单、复杂报表统计、需逐条审 SQL 的金融政务系统
- **作者口诀**：它解决 80% 的简单 CRUD 重复工作，剩下 20% 复杂场景手写 SQL，两者结合是最佳实践

## 关联连接
- [[摘要-mybatisplus-pro-crud自动化]] — 来源
- [[MyBatisPlus]] — 所增强的基础框架
- [[MyBatis]] — 最底层 ORM 框架
- [[苏三]] — 介绍作者
- MyBatisPlus 的 LambdaQueryWrapper — 规避魔法值的推荐写法
