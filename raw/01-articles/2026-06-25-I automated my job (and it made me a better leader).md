---
title: "I automated my job (and it made me a better leader)"
source: "GitHub Blog"
url: "https://github.blog/developer-skills/github/i-automated-my-job-and-it-made-me-a-better-leader/"
date: "Tue, 23 Jun 2026 16:00:00 +0000"
score: 1.0
tags: ["Git", "开源", "开发工具", "DevOps"]
auto_captured: true
---

# I automated my job (and it made me a better leader)

> **来源**: GitHub Blog  
> **链接**: https://github.blog/developer-skills/github/i-automated-my-job-and-it-made-me-a-better-leader/  
> **抓取日期**: 2026-06-25  
> **相关性评分**: 1.0

Here’s the thing about senior leadership that nobody warns you about: the job isn’t hard because of any single task. It’s hard because your work lives in fifteen different places and your brain is the only system connecting them.

Meetings bleed into each other. Decisions are made in threads without you. Someone mentioned your name in a planning meeting, and now there’s an action item living in a doc you’ve never seen. You’ll find out about it in two weeks when someone casually asks for an update. Fun.

Last year, my team almost missed a performance review deadline because it was announced in a channel nobody was watching. One person spent ten minutes searching Slack and couldn’t find it. Another found the date in a random, unrelated channel. I ended up posting “I’ll admit we dropped the ball on following up in Slack, so that’s on me.” That’s the kind of thing that keeps happening when your brain is the only system connecting everything.

