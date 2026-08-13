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
LINK_RE = re.compile(r'\[\[([^\[\]]+?)\]\]')

def parse_target(raw):
    name = raw.split("|")[0]                  # 去别名
    name = re.split(r'[#\^]', name)[0]        # 去 anchor / block id
    name = name.split("/")[-1].strip()        # 取 basename
    return name

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
            path = os.path.join(root, f)
            try:
                content = open(path, encoding="utf-8").read()
            except Exception:
                continue
            targets = set()
            for m in LINK_RE.finditer(content):
                t = parse_target(m.group(1))
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
