---
title: "LangGraph Server Agent 框架本地部署指南 - lyshark"
source: "博客园"
url: "https://www.cnblogs.com/LyShark/p/22655620"
date: "2026-08-24T10:29:00Z"
score: 0.7
tags: ["编程", "中文", "技术"]
auto_captured: true
---

# LangGraph Server Agent 框架本地部署指南 - lyshark

> **来源**: 博客园  
> **链接**: https://www.cnblogs.com/LyShark/p/22655620  
> **抓取日期**: 2026-08-24  
> **相关性评分**: 0.7

本文讲解基于 LangGraph Server 服务搭建本地离线 AI Agent 的完整部署流程，适配 Windows 开发环境，全程无需调用公有大模型接口，实现纯本地化 AI 推理与工作流编排，帮助开发者快速搭建可调试、可复用的本地私有化 AI Agent 服务，适用于个人开发、本地功能调试、轻量化私有化 AI 场景落地。

需要特别区分的是，LangGraph 底层核心 Python 库采用 MIT 开源协议，可以永久免费使用，不存在运行额度限制；但教程中用到的 LangGraph Server 属于配套服务组件，即便采用本地自托管的 Lite 轻量模式，也受软件许可约束：每年最多提供 100 万次节点运行额度，该统计为工作流内部节点执行次数，不等同于接口请求次数。当年度节点执行量超出额度，按照许可要求，则需要升级购买企业版授权。

## LangGraph Server

1、本次部署仅安装运行 LangGraph Server 与 SDK 所需核心依赖，保证环境纯净无冗余、无版本冲突，采用清华源加速安装，适配 Windows 离线本地化部署。执行以下 CMD 命令安装核心组件。
    
    
    CMD> pip install -i https://mirrors.tuna.tsinghua.edu.cn/pypi/web/simple "langgraph-cli[inmem]"
    CMD> pip install -i https://mirrors.tuna.tsinghua.edu.cn/pypi/web/simple langgraph-sdk
    CMD> pip list
    Package                                  Version
    ---------------------------------------- -----------
    langchain                                1.3.15
    langgraph-api                            0.12.6
    langgraph-checkpoint                     4.2.0
    langgraph-cli                            0.4.31
    langgraph-prebuilt                       1.1.0
    langgraph-runtime-inmem                  0.32.6
    langgraph-sdk                            0.4.2
    langsmith                                0.11.0
    

2、为快速搭建标准化 LangGraph 项目结构，直接拉取官方开源模板项目，适配 LangGraph Server 运行规范。

打开 CMD 执行以下命令，克隆项目并进入项目根目录：
    
    
    CMD> git clone https://github.com/langchain-ai/new-langgraph-project
    CMD> cd new-langgraph-project
    CMD> pip install -e .
    

3、进入项目根目录，新建 `.env` 环境配置文件。Windows 系统无法直接右键创建/改名该文件，可通过 Sublime Text、VS Code 等编辑器直接新建保存。该文件用于配置本地大模型地址、项目标识，实现完全离线私有化调用。

文件配置内容如下，适配本地 llama.cpp 部署的大模型接口
    
    
    # To separate your traces from other application
    LANGSMITH_PROJECT=new-agent
    
    # Add API keys for connecting to LLM providers, data sources, and other integrations here
    OPENAI_API_KEY=dummy
    OPENAI_BASE_URL=http://127.0.0.1:11433/v1
    

4、为避免 Windows 编码乱码问题，先配置系统编码为 UTF-8，再启动 LangGraph 内存开发服务，内存模式专为本地调试、功能测试设计，支持代码热重载、可视化调试。

在项目根目录 CMD 中依次执行命令，其中测试环境可以使用`dev`，在编译环境则使用`build`部署
    
    
    CMD> set PYTHONUTF8=1
    CMD> set PYTHONIOENCODING=utf-8
    CMD> langgraph dev
    
    INFO:langgraph_api.cli:
            Welcome to
    ╦  ┌─┐┌┐┌┌─┐╔═╗┬─┐┌─┐┌─┐┬ ┬
    ║  ├─┤││││ ┬║ ╦├┬┘├─┤├─┘├─┤
    ╩═╝┴ ┴┘└┘└─┘╚═╝┴└─┴ ┴┴  ┴ ┴
    
    - API: http://127.0.0.1:2024
    - Studio UI: https://smith.langchain.com/studio/?baseUrl=http://127.0.0.1:2024
    - API Docs: http://127.0.0.1:2024/docs
    
    This in-memory server is designed for development and testing.
    For production use, please use LangSmith Deployment.
    

