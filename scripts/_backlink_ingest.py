#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""一次性回填脚本：把本轮 ingest 新增页面反向链接到既有页面的 ## 关联连接 区块。
幂等：若目标页已含该链接则跳过。仅修改 ## 关联连接 区块，不动 frontmatter。"""
import os, glob, io

WIKI = os.path.join(os.path.dirname(__file__), "..", "wiki")

# 目标页 basename -> [(新链接, 备注), ...]
MAP = {
    "程序汪": [("摘要-程序汪-ai漫剧平台项目", "AI 漫剧平台私活项目"), ("AI漫剧创作平台", "SaaS 项目实体")],
    "冰河": [("摘要-pi-desktop-冰河测评", "PI-Desktop 实测")],
    "苏三": [("摘要-spring-异步流式接口", "Spring 三种异步流式接口")],
    "程序员小灰": [("摘要-iquestrt-推理引擎", "IQuestRT 推理引擎")],
    "DeepSeekHarness": [("摘要-dsh-创造模式插件教程", "创造模式插件教程"), ("摘要-dsh-go-安卓app", "DSH Go 安卓 App"), ("摘要-deepseek-temperature", "Temperature 采样对照")],
    "插件生态": [("摘要-dsh-创造模式插件教程", "创造模式自举造插件"), ("摘要-dsh-go-安卓app", "DSH Go 移动端生态")],
    "投机解码": [("IQuestRT", "推测解码优化"), ("IQuestQ1", "递归多词元预测"), ("摘要-iquestrt-推理引擎", "推测解码同名概念")],
    "MoE": [("IQuestRT", "专家预取"), ("IQuestQ1", "MoE 架构")],
    "JavaAgent": [("摘要-手把手实现java-agent-IT码徒", "手把手实现 JavaAgent")],
    "字节码增强": [("摘要-手把手实现java-agent-IT码徒", "字节码增强实现")],
    "Arthas": [("摘要-手把手实现java-agent-IT码徒", "trace 命令字节码增强原理")],
    "IntelliJIDEA": [("摘要-idea-30款插件", "30 款 IDEA 插件盘点")],
    "LLM": [("摘要-deepseek-temperature", "Temperature 采样"), ("Temperature采样", "温度采样概念")],
    "SSE流式输出": [("摘要-spring-异步流式接口", "Spring SSE 流式接口"), ("异步流式接口", "异步流式接口概念")],
    "SSE": [("摘要-spring-异步流式接口", "SseEmitter"), ("异步流式接口", "流式接口")],
    "AI漫剧工作流": [("摘要-程序汪-ai漫剧平台项目", "九阶段平台化落地"), ("AI漫剧创作平台", "九阶段 SaaS 平台")],
    "ClaudeCode": [("摘要-deepseek-temperature", "temperature 处理对照"), ("IQuestQ1", "可接入编程入口")],
    "Codex": [("摘要-deepseek-temperature", "temperature 处理对照")],
    "PI-Desktop": [("摘要-pi-desktop-冰河测评", "冰河实测")],
    "推理系统": [("IQuestRT", "推理引擎"), ("摘要-iquestrt-推理引擎", "推理引擎来源")],
    "NVIDIA": [("IQuestRT", "Blackwell/NVLink 依赖")],
    "GPU架构": [("摘要-iquestrt-推理引擎", "多卡并行语境"), ("NaN同步", "NaN 同步机制")],
    "everything-is-a-plugin": [("摘要-dsh-创造模式插件教程", "创造模式自举"), ("DSHGo", "移动端插件生态")],
    "FastAPI": [("摘要-程序汪-ai漫剧平台项目", "后端框架"), ("AI漫剧创作平台", "后端框架")],
    "Celery": [("摘要-程序汪-ai漫剧平台项目", "异步任务队列"), ("AI漫剧创作平台", "异步任务")],
    "Vue3": [("摘要-程序汪-ai漫剧平台项目", "前端框架"), ("AI漫剧创作平台", "前端框架")],
    "PostgreSQL": [("摘要-程序汪-ai漫剧平台项目", "JSONB 存储"), ("AI漫剧创作平台", "JSONB 混合存储")],
    "微短剧": [("摘要-程序汪-ai漫剧平台项目", "内容产业语境"), ("AI漫剧创作平台", "内容产业")],
    "LLM网关": [("摘要-程序汪-ai漫剧平台项目", "多模型统一网关"), ("AI漫剧创作平台", "多模型统一网关")],
    "静态代码检查": [("摘要-idea-30款插件", "代码质量类插件")],
    "异步流式接口": [("摘要-spring-异步流式接口", "Spring 三种异步流式接口")],
    "WebSocket": [("摘要-spring-异步流式接口", "双向通讯对照")],
    "轮询": [("摘要-spring-异步流式接口", "下策对照")],
    "Subagent": [("摘要-pi-desktop-冰河测评", "并行调查")],
    "多Agent": [("摘要-pi-desktop-冰河测评", "多 Agent 编排")],
    "MCP": [("摘要-pi-desktop-冰河测评", "插件可接入协议")],
    "Pi (coding harness)": [("摘要-pi-desktop-冰河测评", "Agent Runtime 生态")],
    "TRAE": [("AI漫剧创作平台", "代码生成工具")],
    "AOP": [("摘要-手把手实现java-agent-IT码徒", "代理 vs 字节码对比")],
    "Java": [("摘要-idea-30款插件", "开发语言")],
    "DeepSeek": [("摘要-deepseek-temperature", "API 提供方")],
    "沉默王二": [("摘要-deepseek-temperature", "Temperature 采样作者")],
    "程序员追风": [("摘要-dsh-go-安卓app", "DSH Go 作者")],
    "小哈": [("摘要-idea-30款插件", "IDEA 插件作者")],
    "IT码徒": [("摘要-手把手实现java-agent-IT码徒", "JavaAgent 作者")],
}

def find_file(basename):
    hits = glob.glob(os.path.join(WIKI, "**", basename + ".md"), recursive=True)
    return hits[0] if hits else None

def add_links(path, links):
    with io.open(path, "r", encoding="utf-8") as f:
        text = f.read()
    # 定位 ## 关联连接 区块
    idx = text.find("## 关联连接")
    if idx == -1:
        return False, "NO_SECTION"
    # 找区块结束：下一个 '## ' 标题 或文件结尾
    rest = text[idx+len("## 关联连接"):]
    nxt = rest.find("\n## ")
    if nxt == -1:
        section = rest
        tail = ""
    else:
        section = rest[:nxt]
        tail = rest[nxt:]
    section_end = idx + len("## 关联连接") + len(section)
    added = []
    newlines = []
    for (link, note) in links:
        token = "[[" + link + "]]"
        if token in section:
            continue
        newlines.append(f"- [[{link}]] — {note}")
        added.append(link)
    if not newlines:
        return False, "ALREADY"
    # 在区块末尾（section 之后、tail/EOF 之前）插入新行
    insert_at = section_end
    prefix = "" if section.endswith("\n") or section.endswith("\r") else "\n"
    new_block = prefix + "\n".join(newlines) + "\n"
    text = text[:insert_at] + new_block + text[insert_at:]
    with io.open(path, "w", encoding="utf-8") as f:
        f.write(text)
    return True, added

if __name__ == "__main__":
    total = 0
    for t, links in MAP.items():
        p = find_file(t)
        if not p:
            print(f"[MISSING] {t}")
            continue
        ok, info = add_links(p, links)
        if ok:
            print(f"[ADD] {t}: {info}")
            total += 1
        else:
            print(f"[SKIP] {t}: {info}")
    print(f"\n完成，新增回填页 {total} 个")
