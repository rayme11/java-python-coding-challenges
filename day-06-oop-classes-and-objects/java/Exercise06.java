/**
 * ============================================================================
 * DAY 06 EXERCISE (Java) — Library Book Tracker
 * ============================================================================
 * Apply today's concepts: classes, constructors, this, static vs instance,
 * encapsulation, toString()/equals().
 * Fill in every TODO, then run:  javac Exercise06.java && java Exercise06
 * Target time: 25 minutes.
 *
 * NOTE: write the Book class at the BOTTOM of this file, below Exercise06
 * (like Dog/Point/BankAccount in Concept06.java).
 * ============================================================================
 */
public class Exercise06 {

    public static void main(String[] args) {

        // ---------------------------------------------------------------
        // TASK 1: Create a Book class with private fields:
        //   title (String), author (String), pageCount (int)
        // Write a full constructor using `this` for all three.
        // Then uncomment and run:
        // ---------------------------------------------------------------
        // Book b1 = new Book("Clean Code", "Robert Martin", 464);
        // System.out.println("Created: " + b1.getTitle());
        // TODO 1


        // ---------------------------------------------------------------
        // TASK 2: Add a chained no-arg constructor Book() that calls
        // this("Untitled", "Unknown", 0). Create one and print its author.
        // Comment: what rule must this(...) follow inside a constructor?
        // ---------------------------------------------------------------
        // TODO 2


        // ---------------------------------------------------------------
        // TASK 3: Track the collection size. Add a static int totalBooks
        // that increments in the constructor, plus a static method
        // getTotalBooks(). Create 3 books, print Book.getTotalBooks().
        // Comment: why is totalBooks static but title is not?
        // ---------------------------------------------------------------
        // TODO 3


        // ---------------------------------------------------------------
        // TASK 4: Encapsulate reading progress. Add a private field
        // currentPage (starts at 0) and:
        //   public void read(int pages)  — advances currentPage, but never
        //                                  past pageCount
        //   public double progressPct()  — 100.0 * currentPage / pageCount
        //                                  (guard pageCount == 0!)
        //   public int getCurrentPage()  — getter only, NO setter
        // Test: read(100) then read(10000) on a 464-page book; print
        // currentPage and progressPct. Comment why no setter exists.
        // ---------------------------------------------------------------
        // TODO 4


        // ---------------------------------------------------------------
        // TASK 5: Override toString() to return:
        //   "Clean Code by Robert Martin (464 pages)"
        // Print a book directly: System.out.println(b1);
        // Then comment: what would print WITHOUT the override?
        // ---------------------------------------------------------------
        // TODO 5


        // ---------------------------------------------------------------
        // TASK 6: Override equals() so two Books are equal when title and
        // author match (ignore pageCount). Then test:
        //   new Book("Dune", "Herbert", 412).equals(new Book("Dune", "Herbert", 896))
        // should be true, and == should be false. Print both and explain
        // the difference in a comment.
        // ---------------------------------------------------------------
        // TODO 6


        // ---------------------------------------------------------------
        // BONUS: Scope + OOP combo (Day 05 callback). In a loop, create a
        // Book each iteration and store it in a variable declared INSIDE
        // the loop. After the loop, try to print it. What happens and why?
        // ---------------------------------------------------------------
    }

    // SELF-CHECK (answer out loud):
    // 1. If you delete ALL constructors from Book, what still compiles?
    // 2. Why can't a static method like getTotalBooks() read currentPage?
    // 3. main is static — so why can it call `new Book(...)` and b1.read(10)?
}


// TODO: write your Book class here (not public — one public class per file)
