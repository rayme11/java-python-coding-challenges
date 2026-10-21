# Day 01 — Variables, Types & Mutability

**Time:** 30–60 min | **Branch:** `day-01-variables-and-types`

---

## Today's Concept

How each language stores and passes data. This is the #1 "gotcha" category in
interviews: candidates lose offers over `==` vs `.equals()` vs `is`, and over
not knowing what mutability means.

## Goals

By the end of today you should be able to answer, out loud, without notes:

1. What is the difference between a primitive and a reference type in Java?
2. Why does `"a" == "a"` sometimes print `true` in Java — and why should you never rely on it?
3. In Python, what's the difference between `==` and `is`?
4. What happens to a list passed into a function in Python vs an `int`?
5. Is Java pass-by-value or pass-by-reference? (Trick question — know why.)

## Plan (suggested 45 min)

| Time | Task |
|------|------|
| 10 min | Read + run `java/Concept01.java`, retype key snippets yourself |
| 10 min | Read + run `python/concept01.py`, retype key snippets |
| 20 min | Complete `java/Exercise01.java` |
| 15 min | Complete `python/exercise01.py` |
| 5 min  | Answer the 5 questions above out loud, then commit |

## Run it

```bash
cd java   && javac Concept01.java && java Concept01
cd ../python && python3 concept01.py
```

## Done?

```bash
git add .
git commit -m "Day 01: variables, types & mutability"
git checkout main && git merge day-01-variables-and-types
```
