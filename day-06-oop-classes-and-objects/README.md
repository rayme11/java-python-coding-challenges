# Day 06 — OOP: Classes & Objects

**Time:** 30–60 min | **Branch:** `day-06-oop-classes-and-objects`

---

## Today's Concept

Classes and objects: constructors, `this` (Java) vs `self` (Python),
instance vs class/static state, encapsulation with private fields and
getters/setters vs Python's `_convention` and `@property`, and how
`toString()` / `__str__` / `__repr__` / `__eq__` make objects printable
and comparable. Interviews probe whether you understand *what an object
really is* in each language — including the shared-mutable-class-attribute
trap.

## Goals

By the end of today you should be able to answer, out loud, without notes:

1. What's the difference between an instance field and a `static` (Java) /
   class attribute (Python)? What breaks if you mutate a shared one?
2. What does the compiler give you if you write NO constructor in Java?
   And once you write one?
3. Why make fields private? What does Python do instead of `private`?
4. What are `this` and `self` — and where is `self` explicitly declared?
5. What prints when you `System.out.println(obj)` / `print(obj)` without
   overriding `toString()` / `__str__`?

## Plan (suggested 50 min)

| Time | Task |
|------|------|
| 15 min | Read + run `java/Concept06.java`, retype key snippets yourself |
| 10 min | Read + run `python/concept06.py`, retype key snippets |
| 25 min | Complete `java/Exercise06.java` |
| 15 min | Complete `python/exercise06.py` |
| 5 min  | Answer the 5 questions above out loud, then commit |

## Run it

```bash
cd java   && javac Concept06.java && java Concept06
javac Exercise06.java && java Exercise06
cd ../python && python3 concept06.py && python3 exercise06.py
```

## Done?

```bash
git add .
git commit -m "Day 06: OOP classes & objects (Java + Python)"
git checkout main && git merge day-06-oop-classes-and-objects
```
