---
title: "用 Solon AI ReActAgent 落地智能客服工单处理 - 带刺的坐椅"
source: "博客园"
url: "https://www.cnblogs.com/noear/p/21388621"
date: "2026-07-12T14:40:00Z"
score: 0.65
tags: ["编程", "中文", "技术"]
auto_captured: true
---

# 用 Solon AI ReActAgent 落地智能客服工单处理 - 带刺的坐椅

> **来源**: 博客园  
> **链接**: https://www.cnblogs.com/noear/p/21388621  
> **抓取日期**: 2026-07-12  
> **相关性评分**: 0.65

某电商平台售后工单日均 5,000+，人工处理有三个老大难：

痛点 | 表现 | 后果  
---|---|---  
响应慢 | 首响经常要等很久 | 客户满意度下降  
处理不一致 | 同样“丢件”，不同客服结果不同 | 投诉升级  
重复劳动 | 大量工单是同一类问题 | 人力被低价值查询占满  
  
**核心矛盾** ：工单量增速明显快于客服团队扩编速度。

## 一、业务方案

### 1.1 目标

  * 常见问题由 Agent 自动处理
  * 首响从分钟级降到秒级
  * 同类问题走同一套 SOP
  * 复杂 / 敏感工单自动转人工



### 1.2 流程对比
    
    
    改造前：
    客户提交工单 → 排队 → 客服人工查看 → 查订单 → 查物流 → 判断 → 回复
    
    改造后：
    客户提交工单 → Agent 秒级响应 → 自动查订单、查物流 → 自动判断 → 自动处理
    （无法处理时 → 转人工 + 附完整上下文）
    

## 二、技术落地（ReActAgent 实现）

### 2.1 模块结构
    
    
    com.example.csagent/
    ├── tools/
    │   ├── OrderTools.java            # 查询订单
    │   ├── LogisticTools.java         # 查询物流
    │   └── MarketingTools.java        # 申请退款/发券
    ├── hitl/
    │   └── HitlWebController.java     # 审批续传接口
    └── CSAgentApp.java                # 启动入口
    

### 2.2 工具定义（真实 API）

在 Solon AI 中，业务工具应继承 `AbsToolProvider`，方法上标注 `@ToolMapping`：
    
    
    import org.noear.solon.ai.annotation.ToolMapping;
    import org.noear.solon.ai.chat.tool.AbsToolProvider;
    import org.noear.solon.annotation.Param;
    
    /** 订单领域工具 */
    public class OrderTools extends AbsToolProvider {
        @ToolMapping(description = "根据订单号查询订单详情，获取商品名、金额、物流单号")
        public String get_order(@Param(description = "订单号") String orderId) {
            // 生产环境改为调用内部订单服务
            if ("ORD_20251229".equals(orderId)) {
                return "{\"orderId\":\"ORD_20251229\", \"amount\": 158.0, "
                        + "\"trackNo\": \"track_123\", \"sku\": \"智能耳机\"}";
            }
            return "{\"error\": \"订单不存在\"}";
        }
    }
    
    /** 物流领域工具 */
    public class LogisticTools extends AbsToolProvider {
        @ToolMapping(description = "根据物流单号查询当前运输状态")
        public String get_logistic_status(@Param(description = "物流单号") String trackNo) {
            if ("track_123".equals(trackNo)) {
                return "{\"status\": \"lost\", \"info\": \"包裹在上海分拨中心丢失\"}";
            }
            return "{\"error\": \"查无此单\"}";
        }
    }
    
    /** 营销/补偿领域工具 */
    public class MarketingTools extends AbsToolProvider {
        @ToolMapping(description = "根据赔付策略发放补偿。"
                + "规则：小额订单(<=100)发优惠券(coupon)；大额订单(>100)申请全额退款(refund)")
        public String apply_compensation(
                @Param(description = "赔付策略：coupon 或 refund") String strategy,
                @Param(description = "订单金额") double amount) {
            if ("refund".equals(strategy) && amount > 100) {
                return "【系统指令】已成功提交退款申请，金额 " + amount
                        + " 元预计 24 小时内原路退回。";
            } else if ("coupon".equals(strategy)) {
                return "【系统指令】已发放 20 元补偿优惠券至用户账户。";
            }
            return "【人工逻辑】赔付策略与金额不匹配，已转交人工客服审核。";
        }
    }
    

### 2.3 组装 ReActAgent
    
    
    import org.noear.solon.ai.agent.AgentSession;
    import org.noear.solon.ai.agent.react.ReActAgent;
    import org.noear.solon.ai.agent.session.InMemoryAgentSession;
    import org.noear.solon.ai.chat.ChatModel;
    
    ChatModel chatModel = LlmUtil.getChatModel();
    
    ReActAgent agent = ReActAgent.of(chatModel)
            .defaultToolAdd(new OrderTools())
            .defaultToolAdd(new LogisticTools())
            .defaultToolAdd(new MarketingTools())
            .modelOptions(o -> o.temperature(0.0)) // 决策场景建议低温
            .maxTurns(10)
            .autoRethink(true)
            .build();
    
    AgentSession session = InMemoryAgentSession.of("demo_customer_job_001");
    
    String userPrompt = "我的订单号是 ORD_20251229，到现在还没收到货，帮我查查怎么回事并给出处理方案。";
    
    String result = agent.prompt(userPrompt)
            .session(session)
            .call()
            .getContent();
    
    System.out.println(result);
    

