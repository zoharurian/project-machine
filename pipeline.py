#!/usr/bin/env python3
"""
Food Future v3 — Complete rebuild with all fixes.
HTML→PNG→PPTX | 42 slides | No offset | Large pictograms | Deep content
"""
import asyncio, os, tempfile
from pathlib import Path

# ═══════ BRAND ═══════
BG='#0D1117'; CARD='#161B22'; A1='#D87B2B'; A2='#BB1B4E'; A3='#1D7AA5'; A4='#0D9488'
TP='#F0F6FC'; TS='#8B949E'; BD='#30363D'; GRN='#22C55E'; YEL='#EAB308'; RED='#EF4444'
ACOLS={'RESEARCHER':A3,'ANALYST':A4,'WRITER':A2,'DESIGNER':A1}
AHEB={'RESEARCHER':'חוקר','ANALYST':'אנליסט','WRITER':'כותב','DESIGNER':'מעצב'}

# ═══════ LARGE PICTOGRAM SVGS (150x150 display) ═══════
PSVG={
'wheat':'''<svg viewBox="0 0 64 64" fill="none" stroke="{c}" stroke-width="1.8" stroke-linecap="round"><path d="M32 58V28"/><path d="M32 28c-4-8-14-12-18-10s2 12 10 14"/><path d="M32 28c4-8 14-12 18-10s-2 12-10 14"/><path d="M32 38c-4-6-12-9-15-7s1 10 9 11"/><path d="M32 38c4-6 12-9 15-7s-1 10-9 11"/><path d="M32 48c-3-5-9-7-12-5s1 8 7 9"/><path d="M32 48c3-5 9-7 12-5s-1 8-7 9"/></svg>''',
'dna':'''<svg viewBox="0 0 64 64" fill="none" stroke="{c}" stroke-width="2" stroke-linecap="round"><path d="M20 8c0 12 24 12 24 24s-24 12-24 24"/><path d="M44 8c0 12-24 12-24 24s24 12 24 24"/><line x1="22" y1="20" x2="42" y2="20"/><line x1="20" y1="32" x2="44" y2="32"/><line x1="22" y1="44" x2="42" y2="44"/></svg>''',
'globe':'''<svg viewBox="0 0 64 64" fill="none" stroke="{c}" stroke-width="2"><circle cx="32" cy="32" r="26"/><ellipse cx="32" cy="32" rx="12" ry="26"/><line x1="6" y1="32" x2="58" y2="32"/><path d="M10 18h44"/><path d="M10 46h44"/></svg>''',
'brain':'''<svg viewBox="0 0 64 64" fill="none" stroke="{c}" stroke-width="2" stroke-linecap="round"><path d="M32 56V32"/><path d="M24 12a10 10 0 0118 0"/><path d="M18 22a8 8 0 010 12"/><path d="M46 22a8 8 0 000 12"/><circle cx="26" cy="20" r="6" fill="{c}" opacity=".15"/><circle cx="38" cy="20" r="6" fill="{c}" opacity=".15"/><circle cx="20" cy="32" r="5" fill="{c}" opacity=".1"/><circle cx="44" cy="32" r="5" fill="{c}" opacity=".1"/><path d="M22 40c3 4 7 6 10 6s7-2 10-6"/></svg>''',
'drop':'''<svg viewBox="0 0 64 64" fill="none" stroke="{c}" stroke-width="2"><path d="M32 6C32 6 12 30 12 42a20 20 0 0040 0C52 30 32 6 32 6z" fill="{c}" opacity=".1"/><path d="M32 6C32 6 12 30 12 42a20 20 0 0040 0C52 30 32 6 32 6z"/></svg>''',
'layers':'''<svg viewBox="0 0 64 64" fill="none" stroke="{c}" stroke-width="2" stroke-linecap="round"><path d="M32 8L6 24l26 16 26-16z" fill="{c}" opacity=".1"/><path d="M32 8L6 24l26 16 26-16z"/><path d="M6 32l26 16 26-16"/><path d="M6 40l26 16 26-16"/></svg>''',
'shield':'''<svg viewBox="0 0 64 64" fill="none" stroke="{c}" stroke-width="2"><path d="M32 4L8 16v18c0 14 10 22 24 26 14-4 24-12 24-26V16z" fill="{c}" opacity=".08"/><path d="M32 4L8 16v18c0 14 10 22 24 26 14-4 24-12 24-26V16z"/><path d="M24 32l6 6 12-12" stroke-width="3"/></svg>''',
'pill':'''<svg viewBox="0 0 64 64" fill="none" stroke="{c}" stroke-width="2"><rect x="12" y="22" width="40" height="20" rx="10" fill="{c}" opacity=".1"/><rect x="12" y="22" width="40" height="20" rx="10"/><line x1="32" y1="22" x2="32" y2="42"/></svg>''',
'flag':'''<svg viewBox="0 0 64 64" fill="none" stroke="{c}" stroke-width="2"><line x1="14" y1="8" x2="14" y2="58"/><path d="M14 8h32l-8 12 8 12H14" fill="{c}" opacity=".12"/><path d="M14 8h32l-8 12 8 12H14"/></svg>''',
'chart':'''<svg viewBox="0 0 64 64" fill="none" stroke="{c}" stroke-width="2"><rect x="8" y="36" width="10" height="20" rx="2" fill="{c}" opacity=".2"/><rect x="22" y="24" width="10" height="32" rx="2" fill="{c}" opacity=".3"/><rect x="36" y="14" width="10" height="42" rx="2" fill="{c}" opacity=".2"/><rect x="50" y="8" width="10" height="48" rx="2" fill="{c}" opacity=".3"/><line x1="4" y1="58" x2="62" y2="58"/></svg>''',
'target':'''<svg viewBox="0 0 64 64" fill="none" stroke="{c}" stroke-width="2"><circle cx="32" cy="32" r="26" fill="{c}" opacity=".05"/><circle cx="32" cy="32" r="26"/><circle cx="32" cy="32" r="17"/><circle cx="32" cy="32" r="8"/><circle cx="32" cy="32" r="2" fill="{c}"/></svg>''',
'road':'''<svg viewBox="0 0 64 64" fill="none" stroke="{c}" stroke-width="2" stroke-linecap="round"><path d="M8 56L28 8h8L56 56" fill="{c}" opacity=".06"/><path d="M8 56L28 8h8L56 56"/><line x1="32" y1="16" x2="32" y2="24" stroke-dasharray="4 4"/><line x1="32" y1="30" x2="32" y2="38" stroke-dasharray="4 4"/><line x1="32" y1="44" x2="32" y2="52" stroke-dasharray="4 4"/></svg>''',
'search':'''<svg viewBox="0 0 64 64" fill="none" stroke="{c}" stroke-width="2.5"><circle cx="28" cy="28" r="18" fill="{c}" opacity=".06"/><circle cx="28" cy="28" r="18"/><line x1="40" y1="40" x2="56" y2="56" stroke-width="3"/></svg>''',
'doc':'''<svg viewBox="0 0 64 64" fill="none" stroke="{c}" stroke-width="2"><path d="M40 4H16a4 4 0 00-4 4v48a4 4 0 004 4h32a4 4 0 004-4V16z" fill="{c}" opacity=".06"/><path d="M40 4H16a4 4 0 00-4 4v48a4 4 0 004 4h32a4 4 0 004-4V16z"/><polyline points="40 4 40 16 52 16"/><line x1="20" y1="28" x2="44" y2="28"/><line x1="20" y1="36" x2="44" y2="36"/><line x1="20" y1="44" x2="36" y2="44"/></svg>''',
}

def picto(key, color, size=150, x='40px', y='40px', opacity=0.12):
    svg = PSVG.get(key, PSVG['search']).replace('{c}', color)
    return f'<div style="position:absolute;left:{x};top:{y};width:{size}px;height:{size}px;opacity:{opacity};z-index:0;pointer-events:none;">{svg}</div>'

def conf(level, source):
    c = GRN if level=='HIGH' else YEL if level=='MEDIUM' else RED
    return f'<span style="display:inline-block;padding:3px 12px;border:1.5px solid {c};border-radius:5px;font-size:11px;color:{c};font-weight:700;background:rgba(0,0,0,0.4);margin-top:6px;">{level} | {source}</span>'

# ═══════ HTML TEMPLATE — ALL FIXES APPLIED ═══════
def html_slide(content, agent='RESEARCHER', stats='', icon='search', num=1):
    ac=ACOLS.get(agent,A3); ah=AHEB.get(agent,agent)
    badge_svg=PSVG.get(icon,PSVG['search']).replace('{c}',ac)
    return f'''<!DOCTYPE html>
<html lang="he">
<head>
<meta charset="UTF-8">
<style>
@import url('https://fonts.googleapis.com/css2?family=Heebo:wght@300;400;500;700;900&display=swap');
*{{margin:0;padding:0;box-sizing:border-box;}}
body{{
  position:fixed;top:0;left:0;
  width:1333px;height:750px;overflow:hidden;
  font-family:'Calibri','Heebo',sans-serif;
  color:{TP};background:{BG};
}}
.slide{{width:1333px;height:750px;position:relative;display:grid;grid-template-rows:auto 1fr 60px;padding:0;}}
.topbar{{height:4px;display:flex;}}
.topbar .o{{flex:1;background:{A1};}} .topbar .r{{flex:1;background:{A2};}} .topbar .b{{flex:1;background:{A3};}}
.main{{padding:30px 50px;position:relative;overflow:hidden;display:flex;flex-direction:column;}}
.footer{{display:flex;align-items:center;justify-content:space-between;padding:0 50px;}}
.badge{{display:flex;align-items:center;gap:10px;background:rgba(0,0,0,0.55);border:2px solid {ac};border-radius:10px;padding:8px 18px;height:52px;}}
.badge svg{{width:26px;height:26px;color:{ac};flex-shrink:0;}}
.badge .nm{{font-size:15px;font-weight:700;color:{ac};direction:rtl;}}
.badge .st{{font-size:10px;color:{ac};opacity:0.8;}}
.sn{{font-size:11px;color:{TS};}}
.blob1{{position:absolute;top:-15%;right:-8%;width:55%;height:55%;background:radial-gradient(ellipse,rgba(187,27,78,0.06) 0%,transparent 70%);pointer-events:none;}}
.blob2{{position:absolute;bottom:-15%;left:-8%;width:55%;height:55%;background:radial-gradient(ellipse,rgba(216,123,43,0.04) 0%,transparent 70%);pointer-events:none;}}
.h1{{font-size:52px;font-weight:900;line-height:1.1;direction:rtl;text-align:right;}}
.h2{{font-size:28px;font-weight:900;line-height:1.2;direction:rtl;text-align:right;border-bottom:2px solid {BD};padding-bottom:10px;margin-bottom:16px;}}
.h3{{font-size:20px;font-weight:700;direction:rtl;text-align:right;}}
.t{{font-size:15px;font-weight:400;line-height:1.65;color:rgba(255,255,255,0.75);direction:rtl;text-align:right;}}
.ts{{font-size:13px;color:{TS};direction:rtl;text-align:right;}}
.lbl{{font-size:11px;font-weight:700;letter-spacing:1px;text-transform:uppercase;}}
.g{{background:rgba(255,255,255,0.04);border:1px solid rgba(255,255,255,0.08);border-radius:12px;padding:22px;position:relative;}}
.ga{{border-top:3px solid;}}
.flex{{display:flex;}} .gap{{gap:16px;}} .f1{{flex:1;min-width:0;}} .col{{flex-direction:column;}}
.ctr{{display:flex;align-items:center;justify-content:center;}}
</style>
</head>
<body>
<div class="slide">
  <div class="topbar"><div class="o"></div><div class="r"></div><div class="b"></div></div>
  <div class="main">
    <div class="blob1"></div><div class="blob2"></div>
    {content}
  </div>
  <div class="footer">
    <div class="badge">
      <svg viewBox="0 0 24 24" style="width:26px;height:26px;" fill="none" stroke="{ac}" stroke-width="2">{badge_svg.split('stroke-width="')[0].split('<svg')[1].split('>')[-1] if '<' in badge_svg else ''}</svg>
      <div style="display:flex;flex-direction:column;">
        <span class="nm">{ah}</span>
        <span class="st">{stats}</span>
      </div>
    </div>
    <div class="sn">{num} / 45</div>
  </div>
</div>
</body>
</html>'''

