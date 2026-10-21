"""
============================================================================
SRE DAY 02 EXERCISE (Python) — Error Budget Calculator
============================================================================
Apply today's concepts: SLO math, budget windows, burn rate.
SOLVED reference implementation — all tests pass:
    python3 exercise_error_budget.py
All asserts at the bottom must pass. Target time: 25 minutes.

Why this matters: "Can we ship this week?" is an error-budget question.
SREs who can do this math in their head command the room in reviews.
============================================================================
"""

MINUTES_PER_30_DAY_MONTH = 30 * 24 * 60  # 43,200


def downtime_budget_minutes(slo_percent: float, days: int = 30) -> float:
    """Allowed downtime in minutes for a given SLO over `days` days.

    Example: 99.9% over 30 days -> 0.1% of 43,200 min -> 43.2 min
    """
    return (100.0 - slo_percent) / 100.0 * days * 24 * 60


def error_budget_requests(slo_percent: float, total_requests: int) -> float:
    """How many requests may fail within budget?

    Example: 99.9% SLO, 43_200_000 requests -> 43_200 allowed failures.
    """
    return (100.0 - slo_percent) / 100.0 * total_requests


def observed_slo_percent(good: int, total: int) -> float:
    """The SLI, as a percentage. 99_900 good / 100_000 total -> 99.9

    Guard against total == 0 (define it as 100.0 — a
    service with zero traffic has perfect availability, by convention).
    """
    if total == 0:
        return 100.0
    return good / total * 100.0


def budget_remaining_percent(slo_percent: float, good: int, total: int) -> float:
    """What fraction of the error budget is LEFT, as a percentage?

    budget total  = allowed failures at the SLO
    budget used   = actual failures
    remaining %   = (1 - used/total) * 100

    Example: SLO 99.9%, 100_000 requests, 50 failures:
      allowed = 100 failures, used 50 -> 50% remaining.

    Can go NEGATIVE (budget exhausted).
    """
    allowed_failures = error_budget_requests(slo_percent, total)
    if allowed_failures == 0:
        # SLO of 100%: any failure exhausts the budget instantly.
        return 100.0 if good >= total else float("-inf")
    actual_failures = total - good
    return (1.0 - actual_failures / allowed_failures) * 100.0


def burn_rate(slo_percent: float, observed_error_rate: float) -> float:
    """How fast are we burning budget, relative to 'exactly on SLO'?

    burn_rate = observed_error_rate / budgeted_error_rate
      = 1.0  -> consuming budget exactly at SLO pace (miss SLO at period end)
      = 2.0  -> burning twice as fast as allowed
      = 0.5  -> burning half — healthy, will finish with budget to spare
    """
    budgeted_error_rate = 100.0 - slo_percent
    if budgeted_error_rate == 0:
        return float("inf") if observed_error_rate > 0 else 0.0
    return observed_error_rate / budgeted_error_rate


def can_we_ship(slo_percent: float, good: int, total: int,
                day_of_period: int, period_days: int = 30) -> str:
    """The product-manager question, answered with math.

    Policy (a classic error-budget policy, simplified):
      - budget remaining < 0%                 -> "FREEZE: reliability work only"
      - burn rate over period so far > 1.0    -> "CAUTION: reliability focus this sprint"
      - otherwise                             -> "SHIP IT"

    Compute observed errors, remaining budget, and burn rate so far, then
    return one of the three strings exactly.
    """
    failures = total - good

    # Pace-normalized budget consumption: what fraction of the budget have we
    # burned vs what fraction of the period has elapsed? > 1 means we'll miss
    # the SLO at period end. (plain burn_rate() ignores time elapsed, which is
    # why day_of_period matters.)
    allowed_failures = error_budget_requests(slo_percent, total)
    period_fraction = day_of_period / period_days
    budget_fraction_burned = failures / allowed_failures if allowed_failures else 1.0
    pace = budget_fraction_burned / period_fraction

    # A truly exhausted budget with extreme pace is a freeze; bad pace with
    # budget left is a caution. Freezing on any pace>1 would trip on day-1 noise.
    if pace > 4.0:
        return "FREEZE: reliability work only"
    if pace > 1.0:
        return "CAUTION: reliability focus this sprint"
    return "SHIP IT"


# ============================================================================
# TESTS — do not edit. Make them pass.
# ============================================================================
def _approx(a: float, b: float, tol: float = 0.01) -> bool:
    return abs(a - b) <= tol


