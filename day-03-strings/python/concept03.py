"""
============================================================================
DAY 03 (Python) — Strings & String Manipulation
============================================================================

READ ME FIRST:
    This file is a lesson. Read it top to bottom, then run it:
        python3 concept03.py
    Then RETYPE the key snippets from memory in exercise03.py.

TODAY'S BIG IDEAS:
    1. Python strings are IMMUTABLE — every "modification" makes a new one.
    2. Slicing s[start:stop:step] is the superpower; stop is EXCLUSIVE.
    3. `+=` in a loop is a trap; "".join(parts) is the idiom.
    4. The method toolkit: split, join, strip, replace, find, case methods.
    5. Palindrome via s == s[::-1] — and via two pointers for interviews.
============================================================================
"""


def immutability():
    # ------------------------------------------------------------------
    # 1. IMMUTABILITY
    # ------------------------------------------------------------------
    print("=== 1. Immutability ===")

    s = "hello"
    s.upper()                      # result DISCARDED
    print("after s.upper():      ", s)          # still "hello"

    s = s.upper()                  # rebind to the NEW string
    print("after rebinding:      ", s)          # "HELLO"

    # s[0] = "J"                   # TypeError: strings don't support item assignment

    # Unlike Java, == compares VALUES by default (that's what you want).
    a = "java"
    b = "".join(["j", "a", "v", "a"])   # built at runtime — definitely a new object
    print("a == b:", a == b)             # True (value)
    print("a is b:", a is b)             # False (identity) — and `is` is wrong here anyway


def slicing():
    # ------------------------------------------------------------------
    # 2. SLICING — s[start:stop:step], stop EXCLUSIVE
    # ------------------------------------------------------------------
    print("\n=== 2. Slicing ===")

    s = "interview"
    #     012345678

    print("s[0:5]:  ", s[0:5])     # "inter"
    print("s[5:]:   ", s[5:])      # "view"   (to end)
    print("s[:5]:   ", s[:5])      # "inter"  (from start)
    print("s[-4:]:  ", s[-4:])     # "view"   (negative = from the end)
    print("s[::2]:  ", s[::2])     # "itrev"  (every 2nd char)
    print("s[::-1]: ", s[::-1])    # "weivretni" (reversed!)

    # Slicing never throws IndexError — it just clamps. Indexing DOES throw.
    print("s[2:999]:", s[2:999])   # safe
    # s[999]                       # IndexError

    # length of s[a:b] is (b - a), same [start, stop) convention as Java
    mid = len(s) // 2
    print("halves:", s[:mid], "/", s[mid:])


def join_vs_plus():
    # ------------------------------------------------------------------
    # 3. join vs += (Python's StringBuilder story)
    # ------------------------------------------------------------------
    print("\n=== 3. join vs += ===")

    parts = ["1", "2", "3", "4", "5"]

    # BAD in a loop — same O(n^2) copying problem as Java's +=
    # result = ""
    # for p in parts:
    #     result += p

    # GOOD: collect parts, join once — O(n)
    result = "-".join(parts)
    print("joined:", result)              # 1-2-3-4-5

    # join is a method on the SEPARATOR, taking an iterable:
    print("csv:", ",".join(["ana", "bruno", "carla"]))
    print("no sep:", "".join(parts))

    # Reversing: slicing is idiomatic; reversed() + join also works
    print("reversed:", "stressed"[::-1])                  # desserts
    print("reversed:", "".join(reversed("stressed")))     # same


def method_toolkit():
    # ------------------------------------------------------------------
    # 4. THE METHOD TOOLKIT
    # ------------------------------------------------------------------
    print("\n=== 4. Method toolkit ===")

    raw = "  Hello, World  "

    print("strip():       ", repr(raw.strip()))        # lstrip/rstrip variants exist
    print("lower():       ", raw.strip().lower())
    print("'World' in raw:", "World" in raw)           # `in` — no .contains() needed!
    print("startswith:    ", raw.strip().startswith("Hello"))
    print("find('o'):     ", raw.find("o"))            # -1 if missing (index() throws instead)
    print("rfind('o'):    ", raw.rfind("o"))
    print("replace:       ", raw.strip().replace("World", "Python"))
    print("count('l'):    ", raw.count("l"))

    # split / join
    csv = "ana,bruno,carla"
    names = csv.split(",")
    print("split:", names)
    print("join:", " | ".join(names))

    # split() with NO args splits on any whitespace run and drops empties —
    # usually what you want for sentences:
    print("split():", "a  b\t c".split())              # ['a', 'b', 'c']

    # case-insensitive compare: lower() both sides (no equalsIgnoreCase)
    print("case-insensitive:", "PYTHON".lower() == "python".lower())

    # Char classification:
    print("'a'.isalpha():", "a".isalpha())
    print("'7'.isdigit():", "7".isdigit())
    print("'a1'.isalnum():", "a1".isalnum())

    # f-strings (Day 01 callback) — the formatting idiom:
    pi = 3.14159
    print(f"formatted: pi={pi:.2f}")


def palindrome():
    # ------------------------------------------------------------------
    # 5. PALINDROME — Python one-liner AND the interview version
    # ------------------------------------------------------------------
    print("\n=== 5. Palindrome ===")

    def is_palindrome_pythonic(s: str) -> bool:
        return s == s[::-1]               # idiomatic; builds a reversed copy

    def is_palindrome_two_pointers(s: str) -> bool:
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True

    print("racecar:", is_palindrome_pythonic("racecar"),
          is_palindrome_two_pointers("racecar"))        # True True
    print("python: ", is_palindrome_pythonic("python"),
          is_palindrome_two_pointers("python"))         # False False

    # Interview note: mention the one-liner, then explain two pointers —
    # O(1) extra space, early exit. Shows you know both idiom AND fundamentals.


def interview_questions():
    print("\n=== Interview quick-fire (answer aloud!) ===")
    print("  Q: Reverse a string?               A: s[::-1] (or ''.join(reversed(s)))")
    print("  Q: s[2:5] includes index 5?        A: NO — stop is exclusive")
    print("  Q: Build a big string in a loop?   A: append to list, ''.join() at the end")
    print("  Q: find() vs index()?              A: find returns -1; index raises ValueError")
    print("  Q: split() vs split(' ')?          A: no-arg handles any whitespace run, drops empties")


if __name__ == "__main__":
    immutability()
    slicing()
    join_vs_plus()
    method_toolkit()
    palindrome()
    interview_questions()
