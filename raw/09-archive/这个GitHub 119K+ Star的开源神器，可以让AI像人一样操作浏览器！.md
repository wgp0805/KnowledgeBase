---
title: "这个GitHub 119K+ Star的开源神器，可以让AI像人一样操作浏览器！"
source: "https://mp.weixin.qq.com/s/LXVNNSc27XDRwrXWY2SCFA"
---
冰v河 冰河技术 *2026年10月23日 07:45*

**大家好，我是冰河~~**

网页自动化最耗人的地方，往往不是业务逻辑，而是元素定位。页面结构一调整，class 改名、按钮换位置，原先写好的 CSS 选择器或 XPath 就可能整片失效。脚本跑不起来，时间都花在排查“第几步找不到元素”上，真正要验证的业务流程反而被挤到后面。

![图片](assets/%E8%BF%99%E4%B8%AAGitHub%20119K+%20Star%E7%9A%84%E5%BC%80%E6%BA%90%E7%A5%9E%E5%99%A8%EF%BC%8C%E5%8F%AF%E4%BB%A5%E8%AE%A9AI%E5%83%8F%E4%BA%BA%E4%B8%80%E6%A0%B7%E6%93%8D%E4%BD%9C%E6%B5%8F%E8%A7%88%E5%99%A8%EF%BC%81/421426250702d87a6f9b346c36997347_MD5.webp)

Browser-Use 想绕开这个循环。它在 GitHub 上的热度已经很高，Star 超过 119k。它的做法不是让开发者把点击步骤写得更细，而是把浏览器里的无障碍树交给大模型，让模型根据页面语义判断下一步该操作什么。

使用者用自然语言描述目标，Agent 自己去打开页面、找控件、填内容、翻页、截图，完成一整条操作链路。

## 它为什么能绕开选择器维护

传统自动化工具依赖固定的元素路径。页面只要动一点结构，路径就可能对不上。另一种常见方案是截图加视觉识别，让多模态模型看页面，但每轮都要处理图像，速度和调用成本都不低。

Browser-Use 走的是中间路线：读取浏览器原生的 Accessibility Tree。这棵树描述页面上有哪些按钮、输入框、链接，以及它们对应的文本语义，不依赖 CSS 样式和 class 名称。模型拿到的是一份结构化的页面说明，再结合任务目标决定操作顺序。

![图片](assets/%E8%BF%99%E4%B8%AAGitHub%20119K+%20Star%E7%9A%84%E5%BC%80%E6%BA%90%E7%A5%9E%E5%99%A8%EF%BC%8C%E5%8F%AF%E4%BB%A5%E8%AE%A9AI%E5%83%8F%E4%BA%BA%E4%B8%80%E6%A0%B7%E6%93%8D%E4%BD%9C%E6%B5%8F%E8%A7%88%E5%99%A8%EF%BC%81/1d63df38c3803f99062b1d6842c39293_MD5.webp)

它的底层可以分成三层：上层是 Python API，中间是 Rust 编写的高性能核心，底层由 Playwright 驱动浏览器。所以它并不是简单把 Playwright 包一层，而是把“元素定位”这件事从代码里转移到了模型推理里。

支持的模型也比较开放：OpenAI GPT 系列、Anthropic Claude、Gemini、Ollama 本地模型都可以接。项目还提供了针对浏览器任务优化的 BU 2.0 模型 ChatBrowserUse，官方说法是执行效率比通用模型有明显提升。实际选型时，可以先用自己熟悉的模型跑通，再决定是否换专用模型。

## 和常见方案比，取舍在哪里

硬编码选择器的方案执行可控、速度快，但页面改版后维护成本高。截图视觉方案不依赖 DOM 结构，却要反复处理图像，token 消耗和响应时间都会上去。Browser-Use 依靠无障碍树，既不完全绑前端样式，也不每步都走视觉，在稳定性和成本之间做了一个折中。

![图片](assets/%E8%BF%99%E4%B8%AAGitHub%20119K+%20Star%E7%9A%84%E5%BC%80%E6%BA%90%E7%A5%9E%E5%99%A8%EF%BC%8C%E5%8F%AF%E4%BB%A5%E8%AE%A9AI%E5%83%8F%E4%BA%BA%E4%B8%80%E6%A0%B7%E6%93%8D%E4%BD%9C%E6%B5%8F%E8%A7%88%E5%99%A8%EF%BC%81/40d9d42e78ded37b860c984cfb121d92_MD5.png)

