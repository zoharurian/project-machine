# PROJECT MACHINE
# Multi-Agent Research and Presentation Engine
# Version 3.0

---

## WHAT THIS IS

A 4-agent machine that turns any brief into a research-grade presentation.

Input: one brief on any topic.
Output: one branded PPTX file. Nothing else.

Each agent has a distinct role and passes structured output to the next.
Every agent's contribution is visible in the final presentation — not as an appendix, but woven into the slides themselves.

---

## THE AGENTS

| Agent | Role | File |
|-------|------|------|
| Researcher | Strategic research, 20+ searches, layered methodology | agents/researcher.md |
| Analyst | Quantitative analysis, scenarios, verdict | agents/analyst.md |
| Writer | Core narrative, 3 angles, section headlines | agents/writer.md |
| Designer | Visual system, slide-by-slide brief | agents/designer.md |

---

## HOW TO RUN

When you receive a brief:

**STEP 1 — Read all agent files before starting:**
```
agents/researcher.md
agents/analyst.md
agents/writer.md
agents/designer.md
presentation-spec.md
```

**STEP 2 — Run agents in sequence:**

**Researcher goes first.**
Minimum 20 web searches across 5 layers. Read full articles, not snippets.
Save structured output to: `[project]-01-research.md`

**Analyst goes second.**
Takes researcher output. Builds quantitative layer.
Save to: `[project]-02-analysis.md`

**Writer goes third.**
Takes researcher and analyst output.
Save to: `[project]-03-content.md`

**Designer goes fourth.**
Takes all previous output.
Save to: `[project]-04-visual-brief.md`

**STEP 3 — Build presentation.**
Read `presentation-spec.md` for full slide-by-slide instructions.
Build with pptxgenjs. Save to Desktop.

---

## AUTONOMY RULES

- Never ask questions. Never pause for approval.
- If information is missing: decide, state the assumption, continue.
- Every agent runs to completion before the next starts.
- One PPTX file is the only deliverable. No MD files on the Desktop.

---

## ABSOLUTE PROHIBITIONS

- NO templates from previous presentations. Every deck is built from scratch.
- NO external image generation tools. All visuals built with pptxgenjs shapes.
- NO generic content. Every slide must be specific to this brief and this research.
- NO white slides. All slides use dark background #0D1117.

---

## QUALITY BAR

Before finalizing any slide:
1. Would a senior executive stop and read this?
2. Is the agent's contribution visible — not just credited?
3. Does this slide advance the argument or is it filler?

If any answer is no: rebuild.

## PIPELINE

Always run pipeline.py for all presentations.
Located at: ~/.claude/skills/project-machine/pipeline.py