# Simpler badge SVG extraction — just use inline mini SVGs
def html_s(content, agent='RESEARCHER', stats='', icon='search', num=1):
    ac=ACOLS.get(agent,A3); ah=AHEB.get(agent,agent)
    mini_svgs = {
        'search':'<circle cx="10" cy="10" r="6" fill="none" stroke="{c}" stroke-width="2"/><line x1="14" y1="14" x2="20" y2="20" stroke="{c}" stroke-width="2.5"/>',
        'chart':'<rect x="2" y="13" width="4" height="8" fill="{c}" opacity=".4"/><rect x="8" y="8" width="4" height="13" fill="{c}" opacity=".4"/><rect x="14" y="3" width="4" height="18" fill="{c}" opacity=".4"/>',
        'doc':'<path d="M14 2H6a2 2 0 00-2 2v16a2 2 0 002 2h12a2 2 0 002-2V8z" fill="none" stroke="{c}" stroke-width="1.5"/><line x1="8" y1="13" x2="16" y2="13" stroke="{c}"/><line x1="8" y1="17" x2="14" y2="17" stroke="{c}"/>',
        'target':'<circle cx="12" cy="12" r="9" fill="none" stroke="{c}" stroke-width="1.5"/><circle cx="12" cy="12" r="5" fill="none" stroke="{c}"/><circle cx="12" cy="12" r="1.5" fill="{c}"/>',
        'globe':'<circle cx="12" cy="12" r="9" fill="none" stroke="{c}" stroke-width="1.5"/><path d="M12 3a18 18 0 010 18M12 3a18 18 0 000 18" fill="none" stroke="{c}"/><line x1="3" y1="12" x2="21" y2="12" stroke="{c}"/>',
        'shield':'<path d="M12 2L4 6v5c0 5.5 3.4 10 8 12 4.6-2 8-6.5 8-12V6z" fill="none" stroke="{c}" stroke-width="1.5"/>',
        'water':'<path d="M12 2S4 12 4 17a8 8 0 0016 0c0-5-8-15-8-15z" fill="none" stroke="{c}" stroke-width="1.5"/>',
        'brain':'<circle cx="9" cy="9" r="4" fill="none" stroke="{c}"/><circle cx="15" cy="9" r="4" fill="none" stroke="{c}"/><path d="M7 14c2 3 4 5 5 5s3-2 5-5" fill="none" stroke="{c}"/>',
        'pill':'<rect x="4" y="8" width="16" height="8" rx="4" fill="none" stroke="{c}" stroke-width="1.5"/><line x1="12" y1="8" x2="12" y2="16" stroke="{c}"/>',
        'dna':'<path d="M8 2c0 5 8 5 8 10s-8 5-8 10" fill="none" stroke="{c}" stroke-width="1.5"/><path d="M16 2c0 5-8 5-8 10s8 5 8 10" fill="none" stroke="{c}" stroke-width="1.5"/>',
        'flag':'<line x1="6" y1="3" x2="6" y2="21" stroke="{c}" stroke-width="1.5"/><path d="M6 3h12l-4 5 4 5H6" fill="none" stroke="{c}" stroke-width="1.5"/>',
        'road':'<path d="M4 20l8-16h0l8 16" fill="none" stroke="{c}" stroke-width="1.5"/><line x1="12" y1="8" x2="12" y2="18" stroke="{c}" stroke-dasharray="2 2"/>',
        'layers':'<path d="M12 3L2 10l10 7 10-7z" fill="none" stroke="{c}" stroke-width="1.5"/><path d="M2 14l10 7 10-7" fill="none" stroke="{c}"/><path d="M2 18l10 7 10-7" fill="none" stroke="{c}"/>',
        'wheat':'<line x1="12" y1="22" x2="12" y2="8" stroke="{c}" stroke-width="1.5"/><path d="M12 8c-2-4-7-5-8-4s1 5 5 6" fill="none" stroke="{c}"/><path d="M12 8c2-4 7-5 8-4s-1 5-5 6" fill="none" stroke="{c}"/><path d="M12 14c-2-3-5-4-6-3s0 4 4 5" fill="none" stroke="{c}"/><path d="M12 14c2-3 5-4 6-3s0 4-4 5" fill="none" stroke="{c}"/>',
    }
    ms = mini_svgs.get(icon, mini_svgs['search']).replace('{c}', ac)
    return f'''<!DOCTYPE html>
<html lang="he">
<head>
<meta charset="UTF-8">
<style>
@import url('https://fonts.googleapis.com/css2?family=Heebo:wght@300;400;500;700;900&display=swap');
*{{margin:0;padding:0;box-sizing:border-box;}}
body{{position:fixed;top:0;left:0;width:1333px;height:750px;overflow:hidden;font-family:'Calibri','Heebo',sans-serif;color:{TP};background:{BG};}}
.S{{width:1333px;height:750px;position:relative;display:grid;grid-template-rows:4px 1fr 56px;}}
.bar{{display:flex;}}.bar .o{{flex:1;background:{A1};}}.bar .r{{flex:1;background:{A2};}}.bar .b{{flex:1;background:{A3};}}
.M{{padding:28px 50px;position:relative;overflow:hidden;display:flex;flex-direction:column;}}
.F{{display:flex;align-items:center;justify-content:space-between;padding:0 50px;}}
.bdg{{display:flex;align-items:center;gap:10px;background:rgba(0,0,0,0.55);border:2.5px solid {ac};border-radius:10px;padding:6px 16px;height:44px;}}
.bdg svg{{width:22px;height:22px;flex-shrink:0;}}
.bdg .n{{font-size:15px;font-weight:700;color:{ac};}}
.bdg .s{{font-size:10px;color:{ac};opacity:0.75;}}
.sn{{font-size:11px;color:{TS};}}
.bl1{{position:absolute;top:-15%;right:-8%;width:55%;height:55%;background:radial-gradient(ellipse,rgba(187,27,78,0.06) 0%,transparent 70%);pointer-events:none;z-index:0;}}
.bl2{{position:absolute;bottom:-15%;left:-8%;width:55%;height:55%;background:radial-gradient(ellipse,rgba(216,123,43,0.04) 0%,transparent 70%);pointer-events:none;z-index:0;}}
.Z{{position:relative;z-index:1;flex:1;display:flex;flex-direction:column;}}
.h1{{font-size:52px;font-weight:900;line-height:1.1;direction:rtl;text-align:right;}}
.h2{{font-size:26px;font-weight:900;line-height:1.2;direction:rtl;text-align:right;border-bottom:2px solid {BD};padding-bottom:8px;margin-bottom:14px;}}
.h3{{font-size:18px;font-weight:700;direction:rtl;text-align:right;}}
.t{{font-size:14px;line-height:1.6;color:rgba(255,255,255,0.72);direction:rtl;text-align:right;}}
.ts{{font-size:12px;color:{TS};direction:rtl;text-align:right;}}
.g{{background:rgba(255,255,255,0.04);border:1px solid rgba(255,255,255,0.08);border-radius:10px;padding:18px;position:relative;}}
.flex{{display:flex;}}.gap{{gap:14px;}}.f1{{flex:1;min-width:0;}}.col{{flex-direction:column;}}
.ctr{{display:flex;align-items:center;justify-content:center;}}
</style>
</head>
<body>
<div class="S">
  <div class="bar"><div class="o"></div><div class="r"></div><div class="b"></div></div>
  <div class="M">
    <div class="bl1"></div><div class="bl2"></div>
    <div class="Z">{content}</div>
  </div>
  <div class="F">
    <div class="bdg"><svg viewBox="0 0 24 24" fill="none">{ms}</svg><div style="display:flex;flex-direction:column;"><span class="n">{ah}</span><span class="s">{stats}</span></div></div>
    <div class="sn">{num} / 45</div>
  </div>
</div>
</body>
</html>'''

# ═══════ SLIDE DEFINITIONS ═══════
slides = []
def S(content, agent='RESEARCHER', stats='', icon='search'):
    slides.append((content, agent, stats, icon))

# SLIDE 1: TITLE
S(f'''
{picto('wheat',A1,180,'50px','30px',0.1)}
<div style="display:flex;flex-direction:column;height:100%;justify-content:center;position:relative;z-index:1;">
  <div style="font-size:14px;font-weight:700;color:{A1};margin-bottom:12px;direction:rtl;text-align:right;">מחקר אסטרטגי: אפריל 2026</div>
  <div class="h1" style="max-width:1000px;">עתיד המזון<br>בעוד 20 שנה</div>
  <div style="font-size:18px;color:{TS};margin-top:16px;direction:rtl;text-align:right;max-width:900px;">לא טכנולוגיית מזון תקבע את העתיד. תרופות, גיאופוליטיקה ובינה מלאכותית יקבעו.</div>
  <div style="width:180px;height:3px;background:{A1};margin-top:28px;border-radius:2px;"></div>
  <div style="margin-top:14px;font-size:13px;color:{TS};direction:rtl;text-align:right;">מכונת המחקר | Project Machine</div>
</div>
''','DESIGNER','Visual System: Narrative Bold','target')

# SLIDE 2: DIVIDER
S(f'''
{picto('search',A2,200,'580px','80px',0.08)}
<div class="ctr" style="height:100%;flex-direction:column;">
  <div style="font-size:88px;font-weight:900;color:{A2};direction:rtl;text-align:center;">נתחיל מהסוף</div>
  <div style="display:flex;gap:12px;margin-top:32px;">
    <div style="width:70px;height:4px;background:{A1};border-radius:2px;"></div>
    <div style="width:70px;height:4px;background:{A2};border-radius:2px;"></div>
    <div style="width:70px;height:4px;background:{A3};border-radius:2px;"></div>
  </div>
</div>
''','RESEARCHER','25 חיפושים: מתחילים','search')

# SLIDE 3: THE ANSWER
S(f'''
{picto('target',A4,160,'50px','20px',0.09)}
<div style="display:flex;flex-direction:column;height:100%;justify-content:center;position:relative;z-index:1;">
  <div style="font-size:13px;font-weight:700;color:{A1};margin-bottom:10px;direction:rtl;text-align:right;">התשובה</div>
  <div style="font-size:24px;font-weight:700;color:{TP};line-height:1.55;direction:rtl;text-align:right;max-width:1050px;">עתיד המזון לא נקבע על ידי טכנולוגיית מזון. הוא נקבע על ידי 3 כוחות חיצוניים: תרופות מסוג GLP-1 שמכווצות את הביקוש, גיאופוליטיקה שמאיימת על האספקה, ובינה מלאכותית שמשנה את כל שרשרת הערך.</div>
  <div style="width:180px;height:3px;background:{A2};margin-top:24px;border-radius:2px;"></div>
  <div style="margin-top:14px;padding:10px 18px;border:2px solid {YEL};border-radius:8px;background:rgba(234,179,8,0.08);display:inline-block;direction:rtl;text-align:right;align-self:flex-start;">
    <span style="font-size:13px;font-weight:700;color:{YEL};">GO-WITH-CONDITIONS: חלון של 24 עד 36 חודשים: 3 טכנולוגיות GO, שתיים NO-GO</span>
  </div>
</div>
''','ANALYST','הכרעה: GO-WITH-CONDITIONS','chart')

