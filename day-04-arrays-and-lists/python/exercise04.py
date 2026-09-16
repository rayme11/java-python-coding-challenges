"""
============================================================================
DAY 04 EXERCISE (Python) — Sales Dashboard
============================================================================
Apply today's concepts: lists, in-place vs copy, two pointers.
Fill in every TODO, then run:  python3 exercise04.py
Target time: 15–20 minutes.
============================================================================
"""


def main():
    daily_sales = [120, 85, 0, 200, 95, 0, 150]

    # ------------------------------------------------------------------
    # TASK 1: Print the list, its length, the first element, and the
    # last element using NEGATIVE indexing.
    # ------------------------------------------------------------------
    # TODO 1


    # ------------------------------------------------------------------
    # TASK 2: Write find_max(nums) WITHOUT using max() — one loop.
    # Edge case in a comment: what should an empty list return?
    # (None? raise ValueError? Pick one, defend it in the comment.)
    # Print find_max(daily_sales), then verify against max(daily_sales).
    # ------------------------------------------------------------------
    # TODO 2


    # ------------------------------------------------------------------
    # TASK 3: Write reverse_in_place(nums) using two pointers and a
    # tuple swap. Print a COPY reversed (daily_sales.copy()) so the
    # original stays intact. Comment: what does this return and why?
    # ------------------------------------------------------------------
    # TODO 3


    # ------------------------------------------------------------------
    # TASK 4: Write remove_zero_days(nums) returning a new list without
    # the zero-sales days — twice:
    #   a) with a loop
    #   b) with a comprehension
    # Print both; they must be equal.
    # ------------------------------------------------------------------
    # TODO 4


    # ------------------------------------------------------------------
    # TASK 5: Write has_pair_summing_to(sorted_nums, target) using
    # opposite-direction two pointers. Sort a COPY of daily_sales first
    # (which function — sort() or sorted()? say why in a comment).
    # Test with 285 (find the real pair) and 999.
    # ------------------------------------------------------------------
    # TODO 5


    # ------------------------------------------------------------------
    # TASK 6: Write running_totals(nums) returning the prefix-sum list:
    #   [120, 85, 0, 200] -> [120, 205, 205, 405]
    # One loop; each element reuses the previous total. Print it.
    # Comment: what's the time complexity, and why is it NOT O(n^2)?
    # ------------------------------------------------------------------
    # TODO 6


    # ------------------------------------------------------------------
    # STRETCH (optional): Write max_subarray_sum(nums) — Kadane's:
    #   [-2, 1, -3, 4, -1, 2, 1, -5, 4] -> 6   (subarray [4, -1, 2, 1])
    # Track current_sum = max(num, current_sum + num) and the best seen.
    # Top-10 interview question — worth the extra 10 minutes.
    # ------------------------------------------------------------------
    # TODO STRETCH


# Write your helper functions below:


if __name__ == "__main__":
    main()
