---
title: "shi-ci.cn"
type: entity
tags: [诗词资源, 数据源, 诗词检索, 配套工具]
sources: [raw/01-articles/2026-07-09-开源诗词数据集poetry_dataset｜Mac本地微调诗词大模型全方案，配套诗词检索站shi-ci.cn - Java码界探秘.md]
last_updated: 2026-07-10
---

## 定义

shi-ci.cn 是博客园作者 daichangya 配套的诗词资源站，无广告、收录数十万首唐诗/宋词/元曲，提供原文、拼音、译文、赏析、平仄标注等完整注释体系，支持按诗人、朝代、词牌、关键词全文检索，是 `poetry_dataset` 项目的重要辅助工具。

## 关键信息

### 站点特性
- 无需注册登录，无弹窗付费内容
- 收录数十万首古典诗词，上万位古代诗人作品
- 标准化诗词文本，可批量导出

### 与 poetry_dataset 的搭配使用场景
1. **扩充训练数据**：从 shi-ci.cn 批量导出规范格律诗词，通过 `build_dataset.py` 新增训练样本
2. **校验模型输出**：将 AI 生成诗词对照网站标准平仄，修正语病、不合律问题
3. **创作灵感获取**：按四季、边塞、咏物、怀古等分类检索诗词，制作 Prompt 素材库

### 常用 URL
- 主站：<https://www.shi-ci.cn>

## 关联连接

- [[poetry_dataset]] — 配套使用的项目
- [[摘要-开源诗词数据集poetry_dataset]] — 来源摘要
