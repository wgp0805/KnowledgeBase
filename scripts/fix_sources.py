#!/usr/bin/env python3
"""
修复 wiki frontmatter sources 路径
ingest 归档把 raw/01-articles/xxx 移到 raw/09-archive/xxx 后，
source 页 sources 字段仍指向旧路径 → 回写为 archive 路径
用法: python fix_sources.py --dry-run   (仅列出改动)
      python fix_sources.py --apply     (实际写回)
"""
import os, re, sys

KB = r"D:\java\KnowledgeBase"
WIKI = os.path.join(KB, "wiki")
ARCHIVE = os.path.join(KB, "raw", "09-archive")

# 建 archive basename 索引: basename -> raw/下的相对路径(正斜杠)
archive_index = {}
for root, _, files in os.walk(ARCHIVE):
    for f in files:
        rel = os.path.relpath(os.path.join(root, f), os.path.join(KB, "raw")).replace("\\", "/")
        archive_index.setdefault(f, rel)  # 同名取第一个

def fix_file(path, apply):
    content = open(path, encoding="utf-8").read()
    if not content.startswith("---"):
        return []
    end = content.find("\n---", 3)
    if end < 0:
        return []
    fm = content[3:end]
    rest = content[end:]
    changes = []
    new_lines = []
    for line in fm.split("\n"):
        m = re.match(r'^(\s*-\s+)(.+)$', line)
        if m and ("/" in m.group(2) or m.group(2).endswith((".md", ".pdf", ".json"))):
            prefix, src = m.group(1), m.group(2).strip().strip('"\'')
            full = os.path.join(KB, src)
            if not os.path.exists(full):
                basename = os.path.basename(src)
                if basename in archive_index:
                    new_src = "raw/" + archive_index[basename]
                    new_line = f'{prefix}{new_src}'
                    changes.append((src, new_src))
                    new_lines.append(new_line)
                    continue
        new_lines.append(line)
    if changes and apply:
        new_fm = "\n".join(new_lines)
        open(path, "w", encoding="utf-8").write("---" + new_fm + rest)
    return changes

def main():
    apply = "--apply" in sys.argv
    dry = "--dry-run" in sys.argv or not apply
    if dry and not apply:
        print("=== DRY RUN (不写文件) ===")
    else:
        print("=== APPLY (写回文件) ===")
    total_changes = 0
    total_files = 0
    samples = []
    for root, _, files in os.walk(WIKI):
        for f in files:
            if not f.endswith(".md"):
                continue
            path = os.path.join(root, f)
            changes = fix_file(path, apply)
            if changes:
                total_files += 1
                total_changes += len(changes)
                if len(samples) < 8:
                    samples.append((os.path.basename(path), changes[:3]))
    print(f"涉及文件: {total_files}")
    print(f"总改动: {total_changes} 处")
    print("\n样例:")
    for name, chs in samples:
        for old, new in chs:
            print(f"  {name}: {old}")
            print(f"        -> {new}")

if __name__ == "__main__":
    main()
