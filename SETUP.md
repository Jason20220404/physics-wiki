# Setup — how to run this wiki

This is a Claude-Code-native knowledge wiki. No software to install beyond an agent + Obsidian.

## Layout
```
physics-wiki/
├── CLAUDE.md   ← the schema (the agent's rules — this is the whole "product")
├── index.md    ← catalog
├── log.md      ← append-only history
├── raw/        ← immutable sources (you add these)
├── ref/        ← explication pages (agent writes; magnetic-potential-energy is the seed)
├── think/      ← your conclusions (you own)
└── output/     ← generated artifacts
```

## Run it
1. Open this folder as an **Obsidian vault** (browse `ref/`, use graph view, follow `[[links]]`).
2. In the **same folder**, start **Claude Code** (or any agent that reads CLAUDE.md). It picks
   up the schema automatically.
3. Two commands drive everything:
   - `explicate <a statement you're stuck on>` → opens a new `ref/` page, joints unexpanded.
   - `saturate Jnn` → expands one joint: classifies it, earns/refuses its warrant, waits.

## The one knob
`saturation_depth` (in CLAUDE.md / page frontmatter): keep at **1** while you're learning the
agent's failure modes. One layer per click is the only view where you can catch a fabricated
warrant before a long chain hides it. Raise to `∞` once you trust it — the stop rule
(bedrock `▣` or `[unverified]`) holds at any depth.

## The point
The agent exposes joints and earns warrants **on your click**. It never runs in the background,
never fills a warrant it can't back (it marks `?!` instead), and never decides a synthesis for
you. You de-compress; you decide.
