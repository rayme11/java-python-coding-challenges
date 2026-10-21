# Java & Python Coding Challenges — Interview Prep Program

A structured, day-by-day program to get interview-sharp in **Java** and **Python**.
Commitment: **30–60 minutes per day**, one concept per day, in both languages.

---

## How This Program Works

Each day you:

1. **Switch to the day's branch** (`day-XX-<topic>`)
2. **Read & run the concept files** — heavily commented teaching code you run first
3. **Do the exercise** — a small focused problem applying that day's concept
4. **Commit your work** on the day's branch, then merge to `main`

### Daily workflow (mimics real team workflow)

```bash
# Start of day — create today's branch (day 2 example)
git checkout main
git checkout -b day-02-control-flow

# ... study, code, run ...

# End of day — commit and merge
git add .
git commit -m "Day 02: control flow exercises"
git checkout main
git merge day-02-control-flow
```

---

## Repo Structure

```
.
├── README.md                  ← you are here
├── requirements.txt           ← Python deps (venv recommended)
├── docs/
│   └── curriculum.md          ← full day-by-day roadmap
└── day-XX-<topic>/            ← one folder per day
    ├── README.md              ← day's goals + instructions
    ├── java/
    │   ├── Concept.java       ← teaching file (read + run)
    │   └── Exercise.java      ← your task (fill in TODOs)
    └── python/
        ├── concept.py         ← teaching file (read + run)
        └── exercise.py        ← your task (fill in TODOs)
```

---

## Setup (one-time)

### Python

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### Java

No build tool needed for daily practice — plain `javac`/`java`:

```bash
# from inside a day's java/ folder
javac Concept.java && java Concept
```

### Verify everything works

```bash
python3 --version   # 3.10+
javac -version      # 17+
```

---

## Running a Day

```bash
# Java (from repo root)
cd day-01-variables-and-types/java
javac Concept01.java && java Concept01

# Python (from repo root)
python3 day-01-variables-and-types/python/concept01.py
```

---

## Rules of the Game

- **One day at a time.** Don't jump ahead — depth beats speed for interviews.
- **Type the code yourself.** Don't copy-paste the concept files; retyping builds recall.
- **Say it out loud.** Each concept file ends with "Interview questions" — answer them verbally before checking.
- **Timebox exercises.** If stuck > 20 min, look at the concept file, then retry.

## Progress Tracker

| Day | Topic | Done |
|-----|-------|------|
| 01  | Variables, Types & Mutability | ☐ |
| 02  | Control Flow & Loops | ☐ |
| 03  | Strings | ☐ |
| ... | See [docs/curriculum.md](docs/curriculum.md) | |
