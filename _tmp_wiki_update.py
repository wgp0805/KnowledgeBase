# -*- coding: utf-8 -*-
"""修复脚本：清理重复插入，干净重插一次，完成 log.md。"""
WIKI = r'D:\java\KnowledgeBase\wiki'

def read(p):
    with open(p, 'rb') as f:
        return f.read()
def write(p, raw):
    with open(p, 'wb') as f:
        f.write(raw)
def detect_eol(raw):
    return '\r\n' if b'\r\n' in raw else '\n'

def remove_lines(path, markers):
    raw = read(path)
    eol = detect_eol(raw)
    lines = raw.decode('utf-8').split(eol)
    kept = [l for l in lines if not any(m in l for m in markers)]
    removed = len(lines) - len(kept)
    write(path, eol.join(kept).encode('utf-8'))
    return removed

def insert_after(path, anchor, new_lines):
    raw = read(path)
    eol = detect_eol(raw)
    lines = raw.decode('utf-8').split(eol)
    idx = None
    for i, l in enumerate(lines):
        if anchor in l:
            idx = i  # 取最后一个匹配
    if idx is None:
        raise Exception("anchor not found: " + anchor)
    lines = lines[:idx+1] + new_lines + lines[idx+1:]
    write(path, eol.join(lines).encode('utf-8'))
    return idx + 1

def insert_at_top(path, new_text):
    raw = read(path)
    eol = detect_eol(raw)
    text = raw.decode('utf-8')
    new_full = new_text.rstrip(eol) + eol + eol + text
    write(path, new_full.encode('utf-8'))

# === 1. 清理所有之前插入的痕迹（含重复） ===
print("clean index.md:", remove_lines(WIKI + r'\index.md',
    ['摘要-高并发短链接系统设计', '[[Caffeine]]', '[[Leaf]]',
     '[[短链接系统]]', '[[分布式发号器]]', '[[Base62编码]]',
     '[[布隆过滤器]]', '[[哈希碰撞]]', '[[HTTP重定向]]', '[[缓存雪崩]]']))
print("clean snowflake:", remove_lines(WIKI + r'\concepts\雪花算法.md',
    ['[[分布式发号器]]', '[[Leaf]]']))
print("clean sharding:", remove_lines(WIKI + r'\concepts\sharding.md',
    ['[[短链接系统]]']))

# === 2. 干净地重新插入一次 ===
insert_after(WIKI + r'\concepts\雪花算法.md', '摘要-分库分表六大痛点',
    ['- [[分布式发号器]] - 发号器场景下的应用', '- [[Leaf]] - 号段模式工程化组件'])
insert_after(WIKI + r'\concepts\sharding.md', '[[idempotency]]',
    ['- [[短链接系统]] - 短链按短码哈希分库分表的应用场景'])
insert_after(WIKI + r'\index.md', '[[摘要-pi-agent-production-guide]]',
    ['- [[摘要-高并发短链接系统设计]] - 高并发短链接系统设计面试题：发号器+Base62、读多写少缓存架构、301/302 重定向'])
insert_after(WIKI + r'\index.md', '[[markdown-it]]',
    ['- [[Caffeine]] - Java 高性能本地缓存库，W-TinyLFU 算法',
     '- [[Leaf]] - 百度开源分布式 ID 生成组件，号段+雪花双模式'])
# Concepts 区改用纯 wikilink anchor，规避 EM DASH 分隔符不匹配
insert_after(WIKI + r'\index.md', '[[降级]]',
    ['- [[短链接系统]] - 长/短链映射服务，读多写少的高并发系统设计',
     '- [[分布式发号器]] - 分布式环境下生成全局唯一递增 ID 的组件',
     '- [[Base62编码]] - 62 字符进制编码，短链 ID 压缩为短码',
     '- [[布隆过滤器]] - 概率型数据结构，缓存穿透防护',
     '- [[哈希碰撞]] - 不同输入得到相同哈希值，MD5 短链方案核心缺陷',
     '- [[HTTP重定向]] - 3xx 状态码跳转机制，短链选 302 临时重定向',
     '- [[缓存雪崩]] - 大量缓存 key 集中过期压垮数据库，含穿透/击穿对比'])

# === 3. log.md 顶部追加（之前未执行） ===
log_entry = (
    "## [2026-08-05] ingest | 摄入「面试经典：高并发短链接系统设计」\n"
    "- **变更**: 新增 source [[摘要-高并发短链接系统设计]]; "
    "新增 concepts [[短链接系统]], [[分布式发号器]], [[Base62编码]], "
    "[[布隆过滤器]], [[哈希碰撞]], [[HTTP重定向]], [[缓存雪崩]]; "
    "新增 entities [[Caffeine]], [[Leaf]]; "
    "增量更新 [[雪花算法]]（补充发号器场景与 Leaf 关联）、"
    "[[sharding]]（补充短链分库分表场景关联）; "
    "更新 [[index.md]]（1 source + 7 concepts + 2 entities）\n"
    "- **冲突**: 无\n"
    "- **归档**: raw/01-articles/面试经典：如何设计高并发短链接系统.md -> raw/09-archive/"
)
insert_at_top(WIKI + r'\log.md', log_entry)

print("ALL DONE")
