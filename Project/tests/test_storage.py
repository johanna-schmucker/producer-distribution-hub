import csv

import pytest

from pdh import config, storage


def test_signup_is_saved_with_header():
    storage.save_signup("Erna Farm", "erna@example.com", "Farm", "hello")
    rows = list(csv.reader(config.SIGNUP_FILE.open(encoding="utf-8")))
    assert rows[0] == ["timestamp", "name", "email", "role", "note"]
    assert rows[1][1:] == ["Erna Farm", "erna@example.com", "Farm", "hello"]


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
