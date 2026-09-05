---
title: "Codex 版本大升级，Computer Use 让 Agent 直接操作 IDEA+Chrome，全栈 Agent 来了。"
source: "https://javabetter.cn/sidebar/itwanger/ai/codex-april-2026-deep-review.html"
---
大家好，我是二哥呀。

Claude 刚放出 Opus 4.7 的大招，OpenAI 反手就把 Codex 升了个大版本——「Codex for (almost) everything」。

一点不谦虚啊。

我高强度用了几天，最大的感受就一个字：猛。

新版一口气加了 Computer Use、内置浏览器、图像生成、90 多个新插件、Memory、自动化，后续 CLI 连着迭代了好几版，今天凌晨又上线了 Chronicle——把屏幕内容也「放进记忆」了。

![](assets/Codex%20%E7%89%88%E6%9C%AC%E5%A4%A7%E5%8D%87%E7%BA%A7%EF%BC%8CComputer%20Use%20%E8%AE%A9%20Agent%20%E7%9B%B4%E6%8E%A5%E6%93%8D%E4%BD%9C%20IDEA+Chrome%EF%BC%8C%E5%85%A8%E6%A0%88%20Agent%20%E6%9D%A5%E4%BA%86%E3%80%82/03abe10cb85d41f648a31b2136925bbf_MD5.png)

## 01、Computer Use

这次更新里最炸裂的，毫无疑问是 Computer Use。

先说它干了什么——Codex 现在能在你的 Mac 上自己点鼠标、敲键盘、看屏幕。

而且跑的是后台服务，不抢你的光标。

![](assets/Codex%20%E7%89%88%E6%9C%AC%E5%A4%A7%E5%8D%87%E7%BA%A7%EF%BC%8CComputer%20Use%20%E8%AE%A9%20Agent%20%E7%9B%B4%E6%8E%A5%E6%93%8D%E4%BD%9C%20IDEA+Chrome%EF%BC%8C%E5%85%A8%E6%A0%88%20Agent%20%E6%9D%A5%E4%BA%86%E3%80%82/56f2ae4277e736b1791d893b257e509f_MD5.png)

这才是 Agent 该有的样子，不只是 Coding，还能操作我的电脑帮我干活，但碍着我干活。

### 开启和配置

Computer Use 需要单独开启。在 Codex 的设置里找到 Computer Use，点安装，几秒钟就好。

我一开始还以为要装什么大型驱动包，结果就一个小插件，轻量得有点出乎意料。

![](assets/Codex%20%E7%89%88%E6%9C%AC%E5%A4%A7%E5%8D%87%E7%BA%A7%EF%BC%8CComputer%20Use%20%E8%AE%A9%20Agent%20%E7%9B%B4%E6%8E%A5%E6%93%8D%E4%BD%9C%20IDEA+Chrome%EF%BC%8C%E5%85%A8%E6%A0%88%20Agent%20%E6%9D%A5%E4%BA%86%E3%80%82/1e93278f85a117e07c70ca7ecb607b68_MD5.png)

第一次让 Codex 操控某个应用时，它会请示你。你可以勾选「始终允许」，之后这个应用就不用反复确认了。建议把 IntelliJ IDEA、Chrome 这类信任度高的直接放开，省得每次都弹窗。

然后 macOS 会弹一个辅助功能权限提示，需要去系统设置里把 Codex 的 Computer Use 勾上。

![](assets/Codex%20%E7%89%88%E6%9C%AC%E5%A4%A7%E5%8D%87%E7%BA%A7%EF%BC%8CComputer%20Use%20%E8%AE%A9%20Agent%20%E7%9B%B4%E6%8E%A5%E6%93%8D%E4%BD%9C%20IDEA+Chrome%EF%BC%8C%E5%85%A8%E6%A0%88%20Agent%20%E6%9D%A5%E4%BA%86%E3%80%82/54c710c40dfcaa07a27ca559d0718dcc_MD5.png)

![](assets/Codex%20%E7%89%88%E6%9C%AC%E5%A4%A7%E5%8D%87%E7%BA%A7%EF%BC%8CComputer%20Use%20%E8%AE%A9%20Agent%20%E7%9B%B4%E6%8E%A5%E6%93%8D%E4%BD%9C%20IDEA+Chrome%EF%BC%8C%E5%85%A8%E6%A0%88%20Agent%20%E6%9D%A5%E4%BA%86%E3%80%82/943a12f12284cbbfdafed78e59de77f4_MD5.jpg)