# SLIDE 4: SCQ
S(f'''
{picto('layers',A3,150,'50px','20px',0.08)}
<div class="h2" style="position:relative;z-index:1;">מצב, סיבוך, שאלה: מסגרת SCQ</div>
<div class="flex gap" style="flex:1;position:relative;z-index:1;">
  <div class="g f1" style="border-right:8px solid {A3};">
    <div class="lbl" style="color:{A3};margin-bottom:8px;">SITUATION</div>
    <div class="t">אוכלוסיית העולם תגיע ל-9.6 מיליארד עד 2050. ייצור מזון חייב לגדול ב-60 אחוז. היבולים ירדו עד 30 אחוז. נדרשים 120 אחוז יותר מים. אקוויפר אוגלאלה: 20 שנה עד התייבשות.</div>
    <div style="margin-top:8px;">{conf('HIGH','IPCC + FAO')}</div>
  </div>
  <div class="g f1" style="border-right:8px solid {A2};">
    <div class="lbl" style="color:{A2};margin-bottom:8px;">COMPLICATION</div>
    <div class="t">תרופות GLP-1 מכווצות ביקוש: 55 מיליארד הפסד. מצר הורמוז קרס: 90 אחוז. תסיסה מדויקת תייצר חלבון זול פי 5 עד 2030. יותר מ-40 חברות נסגרו.</div>
    <div style="margin-top:8px;">{conf('HIGH','JPMorgan + AgFunder')}</div>
  </div>
  <div class="g f1" style="border-right:8px solid {A1};">
    <div class="lbl" style="color:{A1};margin-bottom:8px;">QUESTION</div>
    <div class="t">איך ממצבים ארגון, מדינה, או תעשייה בצד הנכון של 3 מהפכות בו-זמניות, כשחלון ההזדמנות הוא 24 עד 36 חודשים?</div>
  </div>
</div>
''','RESEARCHER','25 חיפושים: SCQ + MECE','search')

# SLIDE 5: STAT CARDS TOP 3
S(f'''
{picto('chart',A1,150,'50px','15px',0.08)}
<div class="h2" style="position:relative;z-index:1;">3 מספרים שעוצרים מנכ"ל באמצע משפט</div>
<div class="flex gap" style="flex:1;position:relative;z-index:1;">
  <div class="g f1" style="border-right:8px solid {A1};text-align:center;">
    <div style="font-size:48px;font-weight:900;color:{A1};">$55B</div>
    <div style="font-size:14px;font-weight:700;color:{TP};margin-top:6px;direction:rtl;">הפסד שנתי מתרופות GLP-1</div>
    <div class="t" style="margin-top:6px;text-align:center;font-size:12px;">1 מכל 8 מבוגרים בארה"ב. חטיפים: ירידה של 10.1 אחוז. מסעדות מהירות: 8 אחוז.</div>
    <div style="margin-top:8px;">{conf('HIGH','JPMorgan')}</div>
  </div>
  <div class="g f1" style="border-right:8px solid {A3};text-align:center;">
    <div style="font-size:48px;font-weight:900;color:{A3};">$540B</div>
    <div style="font-size:14px;font-weight:700;color:{TP};margin-top:6px;direction:rtl;">בזבוז מזון שנתי בעולם</div>
    <div class="t" style="margin-top:6px;text-align:center;font-size:12px;">33 אחוז מהכנסות שרשרת האספקה. גדול מהתוצר של ארגנטינה.</div>
    <div style="margin-top:8px;">{conf('HIGH','Avery Dennison')}</div>
  </div>
  <div class="g f1" style="border-right:8px solid {A4};text-align:center;">
    <div style="font-size:48px;font-weight:900;color:{A4};">40.1%</div>
    <div style="font-size:14px;font-weight:700;color:{TP};margin-top:6px;direction:rtl;">צמיחה שנתית: תסיסה מדויקת</div>
    <div class="t" style="margin-top:6px;text-align:center;font-size:12px;">מ-3.5 ל-34.2 מיליארד דולר עד 2032. חברת Perfect Day כבר מוכרת.</div>
    <div style="margin-top:8px;">{conf('MEDIUM','VMR')}</div>
  </div>
</div>
''','RESEARCHER','25 חיפושים: 6 מספרי מפתח','chart')

# SLIDE 6: STAT CARDS BOTTOM 3
S(f'''
{picto('globe',A2,150,'50px','15px',0.08)}
<div class="h2" style="position:relative;z-index:1;">עוד 3 מספרים שלא עוצרים</div>
<div class="flex gap" style="flex:1;position:relative;z-index:1;">
  <div class="g f1" style="border-right:8px solid {A2};text-align:center;">
    <div style="font-size:48px;font-weight:900;color:{A2};">90%</div>
    <div style="font-size:14px;font-weight:700;color:{TP};margin-top:6px;direction:rtl;">קריסת תנועה במצר הורמוז</div>
    <div class="t" style="margin-top:6px;text-align:center;font-size:12px;">30 אחוז מהדשנים העולמיים. מחירי דשנים עלו ב-20 אחוז.</div>
    <div style="margin-top:8px;">{conf('HIGH','FAO + Kpler')}</div>
  </div>
  <div class="g f1" style="border-right:8px solid {A2};text-align:center;">
    <div style="font-size:48px;font-weight:900;color:{A2};">40+</div>
    <div style="font-size:14px;font-weight:700;color:{TP};margin-top:6px;direction:rtl;">חברות שנסגרו או נרכשו</div>
    <div class="t" style="margin-top:6px;text-align:center;font-size:12px;">בשנה האחרונה: Meatable, Believer, Bowery, AppHarvest.</div>
    <div style="margin-top:8px;">{conf('HIGH','Green Queen')}</div>
  </div>
  <div class="g f1" style="border-right:8px solid {A3};text-align:center;">
    <div style="font-size:48px;font-weight:900;color:{A3};">#2</div>
    <div style="font-size:14px;font-weight:700;color:{TP};margin-top:6px;direction:rtl;">ישראל בחלבון חלופי בעולם</div>
    <div class="t" style="margin-top:6px;text-align:center;font-size:12px;">יותר מ-200 סטארטאפים. 10 אחוז מההשקעות העולמיות.</div>
    <div style="margin-top:8px;">{conf('MEDIUM','GFI Israel')}</div>
  </div>
</div>
''','RESEARCHER','Signal Triangulation','globe')

# Helper for insight slides (3 per topic: overview, data, insight)
def insight_slide(num, title, body_text, nobody, action, conf_lvl, src, accent, pict_icon, badge_icon):
    S(f'''
{picto(pict_icon,accent,160,'40px','10px',0.09)}
<div style="position:absolute;top:0;right:0;width:5px;height:100%;background:{accent};z-index:2;"></div>
<div style="position:relative;z-index:1;">
  <div style="font-size:11px;font-weight:700;color:{accent};direction:rtl;text-align:right;">תובנה {num}</div>
  <div style="font-size:22px;font-weight:900;color:{TP};margin-top:4px;direction:rtl;text-align:right;line-height:1.3;max-width:1100px;">{title}</div>
</div>
<div class="flex gap" style="margin-top:12px;flex:1;position:relative;z-index:1;">
  <div class="g f1" style="border-right:8px solid {A2};">
    <div style="font-size:11px;font-weight:700;color:{A2};margin-bottom:6px;direction:rtl;text-align:right;">אז מה?</div>
    <div class="t" style="font-size:13px;">{body_text}</div>
  </div>
  <div style="display:flex;flex-direction:column;gap:10px;flex:1;">
    <div class="g f1" style="border-right:8px solid {A1};">
      <div style="font-size:11px;font-weight:700;color:{A1};margin-bottom:6px;direction:rtl;text-align:right;">מה שאף אחד לא מדבר עליו</div>
      <div class="t" style="font-size:13px;">{nobody}</div>
    </div>
    <div style="padding:12px 16px;background:rgba(216,123,43,0.08);border:1.5px solid {A1};border-radius:8px;">
      <div style="font-size:12px;font-weight:700;color:{TP};direction:rtl;text-align:right;">פעולה: {action}</div>
    </div>
  </div>
</div>
<div style="margin-top:6px;position:relative;z-index:1;">{conf(conf_lvl,src)}</div>
''', 'RESEARCHER', f'{conf_lvl}: {src}', badge_icon)

# ═══════ 6 INSIGHTS (slides 7-12) ═══════
insight_slide('01','תרופה לסוכרת משנה את תעשיית המזון יותר מכל סטארטאפ שנוסד אי פעם',
'1 מכל 8 מבוגרים בארה"ב על GLP-1. צריכת קלוריות ירדה ב-21 אחוז. חטיפים: ירידה של 10.1 אחוז. הוצאה על מזון: ירידה של 5.3 אחוז למשק בית. חברת Mars רכשה את Kellanova ב-35.9 מיליארד דולר.',
'אם שיעור השימוש יגיע ל-30 אחוז, כל מודל עסקי של חברת מזון גדולה יתמוטט. זו לא מגמה: זה שינוי מבני בביקוש.',
'לבנות אסטרטגיית מוצרים: עתירי חלבון, דלי קלוריות. דדליין: 90 יום.',
'HIGH','JPMorgan + Cornell',A1,'pill','pill')

insight_slide('02','מזון הפך לנשק גיאופוליטי, ורוב המדינות לא ערוכות לזה',
'רוסיה: 200 אלף טון חיטה חינם ל-6 מדינות באפריקה, בתמורה לבסיסים צבאיים. סין: אפס מכס ל-53 מדינות, תלות בזרעים. ארה"ב נסוגה: 1,000 מטבחים נסגרו בסודן. יותר מ-20 מדינות חוסמות ייצוא.',
'סינגפור זנחה את התוכנית "30 by 30" לטובת אסטרטגיית ריבונות מזון חדשה.',
'לבחון חשיפה לנקודות חנק. לגוון ספקים. דדליין: 60 יום.',
'HIGH','War on the Rocks + FAO',A3,'globe','globe')

insight_slide('03','בשר מתורבת כבר מת. תסיסה מדויקת היא הסוס המנצח.',
'70 עד 90 אחוז מהחברות ייכשלו. עלות: 63 דולר לקילו לעומת 6 דולר בשר. 122 מוצרים נבדקו: אף אחד לא הגיע לאיכות טעם. תסיסה מדויקת: 34.2 מיליארד עד 2032, צמיחה של 40.1 אחוז. חברת Perfect Day: 802 מיליון, מוכרת.',
'80 אחוז מעלות הייצור של בשר מתורבת: מדיום, ביוריאקטורים, עבודה. אין נתיב לשוויון מחירים. לתסיסה מדויקת יש.',
'להזיז תקציב מבשר מתורבת לתסיסה מדויקת.',
'MEDIUM','AgFunderNews + RethinkX',A4,'dna','dna')

insight_slide('04','משבר המים: הפצצה המתקתקת שאף אחד לא מדבר עליה',
'אקוויפר אוגלאלה: 20 שנה עד התייבשות. 25 אחוז מהמים לחקלאות אמריקה. ירידה צפויה של 50 מיליארד דולר. 90 אחוז מהשאיבה = חקלאות. חקלאים בקנזס ובטקסס: ירידה של 30 אחוז בתשואות.',
'מחירי מים הם האינדיקטור המקדים הבא. עלייה של 20 אחוז תסמן קריסה.',
'לעקוב אחרי מחירי מים. להשקיע בהתפלה ובהשקיה חכמה.',
'HIGH','USDA ERS + FAO',A1,'drop','water')

insight_slide('05','בינה מלאכותית בחקלאות: לא פיצ\'ר, שכבת הפעלה. מי בעל הנתונים?',
'שוק: 3.37 מיליארד ב-2026, 8.2 מיליארד עד 2030. מערכת Cropwise: 70 מיליון דונם. 78 אחוז מחברות המזון כבר משתמשות. צמצום בזבוז: 35 אחוז. שוק חקלאות דיגיטלית: 84 מיליארד עד 2033.',
'חוק החקלאות 2026: סבסוד 90 אחוז נשמע טוב, אבל "תקנים של המגזר הפרטי" = Google ו-Microsoft.',
'לאמץ בינה מלאכותית עם בעלות מלאה על נתונים. תקנים פתוחים.',
'MEDIUM','Fortune + WEF',A3,'brain','brain')