5、进入本地 llama.cpp 程序目录，执行启动命令，加载本地 GGUF 量化模型，开启 jinja 模板解析，保证与 LangGraph 服务正常消息交互，全程无公网调用。
    
    
    CMD> llama-server.exe -m qwen2.5-1.5b-instruct-q4_k_m.gguf --host 127.0.0.1 --port 11433 -c 4096 --jinja
    init: llama threadpool init, n_threads = 12
    load_model: initializing, n_slots = 4, n_ctx_slot = 4096, kv_unified = 'true'
    llama_server: model loaded
    llama_server: listening on http://127.0.0.1:11433
    

6、项目核心工作流逻辑位于 `new-langgraph-project/src/agent/graph.py`，替换默认代码，实现本地大模型调用、自定义系统提示、消息应答逻辑，完成离线智能体功能调试。

完整测试代码如下：
    
    
    from __future__ import annotations
    from dataclasses import dataclass
    from typing import Any, Dict
    from langgraph.graph import StateGraph
    from langgraph.runtime import Runtime
    from typing_extensions import TypedDict
    from langchain_openai import ChatOpenAI
    
    # 读取.env配置
    llm = ChatOpenAI(model="qwen2.5:1.5b")
    
    class Context(TypedDict):
        my_configurable_param: str
    
    @dataclass
    class State:
        changeme: str = "example"
    
    async def call_model(state: State, runtime: Runtime[Context]) -> Dict[str, Any]:
        messages = [
            ("system", "你是AI助手，所有回答必须使用简体中文，禁止输出英文回答。"),
            ("human", state.changeme)
        ]
        resp = await llm.ainvoke(messages)
        return {
            "changeme": resp.content
        }
    
    graph = (
        StateGraph(State, context_schema=Context)
        .add_node(call_model)
        .add_edge("__start__", "call_model")
        .compile(name="New Graph")
    )
    

## LangGraph SDK

LangGraph SDK 是对接本地 LangGraph Server 的核心工具，支持同步调用、流式响应、批量执行、会话记忆等多种场景，以下提供多套完整可运行案例，适配不同业务需求。

通过 stream 接口实现 SSE 流式输出，逐段返回大模型推理内容，适用于聊天界面实时刷新、长文本生成场景：
    
    
    from langgraph_sdk import get_client
    import asyncio
    
    client = get_client(url="http://127.0.0.1:2024")
    
    async def stream_chat():
        # 流式执行工作流
        async for chunk in client.runs.stream(
            None,
            "agent",
            input={
                "changeme": "你会做什么工作"
            },
        ):
            print(f"事件类型：{chunk.event}")
            print(f"返回数据：{chunk.data}")
            print("-" * 50)
    
    if __name__ == "__main__":
        asyncio.run(stream_chat())
    

输出内容如下
    
    
    CMD> python main.py
    
    事件类型：metadata
    返回数据：{'run_id': '01a0334b-3b5f-7661-8944-ee72f849d1b8', 'attempt': 1}
    --------------------------------------------------
    事件类型：values
    返回数据：{'changeme': '你会做什么工作'}
    --------------------------------------------------
    事件类型：values
    返回数据：{'changeme': '作为一个AI助手，我可以帮助用户进行多种任务，包括但不限于：\n\n1. 提供信息搜索和查询服务。\n2. 回答各种问题，涵盖科技、文化、生活等各个领域。\n3. 收发邮件
    ，处理日常事务。\n4. 与用户进行对话交流，提供娱乐、教育等互动内容。\n5. 进行数据分析和机器学习训练。\n6. 与各种应用和服务进行集成，提供更全面的服务。\n\n总的来说，我会尽力协助用
    户解决各种问题，提供便利和高效的服务。'}
    --------------------------------------------------
    


---
> 原文链接: https://www.cnblogs.com/LyShark/p/22655620