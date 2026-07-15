---
name: "source-command-ingest-all"
description: "批量处理 raw/ 目录中所有未归档的文章到 wiki/ 知识库。当用户说\"批量处理文章\"、\"摄取所有资料\"、\"导入全部文章\"时触发。"
---

# source-command-ingest-all

Use this skill when the user asks to run the migrated source command `ingest-all`.

## Command Template

# 批量摄取命令

## 核心目标
简化 ingest 技能的调用，一次性处理 `raw/` 目录中所有未归档的文章。

## 执行步骤

1. **扫描待处理文件**
   - 使用 Glob 工具扫描 `raw/01-articles/`、`raw/02-papers/`、`raw/03-transcripts/` 目录
   - 排除 `raw/09-archive/` 目录
   - 列出所有未归档的文件

2. **批量处理**
   - 对每个待处理文件执行 ingest 技能的完整流程：
     - 读取源文件内容
     - 提炼核心主旨、实体、概念
     - 创建来源摘要页面（`wiki/sources/`）
     - 创建/更新实体/概念页面（`wiki/entities/` 或 `wiki/concepts/`）
     - 更新 `wiki/index.md` 和 `wiki/log.md`
     - 归档源文件到 `raw/09-archive/`

3. **输出摘要**
   - 显示处理的文件数量
   - 列出新增的 source、entity、concept 页面
   - 报告任何冲突或错误

## 使用方式
- 用户输入 `/ingest-all`
- 用户说"批量处理文章"
- 用户说"摄取所有资料"

## 注意事项
- 遵循 ingest 技能的所有约束和规范
- 处理包含中文和特殊字符的文件名时，使用 Python 脚本读取
- 每个文件处理完成后立即归档，避免重复处理
- 如果发现知识冲突，暂停并询问用户处理方式
