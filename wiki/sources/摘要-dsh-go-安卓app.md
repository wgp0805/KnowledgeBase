---
title: "摘要-dsh-go-安卓app"
type: source
tags: [来源, DeepSeekHarness, 安卓, 移动端, DSHGo]
sources: [raw/01-articles/2026-11-06 - 把 DeepSeek Harness 做成一个正经的安卓 App，在本机直接跑，练 Root 都不用！.md]
last_updated: 2026-11-09
---

## 核心摘要
DSH Go 是开源的安卓 App（GitHub `ccch1mneyyy/dsh-go`，2026-10-25 建仓、5 天冲上 Trendshift 全语言日榜第一、8 千多 Star），把 DeepSeek Harness 装进手机**本机直接跑**，不用 Root、不用自己折腾环境（内置 Ubuntu + Node.js + DSH 运行环境，默认 PRoot 兼容模式，官方建议留 1GB 空间）。除本机跑轻任务外，还能**遥控电脑**上的 DSH：同一局域网走 SSH 直连，跨网络用 DSHarness Remote 远程插件（端到端加密、首次核对身份指纹）。UI 用 Flutter 编写、代码完全开源；模型走用户自己配置的提供方，本机运行不代表模型离线。作者为程序员追风。

## 关键信息
- **本机跑**：内置 Ubuntu/Node.js/DSH 环境，App 开箱即用；演示账单汇总任务（读 CSV→跑 python3 脚本→交回 xlsx+趋势图）全程手机内完成，23 秒/4 步/3.4 万 token
- **遥控电脑**：切换主机即显示电脑那份 DSH 的会话与工作区；局域网 SSH 直连 / 跨网 DSHarness Remote（端到端加密+身份指纹核对）
- **远程模式限制**：只能发图片附件、App 内打不开网页版、插件只能开关不能细管、DS Bot 和对话日志导出不可用
- **生成中插话**：运行中直接发消息即插话（手上活不停，下一步考虑进来）；长按发送可「中断并发送」或「排队」，排队消息可提前「立即发送」；思考过程与工具调用自动折行，想看展开
- **手机操控**：基于安卓无障碍权限，读屏幕/点按/输入文字；三档确认（每次都询问/本任务免确认/始终免确认）；支付/银行/券商默认不碰、微信默认每步确认；「解除限制」含系统设置、密码验证码、DSH Go 自身（默认全关，长按确认）
- **安全提示**：不建议在存支付/银行信息的设备上解除限制；能读屏的 Agent 对提示注入是实打实威胁；「不打扰模式」Android 14+ 配 Shizuku/自连 ADB 在不可见屏幕操作
- **构建**：APK 接近 200MB（塞了一整套运行环境）、Android 8.0+；arm64 包为主；源码构建需 Linux x86_64 + JDK17 + Flutter + Android SDK（setup-toolchain.sh）；自编包为 debug 签名不能覆盖安装官方包
- **生态关联**：同作者还有 dsh-TUI（像素鲸鱼 Deepy 来源，被 DSH 官方公众号收录）；DSH 开源后周边项目爆得快——终端 dsh-TUI、远程 DSHarness Remote、插件导航站、吉祥物清一色鲸鱼

## 关联连接
- [[DSHGo]] — 实体
- [[DeepSeekHarness]] — 宿主 Harness
- [[程序员追风]] — 作者
- [[插件生态]] — 生态语境
- [[远程审批]] — 手机远程审批刚需（见插件生态）
