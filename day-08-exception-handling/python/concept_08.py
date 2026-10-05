'''
DAY 08 (Python) — Exception Handling

READ ME FIRST:
  This file is a lesson. Read it top to bottom, then run it:
      python concept_08.py
  Then RETYPE the key snippets from memory in exercise_08.py.

TODAY'S BIG IDEAS:
  1. Understanding Exceptions: What are exceptions, and why do we need them?
  2. `try-except`: Basic structure for handling exceptions.
  3. Multiple `except` Blocks: Handling different types of exceptions.
  4. `else` and `finally` Blocks: Enhancing exception handling.
  5. `raise` Keyword: Manually raising exceptions.
  6. Custom Exceptions: Creating your own exception types.
'''

def understanding_exceptions():
    print("\n--- 1. Understanding Exceptions ---")
    print("Exceptions are events that disrupt the normal flow of a program.")
    print("They are used to handle errors gracefully, preventing program crashes.")
    # Example of a runtime error (ZeroDivisionError)
    # x = 1 / 0

def basic_try_except():
    print("\n--- 2. Basic try-except ---")
    try:
        result = 10 / 0 # This will cause a ZeroDivisionError
        print(f"Result: {result}")
    except ZeroDivisionError as e:
        print(f"Caught a ZeroDivisionError: {e}")
    print("Continuing after try-except.")

def multiple_except_blocks():
    print("\n--- 3. Multiple except Blocks ---")
    try:
        my_list = [1, 2]
        print(my_list[2]) # IndexError
        int('abc') # ValueError
    except IndexError as e:
        print(f"Caught an IndexError: {e}")
    except ValueError as e:
        print(f"Caught a ValueError: {e}")
    except Exception as e: # Generic except block (should be last)
        print(f"Caught a generic Exception: {e}")

def else_and_finally_blocks():
    print("\n--- 4. `else` and `finally` Blocks ---")
    try:
        x = 10
        y = 2
        result = x / y
    except ZeroDivisionError as e:
        print(f"Caught: {e}")
    else:
        print(f"Division successful, result: {result} (else block)")
    finally:
        print("Finally block executed. This always runs, regardless of exception.")

    print("\n-- Another example with exception --")
    try:
        x = 10
        y = 0
        result = x / y
    except ZeroDivisionError as e:
        print(f"Caught: {e}")
    else:
        print(f"Division successful, result: {result} (else block)")
    finally:
        print("Finally block executed. This always runs, regardless of exception.")

def raise_keyword():
    print("\n--- 5. `raise` Keyword ---")
    def check_age(age):
        if age < 0:
            raise ValueError("Age cannot be negative")
        print(f"Age is: {age}")

    try:
        check_age(-5)
    except ValueError as e:
        print(f"Caught error: {e}")

def custom_exceptions():
    print("\n--- 6. Custom Exceptions ---")
    class InvalidAmountError(Exception):
        """Custom exception for invalid amounts."""
        def __init__(self, amount, message="Invalid amount provided"):
            self.amount = amount
            self.message = message
            super().__init__(self.message)

    def process_transaction(amount):
        if amount <= 0:
            raise InvalidAmountError(amount, "Transaction amount must be positive")
        print(f"Processing transaction for {amount}")

    try:
        process_transaction(-100)
    except InvalidAmountError as e:
        print(f"Caught custom error: {e.message}, Amount: {e.amount}")

# Main execution block
if __name__ == "__main__":
    understanding_exceptions()
    basic_try_except()
    multiple_except_blocks()
    else_and_finally_blocks()
    raise_keyword()
    custom_exceptions()
    print("\nEnd of Day 08 Concepts.")
