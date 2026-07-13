---
title: "11万 Star ! 告别传统UI框架，强烈推荐这个看得见，好维护，AI友好的全新一代 UI 库"
source: "https://mp.weixin.qq.com/s/JcnfRas6xtHUM_27w0kQRQ"
---
小锋 java1234 *2026年7月11日 09:06*

大家好，我是锋哥。

今天分享一个非常不错的开源项目 - shadcn/ui

![图片](assets/11%E4%B8%87%20Star%20!%20%E5%91%8A%E5%88%AB%E4%BC%A0%E7%BB%9FUI%E6%A1%86%E6%9E%B6%EF%BC%8C%E5%BC%BA%E7%83%88%E6%8E%A8%E8%8D%90%E8%BF%99%E4%B8%AA%E7%9C%8B%E5%BE%97%E8%A7%81%EF%BC%8C%E5%A5%BD%E7%BB%B4%E6%8A%A4%EF%BC%8CAI%E5%8F%8B%E5%A5%BD%E7%9A%84%E5%85%A8%E6%96%B0%E4%B8%80%E4%BB%A3%20UI%20%E5%BA%93/68bf375588ab7f35b14de04fda5b813c_MD5.webp)

---

## 目录

- 一、它到底是什么？
- 二、为什么和传统 UI 库不一样？
- 三、核心设计理念
- 四、技术栈与组件生态
- 五、使用流程一览
- 六、快速上手示例

---

## 一、它到底是什么？

一句话概括： **shadcn/ui 不是那种「装个 npm 包就能用」的传统组件库，而是一套帮你把漂亮、好用的组件源码直接放进自己项目里的工具和方法。**

官网有一句很直白的话：

> This is not a component library. It is how you build your component library.（这不是一个组件库，而是你搭建自己组件库的方式。）

所以，别把它想成 Material UI 或 Ant Design 那种「黑盒依赖」。你装下来的每一个按钮、对话框、表单， **源码都在你的项目里** ，想改样式、改逻辑，直接打开文件改就行。

![图片](assets/11%E4%B8%87%20Star%20!%20%E5%91%8A%E5%88%AB%E4%BC%A0%E7%BB%9FUI%E6%A1%86%E6%9E%B6%EF%BC%8C%E5%BC%BA%E7%83%88%E6%8E%A8%E8%8D%90%E8%BF%99%E4%B8%AA%E7%9C%8B%E5%BE%97%E8%A7%81%EF%BC%8C%E5%A5%BD%E7%BB%B4%E6%8A%A4%EF%BC%8CAI%E5%8F%8B%E5%A5%BD%E7%9A%84%E5%85%A8%E6%96%B0%E4%B8%80%E4%BB%A3%20UI%20%E5%BA%93/1e4ba440ae43fd5db81d11013592e0f5_MD5.webp)

---

## 二、为什么和传统 UI 库不一样？

传统 UI 库的典型用法是这样的：

1. `npm install xxx-ui`
2. 从包里 `import { Button } from 'xxx-ui'`
3. 想深度定制时，往往要和组件提供的 props、主题变量较劲

shadcn/ui 换了一条路：

1. 在项目里运行 CLI 命令
2. 组件源码被复制到 `components/ui/` 目录
3. 从此这个组件 **属于你** ，和普通业务代码没区别

这种方式的好处很实在：

- **看得见** ：组件怎么写的，一目了然
- **改得动** ：不用和库的封装层斗智斗勇
- **好维护** ：团队可以按自己的设计规范慢慢演进
- **AI 友好** ：代码在本地，AI 助手也更容易读懂和帮你改
![图片](assets/11%E4%B8%87%20Star%20!%20%E5%91%8A%E5%88%AB%E4%BC%A0%E7%BB%9FUI%E6%A1%86%E6%9E%B6%EF%BC%8C%E5%BC%BA%E7%83%88%E6%8E%A8%E8%8D%90%E8%BF%99%E4%B8%AA%E7%9C%8B%E5%BE%97%E8%A7%81%EF%BC%8C%E5%A5%BD%E7%BB%B4%E6%8A%A4%EF%BC%8CAI%E5%8F%8B%E5%A5%BD%E7%9A%84%E5%85%A8%E6%96%B0%E4%B8%80%E4%BB%A3%20UI%20%E5%BA%93/37801012603aeeb154833d5b124adc0b_MD5.jpg)

