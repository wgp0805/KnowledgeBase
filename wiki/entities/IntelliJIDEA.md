---
title: "IntelliJIDEA"
type: entity
tags: [IDE, Java]
sources: [raw/01-articles/idea的特殊用法及远程DEBUG的方法.md, raw/01-articles/idea控制台输出中文乱码.md, raw/01-articles/idea链接svn报错.md, raw/01-articles/IDEA使用Git提交报错 unable to read askpass response from.md]
last_updated: 2026-05-19
---

## 定义
IntelliJ IDEA 是 JetBrains 公司开发的 Java 集成开发环境，被广泛认为是 Java 开发的最佳 IDE。

## 关键信息
- 远程调试：JDWP 参数配置（-agentlib:jdwp=transport=dt_socket,server=y,suspend=n,address=*:5005）
- 中文乱码解决：文件编码 UTF-8、properties 文件编码、JVM 编码参数
- SVN 集成：SSL 证书验证失败（E170013/E230001）的解决方案
- Git 集成：askpass 响应错误时在远程 URL 中嵌入凭据

## 关联连接
- [[Java]] — 开发语言
- [[Git]] — 版本控制集成
- [[SVN]] — 版本控制集成
- [[SpringBoot]] — 常用项目框架
