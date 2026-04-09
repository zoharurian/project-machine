# Project Machine

A 4-agent research and presentation engine for Claude Code.

Give it a brief on any topic. It researches, analyzes, writes, designs, and builds a presentation — autonomously, end to end.

---

## How it works

```
Brief
  └── Orchestrator
        ├── Researcher  → 20+ searches, 5 layers, McKinsey-grade synthesis
        ├── Analyst     → Quantitative models, scenarios, verdict
        ├── Writer      → 3 angles, core narrative, section headlines
        └── Designer    → Visual system, slide-by-slide brief
              └── Final PPTX (25-28 slides, dark theme, agent-attributed)
```

Every agent's contribution is visible in the slides — not as a footnote, but as a designed element woven throughout the deck.

---

## Installation

**Requirements:** Claude Code, Node.js

```bash
git clone https://github.com/[your-username]/project-machine
cd project-machine
chmod +x install.sh && ./install.sh
npm install -g pptxgenjs
```

The install script copies all files to `~/.claude/skills/project-machine/`.

---

## Usage

Open Claude Code:
```bash
claude --dangerously-skip-permissions
```

Run the machine:
```
Run project-machine on this brief: [your topic here]
```

---

## Customization

**Add your voice:** Edit `agents/writer.md` — define your writing style, tone, and constraints.

**Add your brand:** Edit `agents/designer.md` — add your colors, fonts, and visual motifs.

**Change the orchestrator:** Edit `CLAUDE.md` to modify the flow or add agents.

---

## File structure

```
project-machine/
├── CLAUDE.md               # Orchestrator (auto-read by Claude Code)
├── presentation-spec.md    # Slide-by-slide design instructions
├── install.sh              # Installation script
├── README.md               # This file
└── agents/
    ├── researcher.md       # Strategic research methodology
    ├── analyst.md          # Quantitative analysis framework
    ├── writer.md           # Content strategy and narrative
    └── designer.md         # Visual system and design direction
```

---

## License

MIT — use freely, modify freely, share freely.
