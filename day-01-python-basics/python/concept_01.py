'''
============================================================================
DAY 01 (Python) — Variables, Data Types & Basic I/O
============================================================================

READ ME FIRST:
  This file is a lesson. Read it top to bottom, then run it:
      python concept_01.py
  Then RETYPE the key snippets from memory in exercise_01.py.

TODAY'S BIG IDEAS:
  1. Variables: Dynamic typing, no explicit declaration needed.
  2. Basic Data Types: Integers, Floats, Strings, Booleans.
  3. String Operations: Concatenation, f-strings, basic methods.
  4. User Input & Output: `input()` and `print()`.
============================================================================
'''

# ------------------------------------------------------------------
# 1. VARIABLES - No explicit type declaration!
# ------------------------------------------------------------------
def variables_demo():
    print("=== 1. Variables ===")

    # Python is dynamically typed
    name = "Alice"
    age = 30
    height = 5.9
    is_student = True

    print(f"  Name: {name}, Type: {type(name)}")
    print(f"  Age: {age}, Type: {type(age)}")
    print(f"  Height: {height}, Type: {type(height)}")
    print(f"  Is Student: {is_student}, Type: {type(is_student)}")

    # Variables can change type
    age = "thirty"
    print(f"  Age (after reassign): {age}, Type: {type(age)}
")

# ------------------------------------------------------------------
# 2. BASIC DATA TYPES
# ------------------------------------------------------------------
def data_types_demo():
    print("=== 2. Basic Data Types ===")

    # Integers (int)
    num_int = 100
    print(f"  Integer: {num_int}")

    # Floating-point numbers (float)
    num_float = 3.14159
    print(f"  Float: {num_float}")

    # Strings (str) - single or double quotes
    str_single = 'Hello Python'
    str_double = "World of Code"
    print(f"  String (single quotes): {str_single}")
    print(f"  String (double quotes): {str_double}")

    # Booleans (bool) - True/False (capitalized)
    bool_true = True
    bool_false = False
    print(f"  Boolean True: {bool_true}")
    print(f"  Boolean False: {bool_false}
")

# ------------------------------------------------------------------
# 3. STRING OPERATIONS
# ------------------------------------------------------------------
def string_operations_demo():
    print("=== 3. String Operations ===")

    # Concatenation
    first_name = "John"
    last_name = "Doe"
    full_name = first_name + " " + last_name
    print(f"  Concatenation: {full_name}")

    # f-strings (formatted string literals) - Python 3.6+
    greeting = f"  Hello, {first_name}! Your last name is {last_name}."
    print(greeting)

    # String methods
    message = "  python is FUN"
    print(f"  Original: '{message}'")
    print(f"  Uppercase: '{message.upper()}'")
    print(f"  Lowercase: '{message.lower()}'")
    print(f"  Capitalize: '{message.capitalize()}'")
    print(f"  Title case: '{message.title()}'")
    print(f"  Replace 'FUN' with 'awesome': '{message.replace('FUN', 'awesome')}'
")

# ------------------------------------------------------------------
# 4. USER INPUT & OUTPUT
# ------------------------------------------------------------------
def io_demo():
    print("=== 4. User Input & Output ===")

    # Output using print()
    print("  This is a simple print statement.")
    print("  You can print multiple items:", 1, True, 3.14)
    print("  By default, print adds a newline. Use end='' to change it.", end='')
    print("  This is on the same line.")
    print("  Separator for multiple items:", 1, 2, 3, sep=' -- ')

    # Input using input() - ALWAYS returns a string!
    # user_name = input("  Enter your name: ")
    # user_age_str = input("  Enter your age: ")
    # print(f"  Hello, {user_name}! You are {user_age_str} years old.")
    #
    # # Convert input string to integer
    # try:
    #     user_age_int = int(user_age_str)
    #     print(f"  Your age as an integer: {user_age_int}")
    # except ValueError:
    #     print("  Invalid age entered. Please enter a number.")
    print("  (Skipping interactive input for automated run. Please uncomment to test.)
")


# ------------------------------------------------------------------
# INTERVIEW QUESTIONS
# ------------------------------------------------------------------
def interview_questions():
    print("=== Interview Quick-Fire (answer aloud!) ===")
    print("  Q1: How do you declare a variable in Python?")
    print("  Q2: What's the main difference between an integer and a float?")
    print("  Q3: How do you concatenate strings in Python?")
    print("  Q4: What data type does the `input()` function always return?")
    print("  Q5: How can you check the type of a variable in Python?")
    print("  QQ: True or False: Python requires you to declare a variable's type before using it.")
    print("  QQ: What is an f-string and why is it useful?")
    print("  QQ: What is the primary use case for the `int()` function when dealing with user input?")

if __name__ == "__main__":
    variables_demo()
    data_types_demo()
    string_operations_demo()
    io_demo()
    interview_questions()
