---
title: "OnlyOffice"
type: entity
tags: [在线文档, Office, 开源, 文档编辑]
sources: [raw/01-articles/SpringBoot+OnlyOffice：优雅实现在线 Word 编辑、转化、保存等功能.md, raw/01-articles/为什么越来越多人用 OnlyOffice？.md]
last_updated: 2026-09-28
---

## 定义
OnlyOffice 是一款开源免费的在线 Office 文档编辑套件，支持 Word、Excel、PPT 的在线编辑、多人协同编辑、文档转化、文档打印等功能。通过部署 OnlyOffice Document Server，可以集成到各类 Web 应用中实现在线文档处理能力。

## 关键信息
- **核心功能**：在线文档编辑、文档转化、多人协同编辑、文档打印
- **部署方式**：支持 Docker 部署和 Ubuntu 本地部署
- **前端集成**：通过官方 API（`DocsAPI.DocEditor`）集成，支持 Vue/React 等前端框架
- **后端集成**：Spring Boot 等后端框架通过 HTTP 接口提供文件获取和回调处理
- **回调机制**：OnlyOffice 通过回调 URL 通知后端文档状态变化（编辑中、保存就绪、保存出错等），状态码 1-7
- **Token 配置**：可通过修改 `local.json` 和 `default.json` 中的 token 参数启用或禁用安全令牌
- **常见问题**：
  - 文档加载失败：修改配置文件去除 token 验证
  - 后端鉴权冲突：需要将 `/callback` 和 `/getFile/*` 路径加入白名单
  - 文档地址访问：可通过 Nginx 反向代理实现文件路径重定向

### 走红原因与 9.4.0 轻量模式（2026-05-19 发布，详见 [[摘要-为什么越来越多人用onlyoffice]]）
- **产品定位**：本体是 DocumentServer——独立的在线文档编辑后端服务（"云端的 Office"），不是网盘或完整办公套件；文档管理器与存储由集成商提供，DocumentServer 负责编辑、转换、命令与构建服务
- **走红本质**：把"在线文档编辑"从买商业授权变成自己 Docker 部署，数据在自己服务器上、不经过第三方
- **轻量模式（9.4.0 起社区版强制）**：把 Nginx + PostgreSQL + RabbitMQ + 多进程的分布式架构合并为**单进程单体化**，状态全部内存化；部署从 docker-compose 多容器编排变为 `docker run -e MEMORY_MODE=true` 一键启动
  - 适用：中小企业协作、POC 验证与开发测试、NAS/Docker 单容器、ARM 低配机、离线内网
  - 不适用：需要集群、高可用、横向扩展的场景（社区版不支持集群，需企业版）
- **协同编辑原理**：浏览器编辑的是内部缓存的 Editor.bin 而非原始 Word 文件，由 [[document-key机制]] 决定会话与缓存复用；保存发生在全员退出/强制保存后回调 status=2/6 时
- **对比定位（vs Collabora Online / Microsoft 365）**：自研 OOXML 引擎带来开源方案中最强的 Microsoft 格式 round-trip fidelity；空闲内存约 2GB（Collabora 约 1GB）；9.4 起取消社区版 20 并发限制，AGPL v3 协议；内置 JWT 双重校验、回调防伪造等安全能力与 AI 助手
- **主要短板**：资源占用高于 Collabora、非 OOXML 格式兼容一般、document.key 机制易踩坑、社区版不支持集群

## 关联连接
- [[在线文档处理]] — 浏览器中处理 Office 文档的技术方案总览
- [[SpringBoot]] — 后端集成框架
- [[Vue3]] — 前端集成框架
- [[PageOffice]] — 同类 PC 端在线文档处理产品（COM + ActiveX 方案）
- [[MobOffice]] — 同类移动端在线文档处理产品
- [[摘要-springboot-onlyoffice-在线编辑]] — 来源
- [[document-key机制]] — 协同编辑版本标识机制
- [[摘要-为什么越来越多人用onlyoffice]] — 来源（9.4 轻量模式与走红原因）