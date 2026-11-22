"""Shared building blocks: HTML helper, top bar, footer, sign-up pop-up."""
from __future__ import annotations

import streamlit as st

from pdh import config, content, storage

CHECK = ('<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#2E7D32" stroke-width="2.5" '
         'stroke-linecap="round" stroke-linejoin="round"><path d="M5 12.5l4.5 4.5L19 7.5"></path></svg>')


def html(block: str) -> None:
    """Render raw HTML. Indentation is stripped so Markdown does not turn it into a code block."""
    st.markdown("\n".join(line.strip() for line in block.splitlines()), unsafe_allow_html=True)


def spacer(px: int = 64) -> None:
    html(f'<div style="height:{px}px"></div>')


def checklist(items: list[str]) -> None:
    html('<ul class="checks">' + "".join(f"<li>{CHECK}<span>{t}</span></li>" for t in items) + "</ul>")


@st.dialog("Join our first season")
def join_dialog() -> None:
    st.write("We are starting with a small trial of two or three farms and one grocer. "
             "Leave your details and we will get back to you.")
    st.caption(content.PRIVACY)
    default_role = st.session_state.get("role_default", "Farm")
    with st.form("signup"):
        name = st.text_input("Your name")
        email = st.text_input("Email")
        role = st.selectbox("I am a", config.ROLES,
                            index=config.ROLES.index(default_role) if default_role in config.ROLES else 0)
        feedback = st.text_area(content.FEEDBACK_LABEL, height=90)
        note = st.text_area("Anything else we should know? (optional)", height=70)
        submitted = st.form_submit_button("Send", type="primary")
    if submitted:
        if not name.strip() or not storage.valid_email(email):
            st.error("Please enter your name and a valid email address.")
        else:
            storage.save_signup(name.strip(), email.strip(), role, note.strip(), feedback.strip())
            st.success("Thank you. We will be in touch.")


def open_join(role: str) -> None:
    st.session_state["role_default"] = role
    join_dialog()


LOGO = '<svg width="34" height="20" viewBox="0 0 34 20" aria-hidden="true"><line x1="5" y1="10" x2="29" y2="10" stroke="#111" stroke-width="2"/><circle cx="5" cy="10" r="4" fill="#111"/><circle cx="17" cy="10" r="6" fill="#2E7D32"/><circle cx="29" cy="10" r="4" fill="#111"/></svg>'

NAV = [("views/home.py", "Home"), ("views/farms.py", "For farms"),
       ("views/buyers.py", "For grocers and restaurants"), ("views/model.py", "Business model")]


def top_bar() -> None:
    """Brand, page tabs and Join button. The row wraps onto a second line when the window gets narrow."""
    with st.container(key="topbar"):
        brand, *tabs, join = st.columns(6, vertical_alignment="center")
        with brand:
            html('<div class="brand">'+LOGO+f'{config.BRAND}</div>')
        for col, (path, label) in zip(tabs, NAV):
            with col:
                st.page_link(path, label=label)
        with join:
            if st.button("Join", type="primary", key="top_join"):
                open_join("Farm")
    spacer(28)


def footer() -> None:
    html(f"""
    <div class="footer"><span>{config.BRAND}, Montérégie, Québec</span>
    <span>Contact: <a href="mailto:{config.CONTACT_EMAIL}" style="color:inherit">{config.CONTACT_EMAIL}</a> &nbsp;|&nbsp; A student start-up project, HEC Montréal</span></div>
    """)
