import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

import feedparser, requests, json, time

# Test juejin AI category more carefully
headers = {"User-Agent": "Mozilla/5.0", "Content-Type": "application/json"}

# Try without category_id for AI
r = requests.post(
    "https://api.juejin.cn/recommend_api/v1/article/recommend_all_feed",
    json={"before": "0", "limit": 5},
    headers=headers,
    timeout=10
)
data = r.json()
items = data.get("data", [])
print(f"掘金-无分类: {len(items)} entries")
for item in items[:3]:
    info = item.get("item_info", {}).get("article_info", {})
    title = info.get("title", "")
    article_id = info.get("article_id", "")
    tags = [t.get("tag_name","") for t in (info.get("tags", []) or [])]
    print(f"  - {title[:50]}")
    print(f"    id: {article_id}, tags: {tags}")
    print(f"    link: https://juejin.cn/post/{article_id}")

# Test juejin with category_id in the right format
print("\n=== 掘金 category_id test ===")
for cat_id in ["6809637769959178254", "6809637773935378440"]:
    r = requests.post(
        "https://api.juejin.cn/recommend_api/v1/article/recommend_all_feed",
        json={"before": "0", "limit": 5, "category_id": cat_id},
        headers=headers,
        timeout=10
    )
    data = r.json()
    items = data.get("data", [])
    print(f"category_id={cat_id}: {len(items)} entries")
    for item in items[:2]:
        info = item.get("item_info", {}).get("article_info", {})
        title = info.get("title", "")
        article_id = info.get("article_id", "")
        print(f"  - {title[:50]} (id={article_id})")

# Test cnblogs with different URL
print("\n=== 博客园 RSS ===")
for url in ["https://www.cnblogs.com/rss.aspx", "https://feed.cnblogs.com/blog/picked/rss"]:
    feed = feedparser.parse(url)
    print(f"{url}: {len(feed.entries)} entries")
    for entry in feed.entries[:2]:
        print(f"  - {entry.get('title','')[:60]}")
