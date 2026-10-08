---
title: "从一句话需求到可运营网站：WorkBuddy 建站工作流实录"
source: "人人都是产品经理"
url: "https://www.woshipm.com/ai/6473412.html"
date: "Sat, 03 Oct 2026 04:43:37 +0000"
score: 1.0
tags: ["产品经理", "AI产品", "Agent", "中文"]
auto_captured: true
---

# 从一句话需求到可运营网站：WorkBuddy 建站工作流实录

> **来源**: 人人都是产品经理  
> **链接**: https://www.woshipm.com/ai/6473412.html  
> **抓取日期**: 2026-10-03  
> **相关性评分**: 1.0

> 从一句模糊需求到完整外贸B2B官网落地，本文以Lumicore灯饰站点为例，拆解专家团协作、MCP连接、四阶段SOP及关键避坑点。无论你是想复现建站流程，还是优化AI协作效率，这份实操指南都值得收藏。

![](https://image.woshipm.com/2023/04/14/d9c0bc28-da8e-11ed-a86f-00163e0b5ff3.jpg)

一句话需求 → 专家团协作 → 真实站点落地。本文以「Lumicore Optoelectronics 外贸 B2B 灯饰官网」为例，拆解从需求到上线的完整节点、工具调用与踩坑修复，可直接照做。

## 一、需求起点：一句”随意”的话

用户的原始需求只有一句话：

> 「帮我创建一个灯饰的品牌官网，外贸 B2B 询盘类型的，页面需要的图片和产品以及新闻、询盘，你按照需求自行处理补充。」

这句话信息量很大，但留白也很大——**品牌名、语言、页面清单、产品/新闻内容、配图来源、询盘表单怎么绑** ，全部需要补全。这正是「可运营网站」与工作流的价值所在：把模糊需求结构化为可执行、可验收的交付。

**要点：** 遇到”自行补充”类需求，不要闷头瞎猜，也不要逐条追问打断节奏。正确做法是——先按行业最佳实践给出**假设清单** ，在动手前用一次确认收口，既尊重用户授权，又保留 AI 补全的发挥空间。

## 二、谁在做：专家团 + 连接器架

本任务由 **「云指建站运营专家团」** 承接。它不是一个人在写代码，而是一套标准协作机制：

![](https://image.woshipm.com/2026/10/02/bbcfc872-be64-11f1-8a75-00163e4b86a1.png)

### 2.1 找到建站专家团

![](https://pica.zhimg.com/v2-2cb244afbf5f9427b95413b78bc8f3bc_1440w.jpg)

### 2.2 链接通过id和token链接mcp

![](https://pic1.zhimg.com/v2-1adfbfa96e9a1dec98f13f07ce302772_1440w.jpg)

### 2.3 获取建站后台的站点id和token

![](https://pic1.zhimg.com/v2-846cc541bbb684b66a74993d931a4bb0_1440w.jpg)

![](https://pic4.zhimg.com/v2-f37960b10735aad0728282b90c0852f9_1440w.jpg)

![](https://pic1.zhimg.com/v2-d7d7215683344eb14eab3a0515785cbc_1440w.jpg)

![](https://pic4.zhimg.com/v2-a14300122bf443e9cc993922f200076b_1440w.jpg)

### 2.4 填入获取到的id和token 链接mcp

![](https://pica.zhimg.com/v2-1b816292bb1b3b4c8028eb1a53817080_1440w.jpg)

## 三、工作流总览（四阶段 SOP）

**【阶段 0】澄清与建团** — 定目标、建团队、通报上下文

**【阶段 1】路由与调度** — 按类型派单、下发子任务

**【阶段 2】连接确认** — test 站点、核对现状

**【阶段 3】落地与收尾** — 专家执行、主理人核对、上线

本次是**复合型任务（新建整站）** ，主路由给「建站专家」一次跑完，SEO/GEO/获客作为后续可接力的阶段。动线上站点前，**阶段 2 的连接确认是铁律** 。

### 阶段 0 · 澄清与建团

**4.1 先确认连接器连通**

调用 yunzhi-mcp.test 做健康检查（回显通过即说明连接器在线）。它只回显文本、不含站点信息，所以**真正确认”连的是哪个站点”要靠读真实数据** 。

**4.2 读取现状 + 建团**

主理人并行发起 6 次查询（get_site_seo / list_page / list_product_class / list_news_class / list_custom_form / get_enquiry_form_id），确认这是一个**全新空白站点** ：无页面、无分类、无新闻、无自定义表单，但系统已自动初始化一个在线询盘表单 72931。

随后主理人亲自 TeamCreate 建立团队 yunzhi-lumicore-b2b，向成员通报边界与上下文（严禁成员代建团队、严禁成员互相直连）。

**4.3 假设清单 + 一次确认**

基于”外贸 B2B 灯饰”最佳实践，主理人给出假设并请用户确认：

![](https://image.woshipm.com/2026/10/02/f23522e0-be64-11f1-bf4f-00163e4b86a1.png)

**铁律：** 联系页与询盘页的表单**必须是不同 ID** ，平台约束不允许两页共用同一表单。因此联系页需 add_custom_form 新建一个。

### 阶段 1 · 路由与调度

新建整站属于「建站专家」主责，主理人下发一份**自包含子任务** ：把已确认的站点状态、品牌设定、产品/新闻规划、表单绑定、全部平台约束一次性写清，专家据此独立执行，无需再回头追问。

子任务关键约束（直接决定成败，必须写进派单）：

  * **资源 ID 以实测为准** ：询盘表单直接用 72931，不要再调 get_enquiry_form_id；每步先用 list_* 核对 ID 再写，避免混用站点资源。
  * **Twig 1.3 约束** ：{% if %}/{% for %} 只能放在完整 HTML 元素外部，禁止写在标签属性或 <title> 内；保留逻辑用 <!—-> 包裹；标签属性规范闭合。
  * **资源 URL 函数** ：拼接域名用 {{ FnGetHost($type) }}（0=域名，1=协议+域名），当前完整 URL 用 {{ FnGetCurrentUrl() }}，站内链接用相对路径。
  * **公共头尾** ：若建模板页则用 {{ FnInclude($codePath) }} 嵌入，片段必须自包含（各自带 <style>+<script>），不含 <html> 壳。
  * **表单 JS 铁律** ：隐藏字段、AJAX 提交、文件上传、短信/邮箱/图形验证码、地区三级联动逻辑必须完整保留，禁止简化重写。



### 阶段 2 · 连接确认（动线上站点）

专家开工前再次 test 确认目标站点，并基于阶段 0 的空白站点现状开始写入。**关键提醒** ：本次连接的实际 SiteID 是 82572，与用户旧记忆里的 80676 不同——动线上站点一律以 MCP 实际返回的 SiteID 为准，不沿用旧记忆。

### 阶段 3 · 建站专家落地（核心实操）

建站专家按以下顺序在空白站点上从零搭建，每类资源先建后取 ID，再被后续步骤引用：

**7.1 公司信息**

edit_company_info 设置：站点名 Lumicore Optoelectronics、公司全称、邮箱 sales@lumicore-led.com、电话、广州地址等。页尾联系信息可读取系统值，也可直接写。

**7.2 产品分类（6 个一级，parentId=0）**

add_product_class 逐个创建，记录返回 ClassID：

![](https://image.woshipm.com/2026/10/02/096e1c50-be65-11f1-bf4f-00163e4b86a1.png)

**7.3 AI 配图 + 上传**

用 ImageGen 生成产品主图与新闻配图（产品图建议压缩为 WebP 节省生图额度），再通过 upload_product_image（产品图）和 upload_file（新闻图）上传，取回文件名用于后续绑定。

![](https://image.woshipm.com/2026/10/02/220fa530-be65-11f1-bf4f-00163e4b86a1.png)

![](https://image.woshipm.com/2026/10/02/220fa530-be65-11f1-bf4f-00163e4b86a1.png)

**7.4 上架产品（10 款）**

add_product 立即发布，按分类分配，mainImage 用上传返回的文件名原样传入。每款写 summary 与 content（JSON 多详情，含 Product Description + Specifications 表，参数含功率/光通量/色温/尺寸/CE RoHS 认证）。

![](https://image.woshipm.com/2026/10/02/4c11ab4e-be65-11f1-84ff-00163e4b86a1.png)

**7.5 新闻分类 + 5 篇新闻**

add_news_class 建 Company News (1)；add_news 发 5 篇（status=1），含配图、英文 HTML 正文、descriptor 摘要与 SEO 三项。示例 ArticleID：8806158–8806162。

**7.6 联系表单（独立自定义表单）**

add_custom_form 建 Contact Us，返回 FormID = 151453。字段用临时 ID 起步：公司名 / 联系人 / 邮箱(邮箱校验) / 电话 / 国家(国际地区) / 产品兴趣(下拉) / 留言。开启邮件通知至 sales@lumicore-led.com。

**7.7 页面构建（8 页）**

save_ai_page 逐页保存，设计系统统一：深海蓝 #0f3d5e + 琥珀金 #ffb400，移动端 1024/768 双断点 + 汉堡菜单。

![](https://image.woshipm.com/2026/10/02/795f24be-be65-11f1-8891-00163e4b86a1.png)

### 阶段 3 · 主理人独立核对（不要只信汇报）

专家说”全部建成”不等于真的建成。主理人独立发起核对，**不采信专家汇报，直接读真实数据** ：

  * list_page：8 个页面 ID 与专家汇报一致 ![✅](https://s.w.org/images/core/emoji/16.0.1/72x72/2705.png)
  * list_custom_form：联系表单 151453 存在 ![✅](https://s.w.org/images/core/emoji/16.0.1/72x72/2705.png)
  * list_product_class：6 个分类 ID 一致 ![✅](https://s.w.org/images/core/emoji/16.0.1/72x72/2705.png)
  * get_product_list(classId=0)：10 款全部存在、含 WebP 主图与 SEO ![✅](https://s.w.org/images/core/emoji/16.0.1/72x72/2705.png)
  * get_news_list：5 篇全部存在、含配图与 SEO ![✅](https://s.w.org/images/core/emoji/16.0.1/72x72/2705.png)
  * **分类绑定验证** ：get_product_list(classId=704427) 精确返回 2 款面板灯 → 证明产品已正确归属分类，产品中心按分类筛选可用 ![✅](https://s.w.org/images/core/emoji/16.0.1/72x72/2705.png)



**为什么这步不能省：** get_product_list(0) 返回的 ClassID 字段为空，若只信列表会误判”分类没绑上”。必须用具体 classId 反查验证，才能确认筛选功能真实可用。

## 四、可复用操作清单（Checklist）

照着这份清单，任何人都能复现一次标准建站：

![✅](https://s.w.org/images/core/emoji/16.0.1/72x72/2705.png) **建团前** ：调 test 确认连接器在线；并行 6 查询摸清站点现状（SEO/页/产品分类/新闻分类/自定义表单/询盘表单 ID）。

![✅](https://s.w.org/images/core/emoji/16.0.1/72x72/2705.png) **需求澄清** ：给出品牌/语言/页面/分类/内容/表单假设清单，动手前一次确认收口。

![✅](https://s.w.org/images/core/emoji/16.0.1/72x72/2705.png) **表单隔离** ：联系页与询盘页用不同表单 ID；询盘页用系统表单，联系页 add_custom_form 新建。

![✅](https://s.w.org/images/core/emoji/16.0.1/72x72/2705.png) **写顺序** ：公司信息 → 产品分类 → AI 配图上传 → 产品 → 新闻分类 → 新闻 → 联系表单 → 页面 → 设首页 → 清缓存。

![✅](https://s.w.org/images/core/emoji/16.0.1/72x72/2705.png) **资源 ID** ：每步先 list_* 核对 ID 再写；动线站点以 MCP 返回的 SiteID 为准，不沿用旧记忆。

![✅](https://s.w.org/images/core/emoji/16.0.1/72x72/2705.png) **Twig 1.3** ：控制语句放元素外；不写多重 |default；资源 URL 用 FnGetHost/FnGetCurrentUrl。

![✅](https://s.w.org/images/core/emoji/16.0.1/72x72/2705.png) **表单 JS** ：隐藏字段、AJAX、上传、验证码、地区联动全部保留，不简化。

![✅](https://s.w.org/images/core/emoji/16.0.1/72x72/2705.png) **结构化数据** ：详情页输出 JSON-LD（Product/NewsArticle）+ TDK + 唯一 H1 + 图片 alt。

![✅](https://s.w.org/images/core/emoji/16.0.1/72x72/2705.png) **独立核对** ：list_page/get_product_list/get_news_list 逐项验证；用具体 classId 反查确认分类绑定。

![✅](https://s.w.org/images/core/emoji/16.0.1/72x72/2705.png) **收尾** ：确认 isHome、clear_site_cache；告知用户实际 SiteID 与两点须知（公共头尾方案、站点 ID 确认）。

## 五、关键经验与避坑

  * **“自行补充”≠”随意发挥”** ：先假设、后确认，既快又稳，避免返工。
  * **复合任务单路由也能成** ：新建整站主路由给建站专家一次跑完，SEO/GEO/获客作为后续可接力阶段，不强行并行以免冲突。
  * **平台约束是硬边界** ：表单隔离、Twig 1.3、FnInclude 兼容性——这些在派单时写清，专家才不会踩坑。
  * **AI 配图要算额度** ：产品图压 WebP 可省 25–50 credits；新闻图另计 15–30 credits，提前知会用户。
  * **核对必须独立** ：列表接口字段可能为空，要用反查验证关键功能（分类筛选）。
  * **站点 ID 以实测为准** ：切换连接器/新会话后，旧记忆里的站点 ID 不可信。



## 六、结语

从一句”帮我建个灯饰官网”到 8 个页面、10 款产品、5 篇新闻、双表单询盘的真实站点上线，耗时约 35 分钟。真正的”可运营”不仅在于页面能打开，更在于：需求被结构化、资源 ID 可追溯、平台约束被遵守、交付被独立核对。这正是 WorkBuddy 建站工作流的价值——**把一次性的 AI 生成，变成可复盘、可复用、可接力的标准动作** 。

本文由 @艾特先生 原创发布于人人都是产品经理。未经作者许可，禁止转载

题图来自Unsplash，基于CC0协议


---
> 原文链接: https://www.woshipm.com/ai/6473412.html