它也不是没有短板。遇到结构复杂、动态渲染很强的页面，模型仍可能判断失误，结果取决于模型推理质量。所以它更适合作为传统自动化的补充，而不是在所有场景里替代 Selenium 或 Playwright。

高频、稳定、接口级测试，传统方案依旧有优势；页面经常改、任务偏一次性、希望非技术同学也能参与的场景，Browser-Use 更合适。

## 哪些事情可以交给它

很多网页没有开放 API，但人可以正常访问。让 AI 操作网页，相当于间接操作了这套系统。这个思路可以落到不少场景里。

测试人员可以用自然语言写 Web UI 冒烟、回归、表单校验和端到端流程。页面迭代后，不必逐条改元素定位；接入 CI/CD 后，可以无头后台执行，并保存截图或录像，方便失败排查。

办公场景里，批量填表、在线系统填报、信息检索整理都可以交给 Agent。把个人资料交给它，模型根据字段语义完成录入。电商场景可以做商品搜索、跨平台比价、加入购物车，直接走网页端，不必等平台接口。数据采集也可以模拟真人浏览，云端模式还带了反爬和验证码处理能力。

如果任务完成后需要通知或联动内部系统，可以注册自定义 Action。比如网页操作结束后发一封邮件，或者调用自有业务接口，把 Agent 和现有系统接起来。

## 安装：先确认 Python 版本

Browser-Use 要求 Python 3.11 及以上，版本不够会在装依赖时直接报错。可以先执行：

```
python --version
```

推荐用 uv 管理依赖，解析速度比 pip 快。安装步骤大致如下：

```
pip install uv
uv init
uv add browser-use
uv sync
uvx browser-use install
```

最后一条会安装 Playwright 需要的浏览器。然后在项目根目录建一个 `.env` 文件，按你使用的模型填写密钥。比如用官方云端能力：

```
BROWSER_USE_API_KEY="你的密钥"
```

如果用 OpenAI：

```
OPENAI_API_KEY="你的OpenAI密钥"
```