---

## 三、核心设计理念

这个UI库的核心设计理念主要有以下5点：

### 1\. 开放代码（Open Code）

组件不是藏在 node\_modules 里的黑盒，而是实实在在的 `.tsx` 文件。你拥有它，也负责它。

### 2\. 可组合（Composition）

各个组件的用法和结构比较统一，拼在一起不别扭，学习成本相对低。

### 3\. 可分发（Distribution）

通过一套 schema 和 CLI 工具，把组件「分发」到不同项目里，还能对接社区注册表（Registry）。

### 4\. 好看又好用（Beautiful Defaults）

默认样式已经挺讲究了，不想折腾设计的人可以直接用；想折腾的人也有足够空间。

### 5\. 为 AI 时代准备（AI-Ready）

组件源码在本地、结构清晰，对 AI 编程助手、v0 这类工具都很友好——它们能读、能改、能帮你拼页面。

---

## 四、技术栈与组件生态

shadcn/ui 站在几个成熟方案的肩膀上：

- **React** ：组件基于 React 编写
- **Tailwind CSS** ：样式主要靠工具类完成，改起来直观
- **Radix UI** ：负责无障碍、键盘交互、弹层行为等底层能力
- **TypeScript** ：类型支持完善，开发体验舒服

常见组件包括：Button、Card、Dialog、Form、Table、Tabs、Toast 等，基本覆盖了后台系统、官网、SaaS 产品的大部分界面需求。

另外，它还支持多种框架场景（如 [Next.js、Vite](http://next.xn--jsvite-jr3e/) 等），并持续扩展对更多技术栈的适配。

---

## 五、使用流程一览

下面展示下从「发现组件」到「在项目中使用」的大致流程：

![图片](assets/11%E4%B8%87%20Star%20!%20%E5%91%8A%E5%88%AB%E4%BC%A0%E7%BB%9FUI%E6%A1%86%E6%9E%B6%EF%BC%8C%E5%BC%BA%E7%83%88%E6%8E%A8%E8%8D%90%E8%BF%99%E4%B8%AA%E7%9C%8B%E5%BE%97%E8%A7%81%EF%BC%8C%E5%A5%BD%E7%BB%B4%E6%8A%A4%EF%BC%8CAI%E5%8F%8B%E5%A5%BD%E7%9A%84%E5%85%A8%E6%96%B0%E4%B8%80%E4%BB%A3%20UI%20%E5%BA%93/ffd6344d8c0e0973129e657d9ed51356_MD5.png)

整个过程不复杂，本质上就是： **挑组件 → 拉源码 → 自己掌控** 。

---

## 六、快速上手示例

假设你已经有一个 React / [Next.js](http://next.js/) 项目，大致步骤如下。

**第一步：初始化**

```
npx shadcn@latest init
```

CLI 会问你用哪种风格、主题色、路径别名等，按提示选就行。

**第二步：添加组件**

比如想要一个按钮组件：

```
npx shadcn@latest add button
```

执行完后，项目里会出现类似 `components/ui/             button.tsx           ` 的文件。

**第三步：在页面里使用**

```javascript
import { Button } from "@/components/ui/button"
export default function Page() {  return <Button>点击我</Button>}
```

就这么简单。后续如果想把按钮改成圆角、加图标、换配色，直接改 `              button.tsx            ` 里的 Tailwind 类名即可。

---

**项目仓库：** [https://github.com/shadcn-ui/ui](https://github.com/shadcn-ui/ui)

[最近，锋哥又开始收Java+AI大模型编程学员了！](https://mp.weixin.qq.com/s?__biz=MzIxNTAwNjA4OQ==&mid=2247571719&idx=1&sn=8a19d877e40d49d46ce3637575bb7403&scene=21#wechat_redirect)