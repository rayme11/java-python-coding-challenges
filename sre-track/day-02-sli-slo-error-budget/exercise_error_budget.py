"""
============================================================================
SRE DAY 02 EXERCISE (Python) — Error Budget Calculator
============================================================================
Apply today's concepts: SLO math, budget windows, burn rate.
Fill in every TODO, then run:  python3 exercise_error_budget.py
All asserts at the bottom must pass. Target time: 25 minutes.

Why this matters: "Can we ship this week?" is an error-budget question.
SREs who can do this math in their head command the room in reviews.
============================================================================
"""

MINUTES_PER_30_DAY_MONTH = 30 * 24 * 60  # 43,200


def downtime_budget_minutes(slo_percent: float, days: int = 30) -> float:
    """Allowed downtime in minutes for a given SLO over `days` days.

    Example: 99.9% over 30 days -> 0.1% of 43,200 min -> 43.2 min

    TODO 1: implement.
    """
    # TODO 1
    pass


def error_budget_requests(slo_percent: float, total_requests: int) -> float:
    """How many requests may fail within budget?

    Example: 99.9% SLO, 43_200_000 requests -> 43_200 allowed failures.

    TODO 2: implement.
    """
    # TODO 2
    pass


def observed_slo_percent(good: int, total: int) -> float:
    """The SLI, as a percentage. 99_900 good / 100_000 total -> 99.9

    TODO 3: implement. Guard against total == 0 (define it as 100.0 — a
    service with zero traffic has perfect availability, by convention).
    """
    # TODO 3
    pass


def budget_remaining_percent(slo_percent: float, good: int, total: int) -> float:
    """What fraction of the error budget is LEFT, as a percentage?

    budget total  = allowed failures at the SLO
    budget used   = actual failures
    remaining %   = (1 - used/total) * 100

    Example: SLO 99.9%, 100_000 requests, 50 failures:
      allowed = 100 failures, used 50 -> 50% remaining.

    Can go NEGATIVE (budget exhausted). TODO 4: implement.
    """
    # TODO 4
    pass


def burn_rate(slo_percent: float, observed_error_rate: float) -> float:
    """How fast are we burning budget, relative to 'exactly on SLO'?

    burn_rate = observed_error_rate / budgeted_error_rate
      = 1.0  -> consuming budget exactly at SLO pace (miss SLO at period end)
      = 2.0  -> burning twice as fast as allowed
      = 0.5  -> burning half — healthy, will finish with budget to spare

    TODO 5: implement.
    """
    # TODO 5
    pass


def can_we_ship(slo_percent: float, good: int, total: int,
                day_of_period: int, period_days: int = 30) -> str:
    """The product-manager question, answered with math.

    Policy (a classic error-budget policy, simplified):
      - budget remaining < 0%                 -> "FREEZE: reliability work only"
      - burn rate over period so far > 1.0    -> "CAUTION: reliability focus this sprint"
      - otherwise                             -> "SHIP IT"

    Compute observed errors, remaining budget, and burn rate so far, then
    return one of the three strings exactly.

    TODO 6: implement using the functions above.
    """
    # TODO 6
    pass


# ============================================================================
# TESTS — do not edit. Make them pass.
# ============================================================================
def _approx(a: float, b: float, tol: float = 0.01) -> bool:
    return abs(a - b) <= tol


def run_tests():
    # TODO 1
    assert _approx(downtime_budget_minutes(99.9), 43.2)
    assert _approx(downtime_budget_minutes(99.99), 4.32)
    assert _approx(downtime_budget_minutes(99.5, days=1), 7.2)

    # TODO 2
    assert _approx(error_budget_requests(99.9, 43_200_000), 43_200)
    assert _approx(error_budget_requests(99.0, 1_000), 10)

    # TODO 3
    assert _approx(observed_slo_percent(99_900, 100_000), 99.9)
    assert _approx(observed_slo_percent(0, 0), 100.0)

    # TODO 4
    assert _approx(budget_remaining_percent(99.9, good=99_950, total=100_000), 50.0)
    assert _approx(budget_remaining_percent(99.9, good=99_900, total=100_000), 0.0)
    assert budget_remaining_percent(99.9, good=99_800, total=100_000) < 0  # exhausted

    # TODO 5
    assert _approx(burn_rate(99.9, 0.1), 1.0)   # 0.1% errors vs 0.1% budget
    assert _approx(burn_rate(99.9, 0.2), 2.0)
    assert _approx(burn_rate(99.9, 0.05), 0.5)

    # TODO 6
    assert can_we_ship(99.9, good=99_950, total=100_000, day_of_period=15) == "SHIP IT"
    assert can_we_ship(99.9, good=99_800, total=100_000, day_of_period=10) == "FREEZE: reliability work only"
    assert can_we_ship(99.9, good=99_880, total=100_000, day_of_period=5) == "CAUTION: reliability focus this sprint"

    print("✅ All error-budget tests pass.")


if __name__ == "__main__":
    run_tests()

    # Once tests pass, play with YOUR numbers:
    # - What's the downtime budget at 99.95%? (common App Service SLA tier)
    # - Your API did 2M requests with 3,000 failures against a 99.9% SLO.
    #   Print the burn rate and the ship/freeze verdict. Would YOU ship?
