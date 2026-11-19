import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))


@pytest.fixture(autouse=True)
def tmp_data(tmp_path, monkeypatch):
    """Never write test data into the real data folder."""
    from pdh import config
    monkeypatch.setattr(config, "SIGNUP_FILE", tmp_path / "signups.csv")
    monkeypatch.setattr(config, "POLL_FILE", tmp_path / "poll.csv")
    return tmp_path