![](assets/Codex%20%E7%89%88%E6%9C%AC%E5%A4%A7%E5%8D%87%E7%BA%A7%EF%BC%8CComputer%20Use%20%E8%AE%A9%20Agent%20%E7%9B%B4%E6%8E%A5%E6%93%8D%E4%BD%9C%20IDEA+Chrome%EF%BC%8C%E5%85%A8%E6%A0%88%20Agent%20%E6%9D%A5%E4%BA%86%E3%80%82/2ae197d1e46593437dc92c2aa660f732_MD5.png)

### 让 Codex 操控 IntelliJ IDEA

适用场景有很多，比如说测试 macOS 应用、跑 iOS 模拟器、用浏览器验证 web 服务、改 GUI 才能改的设置、复现只在图形界面出现的 bug、跨多个应用跑流程等。

我选了一个最贴近日常开发的场景——让 Codex 帮我打开 IntelliJ IDEA 并加载项目。

提示词很简单：用 IntelliJ IDEA 打开我的 PaiFlow 项目。

然后我就看着 IntelliJ IDEA 自己启动了，Codex 在后台操控光标找到项目路径、点击 Open，全程丝滑。

![](assets/Codex%20%E7%89%88%E6%9C%AC%E5%A4%A7%E5%8D%87%E7%BA%A7%EF%BC%8CComputer%20Use%20%E8%AE%A9%20Agent%20%E7%9B%B4%E6%8E%A5%E6%93%8D%E4%BD%9C%20IDEA+Chrome%EF%BC%8C%E5%85%A8%E6%A0%88%20Agent%20%E6%9D%A5%E4%BA%86%E3%80%82/b800791fc4f601484c6c2923ee2d766c_MD5.png)

![](assets/Codex%20%E7%89%88%E6%9C%AC%E5%A4%A7%E5%8D%87%E7%BA%A7%EF%BC%8CComputer%20Use%20%E8%AE%A9%20Agent%20%E7%9B%B4%E6%8E%A5%E6%93%8D%E4%BD%9C%20IDEA+Chrome%EF%BC%8C%E5%85%A8%E6%A0%88%20Agent%20%E6%9D%A5%E4%BA%86%E3%80%82/4b72658ef50125f12629fabc82e58d28_MD5.png)

![](assets/Codex%20%E7%89%88%E6%9C%AC%E5%A4%A7%E5%8D%87%E7%BA%A7%EF%BC%8CComputer%20Use%20%E8%AE%A9%20Agent%20%E7%9B%B4%E6%8E%A5%E6%93%8D%E4%BD%9C%20IDEA+Chrome%EF%BC%8C%E5%85%A8%E6%A0%88%20Agent%20%E6%9D%A5%E4%BA%86%E3%80%82/ddddf9919c43626d84d05355dc2066da_MD5.png)

整个操作大概十来秒，跟我自己手动操作的速度差不多。

这意味着——以前 Agent 只能在命令行里干活，改代码可以，但调试、看 UI、验证效果这些事还是得我们自己来。

现在 Agent 能自己开 IDE、自己跑模拟器、自己切到浏览器看效果，全都能参与了。

### 让 Codex 操控 Chrome 浏览器

我又试了一个更复杂的场景——让 Codex 帮我打开 Chrome，访问技术派官网，截个图给我看。

提示词：帮我用 Chrome 打开 paicoding.com，然后截图。

Codex 照做了。打开 Chrome、输入地址、等页面加载、截图，一气呵成。

![](assets/Codex%20%E7%89%88%E6%9C%AC%E5%A4%A7%E5%8D%87%E7%BA%A7%EF%BC%8CComputer%20Use%20%E8%AE%A9%20Agent%20%E7%9B%B4%E6%8E%A5%E6%93%8D%E4%BD%9C%20IDEA+Chrome%EF%BC%8C%E5%85%A8%E6%A0%88%20Agent%20%E6%9D%A5%E4%BA%86%E3%80%82/5201bfa4d15bc7c221dea5843b170db8_MD5.png)

注意 Chrome 右上角是 Codex 的光标。

