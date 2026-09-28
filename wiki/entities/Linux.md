---
title: "Linux"
type: entity
tags: [操作系统, 服务器]
sources: [raw/09-archive/Liunx常用命令.md, raw/09-archive/liunx命令总结（600条）.md, raw/09-archive/liunx查找文件内的关键字.md, raw/09-archive/liunx挂载硬盘.md, raw/09-archive/liunx链接Ftp和Sftp.md, raw/01-articles/2026-09-26 - 服务器被入侵怎么办？看我操作.md]
last_updated: 2026-09-28
---

## 定义
Linux 是一个自由开源的操作系统内核，基于 Unix 设计理念，广泛应用于服务器、嵌入式设备和云计算环境。

## 关键信息
- 目录结构：/bin、/sbin、/etc、/usr、/home、/var、/dev、/proc
- 文件操作：ls/cd/mkdir/touch/rm/mv/cp/find/grep
- 权限管理：chmod（数字法 777/rwx）、chown、useradd/usermod/userdel
- 压缩打包：tar（.tar.gz/.tar.bz2）、gzip、zip
- 网络配置：ifconfig、firewalld（systemctl）、netstat
- 磁盘管理：fdisk/parted、mount/umount、fstab、df/du
- Vim 编辑器：三种模式（命令/插入/末行）
- 包管理：RPM、YUM（RedHat 系）、APT（Debian 系）
- 文件锁定属性（来源：[[摘要-服务器入侵应急处置]]）：`chattr +ia` 给文件/目录加只读与不可变属性，`lsattr` 查看，`chattr -ia` 解除；入侵者常借此锁死被替换的 `ps`/`top`/`chattr`，需从同版本机器拷贝 `chattr` 先解锁文件**及其所在目录**再还原
- 预加载后门风险：动态链接器读取 `LD_PRELOAD` 与 `/etc/ld.so.preload`，优先级高于 `LD_LIBRARY_PATH`，可被用来注入隐藏进程的恶意 `.so`（详见 [[服务器入侵应急响应]]）
- 定时任务与启动项排查路径：`/var/spool/cron/`、`/etc/crontab`、`/etc/cron.d/`、`/etc/rc.local`、`/var/log/cron`

## 关联连接
- [[CentOS]] — Linux 发行版
- [[Ubuntu]] — Linux 发行版
- [[服务器入侵应急响应]] — 入侵排查与加固方法论
- [[摘要-服务器入侵应急处置]] — chattr/ld.so.preload 案例来源
- [[Vim]] — 编辑器
- [[Nginx]] — Web 服务器
- [[摘要-服务器部署纯静态网站]] — 介绍使用宝塔面板和 Nginx 在 Linux 服务器上部署…
- [[摘要-curl详解]] — curl 命令行工具的全面使用指南，涵盖基础用法（GET/P…
- [[摘要-liunx查找文件内的关键字]] — Linux 中使用 Vim 和 Grep 命令查找文件内关键…
- [[摘要-VMware17-安装ubuntu]] — 在 VMware 17 中安装 Ubuntu 虚拟机的完整步…
