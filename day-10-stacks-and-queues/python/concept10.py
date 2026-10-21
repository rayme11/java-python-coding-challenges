from collections import deque

# --- Day 10: Stacks & Queues ---

# --- STACK (LIFO - Last-In, First-Out) ---
print("\n--- Stack Example (LIFO) ---")
# In Python, a list can be used as a stack
stack = []

# Push elements onto the stack (append to the end)
stack.append("Book 1")
stack.append("Book 2")
stack.append("Book 3")
print(f"Stack after appends: {stack}")

# Peek at the top element (last element)
if stack:
    print(f"Peek (top element): {stack[-1]}")
print(f"Stack after peek: {stack}")

# Pop elements from the stack (remove from the end)
if stack:
    print(f"Popped: {stack.pop()}") # Removes Book 3
print(f"Stack after first pop: {stack}")

if stack:
    print(f"Popped: {stack.pop()}") # Removes Book 2
print(f"Stack after second pop: {stack}")

print(f"Is stack empty? {not stack}")

# --- QUEUE (FIFO - First-In, First-Out) ---
print("\n--- Queue Example (FIFO) ---")
# For efficient queues, use collections.deque (double-ended queue)
queue = deque()

# Enqueue elements (append to the right)
queue.append("Person A")
queue.append("Person B")
queue.append("Person C")
print(f"Queue after appends: {queue}")

# Peek at the front element (leftmost element)
if queue:
    print(f"Peek (front element): {queue[0]}")
print(f"Queue after peek: {queue}")

# Dequeue elements (pop from the left)
if queue:
    print(f"Dequeued: {queue.popleft()}") # Removes Person A
print(f"Queue after first popleft: {queue}")

if queue:
    print(f"Dequeued: {queue.popleft()}") # Removes Person B
print(f"Queue after second popleft: {queue}")

print(f"Is queue empty? {not queue}")

# --- DEQUE (Double-Ended Queue) ---
print("\n--- Deque Example ---")
# collections.deque can efficiently add/remove from both ends
deque_example = deque()

# Add to front
deque_example.appendleft('C')
deque_example.appendleft('B')
deque_example.appendleft('A')
print(f"Deque after appendleft: {deque_example}")

# Add to rear
deque_example.append('D')
deque_example.append('E')
print(f"Deque after append: {deque_example}")

# Remove from front
if deque_example:
    print(f"Removed from front: {deque_example.popleft()}")
# Remove from rear
if deque_example:
    print(f"Removed from rear: {deque_example.pop()}")
print(f"Deque after removals: {deque_example}")
