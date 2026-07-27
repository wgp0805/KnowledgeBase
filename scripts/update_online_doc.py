#!/usr/bin/env python3
"""Update 在线文档处理.md with OnlyOffice info"""

with open('wiki/concepts/在线文档处理.md', 'r', encoding='utf-8') as f:
    content = f.read()

old_products = """- **典型产品**：
  - PageOffice（PC 端）：COM + ActiveX 嵌入式，支持留痕、盖章、套红
  - MobOffice（移动端）：支持移动端审批和盖章，与 PageOffice 互认"""

new_products = """- **典型产品**：
  - PageOffice（PC 端）：COM + ActiveX 嵌入式，支持留痕、盖章、套红
  - MobOffice（移动端）：支持移动端审批和盖章，与 PageOffice 互认
  - OnlyOffice（全平台）：开源免费，支持 Word/Excel/PPT 在线编辑、多人协同编辑、文档转化，通过 Docker 或 Ubuntu 部署"""

content = content.replace(old_products, new_products)

content = content.replace(
    'sources: [raw/01-articles/SpringBoot 实现电子文件签字+合同系统！.md]',
    'sources: [raw/01-articles/SpringBoot 实现电子文件签字+合同系统！.md, raw/01-articles/SpringBoot+OnlyOffice：优雅实现在线 Word 编辑、转化、保存等功能.md]'
)

content = content.replace('last_updated: 2026-07-14', 'last_updated: 2026-07-27')

old_links = """## 关联连接
- [[摘要-springboot-电子文件签字盖章系统]] — 来源
- [[PageOffice]] — PC端在线文档处理产品
- [[MobOffice]] — 移动端在线文档处理产品
- [[电子签名]] — 文档处理中的签章环节
- [[SpringBoot]] — 后端集成框架"""

new_links = """## 关联连接
- [[摘要-springboot-电子文件签字盖章系统]] — 来源
- [[摘要-springboot-onlyoffice-在线编辑]] — Spring Boot 集成 OnlyOffice 实现在线 Word 编辑
- [[PageOffice]] — PC端在线文档处理产品
- [[MobOffice]] — 移动端在线文档处理产品
- [[OnlyOffice]] — 开源在线 Office 文档编辑套件
- [[电子签名]] — 文档处理中的签章环节
- [[SpringBoot]] — 后端集成框架"""

content = content.replace(old_links, new_links)

with open('wiki/concepts/在线文档处理.md', 'w', encoding='utf-8') as f:
    f.write(content)

print('在线文档处理.md updated successfully')