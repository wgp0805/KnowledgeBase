#!/usr/bin/env python3
"""
扫描 raw/ 下待处理的未摄取文件
待处理 = raw 文件(排除 09-archive)的 basename 不在任何 wiki source 页的 sources 引用集合里
"""
import os, re

KB = r"D:\java\KnowledgeBase"
RAW = os.path.join(KB, "raw")
WIKI = os.path.join(KB, "wiki")
ARCHIVE = os.path.join(RAW, "09-archive")

# 1. 收集 wiki 所有页面引用的 raw basename 集合（正则全文提取，兼容 list/单行/正文）
referenced = set()
raw_re = re.compile(r'raw/[^\s\]"\'\)\|,]+?\.(?:md|pdf|json)')
for root, _, files in os.walk(WIKI):
    for f in files:
        if not f.endswith(".md"):
            continue
        try:
            content = open(os.path.join(root, f), encoding="utf-8").read()
        except Exception:
            continue
        for m in raw_re.finditer(content):
            referenced.add(os.path.basename(m.group(0)))

# 2. 遍历 raw(排除 09-archive)，区分已摄取/待处理
pending = []        # 待处理
ingested_not_archived = []  # 已摄取但文件还在原位未归档
for root, dirs, files in os.walk(RAW):
    # 排除 09-archive
    if "09-archive" in root:
        continue
    for f in files:
        if not f.endswith((".md", ".pdf", ".json")):
            continue
        bn = f
        rel = os.path.relpath(os.path.join(root, f), RAW)
        if bn in referenced:
            ingested_not_archived.append((rel, bn))
        else:
            pending.append((rel, bn))

print(f"=== raw/ 待摄取文件扫描 ===")
print(f"wiki 已引用的 raw basename 数: {len(referenced)}")
print(f"已摄取但文件未归档(仍在 raw 原位): {len(ingested_not_archived)}")
print(f"待摄取(未被任何 wiki 页引用): {len(pending)}")
print()
print("--- 待摄取清单 ---")
# 按目录分组
from collections import defaultdict
by_dir = defaultdict(list)
for rel, bn in pending:
    d = os.path.dirname(rel) or "(raw根)"
    by_dir[d].append(bn)
for d, bns in sorted(by_dir.items()):
    print(f"\n[{d}] {len(bns)} 个")
    for bn in sorted(bns):
        print(f"  {bn}")
