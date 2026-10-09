---
title: "triangle attention"
type: concept
tags: [注意力机制, 蛋白设计, kernel优化, 生物模型]
sources: []
last_updated: 2026-10-08
---

triangle attention（三角注意力）是 AlphaFold3、OpenFold3、Boltz-2 等蛋白结构模型大量使用的注意力计算模式，也是生物模型 kernel 优化中的主要计算热点（见 [[摘要-anthropic优化生物模型]]）；[[FlashPairformer]] 即为加速它而开发的自定义 kernel。

## 关联连接
- [[蛋白设计]] — 来源（死链修复）
- [[kernel优化]] — 来源（死链修复）
- [[摘要-anthropic优化生物模型]] — 来源（死链修复）
- [[FlashPairformer]] — 加速它的 kernel
