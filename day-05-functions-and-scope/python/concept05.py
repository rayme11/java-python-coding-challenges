"""
============================================================================
DAY 05 (Python) — Functions & Scope
============================================================================

READ ME FIRST:
    This file is a lesson. Read it top to bottom, then run it:
        python3 concept05.py
    Then RETYPE the key snippets from memory in exercise05.py.

TODAY'S BIG IDEAS:
    1. No overloading in Python — one name, one function. Defaults instead.
    2. *args / **kwargs collect extra positional / keyword arguments.
    3. Default args are evaluated ONCE at def-time — the mutable trap.
    4. Scope follows LEGB: Local, Enclosing, Global, Built-in.
    5. Lambda = one-expression anonymous function; def for everything else.
============================================================================
"""

count = 0  # module-level global for the LEGB demo


def signatures_and_defaults():
    # ------------------------------------------------------------------
    # 1. SIGNATURES, DEFAULTS, KEYWORD ARGS (Python's "overloading")
    # ------------------------------------------------------------------
    print("=== 1. Signatures & defaults ===")

    def greet(name, greeting="Hello", punct="!"):
        return f"{greeting}, {name}{punct}"

    print(greet("Ada"))                          # all defaults
    print(greet("Ada", "Hi"))                    # positional override
    print(greet("Ada", punct="?"))               # keyword override — readable!

    # Python does NOT overload by signature — the LAST def wins:
    def area(x): return x * x
    def area(x, y): return x * y
    # area(5)          # TypeError! The 1-arg version is GONE.
    print("area(3, 4):", area(3, 4), " (the 1-arg area no longer exists)")

    # Idiomatic replacement: defaults + *args
    def area2(x, y=None):
        return x * x if y is None else x * y
    print("area2(5):", area2(5), "| area2(3, 4):", area2(3, 4))

    # Keyword-only args (after the *): must be named at call site.
    def connect(host, *, timeout=30, retries=3):
        return f"{host} timeout={timeout} retries={retries}"
    print(connect("db.local", timeout=5))
    # connect("db.local", 5)      # TypeError — timeout is keyword-only


def args_kwargs():
    # ------------------------------------------------------------------
    # 2. *args AND **kwargs
    # ------------------------------------------------------------------
    print("\n=== 2. *args and **kwargs ===")

    def show(label, *args, **kwargs):
        print(f"  label={label!r} args={args} kwargs={kwargs}")

    show("point", 3, 4, color="red", size=12)
    #   args = (3, 4)         <- TUPLE of extra positionals
    #   kwargs = {'color': 'red', 'size': 12}   <- DICT of extra keywords

    # Unpacking at the CALL site (the other direction):
    def add3(a, b, c):
        return a + b + c
    nums = [1, 2, 3]
    print("add3(*nums):", add3(*nums))           # list -> positional args
    params = {"a": 10, "b": 20, "c": 30}
    print("add3(**params):", add3(**params))     # dict -> keyword args

    # Real-world use: decorators, flexible wrappers, API forwarding.
    def logged_call(func, *args, **kwargs):
        print(f"  calling {func.__name__}...")
        return func(*args, **kwargs)
    print("logged:", logged_call(add3, 1, 2, c=3))


def mutable_default_trap():
    # ------------------------------------------------------------------
    # 3. THE MUTABLE DEFAULT TRAP (Day 01 callback — now explained)
    # ------------------------------------------------------------------
    print("\n=== 3. Mutable default trap ===")

    def append_bad(item, bucket=[]):
        bucket.append(item)
        return bucket

    print("call 1:", append_bad("a"))            # ['a']
    print("call 2:", append_bad("b"))            # ['a', 'b']  <- SHARED!

    # WHY: default expressions evaluate ONCE when the def executes.
    # Every call without `bucket` reuses THE SAME list object.
    #
    # THE FIX — sentinel None pattern (memorize):
    def append_good(item, bucket=None):
        if bucket is None:
            bucket = []          # fresh list per call
        bucket.append(item)
        return bucket

    print("fixed 1:", append_good("a"))
    print("fixed 2:", append_good("b"))          # ['b'] — correct


def scope_legb():
    # ------------------------------------------------------------------
    # 4. SCOPE — LEGB lookup order
    # ------------------------------------------------------------------
    print("\n=== 4. Scope (LEGB) ===")

    x = "global"

    def outer():
        x = "enclosing"
        def inner():
            x = "local"
            return f"inner sees: {x}"
        return f"{inner()} | outer sees: {x}"

    print(outer())
    print("module sees:", x)                     # unchanged

    # Assignment CREATES a local — reading a global is fine, writing is not:
    def broken_increment():
        # count += 1        # UnboundLocalError! (implicitly local because assigned)
        pass

    def increment():
        global count           # explicit opt-in — use sparingly
        count += 1
    increment()
    print("count after global increment:", count)

    # Interview nugget: closures capture by REFERENCE (late binding):
    funcs = [lambda: i for i in range(3)]
    print("late-binding trap:", [f() for f in funcs])        # [2, 2, 2] !
    fixed = [lambda i=i: i for i in range(3)]                # bind at def-time
    print("fixed with default arg:", [f() for f in fixed])   # [0, 1, 2]


def lambdas():
    # ------------------------------------------------------------------
    # 5. LAMBDAS — one expression, no statements
    # ------------------------------------------------------------------
    print("\n=== 5. Lambdas ===")

    square = lambda x: x * x          # legal, but PEP8 prefers a def
    print("square(7):", square(7))

    # Where lambdas belong: short throwaway behavior passed to functions
    words = ["banana", "fig", "apple", "kiwi"]
    print("sorted by length:", sorted(words, key=len))
    print("sorted by last letter:", sorted(words, key=lambda w: w[-1]))

    pairs = [("a", 3), ("b", 1), ("c", 2)]
    print("sorted by value:", sorted(pairs, key=lambda p: p[1]))

    # When a lambda is WRONG:
    #   - needs statements (if/try/multiple lines)  -> def
    #   - reused in two places                      -> def
    #   - hard to understand at a glance            -> def
    # Rule of thumb: if you can't read it aloud in one breath, name it.


def interview_questions():
    print("\n=== Interview quick-fire (answer aloud!) ===")
    print("  Q: Overload methods in Python?     A: no — last def wins; use defaults/*args")
    print("  Q: Why is def f(x=[]) dangerous?   A: default evaluated once — shared forever")
    print("  Q: The fix?                        A: x=None sentinel, create inside")
    print("  Q: LEGB?                           A: Local, Enclosing, Global, Built-in lookup order")
    print("  Q: lambda: i in a loop trap?       A: late binding — all see final i; fix with i=i")


if __name__ == "__main__":
    signatures_and_defaults()
    args_kwargs()
    mutable_default_trap()
    scope_legb()
    lambdas()
    interview_questions()
