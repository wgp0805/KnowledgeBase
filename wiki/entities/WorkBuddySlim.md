---
title: "WorkBuddySlim"
type: entity
tags: [实体, Skill, 开源, WorkBuddy, 运维]
sources: ["raw/09-archive/2026-10-24-WorkBuddy干活变慢还费token，一招教你瘦身加速.md"]
last_updated: 2026-10-26
---

## 定义
WorkBuddySlim（仓库名 workbuddy-slim）是马佳彬（老马）开源的 [[WorkBuddy]] 加速瘦身诊断 Skill（github.com/majiabin2020/workbuddy-slim/）：只诊断 WorkBuddy 越用越慢、token/积分消耗大的根本原因，不代用户删除或关闭任何 Skill、MCP 与记忆，输出红黄绿体检报告、由用户逐项确认后执行非破坏性加速瘦身。

## 关键信息
1. **定位与边界**：只诊断不动手——不会直接删除或关闭用户的 Skill、MCP、记忆；所有操作在用户看完报告、逐项确认后才执行，属非破坏性瘦身
2. **四大诊断维度**：规则膨胀、记忆超限、技能与连接器堆积、会话卫生
3. **红黄绿体检报告**：输出 Markdown 文档——红=严重需及时处理、黄=中等警告可一并处理、绿=状态健康
4. **安装**：在 WorkBuddy 新建任务发送"安装这个skill：github.com/majiabin2020/workbuddy-slim/"；安装失败或无法访问 GitHub 多为网络问题，需配合作者此前文章的 GitHub 访问 Skill 解决
5. **触发**：安装后在会话说"给我的WorkBuddy做个体检"或"帮我的WorkBuddy加速瘦身一下"即启动全面检查
6. **作者实测**：本机安装 56 个技能，40 个踩红线——平时不常用却成为最大包袱
7. **配套处置**：在专家技能连接器关闭不常用技能/连接器（官方建议启用不超过 80 个工具，否则可能影响 AI 回复质量）；对工作区 MEMORY.md 过多内容做一轮 [[记忆蒸馏]]；看不懂报告可让 WorkBuddy 用大白话解释并给优化建议

## 关联连接
- [[摘要-workbuddy-slim加速瘦身]] — 来源
- [[WorkBuddy]] — 宿主产品与诊断对象
- [[马佳彬]] — 作者（另开源 ClineFreePool）
- [[Agent瘦身]] — 体现的方法论
- [[记忆蒸馏]] — 报告处置手段之一
- [[Skill]] — 产品形态
- [[MCP]] — 诊断对象（连接器堆积）
