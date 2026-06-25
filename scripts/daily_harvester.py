#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
知识库自动抓取器 (Daily Harvester)
从配置的信息源抓取文章，过滤后存入 raw/ 目录供后续 /ingest 处理。
"""

import hashlib
import json
import os
import re
import sys
import time
from datetime import datetime, timezone, timedelta
from pathlib import Path
from typing import Optional

import feedparser
import requests
import yaml
from bs4 import BeautifulSoup
import html2text

# ─── 路径 ───
BASE_DIR = Path(__file__).resolve().parent.parent
CONFIG_PATH = BASE_DIR / "scripts" / "sources.yaml"
SEEN_PATH = BASE_DIR / "scripts" / ".seen_urls.json"
RAW_DIR = BASE_DIR / "raw" / "01-articles"
DIGEST_PATH = BASE_DIR / "raw" / "_daily_digest.md"
WIKI_DIR = BASE_DIR / "wiki"

TZ = timezone(timedelta(hours=8))
NOW = datetime.now(TZ)
TODAY = NOW.strftime("%Y-%m-%d")


def load_config() -> dict:
    with open(CONFIG_PATH, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def load_seen() -> set:
    if SEEN_PATH.exists():
        with open(SEEN_PATH, "r", encoding="utf-8") as f:
            return set(json.load(f))
    return set()


def save_seen(seen: set):
    SEEN_PATH.parent.mkdir(parents=True, exist_ok=True)
    with open(SEEN_PATH, "w", encoding="utf-8") as f:
        json.dump(sorted(seen), f, ensure_ascii=False, indent=2)


def load_wiki_tags() -> list:
    tags = set()
    if WIKI_DIR.exists():
        for subdir in ["concepts", "entities", "sources", "syntheses"]:
            d = WIKI_DIR / subdir
            if d.exists():
                for f in d.glob("*.md"):
                    tags.add(f.stem.lower())
    return sorted(tags)


def extract_text_from_html(html: str) -> str:
    soup = BeautifulSoup(html, "html.parser")
    for tag in soup(["script", "style", "nav", "footer", "header", "aside"]):
        tag.decompose()
    return soup.get_text(separator=" ", strip=True)


def html_to_markdown(html: str, url: str = "") -> str:
    converter = html2text.HTML2Text()
    converter.body_width = 0
    converter.ignore_links = False
    converter.ignore_images = False
    converter.ignore_emphasis = False
    converter.skip_internal_links = True
    converter.protect_links = True
    converter.unicode_snob = True
    md = converter.handle(html)
    if url:
        md += f"\n\n---\n> 原文链接: {url}"
    return md


def relevance_score(text: str, wiki_tags: list, source_tags: list) -> float:
    text_lower = text.lower()
    score = 0.0

    for tag in wiki_tags:
        tag_clean = tag.replace("-", " ").replace("_", " ")
        if tag_clean in text_lower:
            score += 0.15

    for tag in source_tags:
        if tag.lower() in text_lower:
            score += 0.20

    core_keywords = [
        "java", "spring", "ai", "agent", "llm", "rag", "gpt", "claude",
        "codex", "docker", "kubernetes", "微服务", "数据库", "redis",
        "kafka", "elasticsearch", "mysql", "postgresql", "vue", "react",
        "mcp", "function calling", "prompt", "obsidian", "设计模式",
        "架构", "分布式", "高并发", "性能优化"
    ]
    for kw in core_keywords:
        if kw.lower() in text_lower:
            score += 0.05

    score = min(score, 1.0)
    return round(score, 3)


def sanitize_filename(title: str) -> str:
    name = re.sub(r'[<>:"/\\|?*]', '', title)
    name = re.sub(r'\s+', ' ', name).strip()
    if len(name) > 80:
        name = name[:80]
    return name


def fetch_article_content(url: str) -> Optional[str]:
    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                          "AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/125.0.0.0 Safari/537.36"
        }
        resp = requests.get(url, headers=headers, timeout=15)
        resp.raise_for_status()
        return resp.text
    except Exception as e:
        print(f"  ⚠ 获取全文失败: {e}")
        return None


def fetch_feed(source: dict) -> list:
    print(f"  [RSS] 正在抓取: {source['name']}")
    try:
        feed = feedparser.parse(source["url"])
        entries = []
        for entry in feed.entries[:source.get("max_per_source", 5)]:
            entries.append({
                "title": entry.get("title", "无标题"),
                "link": entry.get("link", ""),
                "published": entry.get("published", ""),
                "summary": entry.get("summary", ""),
                "content": entry.get("content", [{}])[0].get("value", "")
                if entry.get("content") else "",
                "source_name": source["name"],
                "source_tags": source.get("tags", []),
            })
        print(f"    -> 获取 {len(entries)} 篇")
        return entries
    except Exception as e:
        print(f"    [ERR] 抓取失败: {e}")
        return []


def process_entries(entries: list, seen: set, wiki_tags: list, config: dict) -> list:
    result = []
    filter_cfg = config.get("filter", {})
    min_score = filter_cfg.get("min_score", 0.15)

    for entry in entries:
        url = entry.get("link", "")
        if not url:
            continue

        url_hash = hashlib.md5(url.encode()).hexdigest()
        if url_hash in seen:
            print(f"  [SKIP] 已存在: {entry['title'][:50]}")
            continue

        text = entry.get("title", "") + " " + entry.get("summary", "")
        if entry.get("content"):
            text += " " + extract_text_from_html(entry["content"])

        score = relevance_score(text, wiki_tags, entry.get("source_tags", []))
        entry["score"] = score

        if score < min_score:
            print(f"  [SKIP] 相关性不足 ({score}): {entry['title'][:50]}")
            continue

        result.append(entry)
        seen.add(url_hash)

    return result


def save_article(entry: dict) -> Optional[Path]:
    RAW_DIR.mkdir(parents=True, exist_ok=True)

    title = entry["title"]
    safe_name = sanitize_filename(title)
    fname = f"{TODAY}-{safe_name}.md"
    fpath = RAW_DIR / fname

    counter = 1
    while fpath.exists():
        fname = f"{TODAY}-{safe_name}_{counter}.md"
        fpath = RAW_DIR / fname
        counter += 1

    md = f"""---
