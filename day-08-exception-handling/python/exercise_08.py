'''
DAY 08 (Python) — Exception Handling: EXERCISES

GOAL:
  Retype the key snippets from memory from concept_08.py.
  Focus on understanding, not just copying.

EXERCISES:
  1. Write a function that attempts to perform an integer division by zero.
     Use `try-except` to handle the `ZeroDivisionError`.
  2. Write a function that tries to access a list element out of bounds
     and convert a non-numeric string to an integer. Use multiple `except`
     blocks to handle `IndexError` and `ValueError`.
  3. Create a function `process_input(input_string)` that uses the `raise` keyword
     to manually raise an `ValueError` if the input string is empty or None.
     Call this function and catch the `ValueError`.
  4. Define a custom exception `NegativeBalanceError` that extends `Exception`.
     Create a function `withdraw(amount, balance)` that raises `NegativeBalanceError`
     if the withdrawal `amount` would result in a negative `balance`.
     Demonstrate catching your custom exception.

HINT: Refer back to concept_08.py if you get stuck, but try to
      solve these from memory first!
'''

# Exercise 1: Basic try-except for ZeroDivisionError
def exercise_1():
    print("\n--- Exercise 1: Basic try-except ---")
    # Your code here

# Exercise 2: Multiple except blocks
def exercise_2():
    print("\n--- Exercise 2: Multiple except blocks ---")
    # Your code here

# Exercise 3: `raise` keyword
def exercise_3():
    print("\n--- Exercise 3: `raise` keyword ---")
    # Your code here

# Exercise 4: Custom Exception
class NegativeBalanceError(Exception):
    """Custom exception for negative balance."""
    # Your code here for the custom exception

def withdraw(amount, balance):
    # Your code here for the withdraw function
    pass

def exercise_4():
    print("\n--- Exercise 4: Custom Exception ---")
    # Your code here to demonstrate catching NegativeBalanceError


if __name__ == "__main__":
    exercise_1()
    exercise_2()
    exercise_3()
    exercise_4()
