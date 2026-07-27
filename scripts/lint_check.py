#!/usr/bin/env python3
"""Knowledge base health check script"""
import os
import re
import json

WIKI_DIR = 'wiki'

# Step 1: Collect all wiki files (excluding index.md and log.md)
all_files = set()
for root, dirs, files in os.walk(WIKI_DIR):
    for f in files:
        if f.endswith('.md'):
            rel_path = os.path.relpath(os.path.join(root, f), WIKI_DIR)
            # Get page name without path and extension
            page_name = os.path.splitext(f)[0]
            all_files.add(page_name)

# Exclude index and log
all_files.discard('index')
all_files.discard('log')

print(f"Total wiki files (excluding index/log): {len(all_files)}")

# Step 2: Extract all [[wikilinks]] from index.md
with open(os.path.join(WIKI_DIR, 'index.md'), 'r', encoding='utf-8') as f:
    index_content = f.read()

index_links = set(re.findall(r'\[\[([^\]]+)\]\]', index_content))
print(f"Links in index.md: {len(index_links)}")

# Step 3: Check index consistency - registered but no file
registered_no_file = index_links - all_files
print(f"Registered in index but file missing: {len(registered_no_file)}")
if registered_no_file:
    for r in sorted(registered_no_file):
        print(f"  MISSING: [[{r}]]")

# Check files not registered in index
files_not_indexed = all_files - index_links
print(f"Files exist but not in index: {len(files_not_indexed)}")
if files_not_indexed:
    for f in sorted(files_not_indexed):
        print(f"  UNINDEXED: {f}.md")

# Step 4: Collect all wikilinks from all pages
all_wikilinks = {}  # page -> set of links
for page in all_files:
    # Find the file
    file_path = None
    for root, dirs, files in os.walk(WIKI_DIR):
        if f"{page}.md" in files:
            file_path = os.path.join(root, f"{page}.md")
            break
    if file_path:
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            links = set(re.findall(r'\[\[([^\]]+)\]\]', content))
            # Remove self-references
            links.discard(page)
            all_wikilinks[page] = links
        except Exception as e:
            print(f"  ERROR reading {page}: {e}")

# Step 5: Find dead links
all_pages = all_files | {'index', 'log'}
dead_links = {}  # source_page -> set of dead target pages
for source, links in all_wikilinks.items():
    dead = {l for l in links if l not in all_pages}
    if dead:
        dead_links[source] = dead

print(f"\nDead links found: {sum(len(v) for v in dead_links.values())}")
if dead_links:
    for source, targets in sorted(dead_links.items()):
        for t in sorted(targets):
            print(f"  [[{source}]] -> [[{t}]] (MISSING)")

# Step 6: Find orphan pages
referenced_pages = set()
for source, links in all_wikilinks.items():
    referenced_pages.update(links)
# Also check index.md
index_links_no_self = {l for l in index_links if l not in ('index', 'log')}
referenced_pages.update(index_links_no_self)

orphan_pages = all_files - referenced_pages
print(f"\nOrphan pages (no other page links to them): {len(orphan_pages)}")
if orphan_pages:
    for p in sorted(orphan_pages):
        print(f"  ORPHAN: [[{p}]]")

# Step 7: Check for knowledge conflicts
conflict_pages = []
for page in all_files:
    file_path = None
    for root, dirs, files in os.walk(WIKI_DIR):
        if f"{page}.md" in files:
            file_path = os.path.join(root, f"{page}.md")
            break
    if file_path:
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            if '## 知识冲突' in content:
                conflict_pages.append(page)
        except:
            pass

print(f"\nPages with unresolved knowledge conflicts: {len(conflict_pages)}")
if conflict_pages:
    for p in sorted(conflict_pages):
        print(f"  CONFLICT: [[{p}]]")

# Save all results to JSON for reference
results = {
    'total_files': len(all_files),
    'registered_no_file': sorted(registered_no_file),
    'files_not_indexed': sorted(files_not_indexed),
    'dead_links': {k: sorted(v) for k, v in dead_links.items()},
    'orphan_pages': sorted(orphan_pages),
    'conflict_pages': sorted(conflict_pages),
}
with open('scripts/lint_results.json', 'w', encoding='utf-8') as f:
    json.dump(results, f, ensure_ascii=False, indent=2)

print("\n\nDone. Results saved to scripts/lint_results.json")