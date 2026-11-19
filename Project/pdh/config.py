"""Settings and constants. Change names, paths and contact details here."""
from __future__ import annotations

import os
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
# Where sign-ups and poll answers are written. Override with the PDH_DATA_DIR environment variable.
DATA_DIR = Path(os.environ.get("PDH_DATA_DIR", ROOT / "data"))
SIGNUP_FILE = DATA_DIR / "signups.csv"
POLL_FILE = DATA_DIR / "poll.csv"

BRAND = "Producer Distribution Hub"
TAGLINE = "Know what you eat. High quality. Be conscious."
CONTACT_EMAIL = "johanna-luisa.schmucker@hec.ca"
ROLES = ["Farm", "Grocery store", "Restaurant", "Something else"]

POLL_MIN_TO_SHOW = 5  # show the "N people said yes" line only once the number is credible
PILOT_WEEKS = 30
