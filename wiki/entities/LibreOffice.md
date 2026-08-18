---
title: "LibreOffice"
type: entity
tags: [实体, 开源, 办公套件, 文档转换]
sources: [raw/01-articles/2026-08-17 - 为什么越来越多人用 kkFileView？.md]
last_updated: 2026-08-18
---

## 定义
LibreOffice 是开源的办公套件，提供 Writer（文字）、Calc（表格）、Impress（演示）、Draw（绘图）、Base（数据库）、Math（公式）等组件。在文件预览场景中，常作为文档转换引擎，将 Office 文档（doc/docx/xls/xlsx/ppt/pptx）转换为 PDF 供浏览器渲染。

## 关键信息
- **文档转换能力**：通过 API 调用将复杂 Office 文档转换为 PDF，保证预览效果质量
- **kkFileView 底层引擎**：[[kkFileView]] 依赖 LibreOffice 实现 Office 文档到 PDF 的转换
- **部署注意**：首次启动需联网安装 LibreOffice，纯内网环境需提前准备安装包
- **转换质量影响**：LibreOffice 的转换质量直接影响预览效果，部分复杂文档可能出现格式偏差

## 关联连接
- [[kkFileView]] — 作为其底层转换引擎
- [[OpenOffice]] — 同源开源办公套件
- [[摘要-为什么越来越多人用kkFileView]] — 来源
