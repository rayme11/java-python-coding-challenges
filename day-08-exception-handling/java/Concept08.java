/**
 * ============================================================================
 * DAY 08 (Java) — Exception Handling
 * ============================================================================
 *
 * READ ME FIRST:
 *   This file is a lesson. Read it top to bottom, then run it:
 *       javac Concept08.java && java Concept08
 *   Then RETYPE the key snippets from memory in Exercise08.java.
 *
 * TODAY'S BIG IDEAS:
 *   1. Understanding Exceptions: Errors vs. Exceptions, Checked vs. Unchecked.
 *   2. `try-catch-finally`: Basic structure for handling exceptions.
 *   3. Multiple `catch` Blocks: Handling different types of exceptions.
 *   4. `throw` Keyword: Manually throwing exceptions.
 *   5. `throws` Keyword: Declaring exceptions a method might throw.
 *   6. Custom Exceptions: Creating your own exception types.
 * ============================================================================
 */

public class Concept08 {

    public static void main(String[] args) {
        System.out.println("=== DAY 08: Exception Handling ===");

        // 1. Understanding Exceptions
        // Discuss Errors vs. Exceptions, Checked vs. Unchecked.

        // 2. try-catch-finally
        basicTryCatchFinally();

        // 3. Multiple catch Blocks
        multipleCatchBlocks();

        // 4. throw Keyword
        // Custom methods will demonstrate this.

        // 5. throws Keyword
        // Custom methods will demonstrate this.

        // 6. Custom Exceptions
        // Custom classes and methods will demonstrate this.

        System.out.println("\nEnd of Day 08 Concepts.");
    }

    static void basicTryCatchFinally() {
        System.out.println("\n--- 2. Basic try-catch-finally ---");
        try {
            int result = 10 / 0; // This will cause an ArithmeticException
            System.out.println("Result: " + result);
        } catch (ArithmeticException e) {
            System.out.println("Caught an ArithmeticException: " + e.getMessage());
        } finally {
            System.out.println("Finally block executed. This always runs.");
        }

        System.out.println("Continuing after try-catch-finally.");
    }

    static void multipleCatchBlocks() {
        System.out.println("\n--- 3. Multiple catch Blocks ---");
        try {
            String[] arr = {"one", "two"};
            System.out.println(arr[2]); // ArrayIndexOutOfBoundsException
            Integer.parseInt("abc"); // NumberFormatException
        } catch (ArrayIndexOutOfBoundsException e) {
            System.out.println("Caught an ArrayIndexOutOfBoundsException: " + e.getMessage());
        } catch (NumberFormatException e) {
            System.out.println("Caught a NumberFormatException: " + e.getMessage());
        } catch (Exception e) { // Generic catch block (should be last)
            System.out.println("Caught a generic Exception: " + e.getMessage());
        } finally {
            System.out.println("Multiple catch blocks: Finally executed.");
        }
    }
}
