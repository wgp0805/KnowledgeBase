#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
知识库自动抓取器 (Daily Harvester)
支持 RSS/Atom、API (JSON)、Scrape (HTML) 三种源类型。
"""

import hashlib
import json
import os
import re
import sys
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone, timedelta
from pathlib import Path
from typing import Optional

import feedparser
import requests
import yaml
from bs4 import BeautifulSoup
import html2text
import sys, io
if sys.stdout.encoding and sys.stdout.encoding.upper() not in ("UTF-8", "UTF8"):
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8", errors="replace")


BASE_DIR = Path(__file__).resolve().parent.parent
CONFIG_PATH = BASE_DIR / "scripts" / "sources.yaml"
SEEN_PATH = BASE_DIR / "scripts" / ".seen_urls.json"
RAW_DIR = BASE_DIR / "raw" / "01-articles"
DIGEST_PATH = BASE_DIR / "raw" / "_daily_digest.md"
WIKI_DIR = BASE_DIR / "wiki"

TZ = timezone(timedelta(hours=8))
NOW = datetime.now(TZ)
TODAY = NOW.strftime("%Y-%m-%d")

MAX_WORKERS = 8
FEED_TIMEOUT = 20


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


def _deep_get(obj, path):
    """从嵌套 dict 中按路径取值"""
    for key in path:
        if isinstance(obj, dict):
            obj = obj.get(key, {})
        elif isinstance(obj, list) and len(obj) > 0:
            obj = obj[0].get(key, {}) if isinstance(obj[0], dict) else {}
        else:
            return {}
    return obj


def fetch_feed_rss(source: dict) -> list:
    name = source["name"]
    url = source["url"]
    max_per = source.get("max_per_source", 5)
    print(f"  [RSS] 正在抓取: {name}")
    try:
        feed = feedparser.parse(url)
        entries = []
        for entry in feed.entries[:max_per]:
            content_html = ""
            if entry.get("content"):
                content_html = entry["content"][0].get("value", "")
            elif entry.get("description"):
                content_html = entry["description"]
            entries.append({
                "title": entry.get("title", "无标题"),
                "link": entry.get("link", ""),
                "published": entry.get("published", ""),
                "summary": entry.get("summary", ""),
                "content": content_html,
                "source_name": name,
                "source_tags": source.get("tags", []),
            })
        print(f"    -> 获取 {len(entries)} 篇")
        return entries
    except Exception as e:
        print(f"    [ERR] 抓取失败: {e}")
        return []


def fetch_feed_api(source: dict) -> list:
    name = source["name"]
    url = source["url"]
    max_per = source.get("max_per_source", 5)
    print(f"  [API] 正在抓取: {name}")

    try:
        headers = {"User-Agent": "Mozilla/5.0", "Content-Type": "application/json"}
        method = source.get("method", "GET").upper()
        payload = source.get("payload", None)

        if method == "POST":
            r = requests.post(url, json=payload, headers=headers, timeout=15)
        else:
            r = requests.get(url, headers=headers, timeout=15)
        r.raise_for_status()

        data = r.json()
        data_path = source.get("data_path", ["data"])
        items = _deep_get(data, data_path)

        if not isinstance(items, list):
            items = data.get("data", [])

        item_path = source.get("item_path", [])
        title_field = source.get("title_field", "title")
        link_template = source.get("link_template", "")
        summary_field = source.get("summary_field", "brief_content")

        entries = []
        for item in items[:max_per]:
            # 如果配置了 item_path，先提取嵌套的 item
            raw_item = item
            if item_path:
                raw_item = _deep_get(item, item_path)

            if isinstance(raw_item, dict):
                title = raw_item.get(title_field, "无标题")
                summary = raw_item.get(summary_field, "")
                link = ""
                if link_template:
                    link = link_template.format(**raw_item)
                entries.append({
                    "title": title,
                    "link": link,
                    "published": raw_item.get("published", raw_item.get("ctime", raw_item.get("date", ""))),
                    "summary": summary,
                    "content": raw_item.get("content", raw_item.get("mark_content", "")),
                    "source_name": name,
                    "source_tags": source.get("tags", []),
                })
        print(f"    -> 获取 {len(entries)} 篇")
        return entries
    except Exception as e:
        print(f"    [ERR] 抓取失败: {e}")
        return []


def fetch_feed_scrape(source: dict) -> list:
    name = source["name"]
    url = source["url"]
    max_per = source.get("max_per_source", 5)
    print(f"  [SCRAPE] 正在抓取: {name}")

    try:
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}
        r = requests.get(url, headers=headers, timeout=15)
        r.raise_for_status()

        soup = BeautifulSoup(r.text, "html.parser")
        selector = source.get("selector", "a")
        link_prefix = source.get("link_prefix", "")
        title_attr = source.get("title_attr", None)

        elements = soup.select(selector)[:max_per]
        entries = []
        for el in elements:
            if title_attr:
                title = el.get(title_attr, "").strip()
            else:
                title = el.get_text(strip=True)
            href = el.get("href", "")
            if href and not href.startswith("http"):
                href = link_prefix + href
            if title and href:
                entries.append({
                    "title": title,
                    "link": href,
                    "published": "",
                    "summary": "",
                    "content": "",
                    "source_name": name,
                    "source_tags": source.get("tags", []),
                })
        print(f"    -> 获取 {len(entries)} 篇")
        return entries
    except Exception as e:
        print(f"    [ERR] 抓取失败: {e}")
        return []


def fetch_feed(source: dict) -> list:
    stype = source.get("type", "rss").lower()
    if stype == "api":
        return fetch_feed_api(source)
    elif stype == "scrape":
        return fetch_feed_scrape(source)
    else:
        return fetch_feed_rss(source)


def process_entries(entries: list, seen: set, wiki_tags: list, config: dict) -> list:
    result = []
    filter_cfg = config.get("filter", {})
    min_score = filter_cfg.get("min_score", 0.15)
    max_total = filter_cfg.get("max_total", 50)

    for entry in entries:
        if len(result) >= max_total:
            print(f"  [INFO] 已达当日上限 ({max_total})，停止过滤")
            break

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
        f"# 每日抓取摘要 - {TODAY}",
        "",
        f"| 指标 | 数值 |",
        f"|------|------|",
        f"| 检查条目 | {total_checked} |",
        f"| 新保存 | {len(saved)} |",
        f"| 跳过（去重/低分） | {skipped_count} |",
        "",
    ]

    if saved:
        lines.append("## 今日新抓取")
        lines.append("")
        for s in saved:
            fname = sanitize_filename(s["title"])
            rel_path = f"raw/01-articles/{TODAY}-{fname}.md"
            lines.append(f"- [[{rel_path}]] - **{s['title']}**")
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
    print(f"  知识库自动抓取 - {TODAY}")
    print(f"{'='*50}\n")

    config = load_config()
    sources = [s for s in config["sources"] if s.get("enabled", True)]
    print(f"[INFO] 已启用信息源: {len(sources)} 个")

    wiki_tags = load_wiki_tags()
    print(f"[INFO] 知识库标签: {len(wiki_tags)} 个")

    seen = load_seen()
    print(f"[INFO] 历史记录: {len(seen)} 条\n")

    all_entries = []
    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        fut_map = {executor.submit(fetch_feed, s): s for s in sources}
        for fut in as_completed(fut_map):
            entries = fut.result()
            all_entries.extend(entries)

    print(f"\n[INFO] 共获取 {len(all_entries)} 篇原始条目")

    saved_entries = process_entries(all_entries, seen, wiki_tags, config)
    skipped = len(all_entries) - len(saved_entries)

    print(f"\n[STATS] 过滤结果:")
    print(f"   [OK] 保存: {len(saved_entries)} 篇")
    print(f"   [SKIP] 跳过: {skipped} 篇（去重/低分）")

    saved_paths = []
    for entry in saved_entries:
        fpath = save_article(entry)
        if fpath:
            saved_paths.append(fpath)
            print(f"   [SAVED] {fpath.name}")

    save_seen(seen)
    generate_digest(saved_entries, skipped, len(all_entries))
    print(f"\n[INFO] 摘要已生成: {DIGEST_PATH}")

    print(f"\n{'='*50}")
    print(f"  [DONE] 完成！共保存 {len(saved_paths)} 篇新文章")
    print(f"{'='*50}\n")

    return 0


if __name__ == "__main__":
    sys.exit(main())
