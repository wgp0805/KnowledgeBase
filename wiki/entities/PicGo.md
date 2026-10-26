---
title: "PicGo"
type: entity
tags: [工具, 图床, 效率, 开源]
sources: [raw/09-archive/2026-09-25-GitHub + Cloudflare + Picgo 搭建你的免费图床 - DominicKK.md]
last_updated: 2026-09-28
---

## 定义

PicGo 是一款开源图片上传管理工具，通过图形化界面把本地图片上传到各类图床（GitHub、阿里云 OSS、SM.MS 等）并自动复制外链，是 Markdown 写作与 [[图床]] 方案的常用客户端。

## 关键信息

- **GitHub 图床配置项**：仓库所有者、仓库名、分支、存储路径（二级路径，留空为根目录）、Personal Access Token
- **推荐插件**：`rename-file`，按自定义格式自动重命名，如 `{y}/{m}/{d}{h}{i}-{rand:3}`（年/月/日时分-随机 3 位），避免文件名冲突、目录更好看
- **工作流**：仪表盘选择图床 → 上传 → 成功后自动复制 url 类型链接 → 粘贴即用
- **编辑器集成**：Typora 内置支持配置 PicGo 服务地址，实现写作中一键上传
- 官网下载：picgo.app

## 关联连接

- [[图床]] — 所属方案
- [[GitHub]] — 本方案的存储后端
- [[Cloudflare]] — 本方案的反代层
- [[摘要-github-cloudflare-picgo图床]] — 来源
