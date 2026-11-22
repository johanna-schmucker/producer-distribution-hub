# Producer Distribution Hub: website

Streamlit site with four pages (Home, For farms, For grocers and restaurants, Our numbers), a sign-up pop-up,
a poll, two maps and an interactive break-even model.

## Run
    pip install -r requirements.txt
    streamlit run app.py

## Structure
    app.py            entry point: page config, styles, top navigation
    views/            one file per page
    pdh/content.py    ALL website copy, FAQ and sourced statistics (edit text here)
    pdh/config.py     brand name, contact email, roles, data folder
    pdh/model.py      route economics and break-even maths
    pdh/geo.py        towns, Montréal areas, map
    pdh/storage.py    sign-ups and poll saved to CSV (swap for Google Sheets later)
    pdh/styles.py     white editorial look (colours, fonts)
    tests/            pytest: model, storage, every page
    .streamlit/       theme

## Test
    pip install -r requirements-dev.txt
    python -m pytest

## Before you publish
- Replace the [FARM NAME] style placeholders in the Erna example on the Home page.
- Sign-ups and poll answers go to `data/*.csv` and, once configured, to a Google Sheet (see `docs/google_sheet_setup.md`).
  On Streamlit Community Cloud the CSV is wiped on restart, so set up the Sheet.
- `CHANGELOG.md` records what changed on the page and the insight behind each change.
- Route cost ($500) and fixed costs ($100 a month) are illustrative. Replace with a real carrier quote.
- Map positions are approximate. Montréal areas are examples, not confirmed delivery zones.

## Deploy free
Push to GitHub, then on share.streamlit.io choose the repo and `app.py` as the main file.
