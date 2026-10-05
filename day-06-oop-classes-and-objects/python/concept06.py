"""
============================================================================
DAY 06 (Python) — OOP: Classes & Objects
============================================================================

READ ME FIRST:
    This file is a lesson. Read it top to bottom, then run it:
        python3 concept06.py
    Then RETYPE the key snippets from memory in exercise06.py.

TODAY'S BIG IDEAS:
    1. class = blueprint; calling it (Dog("Rex")) builds an instance.
    2. __init__ initializes; `self` is the explicit "this" — first param
       of every instance method, passed automatically at call time.
    3. Class attributes are SHARED by all instances — mutable ones are a
       classic trap (Day 01/05 callback!).
    4. No true private: `_name` is a convention, `__name` gets mangled.
       @property gives getter/setter control with attribute syntax.
    5. __str__ for humans, __repr__ for devs, __eq__ for ==.
============================================================================
"""


def classes_and_self():
    # ------------------------------------------------------------------
    # 1. CLASSES, __init__, AND self
    # ------------------------------------------------------------------
    print("=== 1. Classes & self ===")

    class Dog:
        def __init__(self, name, age):   # constructor — runs at Dog(...)
            self.name = name             # instance attributes live on self
            self.age = age

        def bark(self):                  # self is explicit in Python!
            return f"{self.name} says woof"

    rex = Dog("Rex", 3)
    fido = Dog("Fido", 5)
    print(" ", rex.bark(), "|", fido.bark())

    # rex.bark() is sugar for Dog.bark(rex) — that's WHERE self comes from.
    print("  Dog.bark(rex):", Dog.bark(rex))

    print("  rex is fido:", rex is fido)          # False — two objects
    alias = rex
    alias.age = 4
    print("  rex.age after alias.age = 4 ->", rex.age)  # one shared object


def class_vs_instance_attributes():
    # ------------------------------------------------------------------
    # 2. CLASS vs INSTANCE ATTRIBUTES — the shared-mutable trap
    # ------------------------------------------------------------------
    print("\n=== 2. Class vs instance attributes ===")

    class Counter:
        total = 0                     # CLASS attribute: one shared copy

        def __init__(self):
            self.count = 0            # instance attribute: one per object

        def increment(self):
            self.count += 1
            Counter.total += 1        # reach the class attr via the class

    c1, c2 = Counter(), Counter()
    c1.increment(); c1.increment(); c2.increment()
    print("  c1.count:", c1.count, "| c2.count:", c2.count)   # 2, 1
    print("  Counter.total:", Counter.total)                  # 3

    # THE TRAP — a mutable class attribute is shared by every instance:
    class BadTeam:
        members = []                  # ONE list shared by ALL teams!

        def add(self, name):
            self.members.append(name)

    red, blue = BadTeam(), BadTeam()
    red.add("Ada")
    print("  blue.members:", blue.members)     # ['Ada'] — surprise!

    # THE FIX — initialize per-instance in __init__:
    class GoodTeam:
        def __init__(self):
            self.members = []         # fresh list per instance

        def add(self, name):
            self.members.append(name)

    red2, blue2 = GoodTeam(), GoodTeam()
    red2.add("Ada")
    print("  blue2.members (fixed):", blue2.members)           # []

    # Gotcha: `self.total += 1` on a class attr would CREATE an instance
    # attr shadowing the class one (int is immutable). Use ClassName.attr.


def encapsulation_python_style():
    # ------------------------------------------------------------------
    # 3. ENCAPSULATION — conventions, name mangling, @property
    # ------------------------------------------------------------------
    print("\n=== 3. Encapsulation, Python style ===")

    class BankAccount:
        def __init__(self, owner, opening_balance=0.0):
            if opening_balance < 0:
                raise ValueError("opening balance must be >= 0")
            self.owner = owner             # public: fair game
            self._balance = opening_balance  # _ = "internal, don't touch"

        def deposit(self, amount):
            if amount > 0:
                self._balance += amount

        def withdraw(self, amount):
            if 0 < amount <= self._balance:
                self._balance -= amount
                return True
            return False

        @property                          # reads like an attribute...
        def balance(self):                 # ...runs like a method
            return self._balance

    acct = BankAccount("Ada", 100)
    acct.deposit(50)
    print("  withdraw(30):", acct.withdraw(30))       # True
    print("  balance:", acct.balance)                  # 120.0 — no ()!
    print("  withdraw(1000):", acct.withdraw(1000))    # False

    # acct.balance = -500       # AttributeError — property has no setter
    acct._balance = -500         # ...but this WORKS. Convention, not walls.
    print("  after rude write:", acct.balance)         # -500 — Python trusts you

    class Demo:
        def __init__(self):
            self.__secret = 42       # name-mangled to _Demo__secret

    d = Demo()
    # d.__secret                   # AttributeError
    print("  mangled access:", d._Demo__secret)        # 42 — still reachable!


def str_repr_eq():
    # ------------------------------------------------------------------
    # 4. __str__, __repr__, __eq__
    # ------------------------------------------------------------------
    print("\n=== 4. __str__, __repr__, __eq__ ===")

    class Point:
        def __init__(self, x, y):
            self.x, self.y = x, y

        def __repr__(self):          # dev-facing: unambiguous, ideally eval-able
            return f"Point({self.x}, {self.y})"

        def __str__(self):           # human-facing: pretty
            return f"({self.x}, {self.y})"

        def __eq__(self, other):     # what == means for Point
            if not isinstance(other, Point):
                return NotImplemented
            return (self.x, self.y) == (other.x, other.y)

    p, p2 = Point(3, 4), Point(3, 4)
    print("  str(p):", str(p))                 # (3, 4)
    print("  repr(p):", repr(p))               # Point(3, 4)
    print("  [p] in a list shows:", [p])       # lists use repr!
    print("  p == p2:", p == p2)               # True  (content)
    print("  p is p2:", p is p2)               # False (identity)

    class Bare:
        pass
    print("  default repr:", Bare())           # <__main__.Bare object at 0x...>
    # Rule: ALWAYS write __repr__; __str__ is optional (falls back to repr).
    # Gotcha: defining __eq__ sets __hash__ to None -> unhashable until
    # you also define __hash__ (matters for dict keys / sets — Day 07!).


def interview_questions():
    # ------------------------------------------------------------------
    # 5. QUICK-FIRE (answer out loud)
    # ------------------------------------------------------------------
    print("\n=== 5. Quick-fire (answer out loud) ===")
    print("  Q1: Where does `self` come from when you call obj.method()?")
    print("  Q2: Why is `members = []` at class level a bug? Where should it go?")
    print("  Q3: Is anything truly private in Python? What does __ do?")
    print("  Q4: print(obj) vs print([obj]) — which dunder runs in each?")
    print("  Q5: What's the difference between == and is?")


if __name__ == "__main__":
    classes_and_self()
    class_vs_instance_attributes()
    encapsulation_python_style()
    str_repr_eq()
    interview_questions()
