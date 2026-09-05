---
title: "OnlyOffice"
type: entity
tags: [在线文档, Office, 开源, 文档编辑]
sources: [raw/01-articles/SpringBoot+OnlyOffice：优雅实现在线 Word 编辑、转化、保存等功能.md]
last_updated: 2026-07-27
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

## 关联连接
- [[在线文档处理]] — 浏览器中处理 Office 文档的技术方案总览
- [[SpringBoot]] — 后端集成框架
- [[Vue3]] — 前端集成框架
- [[PageOffice]] — 同类 PC 端在线文档处理产品（COM + ActiveX 方案）
- [[MobOffice]] — 同类移动端在线文档处理产品
- [[摘要-springboot-onlyoffice-在线编辑]] — 来源