insight_slide('06','לאומיות מזון: יותר מ-20 מדינות משתמשות באוכל כנשק',
'הודו: איסור חיטה 4 שנים, אורז 75-80 אחוז. בלארוס, מאלי, ניגריה, גאנה. מדבדב: "רק לחברים." איסורי ייצוא הוסיפו 45 אחוז למחירי אורז ו-30 אחוז לחיטה ב-2007-08.',
'כל משבר אקלים = גל איסורים = עליית מחירים = עוד איסורים. לולאה הרסנית.',
'מלאי אסטרטגי. הסכמי אספקה ארוכי טווח עם מדינות מגוונות.',
'HIGH','IFPRI + UNCTAD',A2,'flag','flag')

# SLIDE 13: CHOKEPOINTS
S(f'''
{picto('globe',A2,150,'40px','10px',0.08)}
<div class="h2" style="position:relative;z-index:1;">נקודות החנק של המזון העולמי</div>
<div style="display:flex;flex-direction:column;gap:8px;flex:1;position:relative;z-index:1;">
  <div class="flex g" style="padding:10px 16px;border-right:8px solid {A2};align-items:center;">
    <div style="flex:2;direction:rtl;text-align:right;"><span style="font-weight:700;color:{A2};">מצר הורמוז</span><br><span class="ts">30 אחוז דשנים, 20 מיליון חביות נפט ליום</span></div>
    <div style="flex:1;text-align:center;font-weight:700;color:{RED};">קריסה: 90 אחוז</div>
    <div>{conf('HIGH','FAO')}</div>
  </div>
  <div class="flex g" style="padding:10px 16px;border-right:8px solid {A1};align-items:center;">
    <div style="flex:2;direction:rtl;text-align:right;"><span style="font-weight:700;color:{A1};">תעלת סואץ</span><br><span class="ts">12 אחוז מהסחר העולמי</span></div>
    <div style="flex:1;text-align:center;font-weight:700;color:{YEL};">שיבושי חות'ים</div>
    <div>{conf('HIGH','UNCTAD')}</div>
  </div>
  <div class="flex g" style="padding:10px 16px;border-right:8px solid {A3};align-items:center;">
    <div style="flex:2;direction:rtl;text-align:right;"><span style="font-weight:700;color:{A3};">תעלת פנמה</span><br><span class="ts">5 אחוז מהסחר העולמי</span></div>
    <div style="flex:1;text-align:center;font-weight:700;color:{YEL};">בצורת אקלים</div>
    <div>{conf('MEDIUM','UNCTAD')}</div>
  </div>
  <div class="flex g" style="padding:10px 16px;border-right:8px solid {A4};align-items:center;">
    <div style="flex:2;direction:rtl;text-align:right;"><span style="font-weight:700;color:{A4};">מצר מלאקה</span><br><span class="ts">25 אחוז סחר ימי</span></div>
    <div style="flex:1;text-align:center;font-weight:700;color:{YEL};">מתח סין-טייוואן</div>
    <div>{conf('MEDIUM','CSR')}</div>
  </div>
</div>
''','RESEARCHER','HIGH: 5 נקודות חנק','globe')

# SLIDE 14: VERTICAL FARMING
S(f'''
{picto('layers',A1,150,'40px','10px',0.08)}
<div class="h2" style="position:relative;z-index:1;">חקלאות אנכית: בית קברות של הבטחות</div>
<div class="flex gap" style="flex:1;position:relative;z-index:1;">
  <div class="g f1" style="border-right:8px solid {A2};">
    <div class="h3" style="color:{A2};margin-bottom:6px;">הקריסות</div>
    <div class="t">Bowery: 700 מיליון, נסגרה. AppHarvest: פשיטת רגל. AeroFarms: Chapter 11. Plenty: Chapter 11. אף חברה לא רווחית.</div>
    <div style="margin-top:8px;">{conf('HIGH','Indoor Ag-Con')}</div>
  </div>
  <div class="g f1" style="border-right:8px solid {A1};">
    <div class="h3" style="color:{A1};margin-bottom:6px;">הבעיה: חשמל</div>
    <div class="t">10 עד 20 אלף דולר בחודש. תאורה, מיזוג, משאבות 24/7. בנו מתקני ענק לפני הוכחת כדאיות.</div>
    <div style="margin-top:8px;">{conf('HIGH','Fast Company')}</div>
  </div>
  <div class="g f1" style="border-right:8px solid {A4};">
    <div class="h3" style="color:{A4};margin-bottom:6px;">מה כן עובד</div>
    <div class="t">מודל חדש: קטן, ממוקד, הסכמי רכישה מראש. שוק 7.5 מיליארד וצומח. רק עם scaling ממושמע.</div>
    <div style="margin-top:8px;">{conf('MEDIUM','VerticalFarmDaily')}</div>
  </div>
</div>
''','RESEARCHER','HIGH: חקלאות אנכית','layers')

# SLIDE 15: MICROBIOME
S(f'''
{picto('dna',A4,150,'40px','10px',0.08)}
<div class="h2" style="position:relative;z-index:1;">מיקרוביום ותזונה מותאמת אישית</div>
<div class="flex gap" style="flex:1;position:relative;z-index:1;">
  <div class="g f1" style="border-right:8px solid {A4};">
    <div class="h3" style="color:{A4};margin-bottom:6px;">השוק</div>
    <div class="t">1.6 מיליארד דולר ב-2026, צפוי ל-14.41 מיליארד עד 2034. צמיחה: 31.61 אחוז. 59 אחוז מהצרכנים בוחרים מרכיבים פונקציונליים.</div>
    <div style="margin-top:8px;">{conf('MEDIUM','Fortune BI')}</div>
  </div>
  <div class="g f1" style="border-right:8px solid {A3};">
    <div class="h3" style="color:{A3};margin-bottom:6px;">חברות מובילות</div>
    <div class="t">פלטפורמות ZOE, Viome ו-DayTwo מובילות בדיאגנוסטיקה. תוכניות תזונה על בסיס ריצוף מיקרוביום. חברת Nestle משלבת בפורמולות.</div>
    <div style="margin-top:8px;">{conf('MEDIUM','MarketsandMarkets')}</div>
  </div>
</div>
''','RESEARCHER','MEDIUM: מיקרוביום','dna')

# SLIDE 16: CRISPR
S(f'''
{picto('dna',A1,150,'40px','10px',0.08)}
<div class="h2" style="position:relative;z-index:1;">גידולים ערוכים גנטית: CRISPR משנה כללים</div>
<div class="flex gap" style="flex:1;position:relative;z-index:1;">
  <div class="g f1" style="border-right:8px solid {A1};">
    <div class="h3" style="color:{A1};margin-bottom:6px;">מצב רגולטורי</div>
    <div class="t">ארה"ב: 3 מוצרים מסחריים. האיחוד האירופי: מסגרת חדשה דצמבר 2025, מערכת דו-שכבתית. יפן: מובילה. תותים ועגבניות ערוכים צפויים ב-2026.</div>
    <div style="margin-top:8px;">{conf('MEDIUM','Genetic Literacy')}</div>
  </div>
  <div class="g f1" style="border-right:8px solid {A4};">
    <div class="h3" style="color:{A4};margin-bottom:6px;">היתרון</div>
    <div class="t">עמידות למחלות ויובש, תשואה גבוהה. שמנים דלי שומן טרנס, דגנים עשירי סיבים. שונה מ-GMO: עורך גנים קיימים, לא מכניס זרים.</div>
    <div style="margin-top:8px;">{conf('MEDIUM','Congress.gov')}</div>
  </div>
</div>
''','RESEARCHER','MEDIUM: CRISPR','dna')

# SLIDE 17: SEAWEED
S(f'''
{picto('drop',A3,150,'40px','10px',0.08)}
<div class="h2" style="position:relative;z-index:1;">חקלאות ימית ואצות: חלבון בלי קרקע ומים</div>
<div class="flex gap" style="flex:1;position:relative;z-index:1;">
  <div class="g f1" style="border-right:8px solid {A3};">
    <div class="h3" style="color:{A3};margin-bottom:6px;">שוק ופוטנציאל</div>
    <div class="t">4.4 מיליארד דולר עד 2030. הזדמנויות בינוניות: 6 מיליארד. ספיגת פחמן: 2.48 מיליון טון בשנה. לא דורש מים מתוקים או קרקע.</div>
    <div style="margin-top:8px;">{conf('MEDIUM','Nature.org')}</div>
  </div>
  <div class="g f1" style="border-right:8px solid {A1};">
    <div class="h3" style="color:{A1};margin-bottom:6px;">אתגרים</div>
    <div class="t">98 אחוז מהגידול באסיה. חוסר תשתית בשאר העולם. Ocean Rainforest: מיליון טון בשנה עד 2030. מגזר האקווה-קולצ'ר הצומח ביותר.</div>
    <div style="margin-top:8px;">{conf('MEDIUM','NOAA')}</div>
  </div>
</div>
''','RESEARCHER','MEDIUM: חקלאות ימית','water')

# SLIDE 18: REGENERATIVE AG
S(f'''
{picto('layers',A4,150,'40px','10px',0.08)}
<div class="h2" style="position:relative;z-index:1;">חקלאות רגנרטיבית: לרפא קרקע כדי להאכיל עולם</div>
<div class="flex gap" style="flex:1;position:relative;z-index:1;">
  <div class="g f1" style="border-right:8px solid {A4};">
    <div class="h3" style="color:{A4};margin-bottom:6px;">השוק</div>
    <div class="t">11.7 מיליארד ב-2026, צפוי ל-19.59 מיליארד עד 2030. צמיחה: 13.7 אחוז. ספיגת פחמן צומחת ב-17.86 אחוז.</div>
    <div style="margin-top:8px;">{conf('MEDIUM','Mordor Intelligence')}</div>
  </div>
  <div class="g f1" style="border-right:8px solid {A1};">
    <div class="h3" style="color:{A1};margin-bottom:6px;">פוטנציאל אקלימי</div>
    <div class="t">23 גיגה-טון CO2 עד 2050. חוק שיקום הטבע של האיחוד האירופי: 20 אחוז עד 2030. תוכניות תאגידיות הופכות פיילוטים למיינסטרים.</div>
    <div style="margin-top:8px;">{conf('MEDIUM','IPCC + WEF')}</div>
  </div>
</div>
''','RESEARCHER','MEDIUM: רגנרטיבית','layers')

# SLIDE 19: COMPETITIVE MAP
S(f'''
{picto('globe',A3,150,'40px','10px',0.07)}
<div class="h2" style="position:relative;z-index:1;">מפה תחרותית: 5 שחקנים</div>
<div style="display:flex;flex-direction:column;gap:6px;flex:1;position:relative;z-index:1;">
  <div class="flex g" style="padding:8px 14px;background:rgba(29,122,165,0.12);">
    <div style="width:110px;font-weight:700;color:{TP};direction:rtl;text-align:right;font-size:12px;">שחקן</div>
    <div style="flex:1;font-weight:700;color:{TP};direction:rtl;text-align:right;font-size:12px;">עמדה ופעילות</div>
    <div style="flex:1;font-weight:700;color:{TP};direction:rtl;text-align:right;font-size:12px;">פער</div>
  </div>
  <div class="flex g" style="padding:8px 14px;border-right:8px solid {A1};">
    <div style="width:110px;font-weight:700;color:{A1};direction:rtl;text-align:right;font-size:12px;">ישראל</div>
    <div style="flex:1;direction:rtl;text-align:right;font-size:11px;color:{TS};">מקום 2, יותר מ-200 סטארטאפים, רגולציה מוקדמת</div>
    <div style="flex:1;direction:rtl;text-align:right;font-size:11px;color:{TS};">אין scale, גיוסים ירדו 60 אחוז</div>
  </div>
  <div class="flex g" style="padding:8px 14px;border-right:8px solid {A3};">
    <div style="width:110px;font-weight:700;color:{A1};direction:rtl;text-align:right;font-size:12px;">סינגפור</div>
    <div style="flex:1;direction:rtl;text-align:right;font-size:11px;color:{TS};">חלוצה, עברה לריבונות מזון</div>
    <div style="flex:1;direction:rtl;text-align:right;font-size:11px;color:{TS};">שוק זעיר, תלות ביבוא</div>
  </div>
  <div class="flex g" style="padding:8px 14px;border-right:8px solid {A4};">
    <div style="width:110px;font-weight:700;color:{A1};direction:rtl;text-align:right;font-size:12px;">סין</div>
    <div style="flex:1;direction:rtl;text-align:right;font-size:11px;color:{TS};">יצרנית וקונה, רכישת קרקע באפריקה</div>
    <div style="flex:1;direction:rtl;text-align:right;font-size:11px;color:{TS};">לא מייצאת טכנולוגיית מזון</div>
  </div>
  <div class="flex g" style="padding:8px 14px;border-right:8px solid {A2};">
    <div style="width:110px;font-weight:700;color:{A1};direction:rtl;text-align:right;font-size:12px;">ארה"ב</div>
    <div style="flex:1;direction:rtl;text-align:right;font-size:11px;color:{TS};">מובילה שנסוגה, חוק חקלאות AI</div>
    <div style="flex:1;direction:rtl;text-align:right;font-size:11px;color:{TS};">חברות ענק שולטות בנתונים</div>
  </div>
</div>
''','RESEARCHER','מפה תחרותית: 5 שחקנים','globe')

