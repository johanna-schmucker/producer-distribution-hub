import streamlit as st

from pdh import config, content, storage
from pdh.geo import MAIN_STREET, area_map
from pdh.ui import checklist, footer, html, open_join, spacer, top_bar

top_bar()
html("""
<div class="eyebrow">For grocers and restaurants</div>
<div class="page-title">Your customers want local food. Make it easy to find.</div>
<p class="lead">Offer proof of origin and farm stories without managing a dozen small suppliers.</p>
""")
spacer(8)
for col, s in zip(st.columns(len(content.STATS), gap="large"), content.STATS):
    with col:
        cls = "stat text" if s.get("is_text") else "stat"
        html(f"""
        <div class="{cls}"><div class="num">{s['num']}</div><p>{s['text']}</p>
        <div class="src">{s['src']} <a href="{s['url']}" target="_blank" rel="noopener">Source</a></div></div>
        """)

spacer(48)
left, right = st.columns([1, 1.15], gap="large")
with left:
    html('<div class="eyebrow">Our promise to your customers</div>')
    checklist([
        "<b>Know the farm</b> and the harvest date behind every box.",
        "<b>One order, one invoice</b> and one point of contact.",
        "<b>Works alongside</b> your current distributor, so no need to switch.",
        "<b>Fresh, seasonal</b> produce from Montérégie.",
    ])
    html('<div class="eyebrow">Where we would deliver first</div>')
    st.caption("Chemin de la Côte-Sainte-Catherine is the 5.5 km main street of the former village of Outremont. "
               "We would confirm the first delivery area with our first grocer.")
with right:
    area_map(MAIN_STREET, center=(45.5022, -73.6242), zoom=11.5, highlight=tuple(MAIN_STREET))

spacer(48)
with st.container(key="ask"):
    html("""
    <div class="cta-title">Are you one of them?</div>
    <p class="cta-text">You would like to eat, cook or serve more consciously, but the offer is missing where you
    shop or dine. Tell us, and help us decide where to start.</p>
    """)
    st.caption(content.POLL_PRIVACY)
    if not st.session_state.get("voted"):
        c1, c2, _ = st.columns([1.2, 1, 2])
        with c1:
            if st.button("Yes, that's me", type="primary", key="poll_yes"):
                storage.save_poll("yes")
                st.session_state["voted"] = "yes"
                st.rerun()
        with c2:
            if st.button("Not really", key="poll_no"):
                storage.save_poll("no")
                st.session_state["voted"] = "no"
                st.rerun()
    else:
        html('<p class="cta-text">Thank you for telling us.</p>')
    yes, _total = storage.poll_counts()
    if yes >= config.POLL_MIN_TO_SHOW:
        html(f'<p class="small" >{yes} people have already said yes.</p>')
    spacer(8)
    html('<p class="cta-text">Run a grocery or a restaurant and want to transform your offer?</p>')
    if st.button("Bring local to my shop or kitchen", type="primary", key="buyers_join"):
        open_join("Grocery store")
footer()
