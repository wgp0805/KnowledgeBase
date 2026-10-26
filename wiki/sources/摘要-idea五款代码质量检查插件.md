---
title: "摘要-idea五款代码质量检查插件"
type: source
tags: [来源, 原始文件, IDEA, 代码质量]
sources: [raw/09-archive/2026-09-30 - 这五款牛逼的 IDEA 插件，堪称代码质量检查利器！.md]
last_updated: 2026-10-08
---

## 核心摘要
文章推荐五款 IntelliJ IDEA 代码质量检查插件，用工具减少 code review 工作量：①**Alibaba Java Coding Guidelines**——专注 Java 代码规范（OOP/并发/控制语句/命名/常量/注释），按 Blocker>Critical>Major 三级显示，大部分可自动修复，支持实时检测，检查代码规范首选；②**CheckStyle**——侧重文法层面编码格式与风格（命名、Javadoc、空格、过长方法、多余 Import），对 bug 几乎无发现能力，默认配置过严需导入自定义配置；③**PMD**——侧重安全编码规则，具备数据流/路径分析，查潜在 bug、死代码、循环体新建对象、资源未关闭等，支持自定义规则（RuleSets 导入）；④**FindBugs**——侧重发现真实 bug（空指针、资源未关闭、用 == 比较字符串），覆盖 Bad practice、Dodgy code、Performance、多线程正确性等 8 类，适合给新员工做 bug 培训；⑤**SonarLint**——层级最高，除静态 bug 外还关注代码质量、包间依赖、耦合、复杂度、重复代码等整体健康度，可关联 Sonar 平台服务端（自用自审 vs 平台他审），commit 时可勾选自动检查。选型结论：查规范用 Alibaba 规约；找 bug 用 PMD（自定义规则强）+ FindBugs（找 bug 强）+ SonarLint（覆盖面全）相互补充。

## 关联连接
- [[IntelliJIDEA]] — 插件运行的 IDE
- [[静态代码检查]] — 本文核心概念
