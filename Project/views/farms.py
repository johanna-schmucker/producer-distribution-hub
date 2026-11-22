import streamlit as st

from pdh.geo import MONTEREGIE_TOWNS, circle_map
from pdh.ui import checklist, footer, html, open_join, top_bar

top_bar()
left, right = st.columns([1, 1.15], gap="large")
with left:
    html("""
    <div class="eyebrow">For farms</div>
    <div class="page-title">Grow. We handle the rest.</div>
    <p class="lead">Sell your harvest to specialty grocers and restaurants without chasing buyers, delivering or invoicing.</p>
    """)
    checklist([
        "<b>No upfront fee.</b> We only earn a commission when you sell.",
        "<b>Paid within 14 days</b> of delivery. This is our plan for the pilot.",
        "<b>Your farm and your story</b> reach buyers who care about them.",
        "<b>We handle</b> pooling, delivery, invoicing and customer contact.",
    ])
    html('<div class="eyebrow">Is your farm in our area?</div>')
    options = ["Choose your town or area"] + list(MONTEREGIE_TOWNS) + ["Somewhere else in Québec", "Outside Québec"]
    place = st.selectbox("Where is your farm?", options, label_visibility="collapsed", key="farm_place")
    if place in MONTEREGIE_TOWNS:
        st.success(f"{place} is inside our launch area in Montérégie. Join us and be one of our first farms.")
    elif place == "Somewhere else in Québec":
        st.info("We start in Montérégie. Leave your details and we will tell you when we reach your area.")
    elif place == "Outside Québec":
        st.info("We are focused on Québec for now, but tell us about your farm and we will keep you posted.")
    if st.button("Join as a farm", type="primary", key="farms_join"):
        open_join("Farm")
with right:
    circle_map(center=(45.5, -73.3), zoom=7.4, radius=62000)
    st.caption("Montérégie, south of Montréal. The shaded circle is the approximate launch area.")
footer()