# SLIDE 20: FARM BILL TROJAN
S(f'''
{picto('shield',A1,170,'40px','20px',0.09)}
<div style="display:flex;flex-direction:column;height:100%;justify-content:center;position:relative;z-index:1;">
  <div style="font-size:36px;font-weight:900;color:{A1};direction:rtl;text-align:right;line-height:1.2;">חוק החקלאות 2026:<br>סוס טרויאני</div>
  <div class="t" style="font-size:15px;margin-top:16px;line-height:1.7;max-width:1050px;">החוק מסבסד 90 אחוז מעלות אימוץ בינה מלאכותית. לכאורה, חדשנות. בפועל: הפעם הראשונה שטכנולוגיות ספציפיות מקבלות העדפה. התוצאה: תלות בנתונים של Google, Microsoft ו-John Deere. החקלאי מוותר על בעלות. כמו זרעים מהונדסים: ברגע שנכנסים, אין חזרה.</div>
  <div class="g" style="margin-top:14px;padding:10px 14px;border-right:8px solid {A1};max-width:600px;">
    <div class="ts" style="font-style:italic;">מגזין Fortune, מרץ 2026</div>
  </div>
  <div style="margin-top:10px;">{conf('HIGH','Fortune')}</div>
</div>
''','RESEARCHER','Signal Triangulation','shield')

# SLIDE 21: DIVIDER — ANALYSIS
S(f'''
{picto('chart',A4,200,'560px','70px',0.08)}
<div class="ctr" style="height:100%;flex-direction:column;">
  <div style="font-size:88px;font-weight:900;color:{A2};direction:rtl;text-align:center;">ניתוח</div>
  <div style="display:flex;gap:12px;margin-top:32px;">
    <div style="width:70px;height:4px;background:{A1};border-radius:2px;"></div>
    <div style="width:70px;height:4px;background:{A2};border-radius:2px;"></div>
    <div style="width:70px;height:4px;background:{A3};border-radius:2px;"></div>
  </div>
</div>
''','ANALYST','5 מודלים אנליטיים','chart')

# SLIDE 22: VERDICT
S(f'''
{picto('target',A4,180,'40px','20px',0.07)}
<div style="position:relative;z-index:1;text-align:center;margin-top:10px;">
  <div style="display:inline-block;padding:10px 36px;border:2.5px solid {YEL};border-radius:10px;background:rgba(234,179,8,0.08);">
    <span style="font-size:24px;font-weight:900;color:{TP};">GO-WITH-CONDITIONS</span>
  </div>
</div>
<div style="font-size:17px;font-weight:700;color:{TP};text-align:center;margin-top:16px;line-height:1.5;direction:rtl;position:relative;z-index:1;">3 טכנולוגיות GO: תסיסה מדויקת, בינה מלאכותית, תזונה מותאמת.<br>2 טכנולוגיות NO-GO: בשר מתורבת: 70-90 אחוז כישלון. חקלאות אנכית: 10-20 אלף דולר חשמל.</div>
<div class="flex gap" style="margin-top:14px;position:relative;z-index:1;">
  <div style="flex:1;padding:16px;border-radius:10px;background:rgba(34,197,94,0.06);border:1.5px solid {GRN};">
    <div style="font-size:13px;font-weight:700;color:{GRN};margin-bottom:6px;direction:rtl;text-align:right;">אם כן:</div>
    <div class="t" style="font-size:12px;">הובלה בשוק 34 מיליארד. ישראל כיצואנית טכנולוגיית מזון. תסיסה מקומית: חלבון ב-20 אחוז מהמחיר.</div>
  </div>
  <div style="flex:1;padding:16px;border-radius:10px;background:rgba(239,68,68,0.06);border:1.5px solid {RED};">
    <div style="font-size:13px;font-weight:700;color:{RED};margin-bottom:6px;direction:rtl;text-align:right;">אם לא:</div>
    <div class="t" style="font-size:12px;">סין סוגרת פער. חברות ענק שולטות בנתונים. תלות בנתיב ימי אחד. חלון נסגר תוך 36 חודשים.</div>
  </div>
</div>
''','ANALYST','GO-WITH-CONDITIONS','target')

# SLIDE 23: SCENARIOS
S(f'''
<div class="h2" style="position:relative;z-index:1;">3 תרחישים</div>
<div class="flex gap" style="flex:1;position:relative;z-index:1;">
  <div class="g f1" style="border-right:8px solid {RED};">
    <div style="font-size:16px;font-weight:900;color:{RED};direction:rtl;text-align:center;">פסימי: 20 אחוז</div>
    <div class="t" style="margin-top:8px;font-size:12px;">הנחה: משבר מים + חנק + לאומיות מזון.<br>טריגר: 78 מיליון רעבים נוספים.<br>פעולה: הגנתי. אגירה, ייצור מקומי.</div>
  </div>
  <div class="g f1" style="border-right:8px solid {YEL};">
    <div style="font-size:16px;font-weight:900;color:{YEL};direction:rtl;text-align:center;">ריאליסטי: 55 אחוז</div>
    <div class="t" style="margin-top:8px;font-size:12px;">הנחה: תסיסה פי 5. AI חלקי. GLP-1 ב-20 אחוז.<br>טריגר: חנק יציב. PF בסופרמרקטים.<br>פעולה: Sandbox. פיילוטים.</div>
  </div>
  <div class="g f1" style="border-right:8px solid {GRN};">
    <div style="font-size:16px;font-weight:900;color:{GRN};direction:rtl;text-align:center;">אופטימי: 25 אחוז</div>
    <div class="t" style="margin-top:8px;font-size:12px;">הנחה: PF פי 10. AI פותר 80 אחוז בזבוז.<br>טריגר: הסכמי אקלים. PF מיינסטרים.<br>פעולה: השקעה אגרסיבית. שוק 34 מיליארד.</div>
  </div>
</div>
''','ANALYST','3 תרחישים + טריגרים','chart')

# SLIDE 24: DATA CRITIQUE
S(f'''
{picto('search',A1,140,'40px','10px',0.07)}
<div class="h2" style="position:relative;z-index:1;">מה המספרים לא אומרים לכם</div>
<div style="display:flex;flex-direction:column;gap:8px;flex:1;position:relative;z-index:1;">
  <div class="flex g" style="align-items:center;gap:12px;padding:10px 14px;border-right:8px solid {RED};">
    <div style="flex:1;direction:rtl;text-align:right;"><span style="font-weight:700;color:{A1};font-size:13px;">שוק בשר מתורבת: 6.9 עד 25 מיליארד</span><br><span class="ts">פער פי 4. מימון: חברות שגייסו מיליארדים.</span></div>
    <div>{conf('LOW','Multiple')}</div>
  </div>
  <div class="flex g" style="align-items:center;gap:12px;padding:10px 14px;border-right:8px solid {YEL};">
    <div style="flex:1;direction:rtl;text-align:right;"><span style="font-weight:700;color:{A1};font-size:13px;">תסיסה מדויקת זולה פי 5 עד 2030</span><br><span class="ts">RethinkX נוטה לאופטימיות. מימון: קרנות climate-tech.</span></div>
    <div>{conf('MEDIUM','RethinkX')}</div>
  </div>
  <div class="flex g" style="align-items:center;gap:12px;padding:10px 14px;border-right:8px solid {YEL};">
    <div style="flex:1;direction:rtl;text-align:right;"><span style="font-weight:700;color:{A1};font-size:13px;">AI חקלאי: 8.2 מיליארד עד 2030</span><br><span class="ts">חוק החקלאות מנפח מלאכותית. מימון: Google, Deere.</span></div>
    <div>{conf('MEDIUM','Fortune')}</div>
  </div>
  <div class="flex g" style="align-items:center;gap:12px;padding:10px 14px;border-right:8px solid {GRN};">
    <div style="flex:1;direction:rtl;text-align:right;"><span style="font-weight:700;color:{A1};font-size:13px;">הפסד GLP-1: 30 עד 55 מיליארד</span><br><span class="ts">טווח רחב, תלוי באימוץ. JPMorgan: sell-side.</span></div>
    <div>{conf('HIGH','JPMorgan')}</div>
  </div>
</div>
<div class="ts" style="font-style:italic;margin-top:6px;position:relative;z-index:1;">הנתון החלש: שוק בשר מתורבת. מה ישנה: GLP-1 מעל 30 אחוז.</div>
''','ANALYST','ביקורת נתונים: הנתון החלש','search')

# SLIDE 25: RISK MATRIX
S(f'''
{picto('shield',A2,140,'40px','10px',0.07)}
<div class="h2" style="position:relative;z-index:1;">מטריצת סיכונים</div>
<div style="display:flex;flex-direction:column;gap:8px;flex:1;position:relative;z-index:1;">
  <div class="flex g" style="padding:10px 14px;border-right:8px solid {A2};align-items:center;">
    <div style="flex:2;direction:rtl;text-align:right;"><span style="font-weight:700;color:{TP};font-size:13px;">משבר מים גלובלי</span><br><span class="ts">סימן: מחירי מים עולים 20 אחוז</span></div>
    <div style="flex:1;text-align:center;font-weight:700;color:{RED};font-size:12px;">HIGH / CRITICAL</div>
    <div style="flex:1;direction:rtl;text-align:right;font-size:11px;color:{TS};">PF, התפלה, השקיה חכמה</div>
  </div>
  <div class="flex g" style="padding:10px 14px;border-right:8px solid {A1};align-items:center;">
    <div style="flex:2;direction:rtl;text-align:right;"><span style="font-weight:700;color:{TP};font-size:13px;">חנק נוסף נחסם</span><br><span class="ts">סימן: מתח סין-טייוואן</span></div>
    <div style="flex:1;text-align:center;font-weight:700;color:{YEL};font-size:12px;">MEDIUM / HIGH</div>
    <div style="flex:1;direction:rtl;text-align:right;font-size:11px;color:{TS};">גיוון שרשרת, ייצור מקומי</div>
  </div>
  <div class="flex g" style="padding:10px 14px;border-right:8px solid {A3};align-items:center;">
    <div style="flex:2;direction:rtl;text-align:right;"><span style="font-weight:700;color:{TP};font-size:13px;">GLP-1 מעל 30 אחוז</span><br><span class="ts">סימן: FDA מרחיב אישורים</span></div>
    <div style="flex:1;text-align:center;font-weight:700;color:{YEL};font-size:12px;">MEDIUM / HIGH</div>
    <div style="flex:1;direction:rtl;text-align:right;font-size:11px;color:{TS};">Pivot: יותר חלבון, פחות קלוריות</div>
  </div>
  <div class="flex g" style="padding:10px 14px;border-right:8px solid {A4};align-items:center;">
    <div style="flex:2;direction:rtl;text-align:right;"><span style="font-weight:700;color:{TP};font-size:13px;">Big Tech שולט בנתונים</span><br><span class="ts">סימן: חוק החקלאות 2026</span></div>
    <div style="flex:1;text-align:center;font-weight:700;color:{YEL};font-size:12px;">HIGH / MEDIUM</div>
    <div style="flex:1;direction:rtl;text-align:right;font-size:11px;color:{TS};">בעלות נתונים, תקנים פתוחים</div>
  </div>
</div>
''','ANALYST','מטריצת סיכונים: 4 סיכונים','shield')

