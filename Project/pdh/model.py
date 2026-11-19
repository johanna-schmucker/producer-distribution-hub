"""The route economics behind the numbers page. Every input is an assumption we want to test in the pilot."""
from __future__ import annotations

import math
from dataclasses import dataclass

import pandas as pd

from pdh.config import PILOT_WEEKS

FARM_PAYMENT_DAYS = 14  # we pay farms within 14 days of delivery


@dataclass(frozen=True)
class RouteResult:
    per_stop: float          # what we keep from one stop
    break_even: int          # stops per route needed to cover route and fixed costs
    weekly_result: float
    season_result: float
    season_sales: float
    paid_to_farms: float
    working_capital: float   # cash we must front before grocers pay us


def weekly_fixed(monthly_fixed: float) -> float:
    return monthly_fixed * 12 / 52


def route_numbers(order: float, rate: float, route: float, stops: int, routes_per_week: int = 1,
                  monthly_fixed: float = 100, grocer_terms: int = 30, weeks: int = PILOT_WEEKS) -> RouteResult:
    per_stop = order * rate / 100
    fixed = weekly_fixed(monthly_fixed)
    sales_week = routes_per_week * stops * order
    farm_week = sales_week * (1 - rate / 100)
    weekly_result = routes_per_week * stops * per_stop - (routes_per_week * route + fixed)
    gap_days = max(0, grocer_terms - FARM_PAYMENT_DAYS)
    return RouteResult(
        per_stop=per_stop,
        break_even=math.ceil((route + fixed / routes_per_week) / per_stop),
        weekly_result=weekly_result,
        season_result=weekly_result * weeks,
        season_sales=sales_week * weeks,
        paid_to_farms=farm_week * weeks,
        # farm payouts made before grocers pay us, plus carrier costs while we wait
        working_capital=farm_week * gap_days / 7 + routes_per_week * route * grocer_terms / 7,
    )


def money(x: float) -> str:
    return f"-${abs(x):,.0f}" if x < 0 else f"${x:,.0f}"


def break_even_table(route: float, routes_per_week: int, monthly_fixed: float) -> pd.DataFrame:
    fixed = weekly_fixed(monthly_fixed)
    orders, rates = [200, 300, 400, 500], [15, 18, 20, 25]
    data = {f"{r}% commission": [math.ceil((route + fixed / routes_per_week) / (o * r / 100)) for o in orders]
            for r in rates}
    return pd.DataFrame(data, index=[f"${o} average order" for o in orders])


def weekly_result_curve(per_stop: float, route: float, routes_per_week: int, monthly_fixed: float,
                        max_stops: int = 20) -> pd.DataFrame:
    xs = list(range(1, max_stops + 1))
    results = [routes_per_week * x * per_stop - (routes_per_week * route + weekly_fixed(monthly_fixed)) for x in xs]
    return pd.DataFrame({"Loss": [min(v, 0) for v in results], "Profit": [max(v, 0) for v in results]}, index=xs)
