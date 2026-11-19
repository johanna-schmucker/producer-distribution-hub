import pytest

from pdh.model import break_even_table, money, route_numbers


def test_default_assumptions():
    r = route_numbers(300, 18, 500, 12)
    assert r.per_stop == 54
    assert r.break_even == 10
    assert r.weekly_result == pytest.approx(124.9, abs=0.1)
    assert r.season_sales == 108_000
    assert r.paid_to_farms == pytest.approx(88_560)
    assert r.working_capital == pytest.approx(8_890, abs=5)


def test_break_even_stops_means_no_loss():
    r = route_numbers(300, 18, 500, 10)
    assert r.weekly_result > 0
    assert route_numbers(300, 18, 500, 9).weekly_result < 0


def test_faster_grocer_payment_needs_less_cash():
    assert route_numbers(300, 18, 500, 12, grocer_terms=14).working_capital < route_numbers(300, 18, 500, 12).working_capital


def test_money_format():
    assert money(1234.4) == "$1,234"
    assert money(-253.2) == "-$253"


def test_table_shape():
    t = break_even_table(500, 1, 100)
    assert t.shape == (4, 4)
    assert t.loc["$300 average order", "18% commission"] == 10
