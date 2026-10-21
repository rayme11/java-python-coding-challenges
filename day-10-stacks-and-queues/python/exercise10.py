from collections import deque

# Exercise: Balanced Parentheses Checker
#
# Implement a function that checks if a given string of parentheses (and other characters)
# is balanced. You should only consider '(', ')', '{', '}', '[', ']'.
# Ignore other characters.
#
# A string is balanced if:
# 1. Open brackets must be closed by the same type of brackets.
# 2. Open brackets must be closed in the correct order.
#
# Example:
# - "()[]{}" -> true
# - "([{}])" -> true
# - "{()}" -> true
# - "[(])" -> false
# - "{[]" -> false
# - "{([])}" -> true
# - "((()))" -> true
# - "(())" -> true
# - "((())))" -> false
# - "(" -> false
# - ")" -> false
#
# Hint: Use a Stack (list or deque in Python) to keep track of open brackets.

def is_balanced(s: str) -> bool:
    # 1. Initialize a deque (acting as a Stack) to store opening brackets.
    stack = deque()
    # 2. Create a dictionary to easily check matching closing and opening brackets.
    matching_brackets = {
        ')': '(',
        '}': '{',
        ']': '[',
    }

    print(f"\n--- Checking string: {s} ---")

    # 3. Iterate through each character of the input string.
    for char in s:
        print(f"Processing character: '{char}'. Current stack: {list(stack)}")
        # 4. If the character is an opening bracket, push it onto the stack.
        if char in '({[':
            stack.append(char)
            print(f"  -> Appended '{char}'. Stack is now: {list(stack)}")
        # 5. If the character is a closing bracket, check for a match.
        elif char in ')}]':
            print(f"  -> Found closing bracket: '{char}'.")
            # If the stack is empty, it means a closing bracket appeared without a matching open bracket.
            if not stack:
                print(f"    -> Stack is empty. Mismatch: closing bracket without open bracket.")
                return False
            
            top_element = stack.pop()
            expected_open = matching_brackets[char]
            print(f"    -> Popped '{top_element}'. Expected open: '{expected_open}'. Stack is now: {list(stack)}")
            # Or if the popped opening bracket doesn't match the current closing bracket, it's unbalanced.
            if top_element != expected_open:
                print(f"    -> Mismatch: Popped '{top_element}' but expected '{expected_open}'.")
                return False
        # Ignore any other characters that are not brackets.
    
    # 6. After iterating through the entire string, if the stack is empty,
    # all opening brackets were correctly closed, and the string is balanced.
    is_stack_empty = not stack
    print(f"--- End of string. Final stack: {list(stack)}. Is stack empty? {is_stack_empty} ---")
    return is_stack_empty

if __name__ == "__main__":
    print("--- Day 10: Exercise - Balanced Parentheses ---")

    # Test cases
    print(f"()[]{{}}: {is_balanced('()[]{}')}")  # Expected: True
    print(f"([{{}}]): {is_balanced('([{}])')}")  # Expected: True
    print(f"{{()}}: {is_balanced('{()}')}")      # Corrected test case to match Java example, Expected: True
    print(f"[(]): {is_balanced('[(])')}")      # Expected: False
    print(f"{{[]: {is_balanced('{[]')}")        # Expected: False
    print(f"{{([])}}: {is_balanced('({([])})')}")  # Expected: True
    print(f"((())): {is_balanced('((()))')}")  # Expected: True
    print(f"(()): {is_balanced('(()')}")      # Corrected example output, Expected: False
    print(f"((())))): {is_balanced('((()))))')}") # Expected: False
    print(f"(: {is_balanced('(')}")          # Expected: False
    print(f"): {is_balanced(')')}")          # Expected: False
    print(f"abc(def[ghi]klm): {is_balanced('abc(def[ghi]klm)')}") # Expected: True
