import java.util.ArrayDeque;
import java.util.Deque;
import java.util.HashMap;
import java.util.Map;

public class Exercise10 {

    /**
     * Exercise: Balanced Parentheses Checker
     *
     * Implement a method that checks if a given string of parentheses (and other characters)
     * is balanced. You should only consider '(', ')', '{', '}', '[', ']'.
     * Ignore other characters.
     *
     * A string is balanced if:
     * 1. Open brackets must be closed by the same type of brackets.
     * 2. Open brackets must be closed in the correct order.
     *
     * Example:
     * - "()[]{}" -> true
     * - "([{}])" -> true
     * - "{()}" -> true
     * - "[(])" -> false
     * - "{[]" -> false
     * - "{([])}" -> true
     * - "((()))" -> true
     * - "(()" -> false
     * - "((())))))" -> false
     * - "(" -> false
     * - ")" -> false
     *
     * Hint: Use a Stack (Deque in Java) to keep track of open brackets.
     */
    public static boolean isBalanced(String s) {
        // 1. Initialize a Deque (acting as a Stack) to store opening brackets.
        Deque<Character> stack = new ArrayDeque<>();
        // 2. Create a Map to easily check matching closing and opening brackets.
        Map<Character, Character> matchingBrackets = new HashMap<>();
        matchingBrackets.put(')', '(');
        matchingBrackets.put('}', '{');
        matchingBrackets.put(']', '[');

        System.out.println("\n--- Checking string: " + s + " ---");

        // 3. Iterate through each character of the input string.
        for (char c : s.toCharArray()) {
            System.out.println("Processing character: '" + c + "'. Current stack: " + stack);
            // 4. If the character is an opening bracket, push it onto the stack.
            if (c == '(' || c == '{' || c == '[') {
                stack.push(c);
                System.out.println("  -> Pushed '" + c + "'. Stack is now: " + stack);
            // 5. If the character is a closing bracket, check for a match.
            } else if (c == ')' || c == '}' || c == ']') {
                System.out.println("  -> Found closing bracket: '" + c + "'.");
                // If the stack is empty, it means a closing bracket appeared without a matching open bracket.
                if (stack.isEmpty()) {
                    System.out.println("    -> Stack is empty. Mismatch: closing bracket without open bracket.");
                    return false;
                }
                char topElement = stack.pop();
                char expectedOpen = matchingBrackets.get(c);
                System.out.println("    -> Popped '" + topElement + "'. Expected open: '" + expectedOpen + "'. Stack is now: " + stack);
                // Or if the popped opening bracket doesn't match the current closing bracket, it's unbalanced.
                if (topElement != expectedOpen) {
                    System.out.println("    -> Mismatch: Popped '" + topElement + "' but expected '" + expectedOpen + "'.");
                    return false;
                }
            }
            // Ignore any other characters that are not brackets.
        }
        // 6. After iterating through the entire string, if the stack is empty,
        // all opening brackets were correctly closed, and the string is balanced.
        boolean isStackEmpty = stack.isEmpty();
        System.out.println("--- End of string. Final stack: " + stack + ". Is stack empty? " + isStackEmpty + " ---");
        return isStackEmpty;
    }

    public static void main(String[] args) {
        System.out.println("--- Day 10: Exercise - Balanced Parentheses ---");

        // Test cases
        System.out.println("()[]{}: " + isBalanced("()[]{}")); // Expected: true
        System.out.println("([{}]): " + isBalanced("([{}])")); // Expected: true
        System.out.println("{()}: " + isBalanced("{()}"));   // Expected: true
        System.out.println("[(]): " + isBalanced("[(])"));   // Expected: false
        System.out.println("{[]: " + isBalanced("{[]"));     // Expected: false
        System.out.println("{([])}: " + isBalanced("{([])}")); // Expected: true
        System.out.println("((())): " + isBalanced("((()))")); // Expected: true
        System.out.println("(()): " + isBalanced("(()"));     // Expected: false // Corrected example output
        System.out.println("((())))): " + isBalanced("((()))))"));// Expected: false
        System.out.println("(: " + isBalanced("("));         // Expected: false
        System.out.println("): " + isBalanced(" )"));         // Expected: false
        System.out.println("abc(def[ghi]klm): " + isBalanced("abc(def[ghi]klm)")); // Expected: true
    }
}
