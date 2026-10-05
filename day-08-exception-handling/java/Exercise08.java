/**
 * ============================================================================
 * DAY 08 (Java) — Exception Handling: EXERCISES
 * ============================================================================
 *
 * GOAL:
 *   Retype the key snippets from memory from Concept08.java.
 *   Focus on understanding, not just copying.
 *
 * EXERCISES:
 *   1. Write a method that attempts to perform an integer division by zero.
 *      Use `try-catch` to handle the `ArithmeticException`.
 *   2. Write a method that tries to access an array element out of bounds
 *      and convert a non-numeric string to an integer. Use multiple `catch`
 *      blocks to handle `ArrayIndexOutOfBoundsException` and `NumberFormatException`.
 *   3. Create a method `processInput(String input)` that uses the `throw` keyword
 *      to manually throw an `IllegalArgumentException` if the input string is empty or null.
 *      Call this method from `main` and catch the exception.
 *   4. Create a method `readFile(String filePath)` that declares it `throws IOException`.
 *      (You don't need to actually implement file reading, just declare `throws`)
 *      Call this method from `main` and handle the `IOException`.
 *   5. Define a custom exception `InvalidAgeException` that extends `Exception`.
 *      Create a method `setAge(int age)` that throws `InvalidAgeException` if the age is negative or over 120.
 *      Demonstrate catching your custom exception in `main`.
 *
 * HINT: Refer back to Concept08.java if you get stuck, but try to
 *       solve these from memory first!
 * ============================================================================
 */

import java.io.IOException;

public class Exercise08 {

    public static void main(String[] args) {
        System.out.println("=== Day 08 Exercises: Exception Handling ===");

        // Exercise 1: Basic try-catch for ArithmeticException
        // Your code here
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


        // Exercise 2: Multiple catch blocks
        // Your code here


        // Exercise 3: `throw` keyword
        // Your code here


        // Exercise 4: `throws` keyword
        // Your code here


        // Exercise 5: Custom Exception
        // Your code here
    }

    // Method for Exercise 4 (throws IOException)
    // public static void readFile(String filePath) throws IOException {
    //     // Simulation: In a real scenario, this would attempt to read a file.
    //     // For now, just focus on the `throws` declaration.
    //     System.out.println("Attempting to read file: " + filePath);
    //     // throw new IOException("Simulated file read error");
    // }

    // Custom exception class for Exercise 5
    // static class InvalidAgeException extends Exception {
    //     public InvalidAgeException(String message) {
    //         super(message);
    //     }
    // }

    // Method for Exercise 5 (throws InvalidAgeException)
    // public static void setAge(int age) throws InvalidAgeException {
    //     // Your code here
    // }
}
