---
title: "DSHGo"
type: entity
tags: [实体, 开源项目, 安卓, DeepSeekHarness, 移动端]
sources: [raw/01-articles/2026-11-06 - 把 DeepSeek Harness 做成一个正经的安卓 App，在本机直接跑，练 Root 都不用！.md]
last_updated: 2026-11-09
---

## 定义
DSH Go（GitHub `ccch1mneyyy/dsh-go`，2026-10-25 建仓、5 天冲上 Trendshift 全语言日榜第一、8 千多 Star）是开源的安卓 App，把 DeepSeek Harness 装进手机**本机直接跑**（不用 Root、内置 Ubuntu+Node.js+DSH 环境、默认 PRoot 兼容模式），还能**遥控电脑**上的 DSH。UI 用 Flutter 编写、代码完全开源、非 DeepSeek 官方出品；模型走用户自配的提供方。

## 关键信息
- **本机跑**：内置完整运行环境（建议留 1GB 空间）；演示账单汇总任务手机内完成（23 秒/4 步/3.4 万 token），读 CSV→跑 python3→交回 xlsx+趋势图
- **遥控电脑**：切换主机显示电脑那份 DSH 的会话与工作区；同局域网 SSH 直连、跨网 DSHarness Remote（端到端加密+身份指纹核对）；远程模式限制——只能发图片附件、打不开网页版、插件只能开关不能细管、DS Bot 与对话日志导出不可用
- **生成中插话**：运行中直接发消息即插话（活不停、下一步考虑进来）；长按发送可「中断并发送」或「排队」；思考过程与工具调用自动折行
- **手机操控**：安卓无障碍权限（读屏/点按/输入文字）；三档确认（每次询问/本任务免确认/始终免确认）；支付/银行/券商默认不碰、微信默认每步确认；「解除限制」三项默认全关需长按确认；建议不在存支付/银行信息的设备解除限制（提示注入是实打实威胁）
- **构建**：APK 约 200MB、Android 8.0+、arm64 主包；源码构建 Linux x86_64（setup-toolchain.sh 装 JDK17+Flutter+Android SDK）；自编包 debug 签名不能覆盖官方包
- **生态**：同作者还有 dsh-TUI（像素鲸鱼 Deepy 来源）；DSH 开源后周边项目冒得快——终端 dsh-TUI、远程 DSHarness Remote、插件导航站、吉祥物清一色鲸鱼

## 关联连接
- [[摘要-dsh-go-安卓app]] — 来源
- [[DeepSeekHarness]] — 宿主 Harness
- [[程序员追风]] — 作者
- [[插件生态]] — 生态语境
- [[Flutter]] — UI 框架
- [[everything-is-a-plugin]] — 架构理念
