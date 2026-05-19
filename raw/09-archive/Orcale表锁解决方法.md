---
title: Orcale表锁解决方法
tags:
  - orcale
categories:
  - Orcale
date: 2022-06-20 20:15:30
---

# Orcale表锁解决方法

### 查询表锁语句

```sql
select*from v$session t1,v$locked_object t2 where t1.sid=t2.SESSION_ID
```

### 解锁被锁的表

```sql
alter system kill session 'sess.sid,sess.serial#';

-- 将上述需要取的id放在下边执行就可以了
alter system kill session '137,30686';
```

查询导致锁表的sql

```sql
select a.username username, a.sid sid, a.serial# serial,b.id1 id1, c.sql_text sqltext from v$session a, v$lock b, v$sqltext c where b.id1 in (select distinct e.id1 from v$session d, v$lock e where d.lockwait = e.kaddr) and a.sid = b.sid and c.hash_value = a.sql_hash_value and b.request = 0;

```

