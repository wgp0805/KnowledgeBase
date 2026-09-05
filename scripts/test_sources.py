"""测试 sources.yaml 中所有源的可达性"""
import requests
import yaml
import json
import sys
from urllib.parse import urljoin

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

def load_sources():
    with open('scripts/sources.yaml', 'r', encoding='utf-8') as f:
        data = yaml.safe_load(f)
    return data['sources']

def test_rss(url):
    """测试 RSS 源：返回内容是否像 XML/RSS"""
    try:
        resp = requests.get(url, headers=HEADERS, timeout=15)
        if resp.status_code != 200:
            return False, f"HTTP {resp.status_code}"
        text = resp.text[:2000].strip()
        if '<rss' in text or '<feed' in text or '<?xml' in text:
            # 简单计数 item/entry
            item_count = text.lower().count('<item') + text.lower().count('<entry')
            return True, f"OK (RSS/Atom, 前2000字符含 {item_count} 条)"
        return False, f"响应非 RSS/XML (前100字符: {text[:100]})"
    except Exception as e:
        return False, f"异常: {type(e).__name__}: {e}"

def test_api(url, method='GET', payload=None):
    """测试 API 源：返回 JSON 且能解析"""
    try:
        if method.upper() == 'POST':
            resp = requests.post(url, json=payload, headers=HEADERS, timeout=15)
        else:
            resp = requests.get(url, headers=HEADERS, timeout=15)
        if resp.status_code != 200:
            return False, f"HTTP {resp.status_code}"
        data = resp.json()
        return True, f"OK (JSON, 顶层键: {list(data.keys()) if isinstance(data, dict) else type(data).__name__})"
    except json.JSONDecodeError:
        return False, f"响应非 JSON (前100字符: {resp.text[:100]})"
    except Exception as e:
        return False, f"异常: {type(e).__name__}: {e}"

def test_scrape(url, selector_hint=None):
    """测试 scrape 源：返回 HTML 且能匹配到链接"""
    try:
        resp = requests.get(url, headers=HEADERS, timeout=15)
        if resp.status_code != 200:
            return False, f"HTTP {resp.status_code}"
        text = resp.text
        # 简单检查是否有内容
        if len(text) < 500:
            return False, f"响应过短 ({len(text)} 字符)"
        # 检查 selector hint 是否能匹配
        if selector_hint:
            # selector_hint 形如 "a[href*='/question/']" -> 提取 '/question/'
            import re
            m = re.search(r"href\*='([^']+)'", selector_hint)
            if m:
                pattern = m.group(1)
                count = text.count(pattern)
                if count > 0:
                    return True, f"OK (HTML, 匹配到 {count} 处 '{pattern}')"
                else:
                    return False, f"HTML 正常但未匹配到 selector '{pattern}' (可能需要 JS 渲染)"
        return True, f"OK (HTML, {len(text)} 字符)"
    except Exception as e:
        return False, f"异常: {type(e).__name__}: {e}"

def main():
    sources = load_sources()
    print(f"共 {len(sources)} 个源，开始测试...\n")
    results = []
    for s in sources:
        name = s['name']
        stype = s['type']
        url = s['url']
        print(f"--- [{name}] ({stype}) ---")
        print(f"URL: {url}")
        if stype == 'rss':
            ok, msg = test_rss(url)
        elif stype == 'api':
            ok, msg = test_api(url, s.get('method', 'GET'), s.get('payload'))
        elif stype == 'scrape':
            ok, msg = test_scrape(url, s.get('selector'))
        else:
            ok, msg = False, f"未知类型: {stype}"
        status = "[OK]" if ok else "[FAIL]"
        print(f"结果: {status} - {msg}\n")
        results.append((name, stype, ok, msg))

    print("\n========== 汇总 ==========")
    ok_count = sum(1 for r in results if r[2])
    fail_count = len(results) - ok_count
    print(f"可用: {ok_count}  不可用: {fail_count}  总计: {len(results)}\n")
    if fail_count > 0:
        print("不可用列表:")
        for name, stype, ok, msg in results:
            if not ok:
                print(f"  [FAIL] [{name}] ({stype}): {msg}")

if __name__ == '__main__':
    main()
