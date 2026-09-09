---
title: "tail"
type: entity
tags: [Linux, 命令, 日志]
sources: [raw/09-archive/同事查日志太慢，我现场教他一套 awk、tail、grep、sed 组合拳.md]
last_updated: 2026-09-09
---

## 定义
Linux 查看文件尾部内容的命令，是实时监控日志的首选。很多新手习惯用 cat，但对大文件 cat 会导致屏幕刷屏，甚至把终端卡死到 Ctrl+C 都停不下来。

## 关键信息
- **实时监控**：tail -f logs/application.log，-f（follow）实时追加显示文件尾部内容
- **限定行数**：tail -n 200 -f logs/application.log，只看最后 200 行并保持实时刷新，避免被历史日志干扰
- **真实场景 A 发版启动监控**：每次发版重启服务时确认 Spring Boot 是否启动成功、有没有初始化报错
- **真实场景 B 配合测试复现 Bug**：测试说"我现在点一下按钮，你看看后台有没有报错"时，不需要看历史日志，只需盯着最新输出
- **同门能力**：[[less]] 里的 Shift+F 也可切到类似 tail -f 的实时滚动模式，按 Ctrl+C 退回浏览模式

## 关联连接
- [[日志分析]] — 场景化排查方法论
- [[less]] — 需要回溯历史时的替代方案
- [[grep]] — 三剑客之一
- [[sed]] — 三剑客之一
- [[awk]] — 三剑客之一
- [[Linux]] — 运行环境
- [[摘要-日志分析命令组合拳]] — 来源