# SLIDE 26: TECH MATRIX
S(f'''
{picto('chart',A4,140,'40px','10px',0.07)}
<div class="h2" style="position:relative;z-index:1;">מפת טכנולוגיות: מי ישרוד?</div>
<div style="display:flex;flex-direction:column;gap:5px;flex:1;position:relative;z-index:1;">
  <div class="flex g" style="padding:7px 14px;background:rgba(29,122,165,0.1);">
    <div style="flex:2;font-weight:700;color:{TP};direction:rtl;text-align:right;font-size:12px;">טכנולוגיה</div>
    <div style="flex:3;font-weight:700;color:{TP};direction:rtl;text-align:right;font-size:12px;">מציאות 2026</div>
    <div style="flex:1;font-weight:700;color:{TP};text-align:center;font-size:12px;">הכרעה</div>
  </div>
  <div class="flex g" style="padding:7px 14px;border-right:8px solid {GRN};">
    <div style="flex:2;font-weight:600;color:{TP};direction:rtl;text-align:right;font-size:11px;">תסיסה מדויקת</div>
    <div style="flex:3;color:{TS};direction:rtl;text-align:right;font-size:11px;">802 מיליון, מוכרת. CAGR 40 אחוז.</div>
    <div style="flex:1;text-align:center;font-weight:900;color:{GRN};font-size:12px;">GO</div>
  </div>
  <div class="flex g" style="padding:7px 14px;border-right:8px solid {GRN};">
    <div style="flex:2;font-weight:600;color:{TP};direction:rtl;text-align:right;font-size:11px;">AI חקלאי</div>
    <div style="flex:3;color:{TS};direction:rtl;text-align:right;font-size:11px;">70 מיליון דונם. 78 אחוז אימוץ.</div>
    <div style="flex:1;text-align:center;font-weight:900;color:{GRN};font-size:12px;">GO</div>
  </div>
  <div class="flex g" style="padding:7px 14px;border-right:8px solid {GRN};">
    <div style="flex:2;font-weight:600;color:{TP};direction:rtl;text-align:right;font-size:11px;">תזונה מותאמת</div>
    <div style="flex:3;color:{TS};direction:rtl;text-align:right;font-size:11px;">92 אחוז רוצים. שוק מיקרוביום צומח.</div>
    <div style="flex:1;text-align:center;font-weight:900;color:{GRN};font-size:12px;">GO</div>
  </div>
  <div class="flex g" style="padding:7px 14px;border-right:8px solid {RED};">
    <div style="flex:2;font-weight:600;color:{TP};direction:rtl;text-align:right;font-size:11px;">בשר מתורבת</div>
    <div style="flex:3;color:{TS};direction:rtl;text-align:right;font-size:11px;">70-90 אחוז כישלון. 63 דולר/קילו.</div>
    <div style="flex:1;text-align:center;font-weight:900;color:{RED};font-size:12px;">NO-GO</div>
  </div>
  <div class="flex g" style="padding:7px 14px;border-right:8px solid {YEL};">
    <div style="flex:2;font-weight:600;color:{TP};direction:rtl;text-align:right;font-size:11px;">חקלאות אנכית</div>
    <div style="flex:3;color:{TS};direction:rtl;text-align:right;font-size:11px;">Bowery ו-AppHarvest קרסו.</div>
    <div style="flex:1;text-align:center;font-weight:900;color:{YEL};font-size:12px;">בתנאים</div>
  </div>
</div>
''','ANALYST','הערכת מוכנות טכנולוגית','chart')

# SLIDE 27: ISRAEL
S(f'''
{picto('flag',A1,150,'40px','10px',0.08)}
<div class="h2" style="position:relative;z-index:1;">ישראל: מעצמת טכנולוגיית מזון עם שאלה גדולה</div>
<div class="flex gap" style="flex:1;position:relative;z-index:1;">
  <div class="g f1" style="border-right:8px solid {A4};">
    <div class="h3" style="color:{A4};margin-bottom:6px;">יתרון</div>
    <div class="t">מקום 2 בעולם. 200+ סטארטאפים. רגולציה מוקדמת: דצמבר 2024. תמיכה: 43 אחוז צמחי, 38 אחוז תסיסה.</div>
  </div>
  <div class="g f1" style="border-right:8px solid {A2};">
    <div class="h3" style="color:{A2};margin-bottom:6px;">חולשה</div>
    <div class="t">גיוסים: ירידה 60 אחוז, 66 מיליון. שוק מקומי זעיר. אין scale. רוב לפני הכנסות.</div>
  </div>
  <div class="g f1" style="border-right:8px solid {A1};">
    <div class="h3" style="color:{A1};margin-bottom:6px;">הזדמנות</div>
    <div class="t">חלון: 24-36 חודשים. לפני סין ואירופה. יצוא טכנולוגיה, לא מזון. מאיץ GFI Israel.</div>
  </div>
</div>
''','ANALYST','ישראל: S/W/O','flag')

# SLIDE 28: TODAY VS 2046
S(f'''
{picto('road',A3,140,'40px','10px',0.07)}
<div class="h2" style="position:relative;z-index:1;">היום מול 2046</div>
<div style="display:flex;flex-direction:column;gap:5px;flex:1;position:relative;z-index:1;">
  <div class="flex g" style="padding:7px 14px;background:rgba(29,122,165,0.1);">
    <div style="width:150px;font-weight:700;color:{TP};direction:rtl;text-align:right;font-size:12px;">מימד</div>
    <div style="flex:1;font-weight:700;color:{TP};direction:rtl;text-align:right;font-size:12px;">2026</div>
    <div style="flex:1;font-weight:700;color:{TP};direction:rtl;text-align:right;font-size:12px;">2046</div>
  </div>
  <div class="flex g" style="padding:7px 14px;border-right:8px solid {A1};">
    <div style="width:150px;font-weight:700;color:{A1};direction:rtl;text-align:right;font-size:11px;">מקור חלבון</div>
    <div style="flex:1;color:{TS};direction:rtl;text-align:right;font-size:11px;">90 אחוז מבעלי חיים</div>
    <div style="flex:1;color:{TS};direction:rtl;text-align:right;font-size:11px;">40 אחוז PF, 35 צמחי, 25 חיות</div>
  </div>
  <div class="flex g" style="padding:7px 14px;border-right:8px solid {A3};">
    <div style="width:150px;font-weight:700;color:{A1};direction:rtl;text-align:right;font-size:11px;">שרשרת אספקה</div>
    <div style="flex:1;color:{TS};direction:rtl;text-align:right;font-size:11px;">תגובתית ועונתית</div>
    <div style="flex:1;color:{TS};direction:rtl;text-align:right;font-size:11px;">חיזוי AI בזמן אמת</div>
  </div>
  <div class="flex g" style="padding:7px 14px;border-right:8px solid {A4};">
    <div style="width:150px;font-weight:700;color:{A1};direction:rtl;text-align:right;font-size:11px;">תזונה</div>
    <div style="flex:1;color:{TS};direction:rtl;text-align:right;font-size:11px;">מידה אחת לכולם</div>
    <div style="flex:1;color:{TS};direction:rtl;text-align:right;font-size:11px;">DNA + מכשירים לבישים</div>
  </div>
  <div class="flex g" style="padding:7px 14px;border-right:8px solid {A2};">
    <div style="width:150px;font-weight:700;color:{A1};direction:rtl;text-align:right;font-size:11px;">בזבוז מזון</div>
    <div style="flex:1;color:{TS};direction:rtl;text-align:right;font-size:11px;">30-40 אחוז</div>
    <div style="flex:1;color:{TS};direction:rtl;text-align:right;font-size:11px;">10 אחוז עם AI</div>
  </div>
</div>
''','ANALYST','היום מול עתיד: 4 מימדים','road')

# SLIDE 29: DIVIDER — NARRATIVE
S(f'''
{picto('doc',A2,200,'560px','70px',0.08)}
<div class="ctr" style="height:100%;flex-direction:column;">
  <div style="font-size:88px;font-weight:900;color:{A2};direction:rtl;text-align:center;">הנרטיב</div>
  <div style="display:flex;gap:12px;margin-top:32px;">
    <div style="width:70px;height:4px;background:{A1};border-radius:2px;"></div>
    <div style="width:70px;height:4px;background:{A2};border-radius:2px;"></div>
    <div style="width:70px;height:4px;background:{A3};border-radius:2px;"></div>
  </div>
</div>
''','WRITER','זווית C: counterintuitive','doc')

# SLIDE 30: CORE ARGUMENT
S(f'''
{picto('wheat',A2,200,'40px','30px',0.07)}
<div class="ctr" style="height:100%;position:relative;z-index:1;">
  <div style="max-width:1000px;">
    <div style="font-size:36px;font-weight:900;color:{TP};line-height:1.3;direction:rtl;text-align:right;">אנחנו חיים בתקופה שבה תרופה לסוכרת משנה את תעשיית המזון יותר מכל סטארטאפ מזון שנוסד אי פעם.</div>
    <div style="width:180px;height:3px;background:{A2};margin-top:24px;border-radius:2px;"></div>
  </div>
</div>
''','WRITER','זווית C: הטיעון המרכזי','doc')

# SLIDE 31: STORY 1
S(f'''
<div class="h2" style="position:relative;z-index:1;">הנרטיב: חלק ראשון</div>
<div class="t" style="font-size:15px;line-height:1.75;flex:1;position:relative;z-index:1;">בזמן שכולם מדברים על בשר מעבדה, 3 כוחות שקטים מחדשים את עולם המזון מהיסוד. הראשון הוא תרופה: GLP-1, שגורמת ל-1 מכל 8 אמריקאים לאכול פחות. הפסד שנתי של 55 מיליארד דולר. זו הערכת JPMorgan.<br><br>השני הוא גיאופוליטיקה: רוסיה מחלקת 200 אלף טון חיטה חינם לאפריקה בתמורה לבסיסים. סין בונה תלות טכנולוגית. ארה"ב נסוגה. מצר הורמוז קרס. יותר מ-20 מדינות חוסמות ייצוא. מזון הפך לנשק.</div>
''','WRITER','600 מילים: חלק ראשון','doc')

# SLIDE 32: STORY 2
S(f'''
<div class="h2" style="position:relative;z-index:1;">הנרטיב: חלק שני</div>
<div class="t" style="font-size:15px;line-height:1.75;flex:1;position:relative;z-index:1;">השלישי הוא טכנולוגיה, אבל לא זו שכולם חושבים. לא בשר מתורבת: 70-90 אחוז כישלון, 63 דולר לקילו, בעיית צמיגות. לא חקלאות אנכית: Bowery גייסה 700 מיליון ונסגרה, חשמל 10-20 אלף דולר.<br><br>אלא תסיסה מדויקת, שכבר מוכרת, צומחת 40 אחוז, ובדרך לזול פי 5. ובינה מלאכותית חקלאית על 70 מיליון דונם. מי שמחכה לבשר מעבדה, מפספס את מה שכבר קורה.</div>
''','WRITER','600 מילים: חלק שני','doc')

