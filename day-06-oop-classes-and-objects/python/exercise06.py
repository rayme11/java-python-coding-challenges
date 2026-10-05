"""
============================================================================
DAY 06 EXERCISE (Python) — Library Book Tracker
============================================================================
Apply today's concepts: classes, __init__, self, class vs instance
attributes, @property, __str__/__repr__/__eq__.
Fill in every TODO, then run:  python3 exercise06.py
Target time: 15 minutes.
============================================================================
"""


def main():

    # ------------------------------------------------------------------
    # TASK 1: Write a Book class with __init__(self, title, author,
    # page_count). Store all three as instance attributes.
    # Create b1 = Book("Clean Code", "Robert Martin", 464) and print
    # b1.title.
    # ------------------------------------------------------------------
    # TODO 1


    # ------------------------------------------------------------------
    # TASK 2: Give page_count a default of 0 (keyword default — Day 05!).
    # Create Book("Mystery Draft", "Me") and print its page_count.
    # Comment: how does Python avoid needing constructor chaining like
    # Java's this(...)?
    # ------------------------------------------------------------------
    # TODO 2


    # ------------------------------------------------------------------
    # TASK 3: Track collection size with a CLASS attribute total_books = 0,
    # incremented in __init__. Create 3 books and print Book.total_books.
    # Then add a books_read = [] at class level, append in a read() method,
    # create two Books, read from one, and print the OTHER's books_read.
    # Comment: what went wrong, and how do you fix it?
    # ------------------------------------------------------------------
    # TODO 3


    # ------------------------------------------------------------------
    # TASK 4: Encapsulate progress. Store _current_page = 0 internally and
    # expose it ONLY through:
    #   read(self, pages)      — advances, never past page_count
    #   @property current_page — read-only
    #   progress_pct(self)     — 100.0 * current / page_count (guard 0!)
    # Test: read(100), read(10000) on the 464-page book; print
    # current_page and progress_pct(). Try b1.current_page = 999 and
    # comment what happens (and why _current_page = 999 would "work").
    # ------------------------------------------------------------------
    # TODO 4


    # ------------------------------------------------------------------
    # TASK 5: Add __repr__ returning Book('Clean Code', 'Robert Martin', 464)
    # style, and __str__ returning "Clean Code by Robert Martin (464 pages)".
    # Print b1 and print [b1]. Comment which dunder each one used.
    # ------------------------------------------------------------------
    # TODO 5


    # ------------------------------------------------------------------
    # TASK 6: Add __eq__ so Books are equal when title and author match.
    # Test: Book("Dune", "Herbert", 412) == Book("Dune", "Herbert", 896)
    # -> True. Also print `is` between them and explain the difference.
    # Comment: what happens if you try {b1, b2} (a set) after defining
    # __eq__ but not __hash__?
    # ------------------------------------------------------------------
    # TODO 6


    # ------------------------------------------------------------------
    # BONUS: Build a Library class holding a list of Books. Add
    # add_book(), and find_by_author(author) using a list comprehension.
    # Then implement __len__ so len(library) works. (Dunder preview!)
    # ------------------------------------------------------------------


if __name__ == "__main__":
    main()

# SELF-CHECK (answer out loud):
# 1. What is self, and who passes it?
# 2. Why did class-level books_read = [] misbehave in Task 3?
# 3. After defining __eq__, why does hash(book) break?
