import csv

import pytest

from pdh import config, storage


def test_signup_is_saved_with_header():
    storage.save_signup("Erna Farm", "erna@example.com", "Farm", "hello", "more photos")
    rows = list(csv.reader(config.SIGNUP_FILE.open(encoding="utf-8")))
    assert rows[0] == ["timestamp", "name", "email", "role", "note", "feedback"]
    assert rows[1][1:] == ["Erna Farm", "erna@example.com", "Farm", "hello", "more photos"]


def test_formula_injection_is_neutralised():
    storage.save_signup("=HYPERLINK(\"x\")", "a@b.co", "Farm", "+1")
    row = list(csv.reader(config.SIGNUP_FILE.open(encoding="utf-8")))[1]
    assert row[1].startswith("'") and row[4].startswith("'")


@pytest.mark.parametrize("email,ok", [("a@b.co", True), (" a@b.co ", True), ("nope", False), ("a@b", False), ("", False)])
def test_email_validation(email, ok):
    assert storage.valid_email(email) is ok


def test_poll_counts():
    assert storage.poll_counts() == (0, 0)
    for a in ("yes", "yes", "no"):
        storage.save_poll(a)
    assert storage.poll_counts() == (2, 3)
    with pytest.raises(ValueError):
        storage.save_poll("maybe")


def test_no_sheet_configured_returns_none(monkeypatch):
    monkeypatch.setattr(storage, "_sheet_settings", lambda: None)
    assert storage.save_signup("A", "a@b.co", "Farm") is None


def test_sheet_receives_signup_and_csv_backup_kept(monkeypatch):
    sent = {}

    class Reply:
        ok = True
        def json(self): return {"ok": True}

    def fake_post(url, data, headers, timeout):
        sent.update(url=url, body=__import__("json").loads(data))
        return Reply()

    monkeypatch.setattr(storage, "_sheet_settings", lambda: ("https://example.test/exec", "secret"))
    monkeypatch.setattr("requests.post", fake_post)
    assert storage.save_signup("A", "a@b.co", "Farm", "n", "change the photo") is True
    assert sent["body"]["token"] == "secret" and sent["body"]["feedback"] == "change the photo"
    assert config.SIGNUP_FILE.exists()


def test_sheet_failure_does_not_lose_signup(monkeypatch):
    monkeypatch.setattr(storage, "_sheet_settings", lambda: ("https://example.test/exec", "t"))
    def boom(*a, **k): raise OSError("offline")
    monkeypatch.setattr("requests.post", boom)
    assert storage.save_signup("A", "a@b.co", "Farm") is False
    assert config.SIGNUP_FILE.exists()
