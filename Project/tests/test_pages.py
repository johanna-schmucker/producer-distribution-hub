"""Run every page headlessly and exercise its controls."""
from pathlib import Path

import pytest
from streamlit.testing.v1 import AppTest

from pdh import storage

ROOT = Path(__file__).resolve().parent.parent
PAGES = ["home", "farms", "buyers", "model"]


def run(page: str) -> AppTest:
    """Load the real app (so navigation exists) and switch to the page."""
    at = AppTest.from_file(str(ROOT / "app.py"), default_timeout=30).run()
    if page != "home":
        at.switch_page(f"views/{page}.py").run()
    assert not at.exception, at.exception
    return at


@pytest.mark.parametrize("page", PAGES)
def test_page_renders(page):
    at = run(page)
    assert at.button


def test_home_has_ctas_and_is_short():
    at = run("home")
    assert {"hero_join", "cta_join", "top_join"} <= {b.key for b in at.button}
    assert not at.expander


def test_model_page_has_faq_and_correct_split():
    at = run("model")
    assert len(at.expander) == 6
    text = " ".join(m.value for m in at.markdown)
    assert "$54" in text and "$246" in text


def test_farm_picker_reacts():
    at = run("farms")
    at.selectbox(key="farm_place").select("Granby").run()
    assert "launch area" in at.success[0].value
    at.selectbox(key="farm_place").select("Outside Québec").run()
    assert at.info and not at.success


def test_poll_records_answer():
    at = run("buyers")
    at.button(key="poll_yes").click().run()
    assert storage.poll_counts() == (1, 1)
    assert not [b for b in at.button if b.key == "poll_yes"]
