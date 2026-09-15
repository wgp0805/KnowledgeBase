---
title: "摘要-huashu-report-skill"
type: source
tags: [来源, 原始文件, Agent Skill, 报告, 开源]
sources: [raw/01-articles/2026-09-14-正式开源！比橙皮书skill更强10倍的Huashu-Report来了！.md]
last_updated: 2026-09-15
---

## 核心摘要
花叔（@alchaincyf）开源 **huashu-report** skill（MIT 协议，github.com/alchaincyf/huashu-report），声称比其此前的橙皮书 skill 强 10 倍，能力覆盖面更广——橙皮书只是它能做的六种产物之一。它用三层机制解决「AI 写不好报告」的三个真实翻车点（编数字、翻来覆去说三遍、前后口径打架）：(1) 数字唯一来源锁定在 `数据表.json`，正文引用靠函数渲染为上标编号，编译器反向检查「正文引了数据表里没有的条目」，改正文过不了编译；口径写不出一句完整的话这个数字就不能用。(2) 能写成函数或计数的规则一律挪进编译器，只有机器判不了「什么叫具体」的规则才留在手册——手册不是强制力。(3) 渲染脚本自动查编号断号/目录页码/占位符/四边留白实测毫米数，但负值柱画成零高度、标注被版心切掉这类缺陷脚本查不出，必须把 PDF 逐页渲成 PNG 拼成 12 页检查表逐页过眼，且「假警报比漏报贵」。六种原型：16:9 咨询 deck、研报型、学术型、论文型、调查型、科普型（橙皮书属科普型），选错原型是最贵的错误。作者用 19 个 agent 扫出 74 份 2026 顶级机构 AI 报告、实测能下全文 42 份，写成解剖器提取结构指标，让报告品位对齐麦肯锡/BCG/Stanford 的选择。DeepSeek 研报连数据带脚本也开源（github.com/alchaincyf/deepseek-influence-report）。

## 关联连接
- [[Huashu-Report]] — 本文主角 skill
- [[花叔]] — 作者与开源者
- [[报告原型分类]] — 六种报告原型的选型框架
- [[Claims溯源]] — 数字唯一来源锁定与口径溯源机制
- [[摘要-huashu-excel-skill]] — 同一作者的 Excel skill
- [[Anthropic]] — AI 心理学研究灵感来源（能力激发方法）
- [[Twyman定律]] — 异常数字先当 bug 查
- [[AgentSkills]] — Agent 技能生态
