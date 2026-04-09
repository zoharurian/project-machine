# PRESENTATION SPEC
# Dark-theme, agent-attributed, 25-28 slides

---

## DESIGN SYSTEM

**All slides dark. No exceptions.**

| Element | Value |
|---------|-------|
| Background | #0D1117 |
| Card background | #161B22 |
| Top bar | 5px, 3 segments: #D87B2B / #BB1B4E / #1D7AA5 |
| Primary text | #F0F6FC |
| Secondary text | #C9D1D9 |
| Muted text | #8B949E |
| Font | Calibri everywhere. Every addText(): fontFace: 'Calibri' |
| Hebrew RTL | Every addText() with Hebrew: rtlMode: true, align: 'right' |

**Agent colors:**
- Researcher: #1D7AA5 (Steel Blue)
- Analyst: #0D9488 (Teal)
- Writer: #BB1B4E (Deep Rose)
- Designer: #D87B2B (Burnt Orange)

---

## AGENT BADGES

Every content slide gets a badge — bottom-left, visible, not a footnote.

```
x: 0.2, y: 6.8, width: 3.2", height: 0.45"
Background: #161B22
Border: 1.5px in agent color
Border-radius: pill (rectRadius: 0.15)
Content: [SVG icon] + Agent name (11pt bold, agent color) + stats (9pt, #8B949E)
```

SVG icons drawn with addShape/addLine — flat geometric:
- Researcher: magnifying glass (circle + line)
- Analyst: ascending bars
- Writer: document (rect + lines)
- Designer: circle with crosshair

---

## SLIDE STRUCTURE (25-28 slides)

### OPENING (slides 1-3)
1. **Title** — project name + subtitle + "Research Machine: Researcher / Analyst / Writer / Designer"
2. **Divider** — "נתחיל מהסוף" / "Let's start from the end"
3. **Executive answer** — 3 sentences max. The verdict before anything else.

### RESEARCH BLOCK (slides 4-10) — Researcher badge
4. **Chapter divider** — section title, giant text, #BB1B4E
5. **Headline numbers** — 3 stat cards with flat SVG icons + comparison + "why this matters"
6. **Headline numbers 2** — 3 more stat cards
7. **Insight 1** — title + "המשמעות" column + "הזווית הנסתרת" column + action
8. **Insight 2** — same structure
9. **Insight 3** — same structure
10. **Competitive map** — table with dark header, alternating rows

### ANALYSIS BLOCK (slides 11-16) — Analyst badge
11. **Chapter divider**
12. **Verdict** — GO / NO-GO / GO-WITH-CONDITIONS, large, no hedging
13. **Weighted scoring** — table, 7 signals, scores visible
14. **Scenario table** — 3 columns, triggers, probabilities, actions
15. **Data critique** — "מה שהמספרים מסתירים"
16. **Risk matrix** — 4 risks, probability, impact, mitigation

### NARRATIVE BLOCK (slides 17-19) — Writer badge
17. **Chapter divider**
18. **Featured quote** — full dark slide, one sentence, giant text
19. **Core argument** — editorial layout, flowing text, section headlines

### ACTION BLOCK (slides 20-24) — All agents
20. **Chapter divider**
21. **Implementation roadmap** — Now / Short / Long
22. **Strategic verdict** — specific, dated, with consequences
23. **Key takeaways** — one per agent, labeled

### CLOSING (slides 24-26)
24. **Chapter divider** — "Discussion"
25. **Process log** — searches, models, angles, time
26. **Sources** — organized by agent and layer

---

## CHAPTER DIVIDERS

One word or short phrase. Nothing else.
- Background: #0D1117
- Text: #BB1B4E, 88pt, Calibri bold, centered
- Three thin bars below: #D87B2B / #BB1B4E / #1D7AA5, 4px height

---

## CARDS

```javascript
// Glass card
slide.addShape(pptx.ShapeType.roundRect, {
  x, y, w, h,
  fill: { color: '161B22' },
  line: { color: AGENT_COLOR, width: 1.5 },
  rectRadius: 0.08
});
// Top accent
slide.addShape(pptx.ShapeType.rect, {
  x, y, w, h: 0.04,
  fill: { color: AGENT_COLOR },
  line: { color: AGENT_COLOR }
});
```

---

## HEBREW RULES

- No parentheses () — use colon or dash instead
- Numbers before units: "2,000 מהנדסים" not "מהנדסים 2,000"
- English terms after Hebrew: "מערכת של JPMorgan" not "JPMorgan מערכת"
- No "פיילוט" — use "ניסוי"
- No "אז מה?" — use "המשמעות"
- No "מה אף אחד לא מדבר עליו" — use "הזווית הנסתרת"
- No "ROI" — use "תשואה"
- Full Hebrew dates: "אפריל 2026" not "Apr 2026"

---

## TECHNICAL

- Dimensions: 10" x 7.5" (LAYOUT_WIDE)
- Build with: pptxgenjs
- Save to: ~/Desktop/[project-name].pptx
- Speaker notes: 2-3 sentences per slide
