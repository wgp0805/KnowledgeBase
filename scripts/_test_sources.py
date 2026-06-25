import requests, json, sys
sys.stdout.reconfigure(encoding="utf-8")

headers = {"User-Agent": "Mozilla/5.0", "Content-Type": "application/json"}

# Juejin - test category API
categories = {
    "backend": "6809637769959178254",
    "ai": "6809637773935378440",
    "all": "0",
}
for cat_name, cat_id in categories.items():
    r = requests.post(
        "https://api.juejin.cn/recommend_api/v1/article/recommend_all_feed",
        json={"before": "0", "limit": 5, "category_id": cat_id},
        headers=headers,
        timeout=10
    )
    if r.status_code == 200:
        data = r.json()
        items = data.get("data", [])
        print(f"掘金-{cat_name}: {len(items)} entries")
        for item in items[:3]:
            info = item.get("item_info", {}).get("article_info", {})
            title = info.get("title", "")
            url = f"https://juejin.cn/post/{info.get('article_id', '')}"
            print(f"  - {title[:50]}")
            print(f"    链接: {url}")
    else:
        print(f"掘金-{cat_name}: status={r.status_code}")

# Zhihu daily
print("\n=== 知乎日报 ===")
r = requests.get("https://daily.zhihu.com/", headers=headers, timeout=10)
from bs4 import BeautifulSoup
soup = BeautifulSoup(r.text, "html.parser")
for a in soup.select("a")[:10]:
    text = a.get_text(strip=True)
    href = a.get("href", "")
    if text and len(text) > 10:
        print(f"  - {text[:60]}")
        print(f"    链接: {href[:60]}")
