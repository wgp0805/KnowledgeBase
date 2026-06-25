---
title: "A chat with the creator of Postgres"
source: "PostgreSQL Weekly"
url: "https://postgresweekly.com/issues/651"
date: "Wed, 3 Jun 2026 00:00:00 +0000"
score: 1.0
tags: ["PostgreSQL", "数据库", "SQL"]
auto_captured: true
---

# A chat with the creator of Postgres

> **来源**: PostgreSQL Weekly  
> **链接**: https://postgresweekly.com/issues/651  
> **抓取日期**: 2026-06-25  
> **相关性评分**: 1.0

| #​651 — June 3, 2026 | [Web Version](<https://postgresweekly.com/link/186045/rss>)  
---|---  
---  
Postgres Weekly  
---  
[![](assets/2026-06-25-A%20chat%20with%20the%20creator%20of%20Postgres/8c3d834ab3b11978d5bc3649b3df51ea_MD5.jpg)](<https://postgresweekly.com/link/186020/rss>)  
---  
[Handling Graphs with `SQL/PGQ` in Postgres 19](<https://postgresweekly.com/link/186020/rss> "www.cybertec-postgresql.com") — Postgres 19 is adding support for SQL/PGQ, so you can declare a property graph over tables and pattern-match with Cypher-_like_ `MATCH (a IS person)-[IS knows]->(b IS person)` queries. It’s all handled by the query _rewriter_ , so a graph pattern becomes a normal relational query. Hans-Jürgen Schönig   
---  
💡 Want graph queries on _today’s_ Postgres? Elizabeth Garrett Christensen [shows how the Apache AGE extension](<https://postgresweekly.com/link/186021/rss>) brings openCypher to current versions.  
---  
[![](assets/2026-06-25-A%20chat%20with%20the%20creator%20of%20Postgres/42c13cc3ebbf6c1fc9f9584b7f4e7742_MD5.webp)](<https://postgresweekly.com/link/186019/rss>) [95% Less Storage. 40% Faster Analytics. CERN on Postgres](<https://postgresweekly.com/link/186019/rss> "www.tigerdata.com") — CERN's Large Hadron Collider generates hundreds of GB of time-series data daily. In this live webinar, their engineers walk through how they modernized a legacy archiving stack with TimescaleDB. June 25, 9 AM ET. Tiger Data (creators of TimescaleDB) sponsor  
---  
🔓 [Why Postgres Lacks Transparent Data Encryption](<https://postgresweekly.com/link/186022/rss> "www.pgedge.com") — Many other databases have it, but in Postgres you need to lean on third party services or the [pg-tde](<https://postgresweekly.com/link/186023/rss>) extension. Why? Shaun digs into old discussions about the feature, and finds the biggest problem is defining _what_ problem that TDE actually needs to solve. Shaun Thomas   
---  
**IN BRIEF:**

  * [Postgres 19 Beta 1 has been tagged](<https://postgresweekly.com/link/186024/rss>) on the official repo by Tom Lane. There's little to see yet, but a beta announcement seems to be imminent.
  * Microsoft has made its VS Code extension for Postgres [available on the Open VSX registry](<https://postgresweekly.com/link/186025/rss>) (an independent extension store for VS Code compatible editors) so that tools like Cursor can now use it directly.
  * Postgres managed by ClickHouse [is now in beta](<https://postgresweekly.com/link/186026/rss>).

  
---  
[Helping the Planner Help You](<https://postgresweekly.com/link/186027/rss> "www.valerieparhamthompson.com") — When two columns are correlated, Postgres assumes they’re independent and the planner’s row estimates go badly wrong. A practical tour of `CREATE STATISTICS` and the better query plans it unlocks. Valerie Parham-Thompson   
---  
[Egress Problems and Where to Find Them](<https://postgresweekly.com/link/186028/rss> "planetscale.com") — If your database is running in someone else’s datacenter, data egress and associated costs are important to control. Simeon shares tips on how to get the numbers down, along with some PlanetScale-specific advice. Simeon Griggs (PlanetScale)   
---  
📄 [The Night Our Tables Wouldn’t Stop Growing](<https://postgresweekly.com/link/186029/rss>) – A production whodunit: a stray `statement_timeout` quietly broke logical replication and tables ballooned. Semab Tariq 📄 [Postgres Outages That Aren’t Postgres Bugs](<https://postgresweekly.com/link/186030/rss>) – Three OS-level failures that show up as database outages. Payal Singh 📄 [Same Query, Three Results](<https://postgresweekly.com/link/186031/rss>) – One query, three benchmark passes, three very different verdicts between ParadeDB and Postgres FTS. A lesson in how methodology colors the answer. James Blackwood-Sewell (ParadeDB) 📄 [When is a Function `LEAKPROOF`?](<https://postgresweekly.com/link/186032/rss>) Laurenz Albe  
---  
---  
|   
---  
📰 Classifieds  
---  
Spot N+1 queries before your users do. [AppSignal](<https://postgresweekly.com/link/186033/rss>) auto-monitors Postgres performance with real-time alerts. [Try free](<https://postgresweekly.com/link/186033/rss>). 🔎 [Introducing pg_search](<https://postgresweekly.com/link/186034/rss>), a Postgres extension for Elasticsearch-quality full-text, vector and hybrid search in Postgres. 🐘 [Spock 5.0.7](<https://postgresweekly.com/link/186035/rss>): PG18 slotsync integration, add-node data race fix, apply-worker recovery. [Open source multi-master Postgres](<https://postgresweekly.com/link/186035/rss>).  
---  
---  
---  
**RELEASES AND CODE:**  
---  
[DeltaX (δx): Fast Time-Series Extension for Postgres](<https://postgresweekly.com/link/186036/rss> "github.com") — A new columnar storage extension for time-series data from Xata that uses only regular Postgres tables, so things like replication, crash recovery, backups, and `pg_dump` work as they usually would. Here’s [how it works](<https://postgresweekly.com/link/186037/rss>). Xata   
---  
[Streambed: Stream Postgres to Iceberg on S3](<https://postgresweekly.com/link/186038/rss> "github.com") — Streams WAL via logical replication, writes Parquet to S3, and commits Iceberg metadata. You can then query with plain `psql` thanks to a built-in wire-protocol server. viggy28   
---  
[ingestr v1: Copy Data to and from Databases in One Command](<https://postgresweekly.com/link/186039/rss> "github.com") — A Go-powered tool to move data (with incremental append/merge support) between [a myriad of sources and destinations](<https://postgresweekly.com/link/186040/rss>) (Postgres included) without writing code. Bruin Data   
---  
  
  * 🔎 [pg_textsearch 1.3](<https://postgresweekly.com/link/186041/rss>) – Tiger Data's extension for BM25 relevance-ranked full-text search. v1.3 includes revisions for compatibility with disaggregated storage architectures.
  * [SeaQuery 1.0](<https://postgresweekly.com/link/186042/rss>) – Dynamic query builder for Postgres/MySQL/SQLite in Rust.

  
---  
---  
**📺 ONE LAST THING — WORTH A WATCH:**  
---  
[![](assets/2026-06-25-A%20chat%20with%20the%20creator%20of%20Postgres/c5d348f7a1a3b16cb3f105499fda07c4_MD5.jpg)](<https://postgresweekly.com/link/186043/rss>)  
---  
[Postgres at 30: A Chat With Its Creator](<https://postgresweekly.com/link/186043/rss> "www.youtube.com") — With Postgres turning 30 this year, here’s a treat: a wide-ranging interview with Mike Stonebraker, the man who started the Postgres project. He covers how Postgres came to be, where he thinks Google and Amazon get databases wrong, and what he’s building next. The Peterman Pod   
---  
💡 Prefer to read? There’s a [full transcript](<https://postgresweekly.com/link/186044/rss>) too.  
---  
---  
  
![](assets/2026-06-25-A%20chat%20with%20the%20creator%20of%20Postgres/7c0468a65b11fa22737726364a0ece63_MD5.gif)


---
> 原文链接: https://postgresweekly.com/issues/651