---
title: "The only scalable delete is DROP TABLE"
source: "PostgreSQL Weekly"
url: "https://postgresweekly.com/issues/653"
date: "Wed, 17 Jun 2026 00:00:00 +0000"
score: 1.0
tags: ["PostgreSQL", "数据库", "SQL"]
auto_captured: true
---

# The only scalable delete is DROP TABLE

> **来源**: PostgreSQL Weekly  
> **链接**: https://postgresweekly.com/issues/653  
> **抓取日期**: 2026-06-25  
> **相关性评分**: 1.0

| #​653 — June 17, 2026 | [Web Version](<https://postgresweekly.com/link/186683/rss>)  
---|---  
---  
Postgres Weekly  
---  
[![](assets/2026-06-25-The%20only%20scalable%20delete%20is%20DROP%20TABLE/3adbb62ff3c162f7254f3ec833d6e8e7_MD5.jpg)](<https://postgresweekly.com/link/186644/rss>)  
---  
[Scaling Postgres to 226k TPS: A Christmas Day Retrospective](<https://postgresweekly.com/link/186644/rss> "andyatkinson.com") — A meaty post-mortem and tactical walkthrough of how a digital photo-frame company went from having its Postgres deployment crash out during the 2024 holiday season to handling 2025 without a hitch. Andrew Atkinson   
---  
[![](assets/2026-06-25-The%20only%20scalable%20delete%20is%20DROP%20TABLE/c2751a0ed515f00f9599cb0f421a5306_MD5.png)](<https://postgresweekly.com/link/186643/rss>) [Learn How CERN Runs 40% Faster Queries on 95% Less Storage](<https://postgresweekly.com/link/186643/rss> "www.tigerdata.com") — CERN's 800+ SCADA systems generate hundreds of GB of time-series data daily. See how their engineers achieved 95% storage reduction and 40% faster queries with TimescaleDB — inside Postgres. Jun 25, 9 AM ET. Tiger Data (creators of TimescaleDB) sponsor  
---  
[The Only Scalable Delete in Postgres is `DROP TABLE`](<https://postgresweekly.com/link/186645/rss> "planetscale.com") — A reminder that large `DELETE` operations cost more than you think, and how refactoring to a `DROP` or `TRUNCATE` can help in some cases. Tom Pang (PlanetScale)   
---  
**IN BRIEF:**

  * Claire Giordano presents a fantastic roundup of [everything new with Postgres at Microsoft](<https://postgresweekly.com/link/186646/rss>) in the past year, from its hosted services to team members' Postgres 19 contributions.
  * 📺 Microsoft's [POSETTE 2026](<https://postgresweekly.com/link/186647/rss>) virtual Postgres conference is taking place _this week_ , if you want to check out the livestreams.
  * [PgDog](<https://postgresweekly.com/link/186648/rss>) (an open source connection pooler/sharder) has [raised $5.5m in funding](<https://postgresweekly.com/link/186649/rss>).
  * 🇺🇸 [Postgres Summit US](<https://postgresweekly.com/link/186650/rss>) is this September 30-October 2 in NYC. They're [looking for volunteers](<https://postgresweekly.com/link/186651/rss>) if you'd like to help.
  * 🇬🇧 Seven spots remain for next week's [London PostgreSQL Meetup Group](<https://postgresweekly.com/link/186652/rss>) session.

  
---  
🕒 [British Columbia, Time Zones, and Postgres](<https://postgresweekly.com/link/186653/rss> "www.crunchydata.com") — British Columbia [switched to permanent daylight saving time](<https://postgresweekly.com/link/186654/rss>) in March, providing an illustration of a subtle `timestamptz` trap: future local times stored _before_ a `tzdata` update come back an hour wrong! Here’s how to avoid getting caught out. Christopher Winslett (Crunchy Data)   
---  
▶ [How I Got Started Running a Postgres User Group](<https://postgresweekly.com/link/186655/rss> "talkingpostgres.com") — Jeremy Schneider joined Claire Giordano to discuss why local Postgres user groups are career _“express lanes”_ and why the hard work of running one is worth it. [Full transcript.](<https://postgresweekly.com/link/186656/rss>) Talking Postgres Podcast podcast  
---  
💡 The Postgres site maintains [an official list of local user groups](<https://postgresweekly.com/link/186658/rss>) if you want to find one in your area.  
---  
📊 [Write-Heavy `sysbench` Tests on a Large Server: Postgres vs MySQL](<https://postgresweekly.com/link/186661/rss>) – Mark suspects a performance regression in recent Postgres versions and is trying to figure it out. Mark Callaghan 📄 [A Thousand Postgres Branches for $1](<https://postgresweekly.com/link/186664/rss>) – How Xata drastically improved their database provisioning and branching times. Tudor Golubenco (Xata)  
---  
---  
|   
---  
📰 Classifieds  
---  
🧩 [New in pgEdge Control Plane](<https://postgresweekly.com/link/186667/rss>): deploy MCP, RAG, & PostgREST alongside your DB… + systemd preview. When AI writes the data-layer changes, code review stops being a checklist problem. [AgentField](<https://postgresweekly.com/link/186670/rss>) breaks down what review becomes in an AI-native engineering team. [→ Read the post](<https://postgresweekly.com/link/186670/rss>).  
---  
---  
---  
**RELEASES AND CODE:**  
---  
[pg_durable: Durable Execution Inside Postgres](<https://postgresweekly.com/link/186673/rss> "github.com") — Microsoft has open sourced the durable workflow engine it uses in [Azure HorizonDB](<https://postgresweekly.com/link/186674/rss>). There are two [Docker images](<https://postgresweekly.com/link/186675/rss>) running on Postgres 17/18 to experiment with, and [full docs here.](<https://postgresweekly.com/link/186676/rss>) Microsoft   
---  
[pg_ducklake 1.0: A Native Lakehouse in Postgres](<https://postgresweekly.com/link/186677/rss> "pgducklake.select") — An extension that brings columnar storage, vectorized execution, and lakehouse architecture (data lake with a catalog) to Postgres, built with DuckDB and [DuckLake](<https://postgresweekly.com/link/186678/rss>). Relyt   
---  
  
  * [Nandi 3.0](<https://postgresweekly.com/link/186679/rss>) – A migration tool for _Ruby on Rails_ that keeps routine-looking schema changes from taking your database down on large tables.
  * [PostgreSQL Anonymizer 3.1](<https://postgresweekly.com/link/186680/rss>) – Now with Local Differential Privacy (LDP) for stronger privacy 'noise'. Also includes a critical security update with all existing users directed to upgrade ASAP.
  * [pgstream 1.1](<https://postgresweekly.com/link/186681/rss>) – Schema change tracking and CDC tool built around logical replication.
  * 🌐 [osm2pgsql 2.3](<https://postgresweekly.com/link/186682/rss>) – Import OpenStreetMap data into Postgres/PostGIS.

  
---  
---  
  
![](assets/2026-06-25-The%20only%20scalable%20delete%20is%20DROP%20TABLE/7c0468a65b11fa22737726364a0ece63_MD5.gif)


---
> 原文链接: https://postgresweekly.com/issues/653