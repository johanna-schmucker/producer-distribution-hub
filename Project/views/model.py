import streamlit as st

from pdh import content
from pdh.model import route_numbers
from pdh.ui import footer, html, open_join, spacer, top_bar

top_bar()
r = route_numbers(300, 18, 500, 10)
html("""
<div class="eyebrow">Business model</div>
<div class="page-title">One invoice in. Farms paid out. A small share for us.</div>
<p class="lead">Here is how the money moves, using a typical $300 grocer order as the example. These are our planned terms for the pilot.</p>
""")
html(f'''<div class="strip" style="grid-template-columns:repeat(3,1fr)">
<div><div class="n">$300</div><div class="l">the grocer pays us one invoice</div></div>
<div><div class="n">${r.per_stop:,.0f}</div><div class="l">we keep, about 18%</div></div>
<div><div class="n">${300 - r.per_stop:,.0f}</div><div class="l">farms receive within 14 days</div></div></div>''')

spacer(56)
for col, (who, points) in zip(st.columns(3, gap="large"), content.MODEL_PARTS):
    with col:
        items = "".join(f"<p style='margin:0 0 8px'>{p}</p>" for p in points)
        html(f'<div class="col"><h3>{who}</h3>{items}</div>')

spacer(56)
html('<div class="eyebrow">What has to be true</div><div class="section-title">Three things we will test in our pilot</div>')
for col, text in zip(st.columns(3, gap="large"), content.MUST_BE_TRUE):
    with col:
        html(f'<div class="col"><p style="color:#111">{text}</p></div>')
html(f'<p class="small" style="margin-top:16px">A route of about {r.break_even} stops covers its costs. '
     "We assume about $500 per route, to be confirmed with a carrier quote.</p>")

spacer(56)
html('<div class="eyebrow">Questions</div><div class="section-title">What people ask us first</div>')
for q, a in content.FAQ:
    with st.expander(q):
        st.write(a)

spacer(56)
with st.container(key="cta"):
    html('<div class="cta-title">Be part of our first season.</div>')
    if st.button("Join our first season", type="primary", key="cta_join"):
        open_join("Farm")
footer()
