"""
============================================================================
DAY 04 (Python) — Lists & Two Pointers
============================================================================

READ ME FIRST:
    This file is a lesson. Read it top to bottom, then run it:
        python3 concept04.py
    Then RETYPE the key snippets from memory in exercise04.py.

TODAY'S BIG IDEAS:
    1. Python lists ARE dynamic arrays — append is amortized O(1).
    2. In-place vs copying: know which methods mutate and which return new.
    3. Two pointers translate 1:1 from Java — same template, cleaner syntax.
    4. sort() mutates in place; sorted() returns new. Interviewers notice.
============================================================================
"""


def list_fundamentals():
    # ------------------------------------------------------------------
    # 1. LIST FUNDAMENTALS (vs Java arrays)
    # ------------------------------------------------------------------
    print("=== 1. List fundamentals ===")

    # Dynamic — no fixed size, no separate ArrayList. Heterogeneous too:
    items = [1, "two", 3.0]
    print("heterogeneous:", items)

    nums = [10, 20, 30]
    nums.append(40)            # amortized O(1) — Python over-allocates
    nums.insert(0, 5)          # O(n) — everything shifts (same as Java!)
    nums.pop()                 # remove from END: O(1)
    nums.pop(0)                # remove from FRONT: O(n)
    print("after ops:", nums)

    # Need fast front operations? collections.deque — O(1) both ends.
    # (Name-drop this in interviews; deep dive on Day 10 - Stacks & Queues.)

    # Negative indexing (Python-only superpower):
    print("last element:", nums[-1], "| first:", nums[0])

    # len() not .length / .size()
    print("length:", len(nums))


def in_place_vs_copy():
    # ------------------------------------------------------------------
    # 2. IN-PLACE vs COPY — the methods interviewers quiz you on
    # ------------------------------------------------------------------
    print("\n=== 2. In-place vs copy ===")

    a = [3, 1, 2]

    b = sorted(a)              # NEW list, a untouched
    print("sorted(a):", b, "| a still:", a)

    a.sort()                   # MUTATES a, returns None (!)
    print("a.sort(): ", a)

    # TRAP: writing  x = a.sort()  leaves x = None. Same for a.reverse().
    c = [1, 2, 3]
    c.reverse()                # in place
    print("c.reverse():", c)
    print("c[::-1] creates a NEW reversed list:", c[::-1], "| c unchanged:", c)

    # list.remove(x) removes the first VALUE x; del list[i] removes INDEX i.
    d = [1, 2, 3, 2]
    d.remove(2)                # removes first 2
    print("after remove(2):", d)

    # Copying (Day 01 callback — assignment never copies!):
    e = d                      # alias, NOT a copy
    f = d.copy()               # or d[:] or list(d)
    e.append(99)
    print("d after e.append:", d, "| f (real copy):", f)


def two_pointers():
    # ------------------------------------------------------------------
    # 3. TWO POINTERS — same template as Java
    # ------------------------------------------------------------------
    print("\n=== 3. Two pointers ===")

    def reverse_in_place(arr):
        left, right = 0, len(arr) - 1
        while left < right:
            arr[left], arr[right] = arr[right], arr[left]   # tuple swap — no tmp!
            left += 1
            right -= 1

    data = [1, 2, 3, 4, 5]
    reverse_in_place(data)
    print("reversed in place:", data)

    def two_sum_sorted(nums, target):
        """Opposite-direction pointers on a SORTED list -> indices or None."""
        left, right = 0, len(nums) - 1
        while left < right:
            s = nums[left] + nums[right]
            if s == target:
                return (left, right)
            if s < target:
                left += 1      # need bigger sum
            else:
                right -= 1     # need smaller sum
        return None

    print("pair summing to 9:", two_sum_sorted([1, 2, 4, 7, 11, 15], 9))

    def move_zeroes(nums):
        """Slow/fast flavor — same as Java version."""
        slow = 0
        for fast in range(len(nums)):
            if nums[fast] != 0:
                nums[slow], nums[fast] = nums[fast], nums[slow]
                slow += 1

    z = [0, 1, 0, 3, 12]
    move_zeroes(z)
    print("move_zeroes:", z)

    # Pythonic alternative — know both, be ready to defend the tradeoff:
    #   non_zero = [x for x in z if x != 0] + [0] * z.count(0)
    #   Cleaner, but O(n) extra space. Two pointers = O(1) space.


def pythonic_tools():
    # ------------------------------------------------------------------
    # 4. PYTHONIC TOOLS you'd use in real code (mention, don't always use)
    # ------------------------------------------------------------------
    print("\n=== 4. Pythonic tools ===")

    nums = [120, 85, 0, 200, 95, 0, 150]

    print("max/min/sum:", max(nums), min(nums), sum(nums))
    print("non-zero days:", [x for x in nums if x != 0])          # comprehension
    print("running max:", [max(nums[:i+1]) for i in range(3)], "... (O(n^2) — don't!)")

    # enumerate — index + value together (Day 02 callback):
    for i, v in enumerate(nums[:3]):
        print(f"  day {i}: {v}")

    # zip — parallel iteration:
    days = ["Mon", "Tue", "Wed"]
    for d, v in zip(days, nums):
        print(f"  {d}: {v}")


def interview_questions():
    print("\n=== Interview quick-fire (answer aloud!) ===")
    print("  Q: sort() vs sorted()?           A: mutates/None vs returns new list")
    print("  Q: append cost?                  A: amortized O(1) — over-allocation")
    print("  Q: Fast removal from front?      A: collections.deque — O(1)")
    print("  Q: x = mylist.sort() — bug?      A: yes, x is None")
    print("  Q: Two-sum on sorted data?       A: two pointers O(n), not brute force")


if __name__ == "__main__":
    list_fundamentals()
    in_place_vs_copy()
    two_pointers()
    pythonic_tools()
    interview_questions()
