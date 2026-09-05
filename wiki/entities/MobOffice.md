---
title: "MobOffice"
type: entity
tags: [工具, 在线办公, 移动端, 电子签章]
sources: [raw/01-articles/SpringBoot 实现电子文件签字+合同系统！.md]
last_updated: 2026-07-14
---

## 定义
MobOffice 是卓正软件（ZhuozhengSoft）出品的移动端在线 Office 处理产品，支持手机端/平板端对 Word 文档的审批和盖章操作。与 PageOffice 结合使用，实现 PC 端和移动端对文档审批和盖章的互认，为跨平台处理 Office 文件提供完整解决方案。

## 关键信息
- **平台**：移动端（手机/平板）
- **核心功能**：移动端领导审批、移动端领导盖章（电子印章）
- **互认机制**：与 PageOffice 联合使用，PC 端和移动端审批/盖章结果互认
- **集成方式**：通过 MobOfficeCtrl 服务端控制类，配置 sysPath、serverPage、sealServer、saveFilePage 等参数
- **文档格式**：支持 Word 在线编辑、PDF 在线查看
- **开发包**：提供服务器端授权程序 Servlet（如 /mobserver.zz）和移动端控制 API

## 关联连接
- [[摘要-springboot-电子文件签字盖章系统]] — 来源
- [[PageOffice]] — 同厂商PC端产品，双端互认
- [[ZhuozhengSoft]] — 出品方
- [[电子签名]] — 遵循电子签名法
- [[在线文档处理]] — 文档在线处理领域
