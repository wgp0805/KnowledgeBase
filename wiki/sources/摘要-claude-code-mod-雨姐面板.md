---
title: "摘要-claude-code-mod-雨姐面板"
type: source
tags: [来源, 原始文件, ClaudeCode, Mods, 插件开发]
sources: [raw/01-articles/2026-10-05-Claude Code Mod 实测：给编程助手做一个自定义面板.md]
last_updated: 2026-10-08
---

## 核心摘要
作者"赛博禅心"用六个步骤实测 Claude Code 的 Mod 功能（v2.1.287+），搭出一个"雨姐"主题 Mod：①搭工位——三个文件（`.claude-plugin/plugin.json`、`hooks/hooks.json`、`register.tsx`），在 session.start 注册命令/写状态栏/开面板，ui.render 画内容，改完保存自动热重载不用重启；②长脸——用 Raster 字符画布（一个"▀"字符装上下两个像素）搬像素风头像，踩坑 tmux 自动降 256 色、Raster 把颜色通道压成 16 档导致偏色；③旁观——tool.call 钩子 await next(e) 放行后按结果换表情记账，踩坑 `npm test 2>&1 | tail -40` 管道尾成功导致整条命令不标报错，需另扫输出里的 "fail" 字样；④改写——prompt.compose 往系统提示词注入"东北大姐口吻"（用户原话不动），/yujie-talk 斜杠命令直跑本地函数不经过 Claude；⑤接管——tool.call 匹配 rm -rf/强推/`git reset --hard` 时不调 next 直接回 deny，**拒绝理由原样进 Claude 上下文**，Claude 会顺着规矩把命令交还用户而不是绕开（正则匹配可被 `rm -r -f` 绕过，认真防可参考官方 blast-radius 示例）；⑥安全测试——`claude plugin validate --strict` 静态审查 hooks/calls 清单（一眼看出不联网不读文件不调模型），`claude plugin test` 事件级自动化测试不登录不联网几百毫秒跑完，还真抓到无界面环境下拉面板报错的 bug。与 Skill/MCP/settings hooks 的区别：**Mod 是跑在 Claude Code 进程里的 JS/TS 代码**，能直接画界面。分享四方式（发文件夹/git+marketplace.json 团队/托管设置公司/公开仓库），按"名字@集市"安装、版本号不改别人拿不到更新；**Mod 不在沙箱里**，以用户身份运行，只装可信作者的。Claude Code 内置的 /diff 面板本身就是一个 Mod。

## 关联连接
- [[ClaudeCode]] — 宿主产品
- [[Mods]] — 被实测的扩展机制
- [[Anthropic]] — 发布方
- [[摘要-claude-code-mods机制]] — Mods 机制来源
- [[摘要-deepseek-harness-桌面版万字拆解]] — 竞品视角的 Mods 对比
