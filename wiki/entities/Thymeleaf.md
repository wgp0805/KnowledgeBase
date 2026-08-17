---
title: "Thymeleaf"
type: entity
tags: [Java, 模板引擎, Web]
sources:
  - raw/01-articles/优雅使用 Enum 提升 SpringBoot 配置管理效率！.md
last_updated: 2026-08-17
---

## 定义
Thymeleaf 是面向 Java/Web 的现代服务端模板引擎，可处理 HTML、XML、JavaScript、CSS 甚至纯文本。以"自然模板"为设计理念——模板文件可直接由浏览器打开预览（原型），运行时再由引擎注入动态数据，是 Spring Boot 官方推荐的 Web 视图层技术。

## 关键信息
- **Spring Boot 集成**：引入 `spring-boot-starter-thymeleaf` 即可，默认模板目录 `src/main/resources/templates/`，默认后缀 `.html`
- **命名空间**：`xmlns:th="http://www.thymeleaf.org"`，所有指令以 `th:` 前缀
- **常用指令**：
  - `th:text="${var}"` — 设置文本内容（转义）
  - `th:utext` — 设置未转义 HTML
  - `th:if` / `th:unless` — 条件渲染
  - `th:each` — 循环迭代
  - `th:href` / `th:src` — 动态 URL
- **表达式**：`${}` 变量、`@{}` URL、`#{}` 消息国际化、`*{}` 选择/对象
- **与 Controller 协作**：`@Controller` 返回视图名，`Model.addAttribute(key, value)` 传值，模板中以 `${key}` 取值

## 关联连接
- [[SpringBoot]] — 官方推荐视图层
- [[SpringMVC]] — Web MVC 宿主
- [[摘要-优雅使用Enum提升SpringBoot配置管理效率]] — 来源（渲染用户类型表格）
