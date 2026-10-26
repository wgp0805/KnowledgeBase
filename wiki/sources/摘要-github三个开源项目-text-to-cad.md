---
title: "摘要-github三个开源项目-text-to-cad"
type: source
tags: [来源, 开源项目, GitHub, CAD, 安卓, 视频]
sources: [raw/09-archive/2026-10-16 - 最近逛GitHub，挖到3个给力的开源项目，第一个比较硬核。.md]
last_updated: 2026-10-19
---

## 核心摘要

我是程序汪的 GitHub 开源项目盘点（2026-10-16）：①**text-to-cad**——给 Claude Code、Codex 等 Agent 赋予 CAD 建模能力的插件+Skill；②**pdoom-video**——一支音乐 MV 的画面、歌词动画与渲染过程全开源，制作全程用 Claude Code 对话协作完成；③**Jev 聊天助手**（jev-chat-jarvis）——在聊天界面里分析消息并生成候选回复的安卓开源应用。

## 关键信息

### 01 text-to-cad：给 Agent 赋予 CAD 超能力
- 定位：为 Claude Code、Codex 等 Agent 工具增加 CAD 建模能力，把建模、查看、导出流程整理成**插件与 Skill**
- 受众：机械专业大学生、机器人比赛团队、硬件工程师、3D 打印爱好者
- 用法：**描述零件形状和尺寸**（如带安装孔的支架：整体尺寸、厚度、孔径、孔位）→ Agent 编写本地建模脚本 → 生成三维文件；改需求=改参数重新生成，**模型源码保留**方便继续调整
- 导出格式：STEP（继续在 CAD 软件里处理）、STL/3MF（3D 打印）、GLB（三维展示）；配套查看器可打开模型检查后再给 Agent 提修改要求
- 开源地址：github.com/earthtojake/text-to-cad

### 02 pdoom-video：音乐 MV 制作全开源
- 为歌曲《I'm Upping My P(doom)》制作的视觉作品：画面由程序绘制，歌词逐词跟随人声变化
- 画面元素含图表、表格、三维房间、回形针；不同场景各有画风又共用一套色彩与字体规则，切换与音乐节拍对齐
- 开源内容：视觉构思、分场景制作说明、音频、逐词歌词时间、节拍分析数据——**视觉构思、歌词对齐、音频分析和场景实现全部由开发者与 Claude Code 对话协作完成**
- 对动态设计、创意编程者是具体参考
- 开源地址：github.com/mexicat/pdoom-video

### 03 Jev 聊天助手（jev-chat-jarvis）
- 开源安卓应用：在聊天界面里分析消息、帮你想几种回复方式；打开 QQ/飞书，屏幕出现**可拖动小卡片**，展开看分析、挑一条填进输入框、自己点发送
- 分析逻辑：结合当前对话推测对方想表达什么、希望你做什么，据此起草回复；可生成 1/2/3 条（3 条时给候选排序），不合适点**换一组**重新生成
- 手动笔记：给联系人写关系和备注，匹配到联系人或聊天里出现笔记标题/标签时背景一起参与分析；聊天历史本地记录默认关闭
- 适配 QQ、X 私信、飞书；Android 11+，需配置模型接口与密钥，并开启无障碍、悬浮窗权限
- 开源地址：github.com/jev-chat/jev-chat-jarvis
- **重要区分**：与本库既有判断模型实体 [[Jev]]（TypeSafe AI 的哑巴模型）**同名不同物**，已另建实体 [[JevChatJarvis]]

## 关联连接
- [[TextToCad]] — 项目一实体（新建）
- [[PdoomVideo]] — 项目二实体（新建）
- [[JevChatJarvis]] — 项目三实体（新建，与判断模型 Jev 区分）
- [[程序汪]] — 本文作者
- [[Jev]] — 同名不同物的判断模型（勿混淆）
- [[ClaudeCode]] — text-to-cad 与 pdoom-video 的宿主/协作者
- [[Codex]] — text-to-cad 支持的另一 Agent
- [[AgentSkills]] — text-to-cad 的能力载体
- [[AI视频生成]] — pdoom-video 所属的相邻领域
