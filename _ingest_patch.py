# -*- coding: utf-8 -*-
"""ingest 增量更新脚本：补全未完成 ingest 的概念页增量更新与摘要关联补充"""
import os

WIKI = r"D:\java\KnowledgeBase\wiki"

def patch(path, replacements):
    with open(path, 'rb') as f:
        content = f.read().decode('utf-8')
    nl = '\r\n' if '\r\n' in content else '\n'
    hits = 0
    for old, new in replacements:
        old_real = old.replace('\n', nl)
        new_real = new.replace('\n', nl)
        if old_real not in content:
            print(f"  [SKIP] {os.path.basename(path)}: 未找到 <<{old[:60]}>>")
            continue
        content = content.replace(old_real, new_real, 1)
        hits += 1
    with open(path, 'wb') as f:
        f.write(content.encode('utf-8'))
    print(f"  [OK] {os.path.basename(path)} ({hits}/{len(replacements)} 替换)")

# 1. Agent.md
patch(os.path.join(WIKI, "concepts", "Agent.md"), [
    ("Agent 的核心运行机制是 LLM Loop：接收指令->制定计划->调用工具->观察结果->决定下一步->循环直到完成。",
     "Agent 的核心运行机制是 LLM Loop：接收指令->制定计划->调用工具->观察结果->决定下一步->循环直到完成。\n\n### Agent 本质公式与循环终止标准\n- **本质公式**：Agent = 大模型 + 工具集 + 执行循环（源自 [[PiAgent]]）。任何复杂 Agent 框架都只是在基础循环上叠加工程防护。\n- **循环终止标准**：模型判定无需调用工具时循环必须终止，否则无限消耗 Token 甚至死循环（详见 [[trace-turn]]）。\n- **极简模型**：200 行代码即可实现（read_file + write_file + while True），生产级框架在此基础上增加轮次限制、上下文压缩、参数校验、安全拦截、错误自愈、生命周期钩子。"),
    ("- [[摘要-ai-agent-cognitive-navigation]] - 认知导航来源",
     "- [[摘要-ai-agent-cognitive-navigation]] - 认知导航来源\n- [[PiAgent]] - 开源 Agent 框架，工程化实现\n- [[trace-turn]] - Agent 运行单位与生命周期钩子\n- [[摘要-pi-agent-core-principles]] - 本质公式来源\n- [[摘要-pi-agent-production-guide]] - 生产级落地来源"),
    ("last_updated: 2026-07-20", "last_updated: 2026-08-04"),
])

# 2. ContextEngineering.md
patch(os.path.join(WIKI, "concepts", "ContextEngineering.md"), [
    ("- Rerank、压缩、去重、冲突消解都是上下文工程的子问题",
     "- Rerank、压缩、去重、冲突消解都是上下文工程的子问题\n\n### pi-agent 的两大上下文解决方案（源自 [[PiAgent]]）\n1. **工具输出截断机制**：文件读取、命令行执行类工具返回超长文本会瞬间占满 Token 上限。对返回内容按字符/字节截断（保留首尾关键信息），完整原始数据本地持久化，仅将「截断摘要 + 本地文件路径」传入上下文，由模型自主判断是否读取完整文件。\n2. **阈值驱动上下文自动压缩**：实时计算上下文占用，剩余 Token 低于阈值时自动启动压缩（详见 [[context-compression]]）。优化技巧：上一轮任务结束后提前预判压缩，避免新一轮请求开始时卡顿。压缩按结构化模板提炼（用户目标/约束条件/工作流程/历史决策/下一步计划），替换早期历史对话。\n3. **提示词顺序编排**：固定系统提示词前置、减少前缀频繁变动，提升模型缓存命中率。"),
    ("- [[摘要-字节面试官什么是RAG为什么需要RAG]] - 来源",
     "- [[摘要-字节面试官什么是RAG为什么需要RAG]] - 来源\n- [[PiAgent]] - 上下文工程实践来源\n- [[context-compression]] - 阈值驱动压缩机制\n- [[摘要-pi-agent-production-guide]] - 来源"),
    ("last_updated: 2026-06-02", "last_updated: 2026-08-04"),
])