![](assets/Codex%20%E7%89%88%E6%9C%AC%E5%A4%A7%E5%8D%87%E7%BA%A7%EF%BC%8CComputer%20Use%20%E8%AE%A9%20Agent%20%E7%9B%B4%E6%8E%A5%E6%93%8D%E4%BD%9C%20IDEA+Chrome%EF%BC%8C%E5%85%A8%E6%A0%88%20Agent%20%E6%9D%A5%E4%BA%86%E3%80%82/05889fe7afdf6e0327ab899972587aff_MD5.png)

状态栏这里也可以看得到。

![](assets/Codex%20%E7%89%88%E6%9C%AC%E5%A4%A7%E5%8D%87%E7%BA%A7%EF%BC%8CComputer%20Use%20%E8%AE%A9%20Agent%20%E7%9B%B4%E6%8E%A5%E6%93%8D%E4%BD%9C%20IDEA+Chrome%EF%BC%8C%E5%85%A8%E6%A0%88%20Agent%20%E6%9D%A5%E4%BA%86%E3%80%82/de6bdf32f2a30f4663760b5fe753d0e0_MD5.png)

然后截图这事也能干。

![](assets/Codex%20%E7%89%88%E6%9C%AC%E5%A4%A7%E5%8D%87%E7%BA%A7%EF%BC%8CComputer%20Use%20%E8%AE%A9%20Agent%20%E7%9B%B4%E6%8E%A5%E6%93%8D%E4%BD%9C%20IDEA+Chrome%EF%BC%8C%E5%85%A8%E6%A0%88%20Agent%20%E6%9D%A5%E4%BA%86%E3%80%82/bad68a1f18540edec637efccdd0a7529_MD5.png)

这是Codex最后截的图，还挺牛逼的。

![](assets/Codex%20%E7%89%88%E6%9C%AC%E5%A4%A7%E5%8D%87%E7%BA%A7%EF%BC%8CComputer%20Use%20%E8%AE%A9%20Agent%20%E7%9B%B4%E6%8E%A5%E6%93%8D%E4%BD%9C%20IDEA+Chrome%EF%BC%8C%E5%85%A8%E6%A0%88%20Agent%20%E6%9D%A5%E4%BA%86%E3%80%82/ade420b1d66e55492ab07d2cdd38b1eb_MD5.jpg)

这个场景的意义在于——以后可以让 Agent 自己去验证前端页面了。改完代码，让 Codex 自己打开浏览器看效果，不用我们自己切过去刷新。

### 几个要注意的坑

Computer Use 目前的限制和注意事项，我也讲一下。

第一个，目前只有 macOS 用户能用。Windows 的小伙伴暂时只能眼巴巴看着，不过从 CLI 更新日志来看，Windows sandbox 的支持已经在改进了，0.119 版本增加了 Windows elevated sandbox carveouts，0.120 又修了 Windows 相关的路径问题，估计离 Windows 支持不远了。

第二个，Computer Use 不能操作终端应用和 Codex 自身。这合理，不然套娃起来就乱套了。

第三个，它无法以管理员身份执行操作，也处理不了系统隐私弹窗。碰到这种弹窗，还是得你亲自出马。

第四个，涉及账户、支付、密码的操作，一定一定要自己盯着。浏览器操作是在你已登录的状态下执行的。

## 02、内置浏览器

Codex 这次还内置了一个浏览器。

目前支持打开本地 localhost 起的前端页面，或者其他不需要登录的公开页面。

虽然还做不到像 CDP 那样复用登录态访问任意网站，但配合 Computer Use 的浏览器操控能力，基本覆盖了大部分场景。

这个功能对前端开发来说太关键了。以前用 Codex 生成前端代码，得切到浏览器自己刷新看效果，觉得不对再回来改，来来回回折腾好几轮。现在 Codex 直接在内部浏览器里打开页面，你觉得哪里不满意，选中那块内容直接告诉 Codex 怎么改，Codex 看到反馈就自己去改代码了。

操作方式分两步。第一步，开启页面反馈功能。第二步，选中页面上某一块元素，写上你的反馈，比如「这个按钮颜色太深了，换个浅蓝色」。

然后回到对话窗口，Codex 就会根据你的反馈去改代码，改完自动刷新，你直接在内置浏览器里看效果。

这跟以前比简直是质变。

以前是「改代码 → 切浏览器 → 刷新 → 不行 → 切回 Codex → 再改」，现在是「选中 → 说一嘴 → 自动改完自动刷新」，少了四步来回切换。

