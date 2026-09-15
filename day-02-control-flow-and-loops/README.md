# Day 02 — Control Flow & Loops

**Time:** 30–60 min | **Branch:** `day-02-control-flow-and-loops`

---

## Today's Concept

Loop idioms, `break`/`continue`, switch expressions, and the classic
off-by-one bugs. Interviewers watch how you *write* loops — sloppy bounds
and infinite-loop risks are instant red flags.

## Goals

By the end of today you should be able to answer, out loud, without notes:

1. When do you use `for` vs enhanced `for` vs `while` vs `do-while`?
2. What does `break` do inside nested loops — and how do labeled breaks work?
3. Why is `i <= arr.length` a bug, and what's the correct bound?
4. What's new about switch in modern Java (arrow syntax, expressions)?
5. How do you loop backwards, and when would you need to?

## Plan (suggested 45 min)

| Time | Task |
|------|------|
| 15 min | Read + run `java/Concept02.java`, retype key snippets yourself |
| 25 min | Complete `java/Exercise02.java` |
| 5 min  | Answer the 5 questions above out loud, then commit |

## Run it

```bash
cd java && javac Concept02.java && java Concept02
javac Exercise02.java && java Exercise02
```

## Done?

```bash
git checkout -b day-02-control-flow-and-loops
git add .
git commit -m "Day 02: control flow & loops (Java)"
git checkout main && git merge day-02-control-flow-and-loops
```