# SLIDE 33: HEADLINES
S(f'''
<div class="h2" style="position:relative;z-index:1;">6 כותרות פעולה</div>
<div style="display:flex;flex-direction:column;gap:7px;flex:1;position:relative;z-index:1;">
  <div class="g" style="border-right:8px solid {A1};padding:10px 16px;"><div style="font-size:14px;font-weight:700;color:{TP};direction:rtl;text-align:right;">01: תרופה לסוכרת משנה את תעשיית המזון יותר מכל סטארטאפ</div></div>
  <div class="g" style="border-right:8px solid {A3};padding:10px 16px;"><div style="font-size:14px;font-weight:700;color:{TP};direction:rtl;text-align:right;">02: מזון הפך לנשק גיאופוליטי, ורוב המדינות לא ערוכות</div></div>
  <div class="g" style="border-right:8px solid {A4};padding:10px 16px;"><div style="font-size:14px;font-weight:700;color:{TP};direction:rtl;text-align:right;">03: בשר מתורבת כבר מת. תסיסה מדויקת היא הסוס המנצח.</div></div>
  <div class="g" style="border-right:8px solid {A1};padding:10px 16px;"><div style="font-size:14px;font-weight:700;color:{TP};direction:rtl;text-align:right;">04: משבר המים: הפצצה המתקתקת של החקלאות</div></div>
  <div class="g" style="border-right:8px solid {A2};padding:10px 16px;"><div style="font-size:14px;font-weight:700;color:{TP};direction:rtl;text-align:right;">05: חוק החקלאות 2026: סוס טרויאני</div></div>
  <div class="g" style="border-right:8px solid {A1};padding:10px 16px;"><div style="font-size:14px;font-weight:700;color:{TP};direction:rtl;text-align:right;">06: השאלה היא לא מה נאכל. השאלה היא מי יחליט.</div></div>
</div>
''','WRITER','6 כותרות פעולה','doc')

# SLIDE 34: DIVIDER — ACTION
S(f'''
{picto('road',A4,200,'560px','70px',0.08)}
<div class="ctr" style="height:100%;flex-direction:column;">
  <div style="font-size:88px;font-weight:900;color:{A2};direction:rtl;text-align:center;">מה עושים?</div>
  <div style="display:flex;gap:12px;margin-top:32px;">
    <div style="width:70px;height:4px;background:{A1};border-radius:2px;"></div>
    <div style="width:70px;height:4px;background:{A2};border-radius:2px;"></div>
    <div style="width:70px;height:4px;background:{A3};border-radius:2px;"></div>
  </div>
</div>
''','ANALYST','מפת דרכים','road')

# SLIDE 35: TWO TRACKS
S(f'''
{picto('shield',A4,150,'40px','10px',0.07)}
<div class="h2" style="position:relative;z-index:1;">2 מסלולים: ריבונות מול תלות</div>
<div class="flex gap" style="flex:1;position:relative;z-index:1;">
  <div class="g f1" style="border-right:8px solid {A2};">
    <div class="h3" style="color:{A2};margin-bottom:8px;">מסלול תלות</div>
    <div class="t" style="line-height:1.9;font-size:13px;">\u2022 תלות ב-3 נקודות חנק ימיות<br>\u2022 חשיפה לנשק מזון<br>\u2022 נתונים בידי חברות ענק<br>\u2022 חלבון ב-100 אחוז מהמחיר</div>
  </div>
  <div class="g f1" style="border-right:8px solid {A4};">
    <div class="h3" style="color:{A4};margin-bottom:8px;">מסלול ריבונות</div>
    <div class="t" style="line-height:1.9;font-size:13px;">\u2022 PF מקומית: חלבון ב-20 אחוז<br>\u2022 AI חקלאי: הנתונים שלך<br>\u2022 שרשרת מגוונת ועצמאית<br>\u2022 יצוא טכנולוגיה, לא מזון</div>
  </div>
</div>
''','WRITER','ריבונות מול תלות','shield')

# SLIDE 36: ROADMAP
S(f'''
<div class="h2" style="position:relative;z-index:1;">מפת דרכים: 3 אופקים</div>
<div class="flex gap" style="flex:1;position:relative;z-index:1;">
  <div class="g f1" style="border-right:8px solid {A1};">
    <div style="font-size:14px;font-weight:700;color:{A1};direction:rtl;text-align:center;margin-bottom:8px;">עכשיו: 0-30 יום</div>
    <div class="t" style="font-size:12px;line-height:1.8;">\u2022 תקציב מ-cultured ל-PF<br>\u2022 בדיקת חשיפה לחנק<br>\u2022 אסטרטגיית GLP-1</div>
  </div>
  <div class="g f1" style="border-right:8px solid {A3};">
    <div style="font-size:14px;font-weight:700;color:{A3};direction:rtl;text-align:center;margin-bottom:8px;">קרוב: 1-6 חודשים</div>
    <div class="t" style="font-size:12px;line-height:1.8;">\u2022 פיילוט AI + בעלות נתונים<br>\u2022 מלאי אסטרטגי<br>\u2022 מוצרים עתירי חלבון</div>
  </div>
  <div class="g f1" style="border-right:8px solid {A4};">
    <div style="font-size:14px;font-weight:700;color:{A4};direction:rtl;text-align:center;margin-bottom:8px;">רחוק: 6+ חודשים</div>
    <div class="t" style="font-size:12px;line-height:1.8;">\u2022 יצוא טכנולוגיית מזון<br>\u2022 הכנה למשבר מים<br>\u2022 תקנים פתוחים</div>
  </div>
</div>
''','ANALYST','3 אופקים','road')

# SLIDE 37: 5 ACTIONS
colors5=[A1,A3,A4,A2,A1]
acts=['להזיז תקציב מבשר מתורבת לתסיסה מדויקת. הכסף למי שכבר מוכר.',
'לגוון שרשרת אספקה: תלות בנתיב אחד = תלות במדינה אחת.',
'לאמץ AI חקלאי עם בעלות מלאה על נתונים. חוק 2026 = סוס טרויאני.',
'להתכונן ל-GLP-1: עתירי חלבון, דלי קלוריות, מנות קטנות.',
'ישראל: חלון 24-36 חודשים. אחר כך סין ואירופה סוגרות פער.']
acts_html=''
for i,(a,c) in enumerate(zip(acts,colors5)):
    acts_html+=f'<div class="g" style="border-right:8px solid {c};display:flex;align-items:center;gap:14px;padding:10px 16px;"><div style="width:32px;height:32px;border-radius:50%;background:{c};display:flex;align-items:center;justify-content:center;flex-shrink:0;font-size:14px;font-weight:900;color:#fff;">0{i+1}</div><div style="font-size:13px;font-weight:500;color:{TP};direction:rtl;text-align:right;line-height:1.4;">{a}</div></div>'
S(f'''
<div class="h2" style="position:relative;z-index:1;">5 דברים לעשות מחר בבוקר</div>
<div style="display:flex;flex-direction:column;gap:8px;flex:1;position:relative;z-index:1;">{acts_html}</div>
''','WRITER','5 פעולות','target')

# SLIDE 38: TIMELINE
S(f'''
<div class="h2" style="position:relative;z-index:1;">ציר זמן: 2026 עד 2046</div>
<div style="display:flex;flex-direction:column;gap:8px;flex:1;position:relative;z-index:1;">
  <div class="g" style="border-right:8px solid {A1};display:flex;align-items:center;gap:14px;padding:10px 16px;">
    <div style="width:70px;height:34px;border-radius:6px;background:{A1};display:flex;align-items:center;justify-content:center;font-size:11px;font-weight:900;color:#fff;flex-shrink:0;">2026-28</div>
    <div style="direction:rtl;text-align:right;"><span style="font-weight:700;color:{A1};font-size:13px;">חלון ההזדמנות:</span> <span class="ts">PF בסופרמרקטים. AI סטנדרט. GLP-1 משנה תפריטים.</span></div>
  </div>
  <div class="g" style="border-right:8px solid {A3};display:flex;align-items:center;gap:14px;padding:10px 16px;">
    <div style="width:70px;height:34px;border-radius:6px;background:{A3};display:flex;align-items:center;justify-content:center;font-size:11px;font-weight:900;color:#fff;flex-shrink:0;">2028-32</div>
    <div style="direction:rtl;text-align:right;"><span style="font-weight:700;color:{A3};font-size:13px;">נקודת מפנה:</span> <span class="ts">PF זולה פי 5. 70 אחוז חלב עובר. חקלאות אנכית מוצאת מודל.</span></div>
  </div>
  <div class="g" style="border-right:8px solid {A4};display:flex;align-items:center;gap:14px;padding:10px 16px;">
    <div style="width:70px;height:34px;border-radius:6px;background:{A4};display:flex;align-items:center;justify-content:center;font-size:11px;font-weight:900;color:#fff;flex-shrink:0;">2032-38</div>
    <div style="direction:rtl;text-align:right;"><span style="font-weight:700;color:{A4};font-size:13px;">עולם חדש:</span> <span class="ts">ריבונות מזון = ביטחון לאומי. AI בכל שרשרת. הדפסת מזון 3D.</span></div>
  </div>
  <div class="g" style="border-right:8px solid {A2};display:flex;align-items:center;gap:14px;padding:10px 16px;">
    <div style="width:70px;height:34px;border-radius:6px;background:{A2};display:flex;align-items:center;justify-content:center;font-size:11px;font-weight:900;color:#fff;flex-shrink:0;">2038-46</div>
    <div style="direction:rtl;text-align:right;"><span style="font-weight:700;color:{A2};font-size:13px;">אל חזור:</span> <span class="ts">מי שלא השקיע, תלוי. משבר מים. חלבון מחיות = מותרות.</span></div>
  </div>
</div>
''','ANALYST','ציר זמן: 4 שלבים','road')

# SLIDE 39: DISCUSSION
S(f'''
<div class="h2" style="position:relative;z-index:1;">5 שאלות לדיון</div>
<div style="display:flex;flex-direction:column;gap:8px;flex:1;position:relative;z-index:1;">
  <div class="g" style="border-right:8px solid {A1};padding:10px 16px;"><div style="font-size:14px;color:{TP};direction:rtl;text-align:right;">האם הארגון שלכם מוכן לירידה של 20 אחוז בביקוש למזון?</div></div>
  <div class="g" style="border-right:8px solid {A3};padding:10px 16px;"><div style="font-size:14px;color:{TP};direction:rtl;text-align:right;">כמה מנתיבי האספקה שלכם עוברים דרך מצר הורמוז?</div></div>
  <div class="g" style="border-right:8px solid {A4};padding:10px 16px;"><div style="font-size:14px;color:{TP};direction:rtl;text-align:right;">מי בעל הנתונים החקלאיים: אתם, או חברות ענק?</div></div>
  <div class="g" style="border-right:8px solid {A2};padding:10px 16px;"><div style="font-size:14px;color:{TP};direction:rtl;text-align:right;">מה יקרה אם מחירי המים יעלו ב-20 אחוז בשנה הקרובה?</div></div>
  <div class="g" style="border-right:8px solid {A1};padding:10px 16px;"><div style="font-size:14px;color:{TP};direction:rtl;text-align:right;">האם ישראל מנצלת את חלון 24-36 חודשים, או מפספסת?</div></div>
</div>
''','WRITER','5 שאלות','doc')

# SLIDE 40: PROCESS TRANSPARENCY
S(f'''
<div class="h2" style="position:relative;z-index:1;">שקיפות תהליך</div>
<div class="flex gap" style="flex:1;flex-wrap:wrap;position:relative;z-index:1;">
  <div class="g" style="flex:1;min-width:30%;text-align:center;border-right:8px solid {A3};">
    <div style="font-size:46px;font-weight:900;color:{A3};">25</div>
    <div style="font-size:13px;color:{TP};direction:rtl;">חיפושים ברשת</div>
  </div>
  <div class="g" style="flex:1;min-width:30%;text-align:center;border-right:8px solid {A3};">
    <div style="font-size:46px;font-weight:900;color:{A3};">6</div>
    <div style="font-size:13px;color:{TP};direction:rtl;">מאמרים מלאים</div>
  </div>
  <div class="g" style="flex:1;min-width:30%;text-align:center;border-right:8px solid {A4};">
    <div style="font-size:46px;font-weight:900;color:{A4};">5</div>
    <div style="font-size:13px;color:{TP};direction:rtl;">מודלים אנליטיים</div>
  </div>
  <div class="g" style="flex:1;min-width:30%;text-align:center;border-right:8px solid {A2};">
    <div style="font-size:46px;font-weight:900;color:{A2};">3</div>
    <div style="font-size:13px;color:{TP};direction:rtl;">זוויות כתיבה</div>
  </div>
  <div class="g" style="flex:1;min-width:30%;text-align:center;border-right:8px solid {A1};">
    <div style="font-size:46px;font-weight:900;color:{A1};">3</div>
    <div style="font-size:13px;color:{TP};direction:rtl;">כיוונים ויזואליים</div>
  </div>
  <div class="g" style="flex:1;min-width:30%;text-align:center;border-right:8px solid {A1};">
    <div style="font-size:46px;font-weight:900;color:{A1};">45</div>
    <div style="font-size:13px;color:{TP};direction:rtl;">שקפים</div>
  </div>
</div>
''','DESIGNER','שקיפות','target')