## 03、图像生成

Codex 接入了 gpt-image-1.5，OpenAI 去年发的图像模型。

我试了一下，让它给登录页生成一个和 π 相关的 logo。出来的效果还不错。

直接采纳，放到项目里用。

## 04、90 多个新插件

Codex 的 plugin 是三样东西的组合：一组 skills（给 Codex 的任务说明书）、一组 app integrations（能操作的应用权限和接口）、一组 MCP servers（后端的数据和工具源）。

这次一口气多了 90 多个，包括 Atlassian Rovo（管 JIRA）、CircleCI、CodeRabbit、GitLab Issues、Microsoft Suite、Neon by Databricks、Remotion、Render 等。

CLI 0.121 版本还加了一个实用功能——支持从 GitHub 仓库、git URL、本地目录安装插件市场。

这意味着社区可以自己维护插件集，不再完全依赖官方分发。

0.122 版本更进一步，图像生成和工具发现功能默认开启了，不用再手动开启。插件的工作流也增强了，支持 tabbed browsing 和 toggles。

## 05、Memory

Codex 会记住你的偏好、你改过的地方、你上一回花很久才说清楚的那个背景，下一次就不用再讲一遍。

默认是不开启的，需要手动启用。

这个功能对长期项目太有用了。

之前每次开新对话，Codex 都要从头了解项目背景、代码风格、命名约定。现在它会记住这些，下次直接用。

## 06、Chronicle

这东西一句话就能说明白：Codex 的 Memory 之前只记对话历史，现在加了一层屏幕上下文。

它知道你现在屏幕上在看什么，刚才报什么错。

从此，你再跟 Codex 说话的时候，不用反复解释「这个」「那个」指的是什么了。

### 怎么启用

第一步，打开 Codex 的 Settings。

第二步，进入 Personalization，确认 Memories 已开。

第三步，打开 Memories 下方的 Chronicle。

第四步，点击确认对话框的 Continue。

### 技术细节

屏幕截图存在 `$TMPDIR/chronicle/screen_recording/` ，6 小时后 Chronicle 自己删掉。这点还挺好的，不会一直占着磁盘。

生成的 memory 存在 `~/.codex/memories_extensions/chronicle/` ，是未加密的 markdown 文件，用户可以读、可以改、可以删。OpenAI 建议不要手动加新条目，但局部改和删是支持的。

生成 memory 用的模型，默认跟 Codex 用的模型一致。想换别的可以在 config.toml 里设置：

```toml
[memories]
consolidation_model = "gpt-5.4-mini"
```

### 体验 Chronicle

Chronicle 加的是屏幕上下文——你屏幕上正在看什么、刚才浏览器打开了什么页面、终端里跑的是什么命令。

叠加上 Memory 之后，Codex 对「你现在的上下文」理解就从「你说过的」扩展到了「你看过的」。

比如我刚刚在Chrome上打开了 computer use，Codex 就能是被出来。

这就牛逼了，直接省掉「我说的是这个」「不是那个，是另一个」的无效沟通。

## 07、和 Claude Code 到底选谁

先说 Claude Code 的强项，模型推理能力和文本处理。

Opus 的推理确实猛，处理复杂逻辑、理解大项目架构的时候，Claude Code 更稳。尤其是那种需要反复迭代、中间不断调整方向的探索型任务，Claude Code 的交互模式更灵活。

但 Claude 有个大问题，用过的小伙伴应该都懂——付费和使用上的担忧，实名认证出来之后更是焦虑了一波。

再说 Codex 的强项，全栈能力，就比如说 Computer Use 可以让它能操作整个 macOS 系统，更关键的是，不断重置额度，根本用不完。

我从200刀切到100刀后仍然用不完。

但不得不说，Codex的文本能力就是狗屎。

不及 4o 的十分之一。

每次看，每次恶心。

## ending

Codex 这次更新，硬生生把一个写代码的工具推到了超级 APP的高度。

Computer Use 让它能操作你的电脑，Memory让他记住你的喜好，Chronicle 让它知道你在屏幕上正在看什么。

说个大胆的判断，如果 Codex 这样进化下去，没准会 激发另外一个产品的生命力，那就是 IntelliJ IDEA。

直接让 Codex 在后台操控 IDE debug，我们只需要在关键节点做决策就行。

不错不错。