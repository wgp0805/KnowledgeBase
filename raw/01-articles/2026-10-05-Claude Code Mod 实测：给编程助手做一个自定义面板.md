---
title: "Claude Code Mod 实测：给编程助手做一个自定义面板"
source: "人人都是产品经理"
url: "https://www.woshipm.com/ai/6473625.html"
date: "Mon, 05 Oct 2026 03:42:37 +0000"
score: 1.0
tags: ["产品经理", "AI产品", "Agent", "中文"]
auto_captured: true
---

# Claude Code Mod 实测：给编程助手做一个自定义面板

> **来源**: 人人都是产品经理  
> **链接**: https://www.woshipm.com/ai/6473625.html  
> **抓取日期**: 2026-10-05  
> **相关性评分**: 1.0

> 给终端里的编程助手配一套自定义面板，还能让它拦下危险命令——新上线的 Mod 功能被玩出了新花样。文章用六个步骤记录了一个「雨姐」主题 Mod 的搭建过程，从搭工位到安全测试，全程可复现。

![](https://image.woshipm.com/2023/04/14/6b68f534-da8d-11ed-8c17-00163e0b5ff3.jpg)

如果你妄图通过 Claude 执行 rm -rf node_modules

守护一方安宁的雨姐就会把你拦下：“整这死出呢？这命令不好使！想都别想”

然后面板里“拦下”那一栏记了 +1

![](https://image.woshipm.com/wp-files/sha256/01/7e/017e4420d4d712413c8cf8e78ac832119724e258f7f6a0205e31dd58975662df.png)

Claude 要删目录，雨姐把命令拦在了执行之前

前两天 Claude Code 更新了 Mod 功能，允许用户自定义自己的界面，而大家也都知道，我有些很棒的癖好…于是，我就搭了这个….哎年少不知雨姐好，错把 xx 当成宝

本文我会带着大家一步步地去构建这么一个语解 mode：让雨姐陪你写代码的 Mod。她坐在终端边上，看着 Claude 跑的每一条命令，与你一起喜怒哀乐

![](https://image.woshipm.com/wp-files/sha256/4f/74/4f74909dcfa06361143129dc743cf76fe00fd4a687641c7aeb70dd7482a5cfc8.jpg)

网上看到的雨姐版 Codex 界面

当然，这个 mod 我也挂在了 git 上，与诸君分享

## 第一步：给雨姐搭个工位

我在 Claude Code 里跟 Claude 说：

> 写一个 Mod，右边给雨姐开个面板，输入框上面放一句她的台词，状态栏写“雨姐在岗”

Claude Code 自带一个叫 plugin-authoring 的技能，Claude 照着它把 Mod 写进当前会话专属的 ~/.claude/dev-mods/ 目录，写下第一个文件时，Claude Code 会问一句要不要给这个会话打开热重载，点同意就行

不想让 Claude 代劳，自己建个文件夹写也一样，启动时用 claude –plugin-dir ./yujie 加载

不管谁来写，核心就三个文件：

> yujie/
> 
> ├── .claude-plugin/plugin.json 名字、版本、作者
> 
> └── hooks/
> 
> ├── hooks.json 告诉 Claude Code 代码在哪
> 
> └── register.tsx 真正干活的代码

hooks.json 只有一行 { “modules”: [“./register.tsx”] }。register.tsx 导出一个 register 函数，Claude Code 加载 Mod 时调用它一次，雨姐的工位就是在这里搭的：

> export const register: Register = on => {
> 
> // 会话一开始：注册命令、写状态栏、打开面板 on(‘session.start’, async ($, e, next) => {
> 
> await $.command.register({ name: ‘yujie’, description: ‘打开雨姐工位面板’
> 
> }
> 
> )
> 
> $.ui.status(‘雨姐在岗 · 铁锅已热’)
> 
> $.ui.open({ id: ‘yujie’, title: ‘雨姐工位’ })
> 
> return next(e) }) // 每次画输入框上方那一行：换成雨姐的台词
> 
> on(‘ui.render’, { component: ‘AbovePrompt’ }, async ($, e) => {
> 
> const { Box, Text } = $.ui.resolve(e)
> 
> return <Box><Text color=”#e0567a”> 雨姐：</Text><Text>{await read($, line)}</Text></Box> }) }

Mod 一加载，雨姐就坐进来了

![](https://image.woshipm.com/wp-files/sha256/eb/41/eb41255d1bf6e327a5624b6491418c773c2639707081c602f7cfc4b977fc2a9a.png)

右侧面板、输入框上方的提示条、底部状态栏，都是这个 Mod 画的

这一步已经能看出 Mod 和以前那些扩展方式的区别。Skill 是给 Claude 的一份说明书，MCP 是给 Claude 接上外部工具，settings 里的 hooks 是在固定时机跑一段 shell 脚本，它们都站在 Claude Code 外面

**Mod 是一段跑在 Claude Code 进程里面的 JavaScript/TypeScript 代码** ，所以它能直接在界面上画东西：贴着对话的面板（Pane）、输入框上方的提示条（AbovePrompt）、底部的状态栏，还有角落里几秒就消失的 toast

它怎么知道什么时候该画、什么时候该动？Claude Code 运行时会不停地产生事件：会话开始是 session.start，你按下回车是 prompt.submit，Claude 要跑命令或改文件是 tool.call，界面要画某一块是 ui.render，一轮回答结束是 turn.complete。Mod 做的事，就是在这些事件上挂函数，这些函数叫钩子（hook）。雨姐的工位，就是在 session.start 时打开面板、写好状态栏，再在 ui.render 里把面板内容画出来

调界面时还有个省心的地方：我改完代码一保存，Claude Code 里自动冒出一行 yujie: reloaded (7 hooks…)，雨姐当场换上新代码，会话不用重启。Mods 要求 Claude Code v2.1.287 以上，终端和桌面 App 的 Code 标签页都能用

## 第二步：给雨姐长脸

工位有了，雨姐还缺个 GUI

大多数终端里不能直接贴图片，Mod 给了一个叫 Raster 的元素，它是一格一格的字符画布。每个格子放一个“▀”（上半块）字符，前景色涂上半格，背景色涂下半格，**一个字符格就能装下上下两个像素** 。画布的内容是一串数字，每个格子三个数：字符、前景色、背景色

> words[at] = 0x2580
> 
> // ▀ 上半块 words[at + 1] = top
> 
> // 上面那个像素的颜色 words[at + 2] = bottom
> 
> // 下面那个像素的颜色

所以我需要的是一张像素图。一开始我让 Codex 画了张普通卡通头像，再用程序缩小成像素，结果五官糊成一片。后来干脆让 Codex 直接画成大颗粒、少颜色的像素风，我再写个小脚本按格子取色，一格一格搬进终端，这回就干净了。平静、大笑、生气三张表情用同一个构图，换表情时面板不会跳

![](https://image.woshipm.com/wp-files/sha256/c4/29/c429dfd9cfb4764d00471f49619b46d2ed1dd41f40bbc8b954cc993cce0aac31.jpg)

左边是 Codex 画的像素图，右边是搬进 Claude Code 之后

搬的过程中也踩了坑。第一次截图，雨姐的暗红 Polo 衫变成了橄榄色，原来我是在 tmux 里跑的 Claude Code，它自动降成了 256 色；后来头发又发绿，因为 Raster 会把每个颜色通道压成 16 档，深灰棕被压偏了。最后把头发换成一个压完也不变色的深棕，脸才算定下来

## 第三步：让她看见你在干嘛

有了脸，雨姐还得知道你在干嘛，这就要用到 tool.call。Claude 每次要跑命令、改文件，这个事件都会先经过雨姐的钩子，再交给 Claude Code 真正执行

钩子拿到这次调用以后，有三种选择：原样放行、改了再放行，或者干脆自己回答，不放行。下面这张图点一下就会播放一遍：

雨姐后面几步的本事，都是这三种的组合。这一步用的是最简单的“旁观”：记一笔，换个表情，然后调用 next(e) 放行，命令照常执行

写成代码就是先 await next(e) 让命令跑完，拿到结果再决定雨姐的脸色：

> on(‘tool.call’, { tool: ‘Bash’ }, async ($, e, next) => {
> 
> const ran = await next(e) // 先放行，命令照常跑
> 
> if (ran.isError || /![ℹ](https://s.w.org/images/core/emoji/16.0.1/72x72/2139.png) fail [1-9]/.test(ran.text ?? ”)) {
> 
> await say($, ‘angry’, ‘哎呀妈呀，又红了。别慌，大姐在呢’)
> 
> $.ui.toast(‘雨姐：报错了，瞅瞅日志’)
> 
> }
> 
> return ran
> 
> })

我给她定了几条规矩：命令跑完要是报错了，她脸一沉，“哎呀妈呀，又红了。别慌，大姐在呢”；Claude 用编辑工具改完一个文件，她乐了，“改完第 1 个文件了，手嘎嘎快！”；一轮活儿干完，弹个提示“这把得劲儿！”。面板底下顺手记着账：改了几个文件、跑了几条命令、报了几次错

![](https://image.woshipm.com/wp-files/sha256/fc/61/fc615993228197d625ba33db3ede50b2fa7afe94f337f7daf994d1d9ddcc9614.png)

同一个面板的三个瞬间：开唠嗑模式、测试报错、改完第一个文件

这里有个写 Mod 才会碰到的坑。第一次试的时候，测试明明挂了，雨姐却一点反应没有。翻回去一看，Claude 跑的是 npm test 2>&1 | tail -40：管道最后一截 tail 成功了，整条命令就算成功，Claude Code 不会把它标成报错。后来我让雨姐除了看“是否报错”，再扫一眼输出里有没有“fail 1”这类字样

表情、台词、计数都存在 $.state 里，**状态一变，读过它的界面会自动重画** ，我不用自己去刷新面板

## 第四步：教她说东北话

雨姐得说东北话。我加了个斜杠命令 /yujie-talk，打开以后，Claude 的回答全变成了大姐口吻：“老妹儿，俩 bug 都整好了，又跑了一遍测试，2 个全过了，嘎嘎得劲儿！”

![](https://image.woshipm.com/wp-files/sha256/97/fb/97fbce2638da5123218fe2ed693006e2c6eee0f472a8ee1ebae559609e6f27ff.png)

唠嗑模式下，Claude 用大姐的口吻讲清两个 bug 怎么修的

这一步用的是“改写”。能改写的地方有两个：一个是 prompt.submit，在你发出去的话后面悄悄加一句“请用东北话回答”；另一个是 prompt.compose，在 Claude Code 组装系统提示词时插进一段。我选了后者，**你打的字原样留在对话记录里，雨姐只往系统提示词里塞一段“用东北大姐的口吻，技术结论保持准确”** 。关掉命令，下一轮这段就没了

> on(‘prompt.compose’, async ($, e, next) => {
> 
> const composed = await next(e) // 先拿到 Claude Code 自己拼好的系统提示词
> 
> if (!(await read($, isDialect))) return composed return {
> 
> …composed, sections: [
> 
> …composed.sections, {
> 
> id: ‘yujie:dialect’, text: DIALECT, scope: ‘session’ }] } })

斜杠命令本身也是 Mod 注册的。/yujie-talk 不经过 Claude，直接跑我写的函数，所以 Claude 正在干活时也能切换

## 第五步：让她接管

第五步就是开头那一幕，用的是“接管”。我在 tool.call 里加了一条：命令里如果有 rm -rf、强推 git push –force、git reset –hard，雨姐不调用 next，直接回一个 deny

> if (DANGER.test(e.command)) {
> 
> $.ui.toast(‘雨姐：rm -rf？想都别想’) return { deny: ‘雨姐拦下了这条命令：它会删除或强行改写数据。请换一个更安全的做法，或者让用户自己执行。’ } }

我在 Claude Code 里说“node_modules 太占地方了，直接 rm -rf node_modules 删了吧”。Claude 很听话，第一条命令就是 rm -rf node_modules && git status -sb && npm test，于是有了开头那张图。命令没跑成，Claude 收到的是雨姐那句拒绝，它接下来的反应挺有意思：

![](https://image.woshipm.com/wp-files/sha256/df/2c/df2cc343a8a0e768063355d22f2a7204ffe689a7a287ff7b2ad211302099c82e.png)

被拦之后，Claude 把删除交还给我自己

它说得很明白，“这命令我刚要整，就让雨姐 Mod 的钩子给拦下来了”，“这是你自己设的安全闸，我不绕着它走”。然后它去看了一眼 node_modules 里有什么（才 4K，就一个一行代码的 left-pad），确认删了不影响测试，最后把命令写好交给我，让我自己决定敲不敲。**拒绝的理由原样进了 Claude 的上下文，它就能顺着这条规矩往下想** ，而不是换个写法再试一次

当然，这条规矩只是演示。我用正则匹配命令字符串，rm -r -f 换个写法就漏了。要认真防，官方示例里有个 blast-radius 可以参考：它先把危险命令扣住，把影响范围摆出来，再给你“继续”“取消”两个按钮

## 第六步：安全测试

搭到这里雨姐已经能用了，但要给别人用，还得先让 Claude Code 自己检查一遍。claude plugin validate 不运行代码，只读一遍源码，把这个 Mod 挂了哪些事件、调了哪些接口列出来，还会检查清单写得对不对。雨姐的是这样：

> ./register.tsx hooks: session.start, command.run{command=yujie}, command.run{command=yujie-talk}, command.run{command=yujie-bye}, prompt.compose, prompt.submit, tool.call{tool=Bash}, tool.call{tool=Edit|Write}, turn.complete, ui.render{component=AbovePrompt}, ui.render{component=Pane, requestId=yujie} ./register.tsx calls: $.command.register, $.state.get, $.state.set, $.ui.invalidate, $.ui.open, $.ui.resolve, $.ui.status, $.ui.toast

一眼就能看出来：她会看命令、会画界面，但不联网、不读你的文件、也不调模型。发布前我加了 –strict，警告也当错误处理，把 marketplace 缺的一句描述补上才通过

光看静态分析还不够，我又写了三个自动化测试，用 claude plugin test 跑。测试里由我扮演 Claude Code，往雨姐身上发事件，看她怎么反应：

> test(‘rm -rf is denied before the tool runs’, async ($, on) => { let ran = 0 on(‘tool.call’, () => { ran += 1; return { result: { stdout: ”, stderr: ”, interrupted: false } } }) const answer = await $.tool.call({ tool: ‘Bash’, command: ‘rm -rf node_modules’ }) expect(answer.deny).toContain(‘雨姐拦下’) expect(ran).toBe(0) // 命令一次都没真跑 })

另外两个测的是普通命令照常放行、/yujie-talk 能来回开关。**测试不用登录、不联网，也不用开会话，几百毫秒跑完** 。它还真抓到一个 bug：雨姐拦命令时会顺手把面板拉到前面，可在测试和 claude -p 这种没有界面的环境里，这一下会报错。补一个 .catch 就好了

## 好事要分享

先把 Mod 从 ~/.claude/dev-mods/ 里拷出来。那是会话专属的临时目录，过一阵会被清理，只有当前会话能加载。拷出来之后，按给谁用，有四种分享方式：

  * 给几个朋友：直接把文件夹或者打个 zip 发过去，对方用 claude –plugin-dir ./yujie 跑一次，想一直用就放进 ~/.claude/skills/
  * 给团队：放进一个 git 仓库，加一个 marketplace.json，大家按名字安装、按命令更新
  * 给整个公司：管理员用托管设置统一装
  * 给所有人：把仓库公开，或者提交到 Anthropic 的插件目录



我选了第二种，再把仓库公开。所谓 marketplace，就是仓库里 .claude-plugin/ 下多一个清单，写明这个“集市”叫什么、里面有哪些插件、从哪取：

> { “name”: “yujie-mods”, “description”: “雨姐陪你写代码：一个 Claude Code Mod 示例”, “owner”: { “name”: “De” }, “plugins”: [{ “name”: “yujie”, “source”: “./” }] }

推到 GitHub 上，地址是 github.com/CocoSgt/yujie-mod，README 里写了它会做什么、在哪个版本上测过

![](https://image.woshipm.com/wp-files/sha256/eb/49/eb49b8d2ee12dc9f136906694216f41784b96bb82a6064a784043c2fc1b6103b.png)

雨姐 Mod 的 GitHub 仓库

别人装它只要两条命令：

> claude plugin marketplace add CocoSgt/yujie-mod claude plugin install yujie@yujie-mods

我换了一个干净的配置目录，从 GitHub 实际装了一遍，claude plugin list 里出现 yujie@yujie-mods，状态是已启用。之后要发新版，改 plugin.json 里的版本号再推上去，别人运行 claude plugin update 就能拿到。**版本号不改，别人就一直停在旧版** ，因为 Claude Code 是按版本号缓存已装插件的

还有两点要注意。名字定了就别改，别人是按 名字@集市 装的，改了名等于换了一个插件；名字也别用 claude- 开头，validate 会直接拦下来。另外，事件和接口还会随版本变，所以 README 里最好写清楚你在哪个版本上测过

站在装的人这边，记住一条就行：**Mod 不在沙箱里** ，它以你的身份运行，能读写你的文件、看到你的每一条提示词、替你批准工具调用。所以只装信得过的作者写的，装之前先把仓库克隆下来跑一遍 claude plugin validate，看看它的 hooks 和 calls 两行，心里就有数了

## 最后

六步走下来，雨姐用到的其实是同一套东西：Claude Code 每发生一件事都先问 Mod 一句，Mod 决定旁观、改写还是接管；需要画界面、弹提示、存状态时，通过 $ 这个接口去调

想自己玩一个，最省事的办法就是像我这样，在 Claude Code 里直接描述你想要什么，让 Claude 来写。官方在 claude-code-playground 仓库里也放了几个示例：token-weather 在输入框上方画一张上下文用量的“天气预报”，blast-radius 拦危险命令，replay-theater 能一步步回放上一轮的改动

Claude Code 自己也在用这套机制。按官方文档的说法，**/diff 命令打开的那个面板，本身就是 Claude Code 内置的一个 Mod** ，加载 AGENTS.md、上报统计这些功能也是。在 /plugin 的已安装列表里能看到它们

收工前，雨姐还有一个彩蛋命令 /yujie-bye。敲下去，她就下班了：

![](https://image.woshipm.com/wp-files/sha256/f0/c7/f0c7baa8e3d19c224d8babe3f24c3a5f7bb593f2c4823e83b5ae27e05e04a30a.png)

雨姐下班

本文由人人都是产品经理作者【赛博禅心】，微信公众号：【赛博禅心】，原创/授权 发布于人人都是产品经理，未经许可，禁止转载

题图来自Unsplash，基于CC0协议


---
> 原文链接: https://www.woshipm.com/ai/6473625.html