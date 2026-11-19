"""Tiny CSV storage for sign-ups and the poll. Swap this module for a Google Sheet or a database later."""
from __future__ import annotations

import csv
import re
import threading
from datetime import datetime

from pdh import config

_LOCK = threading.Lock()
EMAIL_RE = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")


def valid_email(value: str) -> bool:
    return bool(EMAIL_RE.match(value.strip()))


def _safe(cell: str) -> str:
    """Stop spreadsheet formula injection: a cell starting with = + - @ would run as a formula in Excel."""
    return "'" + cell if cell[:1] in ("=", "+", "-", "@") else cell


def _append(path, header: list[str], row: list[str]) -> None:
    with _LOCK:
        path.parent.mkdir(parents=True, exist_ok=True)
        new_file = not path.exists()
        with path.open("a", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            if new_file:
                writer.writerow(header)
            writer.writerow(row)


def save_signup(name: str, email: str, role: str, note: str) -> None:
    stamp = datetime.now().isoformat(timespec="seconds")
    _append(config.SIGNUP_FILE, ["timestamp", "name", "email", "role", "note"],
            [stamp, _safe(name), _safe(email), role, _safe(note)])


def save_poll(answer: str) -> None:
    if answer not in ("yes", "no"):
        raise ValueError("answer must be 'yes' or 'no'")
    _append(config.POLL_FILE, ["timestamp", "answer"], [datetime.now().isoformat(timespec="seconds"), answer])


def poll_counts() -> tuple[int, int]:
    """Return (yes answers, all answers)."""
    if not config.POLL_FILE.exists():
        return 0, 0
    with config.POLL_FILE.open(newline="", encoding="utf-8") as f:
        answers = [row["answer"] for row in csv.DictReader(f)]
    return answers.count("yes"), len(answers)
