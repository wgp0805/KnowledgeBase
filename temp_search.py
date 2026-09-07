import sqlite3
import sys
import datetime
sys.stdout.reconfigure(encoding='utf-8')
conn = sqlite3.connect(r'C:\Users\w1217\.local\share\mimocode\mimocode.db')
cursor = conn.cursor()

# 计算时间戳
now = datetime.datetime.now()
one_month_ago = now - datetime.timedelta(days=30)
now_ms = int(now.timestamp() * 1000)
one_month_ago_ms = int(one_month_ago.timestamp() * 1000)

# 搜索用户消息中的重复关键词
keywords = ['again', 'every time', 'like last time', 'the usual', 'repeat', 'same as before', '重复', '再次', '每次', '像上次一样', '通常', '一样']

print('搜索用户消息中的重复关键词:')
for keyword in keywords:
    cursor.execute('''
    SELECT m.id, m.session_id, substr(json_extract(p.data, '$.text'), 1, 200) as text_preview
    FROM message m
    JOIN part p ON p.message_id = m.id
    WHERE json_extract(m.data, '$.role') = 'user'
      AND json_extract(p.data, '$.type') = 'text'
      AND json_extract(p.data, '$.text') LIKE ?
      AND m.time_created > ? AND m.time_created <= ?
    LIMIT 5
    ''', (f'%{keyword}%', one_month_ago_ms, now_ms))
    
    results = cursor.fetchall()
    if results:
        print(f'\n关键词 "{keyword}" 找到 {len(results)} 条匹配:')
        for result in results:
            msg_id, session_id, text_preview = result
            print(f'  会话 {session_id}: {text_preview[:100]}...')

conn.close()