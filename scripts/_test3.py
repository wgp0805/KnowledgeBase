import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

import requests, json

# Fix Juejin - check actual response structure
headers = {"User-Agent": "Mozilla/5.0", "Content-Type": "application/json"}
r = requests.post(
    "https://api.juejin.cn/recommend_api/v1/article/recommend_all_feed",
    json={"before": "0", "limit": 3},
    headers=headers,
    timeout=10
)
data = r.json()
items = data.get("data", [])
if items:
    item = items[0]
    print("Top-level keys:", list(item.keys()))
    if "item_info" in item:
        print("item_info keys:", list(item["item_info"].keys()))
        if "article_info" in item["item_info"]:
            ai = item["item_info"]["article_info"]
            print("article_info keys:", list(ai.keys()))
            print("title:", ai.get("title",""))
            print("article_id:", ai.get("article_id",""))
