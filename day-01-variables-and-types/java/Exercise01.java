/**
 * ============================================================================
 * DAY 01 EXERCISE (Java) — Price Calculator
 * ============================================================================
 * Apply today's concepts: primitives vs references, immutability, pass-by-value.
 * Fill in every TODO, then run:  javac Exercise01.java && java Exercise01
 * Target time: 20 minutes.
 * ============================================================================
 */
public class Exercise01 {

    public static void main(String[] args) {
        // ---------------------------------------------------------------
        // TASK 1: Declare variables with the CORRECT types.
        //   - itemName: the text "Mechanical Keyboard"
        //   - price: 79.99 (which primitive? hint: not float — interviews
        //     expect you to know float's precision issues)
        //   - quantity: 3
        //   - inStock: true
        // Print each with its value.
        // ---------------------------------------------------------------
        // TODO 1


        // ---------------------------------------------------------------
        // TASK 2: Compute the line total (price * quantity) and store it
        // in a variable called lineTotal. Print it.
        // Question to answer in a comment: what TYPE is the result, and why?
        // ---------------------------------------------------------------
        // TODO 2


        // ---------------------------------------------------------------
        // TASK 3: Build a label "Mechanical Keyboard x3 = $239.97"
        // WITHOUT using + concatenation in a loop — this is a single
        // string, so + is fine here, BUT do it two ways:
        //   a) with + concatenation
        //   b) with String.format (interviewers love seeing you know it)
        // Print both.
        // ---------------------------------------------------------------
        // TODO 3


        // ---------------------------------------------------------------
        // TASK 4: Fix the bug. This method is SUPPOSED to apply a 10%
        // discount to the price. Predict what it prints BEFORE running,
        // then fix it so the discount actually applies.
        // ---------------------------------------------------------------
        double price4 = 100.0;
        applyDiscountBuggy(price4);
        System.out.println("price after buggy discount: " + price4); // prediction?

        // TODO 4: write applyDiscountFixed() that RETURNS the discounted
        // price, call it, and print the result (should be 90.0)


        // ---------------------------------------------------------------
        // TASK 5: Arrays share references. Given cart below, write a method
        // applyTax(double[] prices) that multiplies EVERY element in place
        // by 1.08. Call it, print the cart before and after.
        // ---------------------------------------------------------------
        double[] cart = {10.0, 20.0, 30.0};
        // TODO 5


        // ---------------------------------------------------------------
        // STRETCH (optional, if time remains):
        // Write a method isSameProduct(String a, String b) that compares
        // two product names correctly. Test it with:
        //   isSameProduct("Mouse", new String("Mouse"))  -> must be true
        // Explain in a comment why the naive version fails.
        // ---------------------------------------------------------------
        // TODO stretch
    }

    static void applyDiscountBuggy(double price) {
        price = price * 0.90;   // why doesn't this work? (answer in a comment)
    }
}
