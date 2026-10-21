'''
DAY 09 (Python) — Collections & Data Structures

READ ME FIRST:
  This file is a lesson. Read it top to bottom, then run it:
      python concept_09.py
  Then RETYPE the key snippets from memory in exercise_09.py.

TODAY'S BIG IDEAS:
  1. Lists: Ordered, mutable collections (like dynamic arrays).
  2. Tuples: Ordered, immutable collections.
  3. Dictionaries: Unordered, mutable key-value pairs.
  4. Sets: Unordered, mutable collections of unique elements.
  5. List, Dictionary, and Set Comprehensions: Concise ways to create collections.
  6. Common Collection Operations: Adding, removing, checking membership, iteration.
'''

def list_demo():
    print("\n--- 1. Lists ---")
    my_list = [1, 2, 3, "apple", True]
    print(f"Original list: {my_list}")
    my_list.append(4)
    print(f"After append: {my_list}")
    my_list.insert(1, "banana")
    print(f"After insert: {my_list}")
    my_list.remove("apple")
    print(f"After remove: {my_list}")
    print(f"Element at index 2: {my_list[2]}")
    print(f"List slice [1:4]: {my_list[1:4]}")

def tuple_demo():
    print("\n--- 2. Tuples ---")
    my_tuple = (1, 2, "hello", False)
    print(f"Original tuple: {my_tuple}")
    # my_tuple.append(3) # This would raise an AttributeError (immutable)
    print(f"Element at index 0: {my_tuple[0]}")
    print(f"Tuple length: {len(my_tuple)}")
    # Tuples are often used for fixed collections of items, e.g., coordinates
    coordinates = (10.0, 20.0)
    print(f"Coordinates: {coordinates}")

def dictionary_demo():
    print("\n--- 3. Dictionaries ---")
    my_dict = {"name": "Alice", "age": 30, "city": "New York"}
    print(f"Original dictionary: {my_dict}")
    my_dict["age"] = 31 # Update value
    my_dict["occupation"] = "Engineer" # Add new key-value pair
    print(f"After update and add: {my_dict}")
    print(f"Alice's age: {my_dict["age"]}")
    print(f"Keys: {my_dict.keys()}")
    print(f"Values: {my_dict.values()}")
    print(f"Items: {my_dict.items()}")
    my_dict.pop("city")
    print(f"After pop: {my_dict}")

def set_demo():
    print("\n--- 4. Sets ---")
    my_set = {1, 2, 3, 2, 1, 4} # Duplicates are automatically removed
    print(f"Original set: {my_set}")
    my_set.add(5)
    print(f"After add: {my_set}")
    my_set.remove(2)
    print(f"After remove: {my_set}")
    other_set = {3, 4, 5, 6}
    print(f"Union: {my_set.union(other_set)}")
    print(f"Intersection: {my_set.intersection(other_set)}")

def comprehensions_demo():
    print("\n--- 5. List, Dictionary, and Set Comprehensions ---")
    # List comprehension
    squares = [x*x for x in range(5)]
    print(f"Squares (list comp): {squares}")
    evens = [x for x in range(10) if x % 2 == 0]
    print(f"Evens (list comp with condition): {evens}")

    # Dictionary comprehension
    square_dict = {x: x*x for x in range(3)}
    print(f"Square dict (dict comp): {square_dict}")

    # Set comprehension
    unique_letters = {char for char in "hello world" if char.isalpha()}
    print(f"Unique letters (set comp): {unique_letters}")

def common_operations_demo():
    print("\n--- 6. Common Collection Operations ---")
    numbers = [1, 2, 3, 4, 5]
    print(f"List: {numbers}")
    print(f"Length: {len(numbers)}")
    print(f"Is 3 in list? {3 in numbers}")

    names = {"Alice": 1, "Bob": 2}
    print(f"Dict: {names}")
    print(f"Is 'Alice' key in dict? {'Alice' in names}")
    print(f"Is 1 value in dict? {1 in names.values()}")

# Main execution block
if __name__ == "__main__":
    list_demo()
    tuple_demo()
    dictionary_demo()
    set_demo()
    comprehensions_demo()
    common_operations_demo()
    print("\nEnd of Day 09 Concepts.")
