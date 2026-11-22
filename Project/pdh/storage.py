"""Sign-ups and poll answers.

Every answer is written to a CSV backup. When a Google Sheet web app is configured (see docs/google_sheet_setup.md),
it is also sent there, so nothing is lost when Streamlit Cloud restarts the app.
"""
from __future__ import annotations

import csv
import json
import os
import re
import threading
import time
from datetime import datetime

from pdh import config

_LOCK = threading.Lock()
EMAIL_RE = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")
_poll_cache: dict = {"t": 0.0, "value": None}


def valid_email(value: str) -> bool:
    return bool(EMAIL_RE.match(value.strip()))


def _safe(cell: str) -> str:
    """Stop spreadsheet formula injection: a cell starting with = + - @ would run as a formula."""
    return "'" + cell if cell[:1] in ("=", "+", "-", "@") else cell


def _sheet_settings() -> tuple[str, str] | None:
    """Return (web app url, shared token) if a Google Sheet is configured, else None."""
    url, token = os.environ.get("PDH_SHEET_URL"), os.environ.get("PDH_SHEET_TOKEN", "")
    if not url:
        try:
            import streamlit as st
            section = st.secrets["sheet"]
            url, token = section["webhook_url"], section.get("token", "")
        except Exception:  # no secrets file or no [sheet] section
            return None
    return (url, token) if url else None


def _post_to_sheet(payload: dict) -> bool | None:
    """Send one row to the Google Sheet. None = not configured, True = saved, False = failed."""
    settings = _sheet_settings()
    if not settings:
        return None
    import requests
    try:
        reply = requests.post(settings[0], data=json.dumps({**payload, "token": settings[1]}),
                              headers={"Content-Type": "text/plain"}, timeout=8)
        return bool(reply.ok and reply.json().get("ok"))
    except Exception:
        return False


def _append(path, header: list[str], row: list[str]) -> None:
    with _LOCK:
        path.parent.mkdir(parents=True, exist_ok=True)
        new_file = not path.exists()
        with path.open("a", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            if new_file:
                writer.writerow(header)
            writer.writerow(row)


def save_signup(name: str, email: str, role: str, note: str = "", feedback: str = "") -> bool | None:
    """Save a sign-up. Returns the Google Sheet result (None when no sheet is configured)."""
    row = [datetime.now().isoformat(timespec="seconds"), _safe(name), _safe(email), role, _safe(note), _safe(feedback)]
    _append(config.SIGNUP_FILE, ["timestamp", "name", "email", "role", "note", "feedback"], row)
    return _post_to_sheet({"kind": "signup", "name": row[1], "email": row[2], "role": role, "note": row[4],
                           "feedback": row[5]})


def save_poll(answer: str) -> None:
    if answer not in ("yes", "no"):
        raise ValueError("answer must be 'yes' or 'no'")
    _append(config.POLL_FILE, ["timestamp", "answer"], [datetime.now().isoformat(timespec="seconds"), answer])
    _post_to_sheet({"kind": "poll", "answer": answer})
    _poll_cache["value"] = None  # next read fetches the new total


def _poll_counts_from_sheet(settings: tuple[str, str]) -> tuple[int, int] | None:
    if _poll_cache["value"] and time.time() - _poll_cache["t"] < 60:
        return _poll_cache["value"]
    import requests
    try:
        data = requests.get(settings[0], params={"token": settings[1]}, timeout=5).json()
        if data.get("ok"):
            _poll_cache.update(t=time.time(), value=(int(data["yes"]), int(data["total"])))
            return _poll_cache["value"]
    except Exception:
        pass
    return None


def poll_counts() -> tuple[int, int]:
    """Return (yes answers, all answers). Uses the Google Sheet when configured, else the CSV."""
    settings = _sheet_settings()
    if settings:
        counts = _poll_counts_from_sheet(settings)
        if counts:
            return counts
    if not config.POLL_FILE.exists():
        return 0, 0
    with config.POLL_FILE.open(newline="", encoding="utf-8") as f:
        answers = [row["answer"] for row in csv.DictReader(f)]
    return answers.count("yes"), len(answers)