云端密钥需要到 [browser-use.com](http://browser-use.com/) 注册获取。装完后可以校验：

```
browser-use --version
```

能输出版本号就说明命令可用；如果提示找不到命令，关掉终端重新打开再试。

## 先用命令行跑一个任务

不想写代码时，可以直接在终端用自然语言下任务。适合临时验证想法，或者快速跑一次页面检查。

```
browser-use run "打开 
            https://example.com/login，输入账号
           demo，密码 demo123，点击登录，确认是否进入首页"
```

也可以让它截图：

```
browser-use screenshot "打开 
            https://example.com，把完整页面截图保存到
           output 目录"
```

如果手里有一批用例文本，可以批量执行：

```
browser-use run --file 
            test_cases.txt
```

## 放进 Python：从登录流程开始

命令行适合试水，真正接入业务还是用 Python API。下面是一个登录流程的示意，实际参数以当前版本文档为准：

```
import asyncio
import os

from dotenv import load_dotenv
from browser_use import Agent, Browser, ChatBrowserUse

load_dotenv()

asyncdef run_login_check():
    browser = Browser(
        headless=False,
        # use_cloud=True  # 需要处理反爬或验证码时可考虑云端浏览器
    )

    llm = ChatBrowserUse(
        api_key=
            os.getenv(
          "BROWSER_USE_API_KEY"),
        model="bu-2-0",
    )

    agent = Agent(
        task=(
            "打开 
            https://example.com/login，"
          
            "账号输入 demo，密码输入 demo123，点击登录。"
            "如果进入首页，返回成功；如果失败，返回页面上的错误提示。"
        ),
        llm=llm,
        browser=browser,
        verbose=True,
    )

    history = await 
            agent.run()
          
    print(
            history.final_result())
          

            asyncio.run(run_login_check())
```

如果页面比较复杂，可以打开视觉辅助：

```
from browser_use import Agent
from langchain_openai import ChatOpenAI
import asyncio

asyncdef run_shopping_flow():
    agent = Agent(
        task=(
            "完成一次商品购买流程："
            "打开电商网站，搜索手机；"
            "进入第一个商品详情；"
            "选择黑色、256GB；"
            "加入购物车并确认商品信息；"
            "进入结算页，填写收货地址；"
            "选择支付方式并确认跳转到支付页面。"
            "任意步骤失败时返回错误信息。"
        ),
        llm=ChatOpenAI(model="gpt-4o"),
        use_vision=True,
    )

    result = await 
            agent.run()
          
    print(
            result.final_result())
          

            asyncio.run(run_shopping_flow())
```

## 接进 CI：无头运行并保留录像

如果要放进 Jenkins、GitLab CI 这类流水线，建议无头执行，并打开录像，失败时方便回看。

```
import pytest
from browser_use import Agent, BrowserConfig

ci_browser_config = BrowserConfig(
    headless=True,
    keep_alive=False,
    save_recording=True,
)

@
            pytest.mark.asyncio
          
asyncdef test_homepage_core_modules():
    agent = Agent(
        task="打开首页，确认关键模块正常渲染，返回检查结果",
        browser_config=ci_browser_config,
        llm=ChatBrowserUse(),
    )

    result = await 
            agent.run()
          
    assert 
            result.success
           isTrue
```

## 自定义动作：任务结束后通知

Agent 完成网页操作后，可以调用自己注册的工具。比如发一封通知邮件：

```
from browser_use import Tools

tools = Tools()

@
            tools.action(description="任务完成后发送邮件通知")
          
def send_notify(content: str) -> str:
    return f"通知已发送，内容：{content}"

agent = Agent(
    task="完成网页任务后发送邮件通知我",
    llm=ChatBrowserUse(),
    browser=browser,
    tools=tools,
)
```

## 本地模式还是云端模式

本地开源模式是 MIT 协议，浏览器实例完全由自己控制，适合调试、内网系统和私有化场景，也不产生托管费用。但反爬、滑块验证码、代理这些事情要自己处理，高频访问时更容易被网站风控拦住。

云端模式提供托管浏览器，内置指纹伪装、代理轮换和验证码处理，适合生产环境。它还能复用登录 Profile，保留会话，不用反复写登录逻辑。新用户通常有免费额度，可以先试再决定。

一个比较稳的试用路径是：先用本地模式跑通一个熟悉的页面，确认任务描述和结果校验方式；如果目标站点风控明显，再切到云端模式验证。

## 几个容易踩的坑

Python 版本一定要达到 3.11，低版本会在依赖阶段报错。复杂动态页面可以打开 `use_vision=True` ，让模型结合视觉信息判断。任务描述要尽量写清楚，把校验条件、失败时返回什么、异常怎么处理都写进 task 文本，指令越明确，结果越稳定。

CI 里记得 `headless=True` ，并打开 `save_recording=True` 。本地模式如果高频访问，容易被目标网站拦截，必要时换云端 Stealth 浏览器。模型方面，浏览器任务可以优先试 BU 2.0 专用模型，再和通用模型做对比。

## 最后怎么选

Browser-Use 并没有让 Playwright 或 Selenium 失去意义。稳定、高频、接口级的自动化，传统硬编码仍然可靠。它补的是另一块：页面经常变、任务偏临时、希望用自然语言描述业务目标、不想把大量时间花在元素定位上的场景。

如果你的团队正被选择器维护拖住，或者有很多“网页没有 API 但人天天在用”的流程，可以先拿一个低风险任务试跑。重点不是让 AI 代替所有脚本，而是把关注点从“怎么点到这个按钮”挪回“这条业务到底要完成什么”。

项目地址： [https://github.com/browser-use/browser-use](https://github.com/browser-use/browser-use)

**好了，今天就到这儿吧，我是冰河，我们下期见~~**

推荐阅读：

[给大家推荐一款AI短剧生成平台](https://mp.weixin.qq.com/s?__biz=Mzg4MjU0OTM1OA==&mid=2247515806&idx=1&sn=6214e0ec2a9ebc09b1c68eb23e818eae&scene=21#wechat_redirect)

[给大家推荐一款可直接使用的AI-CR系统](https://mp.weixin.qq.com/s?__biz=Mzg4MjU0OTM1OA==&mid=2247515790&idx=1&sn=5aeda9e93df686b5e753cb9870fda0da&scene=21#wechat_redirect)

**微信扫一扫赞赏作者**

AI开源合集 · 目录

阅读原文