import streamlit as st

from pdh import config, content
from pdh.graphics import farm_to_plate_html
from pdh.ui import footer, html, open_join, spacer, top_bar

top_bar()

# ---- hero
left, right = st.columns([1.15, 1], gap="large", vertical_alignment="center")
with left:
    html(f"""
    <div class="eyebrow">{config.TAGLINE}</div>
    <div class="hero-title">Local food, with a farmer's name on the box.</div>
    <p class="lead">We are the middleman between small Montérégie farms and the specialty grocers and restaurants
    that want their food. We take the orders, send one invoice, arrange the cold delivery and put a QR code on
    every box.</p>
    """)
    if st.button("Join our first season", type="primary", key="hero_join"):
        open_join("Farm")
with right:
    html("""
    <div class="order"><div class="head"><span>Example weekly order</span><span>1 invoice</span></div>
    <div class="line"><div><b>Carrots</b><span class="f">Farm A</span></div><div>20 kg</div></div>
    <div class="line"><div><b>Heirloom tomatoes</b><span class="f">Farm B</span></div><div>12 kg</div></div>
    <div class="line"><div><b>Salad mix</b><span class="f">Farm C</span></div><div>6 kg</div></div>
    <div class="line"><div><b>Beets</b><span class="f">Farm D</span></div><div>15 kg</div></div>
    <div class="foot"><b>One cold delivery</b><span>QR code on every box</span></div></div>
    """)

# ---- farm to plate graphic
spacer(64)
html('<div class="eyebrow">Farm to table, made visible</div><div class="section-title">Every plate has a farm behind it. We make it visible.</div>')
html(farm_to_plate_html())

# ---- the gap
spacer(72)
html(f'<div class="eyebrow">The gap</div><div class="section-title">Close the gap.</div><p class="prose">{content.GAP_SHORT}</p>')

# ---- what we do
spacer(56)
html('<div class="eyebrow">Why buyers like it</div>')
for col, (n, title, body) in zip(st.columns(3, gap="large"), content.BENEFITS):
    with col:
        html(f'<div class="col"><div class="n">{n}</div><h3>{title}</h3><p>{body}</p></div>')

# ---- closing call to action
spacer(72)
with st.container(key="cta"):
    html("""
    <div class="cta-title">Know what you eat. Be conscious.</div>
    <p class="cta-text">We are starting with a small trial and looking for five grocers, five farms and a cold-chain
    partner. If that is you, join us.</p>
    """)
    if st.button("Join our first season", type="primary", key="cta_join"):
        open_join("Farm")
footer()