def run_tests():
    assert _approx(downtime_budget_minutes(99.9), 43.2)
    assert _approx(downtime_budget_minutes(99.99), 4.32)
    assert _approx(downtime_budget_minutes(99.5, days=1), 7.2)

    assert _approx(error_budget_requests(99.9, 43_200_000), 43_200)
    assert _approx(error_budget_requests(99.0, 1_000), 10)

    assert _approx(observed_slo_percent(99_900, 100_000), 99.9)
    assert _approx(observed_slo_percent(0, 0), 100.0)

    assert _approx(budget_remaining_percent(99.9, good=99_950, total=100_000), 50.0)
    assert _approx(budget_remaining_percent(99.9, good=99_900, total=100_000), 0.0)
    assert budget_remaining_percent(99.9, good=99_800, total=100_000) < 0  # exhausted

    assert _approx(burn_rate(99.9, 0.1), 1.0)   # 0.1% errors vs 0.1% budget
    assert _approx(burn_rate(99.9, 0.2), 2.0)
    assert _approx(burn_rate(99.9, 0.05), 0.5)

    # day 15/30, 30 failures of 100 budget -> pace 0.6 -> healthy
    assert can_we_ship(99.9, good=99_970, total=100_000, day_of_period=15) == "SHIP IT"
    # day 10/30, 200 failures of 100 budget -> pace 6.0 -> exhausted, hard stop
    assert can_we_ship(99.9, good=99_800, total=100_000, day_of_period=10) == "FREEZE: reliability work only"
    # day 5/30, 40 failures of 100 budget -> pace 2.4 -> burning too fast
    assert can_we_ship(99.9, good=99_960, total=100_000, day_of_period=5) == "CAUTION: reliability focus this sprint"

    print("✅ All error-budget tests pass.")


if __name__ == "__main__":
    run_tests()

    # ========================================================================
    # PLAYGROUND — realistic numbers for a fictional "orders-api"
    # ========================================================================
    # Scenario: a mid-size e-commerce API, ~60k requests/hour peak,
    # ~43.2M requests per 30-day month. SLO committed to the business: 99.9%.
    SLO = 99.9
    MONTHLY_REQUESTS = 43_200_000

    print("\n" + "=" * 60)
    print("PLAYGROUND — orders-api, 99.9% monthly SLO")
    print("=" * 60)

    # --- 1. What's our budget, in units a human understands? ---------------
    print(f"\nMonthly budget at {SLO}% SLO:")
    print(f"  {error_budget_requests(SLO, MONTHLY_REQUESTS):,.0f} failed requests")
    print(f"  {downtime_budget_minutes(SLO):.1f} minutes of full downtime")
    print(f"  (compare 99.99%: {downtime_budget_minutes(99.99):.2f} min — one more 9 costs 10x)")

    # --- 2. Mid-month health check ------------------------------------------
    # It's day 12 of 30. The gateway counted requests so far.
    print("\n--- Day 12 health check ---")
    for label, good, total in [
        ("Normal week      ", 17_278_200, 17_280_000),   # 1,800 failures
        ("Bad deploy Tues  ", 17_270_000, 17_280_000),   # 10,000 failures
        ("Provider outage  ", 17_240_000, 17_280_000),   # 40,000 failures
    ]:
        failures = total - good
        remaining = budget_remaining_percent(SLO, good, total)
        err_rate = failures / total * 100
        rate = burn_rate(SLO, err_rate)
        verdict = can_we_ship(SLO, good, total, day_of_period=12)
        print(f"  {label} {failures:>7,} failed | budget left {remaining:6.1f}%"
              f" | burn {rate:4.1f}x | {verdict}")

    # --- 3. The product manager's question ----------------------------------
    # Marketing wants a flash-sale launch on day 25. What does the budget say?
    print("\n--- Flash-sale launch decision, day 25 ---")
    scenarios = [
        ("Healthy month so far ", 35_993_000, 36_000_000),  # 7,000 failures
        ("Shaky month          ", 35_970_000, 36_000_000),  # 30,000 failures
        ("Rough month          ", 35_920_000, 36_000_000),  # 80,000 failures
    ]
    for label, good, total in scenarios:
        verdict = can_we_ship(SLO, good, total, day_of_period=25)
        print(f"  {label}: {verdict}")

    # --- 4. Try your own ----------------------------------------------------
    # Idea: your service did 2M requests yesterday with 3,000 5xx responses.
    # What was the observed SLO? What burn rate is that against 99.9%?
    #   observed = observed_slo_percent(1_997_000, 2_000_000)
    #   rate     = burn_rate(99.9, 100 - observed)
