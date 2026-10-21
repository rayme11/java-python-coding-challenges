"""
============================================================================
DAY 01 EXERCISE (Python) — Price Calculator
============================================================================
Apply today's concepts: dynamic typing, mutability, == vs is, function args.
Fill in every TODO, then run:  python3 exercise01.py
Target time: 15–20 minutes.
============================================================================
"""


def main():
    # ------------------------------------------------------------------
    # TASK 1: Create these variables and print each with its type
    # using f-strings and type().__name__:
    #   item_name = "Mechanical Keyboard"
    #   price     = 79.99
    #   quantity  = 3
    #   in_stock  = True
    # Example output line: item_name = 'Mechanical Keyboard' (str)
    # ------------------------------------------------------------------
    # TODO 1


    # ------------------------------------------------------------------
    # TASK 2: Compute line_total = price * quantity and print it.
    # Notice the floating point result! Then fix the display by printing
    # it rounded to 2 decimals with an f-string format spec.
    # Interview nugget: why is 79.99 * 3 not exactly 239.97?
    # (Answer in a comment — keyword: binary floating point / IEEE 754)
    # ------------------------------------------------------------------
    # TODO 2


    # ------------------------------------------------------------------
    # TASK 3: Build the label "Mechanical Keyboard x3 = $239.97"
    # two ways:
    #   a) f-string
    #   b) str.format()
    # Print both.
    # ------------------------------------------------------------------
    # TODO 3


    # ------------------------------------------------------------------
    # TASK 4: Fix the bug. apply_discount_buggy is SUPPOSED to return a
    # new price with 10% off. It doesn't. Predict the output first,
    # then fix it.
    # ------------------------------------------------------------------
    result = apply_discount_buggy(100.0)
    print("buggy discount result:", result)   # prediction?

    # TODO 4: fix apply_discount_buggy (or write apply_discount) so the
    # printed result is 90.0


    # ------------------------------------------------------------------
    # TASK 5: Lists are mutable and shared. Write apply_tax(prices) that
    # multiplies every element IN PLACE by 1.08 (rounded to 2 decimals).
    # Print the cart before and after.
    # Then answer in a comment: how would you write it to NOT mutate the
    # caller's list? (You don't have to code it — just say how.)
    # ------------------------------------------------------------------
    cart = [10.0, 20.0, 30.0]
    # TODO 5


    # ------------------------------------------------------------------
    # TASK 6: The mutable-default trap. Fix add_to_cart so that two
    # separate calls without a cart argument do NOT share a list.
    # ------------------------------------------------------------------
    # print(add_to_cart("apple"))    # expect ['apple']
    # print(add_to_cart("banana"))   # expect ['banana']  (not ['apple', 'banana'])
    # TODO 6


def apply_discount_buggy(price):
    price = price * 0.90   # something is missing — what?


def add_to_cart(item, cart=[]):
    cart.append(item)
    return cart


if __name__ == "__main__":
    main()
