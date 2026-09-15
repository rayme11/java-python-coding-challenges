"""
============================================================================
DAY 03 EXERCISE (Python) — Word Analyzer
============================================================================
Apply today's concepts: immutability, slicing, join, toolkit methods.
Fill in every TODO, then run:  python3 exercise03.py
Target time: 15–20 minutes.
============================================================================
"""


def main():
    sentence = "The quick brown fox jumps over the lazy dog"

    # ------------------------------------------------------------------
    # TASK 1: Print the length of `sentence`, its first char, and its
    # last char using len() and NEGATIVE indexing (the Pythonic way).
    # ------------------------------------------------------------------
    # TODO 1


    # ------------------------------------------------------------------
    # TASK 2: Extract and print the word "brown" using slicing with
    # explicit indices. Then do it again WITHOUT hardcoding indices —
    # use find("brown") and find(" ", start).
    # Question in a comment: what does find() return if not found,
    # and how does that differ from index()?
    # ------------------------------------------------------------------
    # TODO 2


    # ------------------------------------------------------------------
    # TASK 3: Split the sentence into words and print each on its own
    # line with its index: "0: The"  — use enumerate().
    # ------------------------------------------------------------------
    # TODO 3


    # ------------------------------------------------------------------
    # TASK 4: Write count_vowels(s) returning the number of vowels
    # (case-insensitive). Two versions:
    #   a) a loop
    #   b) a one-liner: sum(c in "aeiou" for c in s.lower())
    # Print both results for `sentence` — they must match.
    # ------------------------------------------------------------------
    # TODO 4


    # ------------------------------------------------------------------
    # TASK 5: Write reverse_words(s) that reverses the ORDER of words
    # but keeps each word intact: "The quick" -> "quick The".
    # Hint: split, reverse the list ([::-1]), then " ".join(...).
    # Print reverse_words(sentence).
    # ------------------------------------------------------------------
    # TODO 5


    # ------------------------------------------------------------------
    # TASK 6: Write is_palindrome(s) two ways:
    #   a) the Pythonic one-liner (ignore case)
    #   b) the two-pointer version (ignore case)
    # Test both with "Racecar" (True) and "hello" (False).
    # ------------------------------------------------------------------
    # TODO 6


    # ------------------------------------------------------------------
    # STRETCH (optional): Write is_palindrome_clean(s) that ignores
    # non-alphanumeric characters. Test with
    # "A man, a plan, a canal: Panama" — should be True.
    # Hint: build a filtered string first (str.isalnum), or skip with
    # two pointers. Which uses less extra space?
    # ------------------------------------------------------------------
    # TODO STRETCH


# Write your helper functions below:


if __name__ == "__main__":
    main()