# 3. context-compression.md
patch(os.path.join(WIKI, "concepts", "context-compression.md"), [
    ("3. **近期缓冲**：最近几轮完整对话原样保留，不压缩",
     "3. **近期缓冲**：最近几轮完整对话原样保留，不压缩\n\n### pi-agent 阈值驱动压缩与结构化模板（源自 [[PiAgent]]）\n- **触发条件**：设定 Token 阈值，实时计算上下文占用，剩余 Token 低于阈值自动启动压缩。优化技巧：上一轮任务结束后提前预判压缩，避免用户等待卡顿。\n- **结构化压缩模板**（编码 Agent 默认）：统一按固定结构提炼历史对话核心信息替代杂乱原始对话——用户原始目标、执行约束条件、完整工作流程、历史关键决策、下一步执行计划。数据类/办公 Agent 可自定义专属模板，无定制模板也可交给模型自由摘要。\n- **使用方式**：用结构化压缩摘要替换被精简的早期历史对话，重组上下文，降低整体 Token 占用。\n- **工具输出截断**：对工具返回长内容做字符/字节截断，完整原始数据本地持久化，仅传入「截断摘要 + 本地文件路径」（详见 [[ContextEngineering]]）。"),
    ("- [[摘要-生产级Agent设计]] - 来源",
     "- [[摘要-生产级Agent设计]] - 来源\n- [[PiAgent]] - 阈值压缩与结构化模板来源\n- [[ContextEngineering]] - 上下文工程\n- [[摘要-pi-agent-production-guide]] - 来源"),
    ("last_updated: 2026-07-24", "last_updated: 2026-08-04"),
])

# 4. 提示词工程.md
patch(os.path.join(WIKI, "concepts", "提示词工程.md"), [
    ("3. **迭代（Iteration）**：提示词有生命周期，先尝试再调整，而非一步到位。关键习惯：把通用提示改为贴合自己生产流程的版本；加入交互逻辑让 AI 主动追问以补充信息。",
     "3. **迭代（Iteration）**：提示词有生命周期，先尝试再调整，而非一步到位。关键习惯：把通用提示改为贴合自己生产流程的版本；加入交互逻辑让 AI 主动追问以补充信息。\n\n### 另一套三大原则：定角色 / 明任务 / 给素材（【AI 梵决】）\n与上述「简洁/框架/迭代」偏宏观方法论不同，【AI 梵决】侧重 Prompt 的结构化构成要素（详见 [[摘要-提示词三大原则-定角色明任务给素材]]）：\n1. **定角色**：清晰界定身份/定位/专业背景，限定思考视角，角色定义放在 Prompt 最开头优先生效\n2. **明任务**：明确要做什么与不要做什么，含执行任务、交付格式、约束条件三要素，防止 AI 自由发挥\n3. **给素材**：把全部参考资料、背景、原始素材交给模型，AI 无记忆不主动猜测，信息缺失易产生幻觉\n\n两套原则互补：「简洁/框架/迭代」是方法论，「定角色/明任务/给素材」是结构化要素。配套通用模板见 [[摘要-通用万能prompt模板]]。"),
    ("- [[AndrejKarpathy]] - 简洁 prompt 范例来源",
     "- [[AndrejKarpathy]] - 简洁 prompt 范例来源\n- [[摘要-提示词三大原则-定角色明任务给素材]] - 另一套三大原则（定角色/明任务/给素材）\n- [[摘要-通用万能prompt模板]] - 基于三大原则的通用模板"),
    ("last_updated: 2026-07-30", "last_updated: 2026-08-04"),
])

# 5. PaiAgent.md
patch(os.path.join(WIKI, "entities", "PaiAgent.md"), [
    ("- ReactFlow - 流程图组件",
     "- ReactFlow - 流程图组件\n- [[PiAgent]] - 名字相近但不同的开源 Agent 框架（70K Star），勿混淆"),
    ("last_updated: 2026-05-19", "last_updated: 2026-08-04"),
])

# 6. 摘要-提示词三大原则-定角色明任务给素材.md (补充 sources + 修复大小写死链 + 幻觉关联)
patch(os.path.join(WIKI, "sources", "摘要-提示词三大原则-定角色明任务给素材.md"), [
    ("sources: [raw/01-articles/【AI 梵决】写好提示词的三大原则.md]",
     "sources: [raw/01-articles/【AI 梵决】写好提示词的三大原则.md, raw/01-articles/Pi-Agent 智能体核心原理实战文档.md]"),
    ("- [[摘要-通用万能Prompt模板]] - 本文原则的具体模板化实现",
     "- [[摘要-通用万能prompt模板]] - 本文原则的具体模板化实现\n- [[幻觉]] - 给素材原则对应的核心问题"),
])

# 7. 摘要-通用万能prompt模板.md (补充关联)
patch(os.path.join(WIKI, "sources", "摘要-通用万能prompt模板.md"), [
    ("- [[摘要-写好提示词的三大原则]] - 另一套三大原则体系",
     "- [[摘要-写好提示词的三大原则]] - 另一套三大原则体系\n- [[幻觉]] - 素材缺失导致的核心问题\n- [[PiAgent]] - 模板可作为 Agent 框架系统提示词注入\n- [[AICoding]] - 代码模板的 AI 编程应用"),
])

print("\n全部增量更新完成")
