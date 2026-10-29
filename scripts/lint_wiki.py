#!/usr/bin/env python3
"""
Wiki Lint 工具 —— 扫描 wiki/ 目录健康度
检查项：孤岛页面(0入链) / 死链 / frontmatter sources 缺失 / 同名 stem 冲突
遵循 AGENTS.md 的 /lint 工作流定义
"""
import os, re, sys
from collections import defaultdict

WIKI_DIR = r"D:\java\KnowledgeBase\wiki"
KB_ROOT = r"D:\java\KnowledgeBase"

# Obsidian 双链正则：[[...]]，支持 [[Name|alias]] [[Name#anchor]] [[Name^block]] [[dir/Name]]
# 注意：代码块(``` 或 ~~~ 包裹)与行内代码(`...`)内的 [[...]] 是 shell 语法(如 [[ "$tool" == "Bash" ]])，
# 需先行剔除，避免误报死链。
LINK_RE = re.compile(r'\[\[([^\[\]]+?)\]\]')
CODE_BLOCK_RE = re.compile(r'(`{3,}|~{3,}).*?\1', re.S)
INLINE_CODE_RE = re.compile(r'`[^`\n]*`')

def strip_code(content):
    """剔除代码块与行内代码，避免其中 [[...]] 被误判为双链"""
    content = CODE_BLOCK_RE.sub('', content)
    content = INLINE_CODE_RE.sub('', content)
    return content

def parse_target(raw):
    """解析双链目标：
    1) 先按完整文本（含 #/^）尝试匹配实际文件名；
    2) 匹配不到时再去掉 anchor/block id 部分（#后或^后）。
    这样 [[Pass^k]] 若存在 Pass^k.md 则整体匹配，不会被误拆成 [[Pass]]。
    """
    name = raw.split("|")[0].strip()       # 去别名
    return name

def resolve_target(raw, existing_lower):
    """返回候选目标列表：优先完整名，其次去 #/^ 锚点后的 basename；
    支持 [[xxx.md]] 写法（Obsidian 允许带扩展名链接）。
    纯 [[#heading]] 或 [[^block]] 开头（指向当前文件内部）返回 None。"""
    name = raw.split("|")[0].strip()
    if name.startswith("#") or name.startswith("^"):
        return None  # 当前文件内部锚点/块引用，非页面双链
    cands = [name]
    # 去 anchor / block id（仅当完整名不存在时才考虑）
    if '#' in name or '^' in name:
        base = re.split(r'[#\^]', name)[0]
        if base:
            cands.append(base)
    # 取 basename（去目录）
    cands = [c.split("/")[-1] for c in cands]
    # 支持带 .md 后缀
    cands = [c[:-3] if c.lower().endswith(".md") else c for c in cands]
    # 返回第一个存在于 existing_lower 的候选（或最后一个）
    for c in cands:
        if c.lower() in existing_lower:
            return c
    return cands[-1]

def main():
    # 1. 收集所有存在页面（按 stem，大小写不敏感匹配，贴近 Obsidian 行为）
    existing = {}                  # stem -> relpath
    stem_conflict = defaultdict(list)  # lower(stem) -> [(stem, relpath)]
    for root, _, files in os.walk(WIKI_DIR):
        for f in files:
            if f.endswith(".md"):
                stem = f[:-3]
                rel = os.path.relpath(os.path.join(root, f), WIKI_DIR)
                existing[stem] = rel
                stem_conflict[stem.lower()].append((stem, rel))

    existing_lower = {s.lower(): s for s in existing}

    # 同名 stem 冲突（不同文件同 stem → 双链歧义）
    dup_stems = {low: lst for low, lst in stem_conflict.items() if len(lst) > 1}

    # 2. 解析每个文件出链，统计入链 + 死链
    inlinks = defaultdict(int)         # target_lower -> count
    deadlinks = defaultdict(list)       # target -> [src_stem, ...]
    sources_missing = []               # (file, src)

    for root, _, files in os.walk(WIKI_DIR):
        for f in files:
            if not f.endswith(".md"):
                continue
            stem = f[:-3]
            # log.md 为 append-only 操作日志，其链接多为历史修复动作的记录（旧名/被改前名），
            # 不参与统计，避免把历史语义记录误报为死链。
            # index.md 为正规导航页，参与入链统计（保证"仅在索引注册"的页面不算孤儿），
            # 但其自身不作为孤儿候选（在孤儿判定中排除）。
            if stem == "log":
                continue
            path = os.path.join(root, f)
            try:
                content = open(path, encoding="utf-8").read()
            except Exception:
                continue
            content = strip_code(content)
            targets = set()
            for m in LINK_RE.finditer(content):
                t = resolve_target(m.group(1), existing_lower)
                if t:
                    targets.add(t)
            for t in targets:
                inlinks[t.lower()] += 1
                if t.lower() not in existing_lower:
                    deadlinks[t].append(stem)

            # frontmatter sources 检查
            if content.startswith("---"):
                end = content.find("\n---", 3)
                if end > 0:
                    fm = content[3:end]
                    for line in fm.split("\n"):
                        s = line.strip()
                        if s.startswith("- ") and ("/" in s or s.endswith(".md")):
                            src = s[2:].strip().strip('"\'')
                            full = os.path.join(KB_ROOT, src)
                            if not os.path.exists(full):
                                sources_missing.append((stem, src))

    # 3. 孤岛：存在但入链=0（排除 index/log 导航页）
    orphans = []
    for stem, rel in existing.items():
        if stem in ("index", "log"):
            continue
        if inlinks.get(stem.lower(), 0) == 0:
            orphans.append((stem, rel))
    orphans.sort()

    # === 输出报告 ===
    print("=" * 60)
    print("Wiki Lint Report")
    print("=" * 60)
    print(f"总页面数: {len(existing)}")
    print(f"双链目标总数(去重): {len(inlinks)}")
    print()

    print(f"--- 孤岛页面 (0 入链): {len(orphans)} ---")
    for stem, rel in orphans:
        print(f"  [[{stem}]]  ({rel})")
    print()

    print(f"--- 死链 (目标不存在): {len(deadlinks)} ---")
    for t in sorted(deadlinks):
        srcs = deadlinks[t]
        show = ", ".join(sorted(srcs)[:4])
        print(f"  [[{t}]]  <- {len(srcs)} 处: {show}")
    print()

    print(f"--- 同名 stem 冲突 (双链歧义): {len(dup_stems)} ---")
    for low, lst in sorted(dup_stems.items()):
        paths = "; ".join(f"{s}@{r}" for s, r in lst)
        print(f"  '{low}': {paths}")
    print()

    print(f"--- frontmatter sources 指向的 raw 缺失: {len(sources_missing)} ---")
    for stem, src in sources_missing[:30]:
        print(f"  {stem}: {src}")
    if len(sources_missing) > 30:
        print(f"  ... 还有 {len(sources_missing)-30} 条")
    print()

    # 健康度评分
    total = len(existing)
    health = 100 * (1 - (len(orphans) + len(deadlinks)) / max(total, 1))
    print(f"--- 健康度估算: {health:.1f}% (越接近 100 越好) ---")
    print("注: 逻辑内容冲突需人工抽查，重点查同名实体页(如 PiAgent)与跨页说法矛盾")

if __name__ == "__main__":
    main()
