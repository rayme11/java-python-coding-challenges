# Day 05 — Functions & Scope

**Time:** 30–60 min | **Branch:** `day-05-functions-and-scope`

---

## Today's Concept

Function signatures, default arguments, variable arguments, method
overloading (Java) vs default/keyword args (Python), scope rules, and a
first look at lambdas. Interviews probe whether you understand *what a
function really is* in each language — including the traps.

## Goals

By the end of today you should be able to answer, out loud, without notes:

1. How does Java "overload" methods — and why can't Python do that?
2. What is the mutable-default-argument trap in Python? (Day 01 callback!)
3. What are `*args` and `**kwargs`, and when would you use them?
4. What's the difference between a lambda and a named function — when is a lambda wrong?
5. In Java, what's the scope of a variable declared inside a loop body?

## Plan (suggested 45 min)

| Time | Task |
|------|------|
| 15 min | Read + run `java/Concept05.java`, retype key snippets yourself |
| 10 min | Read + run `python/concept05.py`, retype key snippets |
| 25 min | Complete `java/Exercise05.java` |
| 15 min | Complete `python/exercise05.py` |
| 5 min  | Answer the 5 questions above out loud, then commit |

## Run it

```bash
cd java   && javac Concept05.java && java Concept05
javac Exercise05.java && java Exercise05
cd ../python && python3 concept05.py && python3 exercise05.py
```

## Done?

```bash
git add .
git commit -m "Day 05: functions & scope (Java + Python)"
git checkout main && git merge day-05-functions-and-scope
```
