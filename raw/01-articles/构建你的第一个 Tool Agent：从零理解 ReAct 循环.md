---
title: "构建你的第一个 Tool Agent：从零理解 ReAct 循环"
source: "https://zyfcodes.blog.csdn.net/article/details/162310384"
---
**目录**

[一、为什么“一次工具调用”还不够？](#t0)

[（一）ReAct 模式要解决的问题](#t1)

[（二）本文要解决什么问题？](#t2)

[二、ReAct 是什么？](#t3)

[（一）简化版工作流引擎](#t4)

[（二）在 LangGraph 中，ReAct 怎么表示？](#t5)

[（三）create\_react\_agent 一行代码背后做了什么？](#t6)

[三、Demo：手写一个等价的 ReAct 循环](#t7)

[（一）关键代码演练](#t8)

[（二）工具定义：Agent 能使用哪些能力？](#t9)

[1\. 第一个是模拟搜索工具](#t10)

[2\. 第二个是计算工具](#t11)

[3\. 第三个是当前时间工具](#t12)

[（三）State：为什么 messages 是核心？](#t13)

[（四）agent 节点：同一个节点里完成“决策”和“收尾”](#t14)

[（五）tools 节点：执行工具，并把结果写回消息链](#t15)

[（六）条件边：如何判断继续还是结束？](#t16)

[（七）防止无限循环：必须有安全阀](#t17)

[（八）运行效果：看懂 ReAct 的“心电图”](#t18)

[演示 1: ReAct Agent 完整调用链](#t19)

[演示 2：工具自动选择](#t20)

[演示 3：最大迭代限制](#t21)

[四、常见坑与排查](#t22)

[（一）坑 1：Agent 陷入无限工具调用循环](#t23)

[（二）坑 2：工具描述重叠，Agent 选错工具](#t24)

[（三）坑 3：忘了把 ToolMessage 加回消息链](#t25)

[（四）坑 4：把 recursion\_limit 当成工具调用次数](#t26)

[五、工程化问题：从 Demo 到生产还差什么？](#t27)

[（一） 流式输出：不要让用户干等](#t28)

[（二）超时兜底：不要让一个工具拖死整个 Agent](#t29)

[（三）可观测性：必须记录完整调用链](#t30)

[（四）最小心智模型：记住这四句话](#t31)

[六、总结](#t32)

[下一篇预告](#t33)

---

干货分享，感谢您的阅读！

这是「LangGraph Agent Engineering Mastery」系列 Stage 2 的第二篇。  
读完本文，你会理解：ReAct 循环每一步在做什么、 `create_react_agent` 一行代码背后封装了什么，以及为什么 **2 个节点 + 1 条条件边** 就能撑起绝大多数 Tool Agent。

![](https://i-blog.csdnimg.cn/direct/0a0dfcd7cb5b4c83b8ad0441af03714f.png)

## 一、为什么“一次工具调用”还不够？

### （一）ReAct 模式要解决的问题

上一篇里，我们手写了一个能调用工具的 Graph。它已经能做到：

- 识别用户问题；
- 判断是否需要工具；
- 调用工具；
- 把结果返回给用户。

但它有一个隐藏前提： **用户的问题一步就能解决。** 现实中的 Agent 任务往往没这么简单。比如：

> 帮我查一下北京天气，再算一下如果气温每天涨 2 度，一周后是多少。

这个问题至少包含两步：

1. 先查北京今天的天气，拿到当前温度；
2. 再基于温度做计算，得到一周后的结果。

这两步之间有明确依赖关系： **第二步的输入来自第一步的输出。** 如果任务再复杂一点，Agent 可能还要继续判断：

- 查到的信息够不够？
- 要不要继续搜索？
- 要不要换一个工具？
- 工具结果是否需要进一步计算？
- 现在能不能给用户最终答案？

这就不再是“一次性函数调用”了，而是一个会反复决策的循环。这正是 ReAct 模式要解决的问题。

### （二）本文要解决什么问题？

Tool Agent 的核心不是“会调用工具”，而是 **会决定什么时候调用工具、调用哪个工具、调用几次，以及什么时候停止** 。

普通的 LLM 对话更像是：

```
用户输入 → 模型回复 → 结束
```

一次性工具调用更像是：

```
用户输入 → 模型决定工具 → 工具执行 → 模型回复 → 结束
```

而真正的 Agent 更像是：

```
用户输入

  → Agent 思考

  → 调工具

  → 观察结果

  → 再思考

  → 可能继续调工具

  → 直到信息足够

  → 最终回复
```

也就是说，Agent 的关键能力是： **多步决策 + 状态延续 + 循环控制。**

## 二、ReAct 是什么？

### （一）简化版工作流引擎

ReAct = **Reasoning + Acting** 。

它让 LLM 在“推理”和“行动”之间交替进行：

```
[Reasoning] 用户在问天气，我需要调用搜索工具

[Acting]    web_search("北京天气")

[Observe]   工具返回：晴，25°C，空气质量良好

[Reasoning] 信息已经足够，可以组织最终回复

[Answer]    北京今天晴，气温 25°C，空气质量良好
```

你可以把 ReAct 理解成一个简化版工作流引擎：

- LLM 是决策节点；
- 工具是执行节点；
- 工具返回结果后，流程回到 LLM；
- LLM 再判断下一步是继续行动，还是结束。

用后端系统类比，ReAct 很像一个带状态的任务编排器：

```python
while not done:

    decision = llm(state)

    if decision.need_tool:

        observation = tool(decision.args)

        state.append(observation)

    else:

        return decision.final_answer
python
```

这个循环看起来简单，但它正是 Tool Agent 能“做事”的核心。

### （二）在 LangGraph 中，ReAct 怎么表示？

LangGraph 最擅长表达这种“带状态的循环流程”。一个最小可用的 ReAct Agent，本质上只需要：

- 一个 `agent` 节点；
- 一个 `tools` 节点；
- 一条条件边，用来判断是否继续调用工具。

结构如下：

![](https://i-blog.csdnimg.cn/direct/b0ef5070e49e4eaf9922165f0122746f.png)

这张图要重点看三件事：

1. **agent 节点负责决策：** 它读取当前 `messages` ，判断下一步是调用工具，还是直接回复。
2. **tools 节点负责执行：** 它不做复杂推理，只负责把 `tool_calls` 里的工具名和参数拿出来，执行对应工具，并把结果写回消息链。
3. **条件边负责循环控制：** 它检查最后一条 `AIMessage` 是否包含 `tool_calls` 。有，就去 `tools` ；没有，就结束。

所以，ReAct Agent 的图结构非常克制：

```cobol
2 个节点 + 1 条条件边
```

但这已经足够支撑大多数工具型 Agent。

### （三）create\_react\_agent 一行代码背后做了什么？

生产环境里，你通常不需要手写整个循环，可以直接使用 LangGraph 预置的封装：

```python
from langchain_core.tools import tool

from langchain_core.messages import HumanMessage

from langgraph.prebuilt import create_react_agent

 

@tool

def web_search(query: str) -> str:

    """在互联网上搜索信息。当用户询问实时信息、新闻或不确定的知识时使用。"""

    return search_api(query)

 

@tool

def calculator(expression: str) -> str:

    """计算数学表达式。当用户要求做数学计算时使用。"""

    return str(eval(expression))

 

agent = create_react_agent(llm, [web_search, calculator])

 

result = agent.invoke(

    {"messages": [HumanMessage("帮我查北京天气并换算成华氏度")]},

    config={"recursion_limit": 10},

)
python
```

这行代码看起来很轻：

```python
agent = create_react_agent(llm, [web_search, calculator])
python
```

但它内部大致帮你做了这些事：

1. 创建一个 `StateGraph` ；
2. 定义核心状态字段 `messages` ；
3. 把工具绑定到模型上；
4. 创建 `agent` 节点，让模型基于消息历史做决策；
5. 创建 `tools` 节点，用来执行模型生成的工具调用；
6. 添加条件边：如果最后一条消息有 `tool_calls` ，就进入工具节点；否则结束；
7. 工具执行完成后，把 `ToolMessage` 写回状态，并再次回到 `agent` 节点。

换句话说， `create_react_agent` 并不是魔法。它只是把我们本来要手写的 ReAct 图结构封装好了。

## 三、Demo：手写一个等价的 ReAct 循环

### （一）关键代码演练

为了理解黑盒内部，本文 Demo 没有一上来就依赖封装，而是手写了一个等价结构。

```python
"""Demo 02: Tool Agent — 完整的 ReAct 工具调用循环。

演示：

1. 使用 create_react_agent 快速构建 Tool Agent

2. 手动构建等价的 ReAct 循环（理解内部原理）

3. 完整的搜索工具调用链（LLM 决策 → 工具执行 → 结果整合）

4. 输出完整的中文调用链日志

运行方式：

    python stages/stage2_tool_calling/02_tool_agent/main.py

"""

 

from __future__ import annotations

 

import sys

from pathlib import Path

from typing import Annotated, TypedDict

 

from langchain_core.messages import (

    AIMessage,

    BaseMessage,

    HumanMessage,

    ToolMessage,

)

from langchain_core.tools import tool

from langgraph.graph import END, START, StateGraph

from langgraph.graph.message import add_messages

 

str

 

from shared import get_logger, log_error, log_step, log_success, log_warning

 

logger = get_logger("demo.02_tool_agent")

 

 

# ============================================================

# 工具定义：模拟搜索引擎和知识库

# ============================================================

@tool

def web_search(query: str) -> str:

    """在互联网上搜索信息。当用户询问实时信息、新闻或不确定的知识时使用。

    Args:

        query: 搜索关键词

    """

    search_results = {

        "北京天气": "北京今日天气：晴，气温 25°C，空气质量良好",

        "python最新版本": "Python 3.12.4 于 2024 年 6 月发布，主要改进包括性能优化和错误消息增强",

        "langgraph": "LangGraph 是 LangChain 团队推出的 Agent 编排框架，支持有状态图执行",

    }

    for key, value in search_results.items():

        if key in query.lower():

            return value

    return f"搜索 '{query}' 的结果：未找到相关信息，请尝试更具体的关键词。"

 

 

@tool

def calculator(expression: str) -> str:

    """计算数学表达式的结果。当用户要求做数学计算时使用。

    Args:

        expression: 数学表达式，如 "2 + 3 * 4"

    """

    try:

        allowed_chars = set("0123456789+-*/.() ")

        if not all(c in allowed_chars for c in expression):

            return "错误：表达式包含不允许的字符"

        result = eval(expression)

        return f"{expression} = {result}"

    except Exception as e:

        return f"计算错误：{e}"

 

 

@tool

def get_current_time() -> str:

    """获取当前时间。当用户询问现在几点或当前时间时使用。"""

    from datetime import datetime

 

    now = datetime.now()

    return f"当前时间：{now.strftime('%Y年%m月%d日 %H:%M:%S')}"

 

 

# ============================================================

# 状态定义

# ============================================================

class AgentState(TypedDict):

    messages: Annotated[list[BaseMessage], add_messages]

    tool_call_count: int

 

 

# ============================================================

# 手动构建 ReAct Agent（演示内部原理）

# ============================================================

MAX_ITERATIONS = 5

 

 

def build_react_agent(tools: list | None = None):

    """手动构建一个 ReAct Agent，模拟 create_react_agent 的内部结构。"""

    if tools is None:

        tools = [web_search, calculator, get_current_time]

 

    tool_map = {t.name: t for t in tools}

    tool_descriptions = "\n".join(

        f"- {t.name}: {t.description}" for t in tools

    )

 

    def agent_node(state: AgentState) -> dict:

        """Agent 节点 — 模拟 LLM 的推理和决策过程。"""

        messages = state["messages"]

        last_msg = messages[-1]

        call_count = state.get("tool_call_count", 0)

 

        if call_count >= MAX_ITERATIONS:

            log_warning(logger, f"达到最大迭代次数 ({MAX_ITERATIONS})，强制终止")

            return {

                "messages": [

                    AIMessage(content="抱歉，工具调用次数已达上限，请简化您的问题。")

                ],

                "tool_call_count": call_count,

            }

 

        if isinstance(last_msg, ToolMessage):

            tool_result = last_msg.content

            log_step(logger, "Agent 推理", f"工具返回结果: '{tool_result[:50]}'")

            log_step(logger, "Agent 决策", "已获得所需信息，生成最终回复")

            return {

                "messages": [

                    AIMessage(content=f"根据查询结果，{tool_result}")

                ],

                "tool_call_count": call_count,

            }

 

        content = str(last_msg.content).lower() if hasattr(last_msg, "content") else ""

        log_step(logger, "Agent 推理", f"分析用户问题: '{last_msg.content}'")

 

        if "天气" in content:

            city = "北京"

            for c in ["北京", "上海", "广州", "深圳"]:

                if c in content:

                    city = c

                    break

            log_step(logger, "Agent 决策", f"需要搜索 '{city}天气'")

            return {

                "messages": [

                    AIMessage(

                        content="",

                        tool_calls=[{

                            "id": f"call_search_{call_count}",

                            "name": "web_search",

                            "args": {"query": f"{city}天气"},

                        }],

                    )

                ],

                "tool_call_count": call_count + 1,

            }

        elif "计算" in content or "+" in content or "-" in content or "*" in content:

            expr = "".join(c for c in content if c in "0123456789+-*/.() ")

            if not expr.strip():

                expr = "2 + 3 * 4"

            log_step(logger, "Agent 决策", f"需要计算: '{expr.strip()}'")

            return {

                "messages": [

                    AIMessage(

                        content="",

                        tool_calls=[{

                            "id": f"call_calc_{call_count}",

                            "name": "calculator",

                            "args": {"expression": expr.strip()},

                        }],

                    )

                ],

                "tool_call_count": call_count + 1,

            }

        elif "时间" in content or "几点" in content:

            log_step(logger, "Agent 决策", "需要获取当前时间")

            return {

                "messages": [

                    AIMessage(

                        content="",

                        tool_calls=[{

                            "id": f"call_time_{call_count}",

                            "name": "get_current_time",

                            "args": {},

                        }],

                    )

                ],

                "tool_call_count": call_count + 1,

            }

        elif "搜索" in content or "查" in content:

            query = content.replace("搜索", "").replace("查一下", "").replace("帮我查", "").strip()

            if not query:

                query = "langgraph"

            log_step(logger, "Agent 决策", f"需要搜索: '{query}'")

            return {

                "messages": [

                    AIMessage(

                        content="",

                        tool_calls=[{

                            "id": f"call_search_{call_count}",

                            "name": "web_search",

                            "args": {"query": query},

                        }],

                    )

                ],

                "tool_call_count": call_count + 1,

            }

        else:

            log_step(logger, "Agent 决策", "不需要工具，直接回复")

            return {

                "messages": [

                    AIMessage(

                        content=f"你好！我是一个配备了搜索和计算工具的 AI 助手。\n"

                        f"我可以帮你：\n"

                        f"可用工具：\n{tool_descriptions}"

                    )

                ],

                "tool_call_count": call_count,

            }

 

    def tool_executor_node(state: AgentState) -> dict:

        """工具执行节点 — 执行 LLM 选择的工具并返回结果。"""

        messages = state["messages"]

        last_msg = messages[-1]

 

        tool_messages = []

        if hasattr(last_msg, "tool_calls") and last_msg.tool_calls:

            for tc in last_msg.tool_calls:

                tool_name = tc["name"]

                tool_args = tc["args"]

                tool_id = tc["id"]

 

                log_step(logger, "工具执行", f"🔧 {tool_name}({tool_args})")

 

                if tool_name in tool_map:

                    try:

                        result = tool_map[tool_name].invoke(tool_args)

                        log_success(logger, f"工具 {tool_name} → {result}")

                    except Exception as e:

                        result = f"工具执行失败: {e}"

                        log_error(logger, f"工具 {tool_name} 异常: {e}")

                else:

                    result = f"未知工具: {tool_name}"

                    log_error(logger, f"未注册的工具: {tool_name}")

 

                tool_messages.append(

                    ToolMessage(content=str(result), tool_call_id=tool_id, name=tool_name)

                )

 

        return {"messages": tool_messages}

 

    def should_continue(state: AgentState) -> str:

        """路由判断：是否需要继续调用工具。"""

        messages = state["messages"]

        last_msg = messages[-1]

        if hasattr(last_msg, "tool_calls") and last_msg.tool_calls:

            return "tools"

        return "end"

 

    graph = StateGraph(AgentState)

    graph.add_node("agent", agent_node)

    graph.add_node("tools", tool_executor_node)

 

    graph.add_edge(START, "agent")

    graph.add_conditional_edges("agent", should_continue, {

        "tools": "tools",

        "end": END,

    })

    graph.add_edge("tools", "agent")

 

    return graph

 

 

# ============================================================

# 演示函数

# ============================================================

def demo_react_agent():

    """演示 1：手动构建的 ReAct Agent 执行完整调用链。"""

    print("\n--- 演示 1: ReAct Agent 完整调用链 ---\n")

 

    graph = build_react_agent()

    app = graph.compile()

 

    test_cases = [

        "今天北京天气怎么样？",

        "帮我计算 12 + 34 * 2",

        "现在几点了？",

        "搜索一下 langgraph 是什么",

    ]

 

    results = []

    for question in test_cases:

        print(f"\n  {'═' * 50}")

        print(f"  用户: {question}")

        print(f"  {'─' * 50}")

 

        result = app.invoke({

            "messages": [HumanMessage(content=question)],

            "tool_call_count": 0,

        })

 

        print("\n  调用链追踪:")

        for i, msg in enumerate(result["messages"]):

            if isinstance(msg, HumanMessage):

                print(f"    [{i}] 👤 用户: {msg.content}")

            elif isinstance(msg, AIMessage):

                if msg.tool_calls:

                    for tc in msg.tool_calls:

                        print(f"    [{i}] 🤖 Agent 决定调用: {tc['name']}({tc['args']})")

                else:

                    print(f"    [{i}] 🤖 Agent 回复: {msg.content[:60]}")

            elif isinstance(msg, ToolMessage):

                print(f"    [{i}] 🔧 工具结果: {msg.content[:60]}")

 

        final = result["messages"][-1]

        print(f"\n  最终回复: {final.content}")

        results.append(result)

 

    return results

 

 

def demo_tool_selection():

    """演示 2：Agent 如何自动选择正确的工具。"""

    print("\n--- 演示 2: 工具自动选择 ---\n")

 

    graph = build_react_agent()

    app = graph.compile()

 

    scenarios = [

        ("查一下 python 最新版本", "web_search"),

        ("帮我算 100 / 4 + 25", "calculator"),

        ("现在几点了", "get_current_time"),

        ("你好啊", "无需工具"),

    ]

 

    results = []

    for question, expected_tool in scenarios:

        result = app.invoke({

            "messages": [HumanMessage(content=question)],

            "tool_call_count": 0,

        })

 

        actual_tool = "无需工具"

        for msg in result["messages"]:

            if isinstance(msg, AIMessage) and msg.tool_calls:

"name"

                break

 

        match = "✓" if actual_tool == expected_tool else "✗"

        print(f"  {match} 问题: '{question}'")

        print(f"    期望工具: {expected_tool} | 实际工具: {actual_tool}")

        results.append({"question": question, "tool": actual_tool, "match": match == "✓"})

 

    return results

 

 

def demo_max_iterations():

    """演示 3：最大迭代限制（防止无限循环）。"""

    print("\n--- 演示 3: 最大迭代限制 ---\n")

 

    graph = build_react_agent()

    app = graph.compile()

 

    result = app.invoke({

        "messages": [HumanMessage(content="帮我查天气")],

        "tool_call_count": 0,

    })

 

    print(f"  工具调用次数: {result['tool_call_count']}")

    print(f"  消息链长度  : {len(result['messages'])}")

    print(f"  最大迭代限制: {MAX_ITERATIONS}")

    log_success(logger, "Agent 在限制范围内完成任务")

 

    return result

 

 

def run_demo() -> dict:

    """运行 Tool Agent 全部演示。"""

    print("=" * 60)

    print("  Demo 02: Tool Agent — 完整的 ReAct 工具调用循环")

    print("=" * 60)

 

    results = demo_react_agent()

    selection = demo_tool_selection()

    iteration = demo_max_iterations()

 

    print()

    print("=" * 60)

    print("  关键概念回顾")

    print("=" * 60)

    print("  1. ReAct 模式  : Reasoning(推理) + Acting(行动) 交替执行")

    print("  2. Agent 节点  : LLM 分析问题，决定是否需要工具")

    print("  3. Tool 节点   : 执行 LLM 选择的工具，返回结果")

    print("  4. 路由函数    : 检查 AIMessage 是否包含 tool_calls")

    print("  5. 循环结构    : agent → tools → agent → ... → end")

    print("  6. 迭代限制    : max_iterations 防止无限循环")

    print("  7. 工具选择    : LLM 根据工具描述自动匹配最合适的工具")

    print()

 

    return {

        "react_results": results,

        "selection_results": selection,

        "iteration_result": iteration,

    }

 

 

if __name__ == "__main__":

    run_demo()
python
```

这个 Demo 做了四件事：

1. 定义工具： `web_search` 、 `calculator` 、 `get_current_time` ；
2. 定义状态： `messages` 和 `tool_call_count` ；
3. 定义 `agent` 节点：模拟 LLM 的推理和工具选择；
4. 定义 `tools` 节点：执行工具并返回 `ToolMessage` 。

运行方式：

```python
source .venv/bin/activate

python stages/stage2_tool_calling/02_tool_agent/main.py
python
```

### （二）工具定义：Agent 能使用哪些能力？

Demo 里定义了三个工具：

#### 1\. 第一个是模拟搜索工具

```python
@tool

def web_search(query: str) -> str:

    """在互联网上搜索信息。当用户询问实时信息、新闻或不确定的知识时使用。

    Args:

        query: 搜索关键词

    """

    search_results = {

        "北京天气": "北京今日天气：晴，气温 25°C，空气质量良好",

        "python最新版本": "Python 3.12.4 于 2024 年 6 月发布，主要改进包括性能优化和错误消息增强",

        "langgraph": "LangGraph 是 LangChain 团队推出的 Agent 编排框架，支持有状态图执行",

    }

    for key, value in search_results.items():

        if key in query.lower():

            return value

    return f"搜索 '{query}' 的结果：未找到相关信息，请尝试更具体的关键词。"
python
```

#### 2\. 第二个是计算工具

```python
@tool

def calculator(expression: str) -> str:

    """计算数学表达式的结果。当用户要求做数学计算时使用。

    Args:

        expression: 数学表达式，如 "2 + 3 * 4"

    """

    try:

        allowed_chars = set("0123456789+-*/.() ")

        if not all(c in allowed_chars for c in expression):

            return "错误：表达式包含不允许的字符"

        result = eval(expression)

        return f"{expression} = {result}"

    except Exception as e:

        return f"计算错误：{e}"
python
```

#### 3\. 第三个是当前时间工具

```python
@tool

def get_current_time() -> str:

    """获取当前时间。当用户询问现在几点或当前时间时使用。"""

    from datetime import datetime

 

    now = datetime.now()

    return f"当前时间：{now.strftime('%Y年%m月%d日 %H:%M:%S')}"
python
```

这里有一个非常重要的点： **工具的 docstring 不是注释，而是给 Agent 看的使用说明。** 真实 LLM 会根据这些描述判断：

- 什么时候该用这个工具；
- 参数应该怎么填；
- 这个工具和其他工具的边界在哪里。

所以，工具描述写得越清楚，Agent 选工具越稳定。

### （三）State：为什么 messages 是核心？

Demo 的状态定义如下：

```python
class AgentState(TypedDict):

    messages: Annotated[list[BaseMessage], add_messages]

    tool_call_count: int
python
```

这里有两个字段。第一个是 `messages` 。它保存整个对话和工具调用轨迹，例如：

```
HumanMessage: 用户问题

AIMessage: Agent 决定调用工具

ToolMessage: 工具返回结果

AIMessage: Agent 最终回复
```

第二个是 `tool_call_count` 。它用于记录工具调用次数，防止 Agent 陷入无限循环。这两个字段分别对应 ReAct Agent 的两个核心问题：

- `messages` 负责让 Agent “记得前面发生了什么”；
- `tool_call_count` 负责让系统“知道什么时候必须停下来”。

尤其要注意 `messages` 的 reducer：

```
messages: Annotated[list[BaseMessage], add_messages]
```

`add_messages` 表示新消息不是覆盖旧消息，而是追加到消息链后面。如果没有这个累加语义，工具结果就可能无法被下一轮 Agent 看到，ReAct 循环也就断了。

### （四）agent 节点：同一个节点里完成“决策”和“收尾”

ReAct 循环里最关键的节点就是 `agent_node` 。它要处理两种情况：

1. 如果上一条消息是用户问题，就判断要不要调用工具；
2. 如果上一条消息是工具结果，就观察结果并生成最终回复。

Demo 中的关键逻辑是：

```python
if isinstance(last_msg, ToolMessage):

    tool_result = last_msg.content

    log_step(logger, "Agent 推理", f"工具返回结果: '{tool_result[:50]}'")

    log_step(logger, "Agent 决策", "已获得所需信息，生成最终回复")

    return {

        "messages": [

            AIMessage(content=f"根据查询结果，{tool_result}")

        ],

        "tool_call_count": call_count,

    }
python
```

这段逻辑非常重要。

当 `agent` 节点发现最后一条消息是 `ToolMessage` ，说明工具刚刚执行完。此时 Agent 不应该再把它当成用户新问题处理，而应该进入“观察”阶段：

```
工具结果来了 → 读取结果 → 判断信息是否足够 → 组织最终回复
```

这就是 ReAct 中的 Observe。也就是说，同一个 `agent` 节点会根据最后一条消息的类型切换角色：

```cobol
HumanMessage → 进入决策模式

ToolMessage  → 进入观察/收尾模式
```

这也是 ReAct 循环能转起来的核心机关。

### （五）tools 节点：执行工具，并把结果写回消息链

工具节点的职责很单纯：

1. 读取最后一条 `AIMessage` ；
2. 找到其中的 `tool_calls` ；
3. 根据工具名找到对应工具；
4. 执行工具；
5. 把结果包装成 `ToolMessage` ；
6. 返回给 Graph，追加到 `messages` 。

核心逻辑如下：

```python
if hasattr(last_msg, "tool_calls") and last_msg.tool_calls:

    for tc in last_msg.tool_calls:

        tool_name = tc["name"]

        tool_args = tc["args"]

        tool_id = tc["id"]

 

        if tool_name in tool_map:

            try:

                result = tool_map[tool_name].invoke(tool_args)

            except Exception as e:

                result = f"工具执行失败: {e}"

        else:

            result = f"未知工具: {tool_name}"

 

        tool_messages.append(

            ToolMessage(content=str(result), tool_call_id=tool_id, name=tool_name)

        )

 

return {"messages": tool_messages}
python
```

这里最容易忽略的是： **工具结果必须以 `ToolMessage` 的形式写回 `messages` 。**

如果你只是打印了工具结果，但没有把它追加到状态里，下一轮 Agent 就看不到工具返回值。

那就会出现一个很典型的 Bug：

```
工具明明执行了，但最终回答完全没用上工具结果。
```

原因不是工具没跑，而是 Agent “失忆”了。

### （六）条件边：如何判断继续还是结束？

ReAct 循环的路由函数非常简单：

```python
def should_continue(state: AgentState) -> str:

    """路由判断：是否需要继续调用工具。"""

    messages = state["messages"]

    last_msg = messages[-1]

    if hasattr(last_msg, "tool_calls") and last_msg.tool_calls:

        return "tools"

    return "end"
python
```

判断标准只有一个：

```
最后一条 AIMessage 里有没有 tool_calls？
```

如果有，说明 Agent 决定继续行动：

```
agent → tools
```

如果没有，说明 Agent 已经给出了最终回复：

```
agent → END
```

这就是为什么 ReAct 图只需要一条条件边。

### （七）防止无限循环：必须有安全阀

只要系统里存在循环，就必须考虑失控问题。Agent 可能因为工具结果不明确、提示词不清楚、工具描述重叠等原因，反复调用同一个工具。

所以 Demo 中加了业务层的最大迭代限制：

```cobol
MAX_ITERATIONS = 5
```

并在 `agent_node` 开头检查：

```python
if call_count >= MAX_ITERATIONS:

    log_warning(logger, f"达到最大迭代次数 ({MAX_ITERATIONS})，强制终止")

    return {

        "messages": [

            AIMessage(content="抱歉，工具调用次数已达上限，请简化您的问题。")

        ],

        "tool_call_count": call_count,

    }
python
```

这是一层业务安全阀。生产中还应该同时设置框架层限制：

```python
result = agent.invoke(

    input,

    config={"recursion_limit": 10},

)
python
```

这两层限制解决的是不同问题：

| 限制 | 作用 |
| --- | --- |
| `tool_call_count` / `MAX_ITERATIONS` | 业务层限制，控制工具调用次数和成本 |
| `recursion_limit` | 框架层限制，防止 Graph 无限递归 |

建议两个都加，不要只依赖其中一个。

### （八）运行效果：看懂 ReAct 的“心电图”

![](https://i-blog.csdnimg.cn/direct/6f2e009e97e8486a8fd4c23e3f52dc0b.png)

#### 演示 1: ReAct Agent 完整调用链

运行 Demo 后，第一组输出如下：

```cobol
--- 演示 1: ReAct Agent 完整调用链 ---

 

  ══════════════════════════════════════════════════

  用户: 今天北京天气怎么样？

  ──────────────────────────────────────────────────

 

  调用链追踪:

    [0] 👤 用户: 今天北京天气怎么样？

    [1] 🤖 Agent 决定调用: web_search({'query': '北京天气'})

25

25

 

  最终回复: 根据查询结果，北京今日天气：晴，气温 25°C，空气质量良好
```

这段调用链就是 ReAct 循环的心电图：

```cobol
[0] HumanMessage

    用户提出问题

 

with

    Agent 判断需要调用 web_search

 

[2] ToolMessage

    tools 节点执行 web_search，并返回结果

 

[3] AIMessage

    Agent 观察工具结果，生成最终回复
```

从图执行路径看，它对应的是：

```sql
START → agent → tools → agent → END
```

注意， `agent` 走了两次。

第一次负责“决策”：  
用户问天气，所以调用搜索工具。

第二次负责“收尾”：  
工具结果已经回来，所以整合结果并回复用户。

这就是 ReAct 的核心节奏。

#### 演示 2：工具自动选择

第二组 Demo 用不同问题测试工具选择：

```cobol
--- 演示 2: 工具自动选择 ---

 

  ✓ 问题: '查一下 python 最新版本'

    期望工具: web_search | 实际工具: web_search

  ✓ 问题: '帮我算 100 / 4 + 25'

    期望工具: calculator | 实际工具: calculator

  ✓ 问题: '现在几点了'

    期望工具: get_current_time | 实际工具: get_current_time

  ✓ 问题: '你好啊'

    期望工具: 无需工具 | 实际工具: 无需工具
```

这说明 Agent 至少具备四种判断能力：

1. 用户问“查一下”，应该用搜索工具；
2. 用户问“算一下”，应该用计算工具；
3. 用户问“现在几点”，应该用时间工具；
4. 用户只是打招呼，不需要工具。

Demo 中为了便于教学，用规则模拟了这个判断过程。在真实 LLM Agent 中，这一步通常由模型根据工具 docstring 自主完成。所以，工具描述越准确，Agent 选工具越准。

#### 演示 3：最大迭代限制

第三组 Demo 验证最大迭代限制：

```cobol
--- 演示 3: 最大迭代限制 ---

 

  工具调用次数: 1

  消息链长度  : 4

  最大迭代限制: 5
```

这里虽然最大限制是 5，但实际只调用了 1 次工具。这说明 Agent 在一次工具调用后已经拿到了足够信息，于是正常结束，没有继续循环。这就是健康的 Agent 行为：

```
需要工具时调用工具；

信息够了就停止；

不要为了循环而循环。
```

## 四、常见坑与排查

### （一）坑 1：Agent 陷入无限工具调用循环

**现象：** Agent 反复调用同一个工具，日志不断刷屏，最后抛出 `GraphRecursionError` ，甚至造成 API 成本飙升。

**常见原因：**

- 工具返回内容太模糊；
- prompt 没有提醒模型“信息足够时应该停止”；
- 工具描述让模型误以为必须继续查；
- 上一轮工具结果没有正确写回 `messages` ；
- 模型对任务完成条件判断不稳定。

**解决方案：**

双保险：

```cobol
MAX_ITERATIONS = 5
```

配合：

```cobol
config={"recursion_limit": 10}
```

前者控制业务层工具调用次数，后者控制 Graph 执行层递归深度。

### （二）坑 2：工具描述重叠，Agent 选错工具

**现象：** 你有两个工具：

- `web_search`
- `db_query`

用户问“查一下用户订单”，Agent 却用了 `web_search` 。

**原因：** 工具描述边界太模糊。LLM 不知道“用户订单”属于内部业务数据，而不是互联网公开信息。

**解决方案：** 在 docstring 中明确适用和不适用场景：

```python
@tool

def db_query(table: str) -> str:

    """查询业务数据库。

    适用于：

    - 用户信息

    - 订单记录

    - 商品库存

    - 内部结构化数据

    不适用于：

    - 互联网公开信息

    - 实时新闻

    - 天气、汇率等外部实时数据

    如果用户询问公开信息，请使用 web_search。

    """
python
```

好的工具描述应该包含：

- 什么时候用；
- 什么时候不用；
- 参数怎么填；
- 和其他工具的边界是什么；
- 最好给一两个典型例子。

### （三）坑 3：忘了把 ToolMessage 加回消息链

**现象：** 工具执行成功了，日志里也能看到工具结果，但最终回复完全没用上。

**原因：** 工具结果没有以 `ToolMessage` 的形式追加到 `messages` 。错误心智模型是：

```cobol
工具执行了 = Agent 知道结果了
```

正确心智模型是：

```cobol
工具执行了 + ToolMessage 写回 messages = Agent 下一轮能看到结果
```

**解决方案：** 确保工具节点返回：

```kotlin
return {"messages": tool_messages}
```

并且 `messages` 使用 `add_messages` reducer：

```
messages: Annotated[list[BaseMessage], add_messages]
```

否则新消息可能覆盖旧消息，导致上下文断裂。

### （四）坑 4：把 recursion\_limit 当成工具调用次数

`recursion_limit` 限制的是 Graph 递归步数，不等同于工具调用次数。

一次完整的工具调用通常至少涉及：

```
agent → tools → agent
```

也就是多个图节点步骤。所以，如果你希望“最多调用 5 次工具”，不要只设置：

```cobol
config={"recursion_limit": 5}
```

更稳妥的方式是自己维护业务计数器：

```cobol
tool_call_count: int
```

然后在每次生成 `tool_calls` 时加一。

## 五、工程化问题：从 Demo 到生产还差什么？

Demo 主要用于理解 ReAct 结构。真实生产环境中，还要额外考虑几类问题。

![](https://i-blog.csdnimg.cn/direct/009896a7a31e4bbf86be0a76815d84c7.png)

### （一） 流式输出：不要让用户干等

ReAct Agent 可能会经历多轮工具调用：

```
正在搜索……

正在计算……

正在查询数据库……

正在整理结果……
```

如果整个过程都等到最后才返回，用户体验会很差。生产里建议使用：

```
agent.stream(...)
```

把中间状态实时推给前端，让用户知道 Agent 当前正在做什么。

### （二）超时兜底：不要让一个工具拖死整个 Agent

工具往往依赖外部系统：

- 搜索 API；
- 数据库；
- 内部 HTTP 服务；
- 第三方 SaaS；
- 文件解析服务。

任何一个工具超时，都可能卡住整个循环。建议设置两层超时：

| 超时类型 | 作用 |
| --- | --- |
| 单工具超时 | 防止某个工具一直不返回 |
| 全局任务超时 | 防止整个 Agent 会话执行太久 |

不要假设外部 API 永远稳定。

### （三）可观测性：必须记录完整调用链

Tool Agent 的问题通常不是“报错了”，而是：

```
它为什么这么做？
```

比如：

- 为什么选了这个工具？
- 为什么参数生成错了？
- 为什么工具返回后又继续调用？
- 为什么最终答案没有使用工具结果？

所以生产中必须记录完整 trace：

- 用户输入；
- 每轮 Agent 输出；
- 每次 tool\_calls；
- 工具参数；
- 工具耗时；
- 工具返回；
- 最终回复；
- 错误和重试信息。

可以接入：

- LangSmith；
- OpenTelemetry；
- 自研日志链路；
- APM 平台。

没有 trace 的 Agent，很难排查线上问题。

### （四）最小心智模型：记住这四句话

如果你只记本文最重要的内容，记住这四句话就够了：

1. **ReAct = 推理和行动交替循环。**
2. **agent 节点负责决策，tools 节点负责执行。**
3. **ToolMessage 必须写回 messages，否则 Agent 看不到工具结果。**
4. **所有循环都必须设置上限，否则迟早会失控。**

## 六、总结

Tool Agent 是连接 LLM 和外部世界的桥梁。

它不只是让模型“知道更多”，而是让模型具备“做事”的能力：

```
理解任务 → 选择工具 → 执行工具 → 观察结果 → 再次决策 → 最终回答
```

LangGraph 用一个非常简洁的图结构表达了这个过程：

```sql
START → agent → tools → agent → ... → END
```

看似只有两个节点和一条条件边，但它背后承载的是 Agent 最核心的执行模式：ReAct 循环。

理解了这套结构，你再看 `create_react_agent` 就不会觉得它是黑盒。它只是把这套循环封装成了一行代码。

### 下一篇预告

目前我们的工具参数都很简单：

但真实业务里的工具参数往往更复杂：

- 嵌套对象；
- 枚举值；
- 日期范围；
- 可选字段；
- 多参数组合；
- 执行前校验。

下一篇《自定义工具进阶：Pydantic Schema 让 LLM 精准调用》，我们会用 Pydantic 定义复杂参数 Schema，让 LLM 更稳定地生成工具参数，并在执行前自动完成校验。

**系列导航：** [LangGraph从零构建生产级 AI Agent 平台的递进式学习项目](https://blog.csdn.net/xiaofeng10330111/article/details/161660196?spm=1001.2014.3001.5501 "LangGraph从零构建生产级 AI Agent 平台的递进式学习项目")