I was spending so much energy on context-switching that I had nothing left for the thinking, connecting, and creating that my role actually requires (and that’s the work I actually like doing). But I started using automations in the [GitHub Copilot app](<https://github.com/features/ai/github-app?utm_source=blog-automations&utm_medium=blog&utm_campaign=github-copilot-app-ga-2026>), and it changed my entire workflow. Bear with me.

## What automations actually are

[](<https://github.com/github/blog/blob/2817a371f278fc5a95b054b5a8c84a32012347f6/blog-drafts/i-automated-my-leadership-job/index.md#what-automations-actually-are>)The [GitHub Copilot app](<https://github.com/features/ai/github-app?utm_source=blog-automations&utm_medium=blog&utm_campaign=github-copilot-app-ga-2026>) is a standalone desktop app for macOS, Windows, and Linux, built for working _with_ agents, not just talking to them. You can run parallel sessions across repositories, each on its own branch and worktree. You can see what agents are doing in real time through canvases, which are bidirectional work surfaces where you and the agent operate on the same plan, terminal, or browser session. Progress is visible and steerable, not buried in chat history.

Automations are scheduled prompts that run against your real work context: your calendar, your email, your messages, your GitHub repos. They connect through MCP servers and integrations, so they can see what’s happening across all the places your work lives. They tell me what actually needs my attention, which lets me ignore the rest.

Think of them as agents with a standing brief. You tell them what to care about, how to think, and when to run. Then they just… do it. Every day. Without you remembering to ask. Which is good, because you won’t.

## What this looks like

[](<https://github.com/github/blog/blob/2817a371f278fc5a95b054b5a8c84a32012347f6/blog-drafts/i-automated-my-leadership-job/index.md#what-this-looks-like>)I’m a senior director at GitHub. I lead developer relations. My scope is wide, my calendar is full, and my brain works differently than most people assume. I’m AuDHD, which means I’m good at pattern recognition and deep focus, but genuinely terrible at remembering which thread I promised to follow up on three days ago.

I didn’t set out to build 40 automations. I was curious about the automations tab, asked the app what it could do, and it suggested things I hadn’t thought of. The first time I set one up, I opened a chat and said something like: “Look across all of my work surfaces, my calendar, my email, my messages, and figure out where I’m dropping balls, where I might need help, and suggest automations that would be useful.”

It immediately suggested about six. The first drafts weren’t perfect, and that’s okay. You refine them. You give them voice. You teach them how you think. Once I saw what was possible, I kept going. Now I have about 40. (I know. I know.)

I’m not going to walk through all of them. (You’re welcome.) But here are the categories that matter most, and some highlights from each.

### The morning brief

[](<https://github.com/github/blog/blob/2817a371f278fc5a95b054b5a8c84a32012347f6/blog-drafts/i-automated-my-leadership-job/index.md#the-morning-brief>)Every day before I open anything, several automations have already run. **Meeting Prep** pulls my calendar and builds context for every meeting, with different formats for one-on-ones vs. large syncs vs. external calls. By the time I sit down, I know what each meeting is about and what I need to bring. **Pre-Meeting Access Check** verifies I actually have access to the docs and links referenced in the invite. No more showing up and realizing the agenda doc is locked. If you’ve never experienced that particular panic, honestly, must be nice. **Daily Triage Digest** sweeps GitHub, email, and messages for anything that needs my attention.

The cumulative effect is that my mornings went from “frantically opening twelve tabs while pretending I’ve read the agenda” to “reading a few summaries with coffee.” It’s a different life.

### Staying current

[](<https://github.com/github/blog/blob/2817a371f278fc5a95b054b5a8c84a32012347f6/blog-drafts/i-automated-my-leadership-job/index.md#staying-current>)I cannot be surprised by our own launches. That’s literally the job.

**Ship Decoder** finds everything GitHub shipped in the last 24 hours and explains it to me in plain language. This is real context I can use in conversations. **Launch Radar** runs weekly and surfaces upcoming launches that touch my team’s space so I’m never blindsided. These two alone probably save me an hour a day of scrolling through channels trying to piece together what happened. I used to spend that hour. I did not enjoy that hour.

### Career architecture

[](<https://github.com/github/blog/blob/2817a371f278fc5a95b054b5a8c84a32012347f6/blog-drafts/i-automated-my-leadership-job/index.md#career-architecture>)This is the category that surprised me most. I built automations that actively work on career development, and if that sounds weird, stay with me.

**Daily Wins Recap** runs every evening and summarizes what I actually accomplished. This one matters more than it sounds. My default mode is to check something off and immediately move to the next thing. I don’t sit with it. I don’t recognize it. I just keep going. Then performance review season comes around. I have to articulate my impact, and I’m panic-staring at a blank doc trying to remember eight months of work.

This automation keeps a running record so I don’t have to. Think of it as a gratitude practice backed by real data rather than a task list. It counters the “what did I even do today?” spiral that hits hardest on the busy days. On the days when imposter syndrome is loud, I need something that talks back to it with facts. The robot believes in me even when I don’t. That’s oddly moving? I don’t know. It works.

### Team and people

[](<https://github.com/github/blog/blob/2817a371f278fc5a95b054b5a8c84a32012347f6/blog-drafts/i-automated-my-leadership-job/index.md#team-and-people>)This is where I want to be really honest, because I know you might be thinking: _is she automating the human parts of her job?_

No. And that distinction matters to me more than anything else in this post.

**Commitments and Follow-Up Tracker** searches my own messages for things I said I’d do and flags what I haven’t done yet. This one is humbling. And essential. Because when I tell someone “I’ll look into this” and then forget, that’s a trust problem. The automation protects the trust.

The kudos I write are still mine. The noticing is still mine. The automation just makes sure my brain doesn’t steal it from the people who deserve it.

These automations don’t replace connection. They _enable_ it. They give me back the headspace to actually show up for people. Before this system, I’d walk into conversations distracted or running on fumes, because my brain was full of operational noise. Now when I sit down in a one-on-one, I’m actually present. When I write recognition for my team, it’s specific and real.

The automations handle the scaffolding. I do the human work. That’s the deal.

### Maintenance and logistics

[](<https://github.com/github/blog/blob/2817a371f278fc5a95b054b5a8c84a32012347f6/blog-drafts/i-automated-my-leadership-job/index.md#maintenance-and-logistics>)This category covers the boring stuff that quietly eats your week if you let it: **Dependabot PR Triage** finds and merges safe dependency updates across my repos daily. Handled. **Stale Work Finder** surfaces pull requests I opened and forgot, issues that went quiet, branches collecting dust. (We all have those. Don’t lie.) **Travel Logistics Tracker** watches for conference-related threads and consolidates logistics into a single brief. Conference season is chaos. This helps.

## What my automations look like

[](<https://github.com/github/blog/blob/2817a371f278fc5a95b054b5a8c84a32012347f6/blog-drafts/i-automated-my-leadership-job/index.md#what-my-automations-look-like>)Here’s a real one from my setup, the **Stale Work Finder** , so you can see what these prompts actually look like in practice:
    
    
    Find all my stale work across GitHub using the gh CLI. Things that are falling through the cracks.
    
    Check for:
    
    - PRs I opened that haven't received a review in 7+ days
    - PRs I'm assigned to review that I haven't reviewed yet (older than 3 days)
    - Issues assigned to me that have had no activity in 14+ days
    - Draft PRs I own that have been drafts for 2+ weeks
    - For each item show: repo, title, link, how long it's been stale, and who's involved.
    
    Format as:
    
      1. 🔴 Embarrassingly stale (3+ weeks)
      2. 🟡 Getting dusty (1-3 weeks)
      3. 🟢 Just needs a nudge (under a week)

That’s it. That’s the whole automation. You write a prompt, set a schedule, and the agent runs it on your behalf. You can get as detailed or as loose as you want. The app fills in context from your connected tools. It runs every Monday for me and the results are… always a little eye-opening. But it’s better to know.

## The AuDHD part

[](<https://github.com/github/blog/blob/2817a371f278fc5a95b054b5a8c84a32012347f6/blog-drafts/i-automated-my-leadership-job/index.md#the-audhd-part>)I’ll just say it: for me, automations are an accessibility tool.

AuDHD means my executive function and working memory are wildly inconsistent, and the inconsistency is the hardest part to explain to people. Some days I can hold seventeen threads in my head. Other days I forget I have a meeting in 10 minutes. There is no in between. The gap between those days used to scare me, because my team deserves consistent leadership regardless of what my brain is doing on any given Tuesday.

These automations narrow that gap. They make me _consistent_. They mean my team gets the same quality of attention whether my executive function showed up today or not. For me, that’s the difference between thriving and slowly burning out. And I’ve done the burning out part. Zero stars, would not recommend.

## How to start (for real)

[](<https://github.com/github/blog/blob/2817a371f278fc5a95b054b5a8c84a32012347f6/blog-drafts/i-automated-my-leadership-job/index.md#how-to-start-for-real>)If you’re thinking about building something like this, here’s what I’d say: don’t try to automate everything at once. Start with the one thing that causes you the most friction.

For me, it was meeting prep. I kept walking into meetings cold because prep required visiting four different tools and synthesizing information I didn’t have bandwidth to synthesize. One automation fixed that. And once I felt that relief, I kept going. And going. And going.

Could I consolidate some of these? Probably. I have about 40, and I’m sure some of them could be combined. I prefer specificity, but you could easily roll several into one big automation if that’s more your style.

Here’s the trick that worked for me: open a chat in the GitHub Copilot app and ask it to audit your work surfaces. Where are you dropping balls? Where are the repetitive patterns? What’s the thing you keep meaning to do but never get to? Start there.

The first draft won’t be perfect. That’s fine. You refine it in conversation. You teach it your voice, your priorities, how you think about “good.” Then you let it run.

Start with one. See how it feels.

Then build another. And another. And before you know it, you have 40, and you’re writing a blog post about it. Anyway.

## The bigger picture

[](<https://github.com/github/blog/blob/2817a371f278fc5a95b054b5a8c84a32012347f6/blog-drafts/i-automated-my-leadership-job/index.md#the-bigger-picture>)I think we’re at an interesting moment for how people relate to AI at work. The early conversation about AI at work was mostly about generation. Make me a thing. Write me the code. The reality, at least for me, is more like augmentation of invisible labor. The stuff that burns you out but never shows up in your output. The meta-work nobody acknowledges in performance reviews but everyone is buried in.

Every leader I know is overwhelmed by context. Every neurodivergent professional I know is spending enormous energy on systems that neurotypical people navigate without thinking about. Automations won’t fix organizational dysfunction or bad management or an unreasonable workload. But they can give you back enough headspace to actually do the work you’re here to do.

And honestly? That’s enough. That’s a lot.

And look, this is a GitHub product. It’ll also run your dependency updates, triage your issues, do security sweeps across your repos. The developer workflows are exactly what you’d expect. I just happen to use it for the parts of my job nobody talks about.

Make your own automations in the [GitHub Copilot app >](<https://github.com/features/ai/github-app?utm_source=blog-automations&utm_medium=blog&utm_campaign=github-copilot-app-ga-2026>)

The post [I automated my job (and it made me a better leader)](<https://github.blog/developer-skills/github/i-automated-my-job-and-it-made-me-a-better-leader/>) appeared first on [The GitHub Blog](<https://github.blog>).


---
> 原文链接: https://github.blog/developer-skills/github/i-automated-my-job-and-it-made-me-a-better-leader/