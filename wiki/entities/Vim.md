---
title: "Vim"
type: entity
tags: [编辑器, Linux]
sources: [raw/01-articles/vim命令大全.md, raw/01-articles/liunx查找文件内的关键字.md]
last_updated: 2026-05-19
---

## 定义
Vim 是 Linux/Unix 系统上最强大的命令行文本编辑器之一，以高效的键盘操作和三种模式设计著称。

## 关键信息
- 三种模式：命令模式（默认）、插入模式（i/a/o）、末行模式（:）
- 光标移动：gg/G（首尾行）、w/b（单词跳转）、H/M/L（屏幕位置）
- 复制粘贴：yy（复制行）、dd（剪切行）、p/P（粘贴）
- 查找替换：/keyword（查找）、:s/old/new/g（替换）、:%s/old/new/g（全局替换）
- 保存退出：:wq、:q!、:x（智能保存退出）
- 配置文件：~/.vimrc（个人配置）、/etc/vimrc（全局配置）

## 关联连接
- [[Linux]] — 操作系统
- [[Grep]] — 文本搜索工具