title: "{title}"
source: "{entry['source_name']}"
url: "{entry['link']}"
date: "{entry.get('published', TODAY)}"
score: {entry['score']}
tags: [{', '.join(f'\"{t}\"' for t in entry.get('source_tags', []))}]
auto_captured: true
---

# {title}

> **来源**: {entry['source_name']}  
> **链接**: {entry['link']}  
> **抓取日期**: {TODAY}  
> **相关性评分**: {entry['score']}

"""

    if entry.get("content"):
        content_md = html_to_markdown(entry["content"], entry["link"])
        md += content_md
    elif entry.get("summary"):
        md += entry["summary"]
        if entry["link"]:
            md += f"\n\n---\n> 原文链接: {entry['link']}"
    else:
        md += f"*（仅标题，无正文内容）*\n\n原文链接: {entry['link']}"

    with open(fpath, "w", encoding="utf-8") as f:
        f.write(md)

    return fpath


def generate_digest(saved: list, skipped_count: int, total_checked: int):
    DIGEST_PATH.parent.mkdir(parents=True, exist_ok=True)

    lines = [
        f"# [RSS] 每日抓取摘要 — {TODAY}",
        "",
        f"| 指标 | 数值 |",
        f"|------|------|",
        f"| 检查条目 | {total_checked} |",
        f"| 新保存 | {len(saved)} |",
        f"| 跳过（去重/低分） | {skipped_count} |",
        "",
    ]

    if saved:
        lines.append("## [OK] 今日新抓取")
        lines.append("")
        for s in saved:
            fname = sanitize_filename(s["title"])
            rel_path = f"raw/01-articles/{TODAY}-{fname}.md"
            lines.append(f"- [[{rel_path}]] — **{s['title']}**")
            lines.append(f"  - 来源: {s['source_name']} | 评分: {s['score']}")
            lines.append("")
    else:
        lines.append("*今日无新增文章。*")
        lines.append("")

    lines.append("---")
    lines.append(f"*自动生成于 {NOW.strftime('%Y-%m-%d %H:%M')}*")

    with open(DIGEST_PATH, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))


def main():
    print(f"\n{'='*50}")
    print(f"  知识库自动抓取 — {TODAY}")
    print(f"{'='*50}\n")

    config = load_config()
    sources = [s for s in config["sources"] if s.get("enabled", True)]
    print(f" 已启用信息源: {len(sources)} 个")

    wiki_tags = load_wiki_tags()
    print(f" 知识库标签: {len(wiki_tags)} 个")

    seen = load_seen()
    print(f" 历史记录: {len(seen)} 条\n")

    all_entries = []
    for source in sources:
        entries = fetch_feed(source)
        all_entries.extend(entries)
        time.sleep(0.5)

    print(f"\n 共获取 {len(all_entries)} 篇原始条目")

    saved_entries = process_entries(all_entries, seen, wiki_tags, config)
    skipped = len(all_entries) - len(saved_entries)

    print(f"\n 过滤结果:")
    print(f"   [OK] 保存: {len(saved_entries)} 篇")
    print(f"   [SKIP] 跳过: {skipped} 篇（去重/低分）")

    saved_paths = []
    for entry in saved_entries:
        fpath = save_article(entry)
        if fpath:
            saved_paths.append(fpath)
            print(f"   [SAVED] 已保存: {fpath.name}")

    save_seen(seen)
    generate_digest(saved_entries, skipped, len(all_entries))

    print(f"\n{'='*50}")
    print(f"  [OK] 完成！共保存 {len(saved_paths)} 篇新文章")
    print(f"{'='*50}\n")

    return 0


if __name__ == "__main__":
    sys.exit(main())
