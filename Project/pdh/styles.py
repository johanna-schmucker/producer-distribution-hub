"""Plain white editorial look: black text, one green accent, hairlines instead of boxes."""
from __future__ import annotations

import streamlit as st

CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=Source+Serif+4:opsz,wght@8..60,500;8..60,600&display=swap');
:root { --ink:#111; --muted:#5B5B5B; --line:#E4E4E4; --accent:#2E7D32; }
.stApp, header[data-testid="stHeader"] { background:#fff; color:var(--ink); font-family:'Inter',system-ui,sans-serif; }
footer, [data-testid="stDecoration"] { display:none !important; }
.block-container { max-width:1080px; padding-top:4.5rem; padding-bottom:4rem; }
h1,h2,h3 { font-family:'Source Serif 4',Georgia,serif !important; font-weight:600; letter-spacing:-0.01em; color:var(--ink); }
:focus-visible { outline:2px solid var(--accent) !important; outline-offset:2px; }

[data-testid^="stBaseButton-primary"] { background:var(--ink); color:#fff; border:1px solid var(--ink); border-radius:4px; font-weight:600; min-height:46px; padding:.5rem 1.4rem; }
[data-testid^="stBaseButton-primary"]:hover { background:var(--accent); border-color:var(--accent); color:#fff; }
[data-testid^="stBaseButton-secondary"] { background:#fff; color:var(--ink); border:1px solid var(--ink); border-radius:4px; font-weight:600; min-height:46px; padding:.5rem 1.4rem; }
[data-testid^="stBaseButton-secondary"]:hover { border-color:var(--accent); color:var(--accent); background:#fff; }

[data-testid="stSidebar"], [data-testid="stSidebarCollapsedControl"], [data-testid="stSidebarNav"] { display:none !important; }
a[data-testid="stPageLink-NavLink"] { background:transparent !important; padding:6px 0; border-radius:0; border-bottom:2px solid transparent; color:#111 !important; }
a[data-testid="stPageLink-NavLink"] p { color:#111 !important; font-weight:500; font-size:15px; white-space:nowrap; }
a[data-testid="stPageLink-NavLink"][aria-current="page"] { border-bottom-color:#111; }
a[data-testid="stPageLink-NavLink"]:hover { border-bottom-color:#111; }
a[data-testid="stPageLink-NavLink"][aria-current="page"] p { font-weight:600; }
.st-key-topbar [data-testid="stHorizontalBlock"] { flex-wrap:wrap !important; gap:8px 28px !important; align-items:center; }
.st-key-topbar [data-testid="stColumn"] { flex:0 0 auto !important; width:auto !important; min-width:0 !important; }
.st-key-topbar [data-testid="stColumn"]:first-child { margin-right:auto; }
@media (max-width:900px) { .st-key-topbar [data-testid="stColumn"]:first-child { flex:1 1 100% !important; } .st-key-topbar [data-testid="stColumn"]:last-child { margin-left:auto; } }
.brand { gap:10px; white-space:nowrap; font-family:'Source Serif 4',Georgia,serif; font-weight:600; font-size:20px; min-height:44px; display:flex; align-items:center; }
.eyebrow { font-size:12px; font-weight:600; letter-spacing:.14em; text-transform:uppercase; color:var(--accent); }
.hero-title, .page-title { font-family:'Source Serif 4',Georgia,serif; font-weight:600; letter-spacing:-0.02em; line-height:1.06; margin:12px 0 18px; }
.hero-title { font-size:clamp(40px,5.4vw,64px); }
.page-title { font-size:clamp(34px,4.4vw,52px); max-width:860px; }
.section-title { font-family:'Source Serif 4',Georgia,serif; font-weight:600; font-size:clamp(28px,3.4vw,40px); line-height:1.12; letter-spacing:-0.015em; margin:8px 0 22px; max-width:820px; }
.lead { font-size:19px; color:var(--muted); max-width:600px; line-height:1.6; margin:0 0 20px; }
.prose { font-size:19px; line-height:1.7; max-width:720px; margin:0 0 16px; }
.stMarkdown p.statement, .statement { font-family:'Source Serif 4',Georgia,serif; font-weight:500; font-size:clamp(24px,2.8vw,34px) !important; line-height:1.25 !important; max-width:820px; margin:8px 0 0; }
.quote { font-family:'Source Serif 4',Georgia,serif; font-size:24px; line-height:1.35; border-left:3px solid var(--accent); padding-left:20px; margin:8px 0 6px; max-width:640px; }
.small { font-size:14px; color:var(--muted); margin:10px 0 0; }
.rule { border-top:1px solid var(--line); }

.f2p { display:grid; grid-template-columns:repeat(4,1fr); gap:56px; }
.f2p-step { position:relative; }
.f2p .tile { height:140px; border:1.5px solid #111; border-radius:18px; background:#fff; display:flex; align-items:center; justify-content:center; }
.f2p .tile.us { border:3px solid var(--accent); background:#F2F8F2; }
.f2p .icon { width:118px; height:118px; }
.f2p h3 { font-size:21px; margin:14px 0 6px; }
.f2p p { color:var(--muted); margin:0; line-height:1.55; font-size:15px; }
.f2p .gap-arrow { position:absolute; right:-50px; top:64px; width:44px; }
.f2p .dash { width:44px; height:10px; display:block; }
@media (max-width:820px) { .f2p { grid-template-columns:1fr 1fr; gap:28px; } .f2p .gap-arrow { display:none; } }
.strip { display:grid; grid-template-columns:repeat(4,1fr); border-top:1px solid var(--ink); margin-top:8px; }
.strip > div { padding:18px 20px 0 0; }
.strip .n { font-family:'Source Serif 4',Georgia,serif; font-weight:600; font-size:clamp(28px,3vw,38px); line-height:1; }
.strip .l { font-size:14px; color:var(--muted); margin-top:6px; }
@media (max-width:720px) { .strip { grid-template-columns:repeat(2,1fr); } }

.col { border-top:1px solid var(--ink); padding-top:16px; }
.col .n { font-size:13px; font-weight:600; letter-spacing:.1em; color:var(--accent); }
.col h3 { font-size:22px; margin:8px 0; }
.col p { color:var(--muted); margin:0; line-height:1.6; }

.order { border-top:1px solid var(--ink); }
.order .head { display:flex; justify-content:space-between; font-size:12px; font-weight:600; letter-spacing:.12em; text-transform:uppercase; color:var(--muted); padding:12px 0; }
.line { display:flex; justify-content:space-between; gap:16px; padding:12px 0; border-top:1px solid var(--line); }
.line b { display:block; font-weight:600; } .line .f { font-size:14px; color:var(--muted); }
.order .foot { border-top:1px solid var(--ink); padding-top:12px; font-size:14px; display:flex; justify-content:space-between; gap:8px; }

.checks { list-style:none; padding:0; margin:0 0 24px; }
.checks li { display:flex; gap:12px; align-items:flex-start; margin-bottom:12px; }
.checks svg { flex:none; margin-top:4px; }

.stat { border-top:1px solid var(--ink); padding-top:16px; height:100%; }
.stat .num { font-family:'Source Serif 4',Georgia,serif; font-weight:600; font-size:clamp(44px,5vw,60px); line-height:1; color:var(--accent); }
.stat.text .num { font-size:clamp(26px,2.8vw,32px); line-height:1.15; color:var(--ink); }
.stat p { margin:12px 0 8px; font-size:17px; line-height:1.5; }
.stat .src { font-size:12px; color:var(--muted); } .stat .src a { color:var(--muted); }

.facts { border-top:1px solid var(--ink); }
.facts .row { display:flex; justify-content:space-between; gap:16px; padding:13px 0; border-bottom:1px solid var(--line); }
.facts .row span { color:var(--muted); } .facts .row b { text-align:right; font-weight:600; }

[data-testid="stExpander"] { border:0 !important; border-top:1px solid var(--line) !important; border-radius:0; background:#fff; }
[data-testid="stExpander"] details { border:0 !important; border-radius:0 !important; background:#fff !important; }
[data-testid="stExpander"] summary { font-weight:600; padding:10px 0; }

.st-key-cta, .st-key-ask { border-top:3px solid var(--ink); padding-top:28px; }
.cta-title { font-family:'Source Serif 4',Georgia,serif; font-weight:600; font-size:clamp(30px,4vw,46px); line-height:1.08; letter-spacing:-0.02em; margin:0 0 12px; }
.cta-text { color:var(--muted); font-size:19px; max-width:620px; margin:0 0 18px; line-height:1.6; }

.footer { color:var(--muted); font-size:14px; border-top:1px solid var(--line); padding-top:20px; margin-top:56px; display:flex; justify-content:space-between; flex-wrap:wrap; gap:8px; }
</style>
"""


def inject() -> None:
    st.markdown("\n".join(line.strip() for line in CSS.splitlines()), unsafe_allow_html=True)
