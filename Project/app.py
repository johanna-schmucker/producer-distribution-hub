"""Producer Distribution Hub website. Run with:  streamlit run app.py"""
import streamlit as st

from pdh import config, styles

st.set_page_config(page_title=f"{config.BRAND} | Local food with a face and a farm", page_icon="🌱", layout="wide")
styles.inject()

st.navigation(
    [
        st.Page("views/home.py", title="Home", default=True),
        st.Page("views/farms.py", title="For farms", url_path="farms"),
        st.Page("views/buyers.py", title="For grocers and restaurants", url_path="grocers"),
        st.Page("views/model.py", title="Business model", url_path="business-model"),
    ],
    position="hidden",
).run()