# SLIDE 41: SOURCES
S(f'''
<div class="h2" style="position:relative;z-index:1;">מקורות עיקריים</div>
<div style="display:flex;flex-direction:column;gap:6px;flex:1;position:relative;z-index:1;">
  <div class="g" style="border-right:8px solid {A1};padding:10px 14px;display:flex;"><div style="width:150px;font-weight:700;color:{A1};direction:rtl;text-align:right;font-size:12px;">נתונים כלכליים</div><div class="ts" style="flex:1;">JPMorgan, KPMG, Cornell University, Avery Dennison</div></div>
  <div class="g" style="border-right:8px solid {A3};padding:10px 14px;display:flex;"><div style="width:150px;font-weight:700;color:{A3};direction:rtl;text-align:right;font-size:12px;">גיאופוליטיקה</div><div class="ts" style="flex:1;">War on the Rocks, Council on Strategic Risks, FAO, UNCTAD, IFPRI</div></div>
  <div class="g" style="border-right:8px solid {A4};padding:10px 14px;display:flex;"><div style="width:150px;font-weight:700;color:{A4};direction:rtl;text-align:right;font-size:12px;">טכנולוגיה</div><div class="ts" style="flex:1;">AgFunderNews, RethinkX, GFI Israel, Verified Market Research, Green Queen</div></div>
  <div class="g" style="border-right:8px solid {A2};padding:10px 14px;display:flex;"><div style="width:150px;font-weight:700;color:{A2};direction:rtl;text-align:right;font-size:12px;">רגולציה</div><div class="ts" style="flex:1;">Fortune, Innovation Israel, Startup Nation Central, Congress.gov</div></div>
  <div class="g" style="border-right:8px solid {A1};padding:10px 14px;display:flex;"><div style="width:150px;font-weight:700;color:{A1};direction:rtl;text-align:right;font-size:12px;">מים ואקלים</div><div class="ts" style="flex:1;">USDA ERS, FAO, PBS, WFP, IPCC, Nature.org, NOAA</div></div>
</div>
''','RESEARCHER','25 חיפושים: מקורות','search')

# SLIDE 42: INSECT PROTEIN + BEYOND MEAT
S(f'''
{picto('dna',A4,140,'40px','10px',0.08)}
<div class="h2" style="position:relative;z-index:1;">חלבון מחרקים: שוק נישתי עם פוטנציאל. Beyond Meat: קריסה.</div>
<div class="flex gap" style="flex:1;position:relative;z-index:1;">
  <div class="g f1" style="border-right:8px solid {A4};">
    <div class="h3" style="color:{A4};margin-bottom:6px;">חלבון מחרקים</div>
    <div class="t" style="font-size:12px;">שוק: 449 מיליון דולר ב-2026, צמיחה שנתית 24 אחוז. 35 אחוז מוכנים לנסות. InnovaFeed: הקיבולת הגדולה בעולם, 2 אתרים בצרפת. Protix: מימון 37 מיליון אירו. עמידות צרכנית חזקה בשווקים מערביים.</div>
    <div style="margin-top:6px;">{conf('MEDIUM','DataM Intelligence')}</div>
  </div>
  <div class="g f1" style="border-right:8px solid {A2};">
    <div class="h3" style="color:{A2};margin-bottom:6px;">Beyond Meat: הקריסה</div>
    <div class="t" style="font-size:12px;">הכנסות: 275.5 מיליון ב-2025, ירידה 15.6 אחוז. הפסד תפעולי: 332.7 מיליון. מניה: ירידה של 99.6 אחוז ב-5 שנים. מכירות קמעונאיות בארה"ב: ירידה 6.5 אחוז. בינלאומי: ירידה 32.5 אחוז.</div>
    <div style="margin-top:6px;">{conf('HIGH','WATT Poultry')}</div>
  </div>
</div>
''','RESEARCHER','חרקים + צמחי: מצב 2026','dna')

# SLIDE 43: BLOCKCHAIN + ROBOTICS + 3D PRINTING
S(f'''
{picto('brain',A3,140,'40px','10px',0.08)}
<div class="h2" style="position:relative;z-index:1;">טכנולוגיות תומכות: Blockchain, רובוטיקה, הדפסת מזון</div>
<div class="flex gap" style="flex:1;position:relative;z-index:1;">
  <div class="g f1" style="border-right:8px solid {A3};">
    <div class="h3" style="color:{A3};margin-bottom:4px;">Blockchain</div>
    <div class="t" style="font-size:11px;">שוק: 1.5 מיליארד ב-2026. Walmart: מעקב מנגו מ-7 ימים ל-2.2 שניות. 71 אחוז מהצרכנים מעדיפים שקיפות. FSMA 204: אכיפה מינואר 2026.</div>
    <div style="margin-top:4px;">{conf('MEDIUM','CXTMS')}</div>
  </div>
  <div class="g f1" style="border-right:8px solid {A1};">
    <div class="h3" style="color:{A1};margin-bottom:4px;">רובוטיקה במטבח</div>
    <div class="t" style="font-size:11px;">Sweetgreen: 20 יחידות Infinite Kitchen, כרטיסים +10 אחוז. Flippy: 40+ פריטי תפריט, הפחתת אינטראקציות 90 אחוז. שוק: 1.9 מיליארד, צפוי 6.7 מיליארד עד 2033.</div>
    <div style="margin-top:4px;">{conf('HIGH','Restaurant Dive')}</div>
  </div>
  <div class="g f1" style="border-right:8px solid {A4};">
    <div class="h3" style="color:{A4};margin-bottom:4px;">הדפסת מזון תלת ממדית</div>
    <div class="t" style="font-size:11px;">שוק: 716 מיליון ב-2026, 9.6 מיליארד עד 2033. 18+ מוסדות בריאות בניסויים. Smoothfood: שחזור מזון טחון לצורתו המקורית לקשישים.</div>
    <div style="margin-top:4px;">{conf('MEDIUM','Astute Analytica')}</div>
  </div>
</div>
''','ANALYST','טכנולוגיות תומכות: 3 תחומים','brain')

# SLIDE 44: UPF REGULATION + FOOD EMISSIONS
S(f'''
{picto('shield',A2,140,'40px','10px',0.08)}
<div class="h2" style="position:relative;z-index:1;">רגולציית מזון מעובד ופליטות: המגמה שלא ניתן לעצור</div>
<div class="flex gap" style="flex:1;position:relative;z-index:1;">
  <div class="g f1" style="border-right:8px solid {A2};">
    <div class="h3" style="color:{A2};margin-bottom:4px;">מזון מעובד במיוחד</div>
    <div class="t" style="font-size:12px;">61 אחוז מצריכת האנרגיה בארה"ב ממזון מעובד. סיכון: סוכרת OR 1.23, השמנה OR 1.26, דיכאון OR 1.40. קולומביה: ראשונה למסות, נובמבר 2023. ברזיל: 90 אחוז טרי בבתי ספר עד 2026. צ'ילה: איסור פרסום 06:00-22:00.</div>
    <div style="margin-top:6px;">{conf('HIGH','Lancet + PMC')}</div>
  </div>
  <div class="g f1" style="border-right:8px solid {A1};">
    <div class="h3" style="color:{A1};margin-bottom:4px;">פליטות מערכת המזון</div>
    <div class="t" style="font-size:12px;">25 אחוז מפליטות גזי חממה: 16.2 מיליארד טון CO2eq. כריתת יערות: 2.9 מיליארד טון. מתאן מבקר: 2.8 מיליארד. בשר בקר: 32 קילו CO2eq לקילו. אצות Asparagopsis מפחיתות מתאן בקר ב-82 אחוז.</div>
    <div style="margin-top:6px;">{conf('HIGH','Our World in Data + FAO')}</div>
  </div>
</div>
''','RESEARCHER','רגולציה + פליטות: הנתונים','shield')

# SLIDE 45: CLOSING
S(f'''
{picto('wheat',A2,200,'560px','60px',0.06)}
<div class="ctr" style="height:100%;flex-direction:column;position:relative;z-index:1;">
  <div style="font-size:34px;font-weight:900;color:{TP};line-height:1.35;direction:rtl;text-align:center;">השאלה היא לא<br>אם עולם המזון ישתנה.<br>השאלה היא מי יהיה<br>בצד הנכון כשזה יקרה.</div>
  <div style="width:140px;height:3px;background:{A1};margin-top:28px;border-radius:2px;"></div>
  <div style="margin-top:14px;font-size:14px;color:{TS};direction:rtl;text-align:center;">מכונת המחקר | Project Machine | 2026</div>
  <div style="margin-top:8px;font-size:10px;color:{BD};">30 חיפושים: 55 נתונים: 5 מודלים: 3 זוויות: 45 שקפים</div>
</div>
''','DESIGNER','מצגת מוכנה','target')

# ═══════ PIPELINE ═══════
async def main():
    tmpdir = tempfile.mkdtemp(prefix='food-v3-')
    html_dir = os.path.join(tmpdir, 'html')
    png_dir = os.path.join(tmpdir, 'png')
    os.makedirs(html_dir); os.makedirs(png_dir)

    print(f'Generating {len(slides)} HTML slides...')
    for i, (content, agent, stats, icon) in enumerate(slides):
        html = html_s(content, agent, stats, icon, i+1)
        p = os.path.join(html_dir, f'slide-{i+1:02d}.html')
        with open(p, 'w', encoding='utf-8') as f: f.write(html)
        print(f'  ✓ slide-{i+1:02d}.html')

    print(f'\nRendering {len(slides)} slides to PNG...')
    from playwright.async_api import async_playwright
    async with async_playwright() as p:
        browser = await p.chromium.launch(args=['--disable-web-security','--allow-file-access-from-files'])
        for i in range(len(slides)):
            hp = os.path.join(html_dir, f'slide-{i+1:02d}.html')
            pp = os.path.join(png_dir, f'slide-{i+1:02d}.png')
            page = await browser.new_page(viewport={'width':1333,'height':750})
            await page.goto(f'file://{os.path.abspath(hp)}', wait_until='networkidle')
            await page.wait_for_timeout(2800)
            try: await page.evaluate('() => document.fonts.ready')
            except: pass
            await page.screenshot(path=pp, full_page=False, clip={'x':0,'y':0,'width':1333,'height':750})
            await page.close()
            print(f'  ✓ slide-{i+1:02d}.png')
        await browser.close()

    print('\nAssembling PPTX...')
    from pptx import Presentation
    from pptx.util import Inches, Emu
    prs = Presentation()
    prs.slide_width = Inches(13.333); prs.slide_height = Inches(7.5)
    sw = prs.slide_width; sh = prs.slide_height
    for png in sorted(Path(png_dir).glob('slide-*.png')):
        sl = prs.slides.add_slide(prs.slide_layouts[6])
        sl.shapes.add_picture(str(png), Emu(0), Emu(0), sw, sh)

    out = '/Users/zoharurian/Desktop/food-perfect-final.pptx'
    prs.save(out)
    print(f'\n✅ {out} ({len(slides)} slides)')

asyncio.run(main())
