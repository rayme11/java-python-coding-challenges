# Day 03 — Strings & String Manipulation

**Time:** 30–60 min | **Branch:** `day-03-strings`

---

## Today's Concept

Strings are the most common interview data type. Today: immutability,
`StringBuilder` vs `+` concatenation, slicing, and the method toolkit
you'll reach for in almost every string problem.

## Goals

By the end of today you should be able to answer, out loud, without notes:

1. Why is `s += c` inside a loop a performance trap in Java — and what do you use instead?
2. What does `str.substring(a, b)` return — is `b` inclusive or exclusive?
3. In Python, what does `s[::-1]` do and why does it work?
4. How do you check if a string is a palindrome in one pass (two pointers)?
5. `charAt()` / indexing vs iterating over `toCharArray()` — what's the difference?

## Plan (suggested 45 min)

| Time | Task |
|------|------|
| 15 min | Read + run `java/Concept03.java`, retype key snippets yourself |
| 10 min | Read + run `python/concept03.py`, retype key snippets |
| 25 min | Complete `java/Exercise03.java` |
| 15 min | Complete `python/exercise03.py` |
| 5 min  | Answer the 5 questions above out loud, then commit |

## Run it

```bash
cd java   && javac Concept03.java && java Concept03
javac Exercise03.java && java Exercise03
cd ../python && python3 concept03.py && python3 exercise03.py
```

## Done?

```bash
git checkout -b day-03-strings
git add .
git commit -m "Day 03: strings & string manipulation"
git checkout main && git merge day-03-strings
```
