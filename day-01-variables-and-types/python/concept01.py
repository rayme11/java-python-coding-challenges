"""
============================================================================
DAY 01 (Python) — Variables, Types & Mutability
============================================================================

READ ME FIRST:
    This file is a lesson. Read it top to bottom, then run it:
        python3 concept01.py
    Then RETYPE the key snippets from memory in exercise01.py.

TODAY'S BIG IDEAS:
    1. Python is DYNAMICALLY TYPED — names have no type; OBJECTS have types.
    2. Assignment never copies — it binds a NAME to an OBJECT.
    3. Mutability decides what happens when you "change" something:
         immutable: int, float, str, tuple, bool, frozenset
         mutable:   list, dict, set
    4. `==` compares VALUES; `is` compares IDENTITY (same object in memory).
============================================================================
"""


def names_are_labels():
    # ------------------------------------------------------------------
    # 1. NAMES ARE LABELS, NOT BOXES
    # ------------------------------------------------------------------
    # In Java you declare `int a = 5;` — a typed box.
    # In Python `a = 5` just sticks the label 'a' on the object 5.
    # The same label can be re-stuck to ANY type (dynamic typing).
    print("=== 1. Names are labels ===")

    a = 5
    print("a =", a, "| type:", type(a).__name__)     # int
    a = "five"                                        # same name, new object/type
    print("a =", a, "| type:", type(a).__name__)     # str

    # Two names, ONE object:
    list1 = [1, 2, 3]
    list2 = list1          # NO copy — both labels point at the same list
    list2.append(99)
    print("list1 after list2.append(99):", list1)     # [1, 2, 3, 99]  (!)

    # To actually copy:
    list3 = list1.copy()   # or list(list1) or list1[:]
    list3.append(100)
    print("list1 after list3.append(100):", list1)    # unchanged


def mutability():
    # ------------------------------------------------------------------
    # 2. MUTABLE vs IMMUTABLE
    # ------------------------------------------------------------------
    print("\n=== 2. Mutability ===")

    # Immutable: operations create NEW objects
    s = "hello"
    print("id before:", id(s))
    s = s.upper()          # NEW string object; the old one is untouched
    print("id after: ", id(s), "| s =", s)

    # Mutable: changed IN PLACE — same object, same id
    nums = [1, 2, 3]
    print("id before:", id(nums))
    nums.append(4)
    print("id after: ", id(nums), "| nums =", nums)   # same id!

    # TUPLE = immutable list. Common interview follow-up:
    #   "Why use a tuple?" -> hashable (dict keys), safe from mutation,
    #   signals intent, slightly faster/lighter.
    point = (3, 4)
    # point[0] = 9         # TypeError: 'tuple' object does not support item assignment
    print("tuple:", point)

    # TRAP: a tuple holding a mutable object...
    tricky = ([1, 2], 3)
    tricky[0].append(99)   # legal! tuple is fixed, but the LIST inside isn't
    print("tricky tuple:", tricky)                     # ([1, 2, 99], 3)


def equality_is_vs_eqeq():
    # ------------------------------------------------------------------
    # 3. == vs is
    # ------------------------------------------------------------------
    # ==  -> do the VALUES match?
    # is  -> are these the SAME OBJECT? (compares id())
    print("\n=== 3. == vs is ===")

    x = [1, 2, 3]
    y = [1, 2, 3]          # equal content, different objects
    z = x                  # same object

    print("x == y:", x == y)    # True
    print("x is y:", x is y)    # False  <- content equal, identity differs
    print("x is z:", x is z)    # True

    # Gotcha: CPython interns small ints & some strings, so `is` may
    # "accidentally work" — NEVER rely on it.
    a = 256; b = 256
    c = 257; d = 257
    print("256 is 256:", a is b)   # True  (cached — implementation detail!)
    print("257 is 257:", c is d)   # often False outside scripts — don't rely!

    # The ONE correct use of `is`: comparing with None
    value = None
    print("value is None:", value is None)   # idiomatic
    # value == None  # works but un-Pythonic; linters will flag it


def functions_and_mutation():
    # ------------------------------------------------------------------
    # 4. FUNCTION ARGUMENTS — "pass by object reference"
    # ------------------------------------------------------------------
    # Python passes the OBJECT REFERENCE by value (like Java):
    #   - mutable object -> callee's changes are visible to caller
    #   - rebinding the parameter -> caller unaffected
    print("\n=== 4. Functions & mutation ===")

    def try_to_rebind(n):
        n = 999            # rebinds local name only

    def mutate(lst):
        lst.append(99)     # mutates the shared object

    def rebind_list(lst):
        lst = [7, 7, 7]    # caller's list unaffected

    num = 5
    try_to_rebind(num)
    print("num after rebind attempt:", num)        # 5

    data = [1, 2, 3]
    mutate(data)
    print("data after mutate:", data)              # [1, 2, 3, 99]

    rebind_list(data)
    print("data after rebind:", data)              # still [1, 2, 3, 99]

    # CLASSIC TRAP: mutable default argument (asked constantly)
    def bad_append(item, bucket=[]):   # the list is created ONCE at def time
        bucket.append(item)
        return bucket

    print("bad_append(1):", bad_append(1))   # [1]
    print("bad_append(2):", bad_append(2))   # [1, 2]  <- shared state! (!!)

    def good_append(item, bucket=None):      # correct pattern
        if bucket is None:
            bucket = []
        bucket.append(item)
        return bucket

    print("good_append(1):", good_append(1)) # [1]
    print("good_append(2):", good_append(2)) # [2]


def interview_questions():
    print("\n=== Say these answers out loud ===")
    print("Q1: What's the difference between == and is?")
    print("Q2: list2 = list1; list2.append(x) — why did list1 change?")
    print("Q3: Name 3 immutable and 3 mutable built-in types.")
    print("Q4: Why is def f(x, items=[]) dangerous? What's the fix?")
    print("Q5: When is `is` the correct operator to use?")


if __name__ == "__main__":
    # This guard means: only run when executed directly,
    # not when imported as a module. You'll see this in every real codebase.
    names_are_labels()
    mutability()
    equality_is_vs_eqeq()
    functions_and_mutation()
    interview_questions()
