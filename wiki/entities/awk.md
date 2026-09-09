---
title: "awk"
type: entity
tags: [Linux, 文本处理, 命令]
sources: [raw/01-articles/面试官：你掌握哪些 Linux 常用命令？.md, raw/09-archive/同事查日志太慢，我现场教他一套 awk、tail、grep、sed 组合拳.md]
last_updated: 2026-09-09
---

## 定义
awk 是 Linux 文本处理三剑客之一，用于文本分析（按列处理），适合统计、分析访问日志等场景。

## 关键信息
- **定位**：文本分析（按列处理）
- **常用示例**：
  - `ps aux | sort -rnk 3 | head -5`：查看 CPU 使用率前 5 的进程
  - `awk '{print $1}' access.log | sort | uniq -c | sort -rn | head`：统计 IP 出现次数
  - `awk -F':' '{print $1, $3}' /etc/passwd`：按 ":" 分隔打印列
- **面试要点**：与 grep（找）、sed（改）区分

### 日志分析实战（来源：[[摘要-日志分析命令组合拳]]）
awk 擅长处理列数据，对格式规范的 [[Nginx]] 访问日志可以直接在服务器上生成简报，不必把文件拉到本地。

- **遭 CC 攻击或爬虫时找恶意 IP**（假设日志第一列是 IP）：
  awk '{print $1}' access.log | sort | uniq -c | sort -nr | head -n 10
  四步管道：提取第一列 → 排序让相同 IP 相邻 → uniq -c 去重并统计次数 → sort -nr 按次数倒序，取前 10 名
- **找出响应最慢的接口**（假设响应时间在最后一列、URL 在第 7 列）：
  awk '$NF > 1.000 {print $7, $NF}' access.log
  $NF 代表最后一列，该写法直接筛出响应时间超过 1 秒的请求并打印 URL 与耗时
- **定位**：CPU 飙升报警后怀疑 CC 攻击或爬虫时，access.log 的 IP 频次分布是最快的第一步排查

## 关联连接
- [[摘要-面试官你掌握哪些Linux常用命令]] — 来源
- [[摘要-日志分析命令组合拳]] — 来源（Nginx 日志实战）
- [[Linux]] — 运行环境
- [[Nginx]] — access.log 的来源
- [[日志分析]] — 场景化排查方法论
- [[tail]] — 同篇介绍的另一命令
- [[less]] — 同篇介绍的回溯工具
- [[grep]] — 三剑客之一
- [[sed]] — 三剑客之一
