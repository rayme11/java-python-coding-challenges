/**
 * ============================================================================
 * DAY 09 (Java) — Collections & Data Structures: EXERCISES
 * ============================================================================
 *
 * GOAL:
 *   Retype the key snippets from memory from Concept09.java.
 *   Focus on understanding, not just copying.
 *
 * EXERCISES:
 *   1. Create an `ArrayList` of `String`s, add a few names, print its size,
 *      and iterate through it using a for-each loop.
 *   2. Create a `HashSet` of `Integer`s, add some duplicate numbers, and observe
 *      that duplicates are not stored. Check if a specific number is present.
 *   3. Create a `HashMap` where keys are `String` (student names) and values are `Integer` (scores).
 *      Add a few student scores, update one, and print all keys and values.
 *   4. Demonstrate using a `LinkedList` to add and remove elements from both ends.
 *   5. Use an `Iterator` to safely remove elements from an `ArrayList` while iterating.
 *   6. Briefly explain the difference between `ArrayList` and `LinkedList` in terms of performance.
 *   7. Briefly explain the difference between `HashSet` and `TreeSet`.
 *
 * HINT: Refer back to Concept09.java if you get stuck, but try to
 *       solve these from memory first!
 * ============================================================================
 */

import java.util.ArrayList;
import java.util.HashSet;
import java.util.HashMap;
import java.util.LinkedList;
import java.util.List;
import java.util.Set;
import java.util.Map;
import java.util.Iterator;

public class Exercise09 {

    public static void main(String[] args) {
        System.out.println("=== Day 09 Exercises: Collections & Data Structures ===");

        // Exercise 1: ArrayList basics
        // Your code here


        // Exercise 2: HashSet basics
        // Your code here


        // Exercise 3: HashMap basics
        // Your code here


        // Exercise 4: LinkedList for efficient adding/removing from ends
        // Your code here


        // Exercise 5: Iterator for safe removal
        // Your code here


        // Exercise 6: ArrayList vs LinkedList performance explanation
        System.out.println("\n--- Exercise 6: ArrayList vs LinkedList ---");
        System.out.println("ArrayList: Good for random access (get by index), slower for insertions/deletions in middle.");
        System.out.println("LinkedList: Good for frequent insertions/deletions at any position, slower for random access.");

        // Exercise 7: HashSet vs TreeSet explanation
        System.out.println("\n--- Exercise 7: HashSet vs TreeSet ---");
        System.out.println("HashSet: Faster performance, unordered elements. Uses hashing for storage.");
        System.out.println("TreeSet: Slower performance, stores elements in sorted order. Uses a balanced tree structure.");
    }
}
