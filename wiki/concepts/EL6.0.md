---
title: "EL6.0"
type: concept
tags: [EL, JakartaEE, JSP, 规范, Tomcat]
sources: ["raw/09-archive/2026-10-25 - Tomcat 11 到底有多强大 ？.md"]
last_updated: 2026-10-26
---

## 定义
EL 6.0（Expression Language 6.0）是 Jakarta EE 11 中的表达式语言规范版本，随 Tomcat 11 内置实现落地。核心变化是终于原生支持 Java record 组件读取，并解除对 `java.desktop` 模块的强依赖。

## 关键信息
- **RecordELResolver 默认启用**：Java 16 就有 record，但此前 EL 只认 JavaBean 风格的 `getXxx()` getter，JSP 里写 `${book.title}` 取不到值；EL 6.0 起默认启用 `RecordELResolver`，record 组件可直接用 `${book.title}`、`${book.author}` 读取，无需再写 getter。
- **数组支持 `.length`**：EL 中终于可以用 `${book.tags.length}` 取数组长度（此前数组不支持 length 属性）。
- **OptionalELResolver**：新增处理 `java.util.Optional` 的解析器，但默认关闭，需要手动加入解析器链才生效。
- **去 `java.desktop` 依赖**：EL 不再强依赖 `java.desktop` 模块，用 `jlink` 裁剪运行时镜像时能更瘦一点。
- **实测验证（2026-10）**：record `Book(title, author, tags)` 通过 Servlet `setAttribute` 转发到 JSP，页面正确显示 `${book.title}`、`${book.author}`、`${book.tags.length}`（值 3）。
- 使用前提：需搭配 Tomcat 11（内置 EL 6.0 实现）；JSP 引擎为 tomcat-embed-jasper（内嵌场景需单独引入）。

## 关联连接
- [[摘要-tomcat-11-new-features]] — 来源（EL 6.0 record/length 实测）
- [[Tomcat]] — Tomcat 11 内置 EL 6.0 实现
- [[servlet-6-1]] — 同属 Jakarta EE 11 Web 子规范
- [[JakartaEE]] — 所属平台规范集合
- [[Java]] — record 语言特性（Java 16 引入）