Agent 会自主完成：

  1. `get_order` → 拿到物流单号 `track_123` 和金额 `158`
  2. `get_logistic_status` → 识别 `lost`
  3. `apply_compensation(strategy=refund, amount=158)` → 触发退款



### 2.4 业务 SOP 怎么写？

不要再写虚构的 `AiInterceptor` 路由表。正确做法是：

  1. **把 SOP 写进 system prompt**
  2. **把动作封装成工具** ，让 Agent 自己按规则调用


    
    
    ReActAgent agent = ReActAgent.of(chatModel)
            .systemPrompt(t -> """
                你是电商售后决策助手。处理规则：
                1. 先查订单，再查物流
                2. 若物流状态为 lost：
                   - 金额 <= 100：发优惠券
                   - 金额 > 100：申请全额退款
                3. 若已签收：引导客户联系邻居/快递员，不要直接退款
                4. 无法判断时说明原因并建议转人工
                """)
            .defaultToolAdd(new OrderTools())
            .defaultToolAdd(new LogisticTools())
            .defaultToolAdd(new MarketingTools())
            .build();
    

### 2.5 人工升级兜底（HITL）

金额超过阈值时，用官方 `HITLInterceptor` 暂停执行：
    
    
    import org.noear.solon.ai.agent.react.intercept.HITLInterceptor;
    import org.noear.solon.ai.agent.react.intercept.HITL;
    import org.noear.solon.ai.agent.react.intercept.HITLDecision;
    import org.noear.solon.ai.agent.react.intercept.HITLTask;
    
    HITLInterceptor hitl = new HITLInterceptor()
            .onTool("apply_compensation", (trace, args) -> {
                double amount = Double.parseDouble(args.get("amount").toString());
                return amount > 100 ? "大额赔付需人工审核" : null; // null = 放行
            });
    
    ReActAgent agent = ReActAgent.of(chatModel)
            .defaultToolAdd(new OrderTools())
            .defaultToolAdd(new LogisticTools())
            .defaultToolAdd(new MarketingTools())
            .defaultInterceptorAdd(hitl)
            .build();
    

审批提交与续传（对齐 article/1286）：
    
    
    HITLTask task = HITL.getPendingTask(session);
    
    if ("approve".equals(action)) {
        HITL.submit(session, task.getToolName(),
                HITLDecision.approve().comment("管理员已核实"));
    } else {
        HITL.submit(session, task.getToolName(),
                HITLDecision.reject("风险操作，已被管理员驳回"));
    }
    
    // 提交后静默续传
    ReActResponse resp = agent.prompt().session(session).call();
    

## 三、业务效果（定性）

上线后常见变化：

  * **自动链路** ：查单 → 定位问题 → 标准赔付，秒级完成
  * **人工链路** ：大额/异常单由 AI 备好上下文，人只做确认
  * **一致性** ：同一类问题按统一规则处理，减少“看人下菜”



> 不在此编造具体百分比。真实数据请以你们线上埋点为准。

### 真实处理示例

> **客户** ：“我的订单号是 ORD_20251229，到现在还没收到货”
> 
> **Agent 处理链路** ：
> 
>   1. `get_order("ORD_20251229")` → 金额 158，物流单号 track_123
>   2. `get_logistic_status("track_123")` → lost
>   3. 金额 > 100 → 触发 `apply_compensation(refund, 158)`
>   4. 若已配 HITL，则先挂起审批，管理员点“批准”后继续
> 


## 四、同类场景扩展

业务场景 | 不同工具 | 不同规则 | 兜底条件  
---|---|---|---  
保险理赔 | 保单查询、定损 | 不同险种流程 | 金额超阈值  
物流投诉 | 运单追踪、赔偿计算 | 延误/破损/丢件 | 赔偿超阈值  
物业报修 | 工单系统、维修派单 | 紧急/普通/预约 | 漏水/断电  
酒店客服 | 预订查询、退款 | 取消/投诉/加订 | 升级值班经理  
银行信用卡 | 账单查询、挂失 | 盗刷/降额/提额 | 账户安全相关  
  
## 五、落地建议

  1. **从高频低价值工单开始** ：查物流、查订单先跑通
  2. **HITL 阈值从宽到严** ：初期退款全审批，再逐步放宽
  3. **SOP 写进 prompt + 工具描述** ：不要虚构拦截器路由
  4. **保留“转人工”底线** ：客户明确要求时立即升级



## 参考

  * [react - 示例2 - 电商售后智能决策](<https://solon.noear.org/article/1285>)
  * [react - 示例3 - 人工介入（HITL）](<https://solon.noear.org/article/1286>)
  * [react - ReActAgent 像人类一样思考与行动](<https://solon.noear.org/article/1282>)




---
> 原文链接: https://www.cnblogs.com/noear/p/21388621