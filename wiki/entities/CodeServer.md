---
title: "CodeServer"
type: entity
tags: [工具, Docker, 远程开发, IDE]
sources: ["raw/09-archive/2026-11-20 - 8 个让你直呼卧槽的 Docker 神器，让你的服务器瞬间开挂！.md"]
last_updated: 2026-11-24
---

## 定义
code-server 是 Coder 开源的 VS Code 服务端，把完整 VS Code 跑在服务器上、用浏览器访问，实现"任何设备打开即得完整开发环境"。

## 关键信息
- 定位：云端 IDE。换设备不用重配环境，代码、插件、设置都在服务端
- 典型用途：远程办公/出差临时开发、学生与初学者在老设备上写代码
- 进阶用法：把宿主机工作目录直接挂载进去（`-v $PWD:/home/coder/project`），当"带语法高亮的文件资源管理器"用，改服务器配置很方便
- 最小启动：`docker run -d --name code-server -p 8080:8080 -v "$HOME/.config:/home/coder/.config" -v "$PWD:/home/coder/project" codercom/code-server:latest`；compose 版通过 `PASSWORD` 环境变量设密码
- 端口注意：默认 8080，与 [[Homer]] 冲突，同机部署需改映射
- 安全提醒：不要把映射了宿主机敏感目录的实例直接暴露公网，至少加密码与 TLS

## 关联连接
- [[Docker]] — 分发方式
- [[VSCode扩展]] — 插件生态在服务端同样可用
- [[Homer]] — 同为 8080 端口的自托管工具
- [[摘要-8个docker神器]] — 来源
