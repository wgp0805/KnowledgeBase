---
title: "摘要-面试官你掌握哪些Linux常用命令"
type: source
tags: [来源, Linux, 面试, 运维, Java诊断]
sources: [raw/01-articles/面试官：你掌握哪些 Linux 常用命令？.md]
last_updated: 2026-08-27
---

## 核心摘要
犬小哈（小哈学 Java）从面试视角梳理 Java 程序员必备的 Linux 常用命令，按场景分类：文件目录操作、文件查看编辑、文本处理三剑客（grep/awk/sed）、进程端口管理、Java 诊断工具、系统性能监控、网络相关、权限用户、压缩解压、其他高频。面试核心得分区是线上问题排查流程：top 找进程 → top -Hp 找线程 → printf 转十六进制 → jstack 看堆栈 → 定位代码。强调按场景分类答才显专业，重点突出实战经验，再提 arthas 现代化诊断工具加分。

## 关键信息
- **面试考察点**：实际开发经验（tail -f/grep -A 20/jstack/netstat -anp vs ls/cd/pwd 三件套）、问题排查能力、知识面广度
- **文本处理三剑客**：grep（文本搜索/找）、awk（文本分析/按列处理）、sed（文本编辑/改）
- **进程端口管理**：ps aux/jps 找进程；netstat -anp/lsof -i/ss -tunlp 查端口；kill -9 强杀、kill -15 优雅终止
- **Java 诊断工具**：jps/jstack/jmap/jstat/jinfo/jhat/arthas
- **CPU 飙高排查流程**：top → top -Hp PID → printf "%x\n" 线程PID → jstack PID | grep 十六进制
- **性能监控**：free -h 内存、df -h 磁盘、du -sh 目录、uptime 负载、iostat -x 1 IO、vmstat 1 虚拟内存、dmesg 内核日志
- **网络**：ping/telnet/curl/wget/nslookup/ifconfig/ip addr
- **高频追问**：CPU 飙高排查、端口占用查看、grep/awk/sed 区别、rm -rf 误删（基本恢复不了，推荐 mv 到 /tmp 或 trash-cli）、kill -9 vs kill -15
- **记忆口诀**：看日志 tail -f+grep、看进程 ps aux+top、看端口 netstat+lsof、看磁盘 df -h+du -sh、看内存 free -h+top、排 Java 问题 jps+jstack+jmap

## 关联连接
- [[Linux]] — 本文核心操作系统
- [[Java]] — 面向 Java 程序员的 Linux 命令
- [[JVM]] — jstack/jmap/jstat 等 JDK 诊断工具的基础
- [[Arthas]] — 阿里开源线上排查神器
- [[grep]] — 文本搜索三剑客之一
- [[awk]] — 文本分析三剑客之一
- [[sed]] — 文本编辑三剑客之一
- [[top]] — 实时系统资源监控
- [[netstat]] — 端口占用查看
- [[lsof]] — 端口占用查看
- [[SpringBoot]] — nohup java -jar 后台运行场景
