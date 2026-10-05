"""
============================================================================
DAY 05 EXERCISE (Python) — Text Formatter Toolkit
============================================================================
Apply today's concepts: defaults, *args/**kwargs, scope, lambdas.
Fill in every TODO, then run:  python3 exercise05.py
Target time: 15–20 minutes.
============================================================================
"""


def main():
    # ------------------------------------------------------------------
    # TASK 1: Write shout(text, punct="!") returning text uppercased with
    # punct appended. shout("hello") -> "HELLO!"
    # Print: shout("functions are fun") and shout("wait", punct="?")
    # Comment: which call used a keyword argument and why is that clearer?
    # ------------------------------------------------------------------
    # TODO 1


    # ------------------------------------------------------------------
    # TASK 2: Write join_all(separator, *parts) using *args:
    #   join_all("-", "a", "b", "c") -> "a-b-c"
    #   join_all("-") -> ""   (empty *args must not crash)
    # Comment: what TYPE is `parts` inside the function?
    # ------------------------------------------------------------------
    # TODO 2


    # ------------------------------------------------------------------
    # TASK 3: Write make_tag(name, **attrs) that builds an HTML-ish tag:
    #   make_tag("div", id="main", class_="box") -> '<div id="main" class_="box">'
    # Hint: iterate kwargs.items(). Print one example.
    # Comment: what type is `attrs`?
    # ------------------------------------------------------------------
    # TODO 3


    # ------------------------------------------------------------------
    # TASK 4: Fix the bug in track_calls below — it's supposed to count
    # how many times it has been called and return the running total.
    # Predict what it currently does, then fix it WITHOUT using a mutable
    # default argument. (Two valid fixes: `global`, or a default-arg trick
    # used deliberately — implement the global version, mention the other
    # in a comment.)
    # ------------------------------------------------------------------
    def track_calls():
        total = 0
        total += 1
        return total
    # print(track_calls(), track_calls(), track_calls())  # expect 1 2 3
    # TODO 4


    # ------------------------------------------------------------------
    # TASK 5: Given `words`, produce three sorted versions with lambdas:
    #   a) by length, shortest first
    #   b) by last letter alphabetically
    #   c) by length, LONGEST first (hint: reverse=True or a key trick)
    # ------------------------------------------------------------------
    words = ["banana", "fig", "apple", "kiwi", "cherry"]
    # TODO 5


    # ------------------------------------------------------------------
    # TASK 6: The late-binding trap, applied. Fix make_multipliers so
    # [m(10) for m in make_multipliers()] returns [0, 10, 20, 30]
    # instead of [30, 30, 30, 30]. Explain the fix in one comment.
    # ------------------------------------------------------------------
    def make_multipliers():
        return [lambda: i * 10 for i in range(4)]
    # TODO 6


    # ------------------------------------------------------------------
    # STRETCH (optional): Write apply_to_each(items, func) that returns a
    # new list with func applied to each item (yes, that's map() — write
    # it yourself with a loop). Then call it with:
    #   a) a lambda reversing each word
    #   b) the built-in str.upper as the function
    # Comment: functions are objects in Python — what does that let you do?
    # ------------------------------------------------------------------
    # TODO STRETCH


# Write your helper functions below:


if __name__ == "__main__":
    main()
