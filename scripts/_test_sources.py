import requests, json, sys
sys.stdout.reconfigure(encoding="utf-8")

headers = {"User-Agent": "Mozilla/5.0", "Content-Type": "application/json"}

# Try different Juejin API endpoints for latest articles
apis = [
    ("推荐feed", "https://api.juejin.cn/recommend_api/v1/article/recommend_all_feed", {"before": "0", "limit": 10}),
    ("最新文章", "https://api.juejin.cn/content_api/v1/article/query_list", {"cursor": "0", "sort_type": 2, "limit": 10}),
    ("热门文章", "https://api.juejin.cn/content_api/v1/article/query_list", {"cursor": "0", "sort_type": 3, "limit": 10}),
]

for name, url, payload in apis:
    r = requests.post(url, json=payload, headers=headers, timeout=10)
    if r.status_code == 200:
        data = r.json()
        items = data.get("data", [])
        print(f"掘金-{name}: {len(items)} entries")
        for item in items[:3]:
            if "article_info" in item:
                info = item["article_info"]
            elif "item_info" in item:
                info = item["item_info"].get("article_info", {})
            else:
                info = item
            title = info.get("title", "")
            print(f"  - {title[:60]}")
    else:
        print(f"掘金-{name}: status={r.status_code}")

# Try to get Zhihu explore page content with better parsing
print("\n=== 知乎探索页 ===")
r = requests.get("https://www.zhihu.com/explore", headers=headers, timeout=10)
from bs4 import BeautifulSoup
soup = BeautifulSoup(r.text, "html.parser")
# Find all question links
for a in soup.select("a[href*=\"question\"]"):
    text = a.get_text(strip=True)
    href = a.get("href", "")
    if text and len(text) > 10:
        print(f"  - {text[:60]}")
        print(f"    链接: https://www.zhihu.com{href}")
