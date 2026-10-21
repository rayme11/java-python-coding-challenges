/**
 * ============================================================================
 * DAY 02 (Java) — Control Flow & Loops
 * ============================================================================
 *
 * READ ME FIRST:
 *   This file is a lesson. Read it top to bottom, then run it:
 *       javac Concept02.java && java Concept02
 *   Then RETYPE the key snippets from memory in Exercise02.java.
 *
 * TODAY'S BIG IDEAS:
 *   1. Choose the RIGHT loop: indexed for / enhanced for / while / do-while.
 *   2. Off-by-one errors are the #1 loop bug — know your bounds cold.
 *   3. break/continue control flow; labeled break exits NESTED loops.
 *   4. Modern switch (Java 14+) is an EXPRESSION with arrow syntax — no fall-through.
 * ============================================================================
 */
public class Concept02 {

    public static void main(String[] args) {
        choosingTheRightLoop();
        offByOne();
        breakAndContinue();
        modernSwitch();
        loopPatternsYouMustKnow();
        interviewQuestions();
    }

    // ------------------------------------------------------------------
    // 1. CHOOSING THE RIGHT LOOP
    // ------------------------------------------------------------------
    // indexed for   -> you need the index, or you mutate by position
    // enhanced for  -> read-only traversal of every element (cleanest)
    // while         -> you don't know the count in advance
    // do-while      -> body must run AT LEAST once (rare, but asked about)
    static void choosingTheRightLoop() {
        System.out.println("=== 1. Choosing the Right Loop ===");

        int[] nums = {10, 20, 30};

        // Indexed: needed when position matters
        for (int i = 0; i < nums.length; i++) {
            System.out.println("  index " + i + " -> " + nums[i]);
        }

        // Enhanced for ("for-each"): no index, can't modify the array via it
        int sum = 0;
        for (int n : nums) {
            sum += n;
        }
        System.out.println("  sum via enhanced for: " + sum);

        // While: condition-driven, count unknown
        int n = 100;
        int halvings = 0;
        while (n > 1) {
            n /= 2;
            halvings++;
        }
        System.out.println("  100 halved to <=1 in " + halvings + " steps (n=" + n + ")");

        // Do-while: runs once even if condition is false
        int x = 0;
        do {
            System.out.println("  do-while ran with x=" + x + " (condition was already false!)");
        } while (x > 0);

        // GOTCHA: enhanced for over an array gives you a COPY of each element.
        for (int v : nums) { v = 999; }        // does NOTHING to nums
        System.out.println("  nums[0] after enhanced-for 'mutation': " + nums[0]); // 10
    }

    // ------------------------------------------------------------------
    // 2. OFF-BY-ONE ERRORS (the classic)
    // ------------------------------------------------------------------
    static void offByOne() {
        System.out.println("\n=== 2. Off-by-One ===");

        int[] arr = {1, 2, 3, 4, 5};

        // WRONG:  i <= arr.length  -> ArrayIndexOutOfBoundsException
        // RIGHT:  i < arr.length
        for (int i = 0; i < arr.length; i++) {
            // safe
        }
        System.out.println("  correct bound: i < arr.length (indices 0.." + (arr.length - 1) + ")");

        // Last element: arr[arr.length - 1], NOT arr[arr.length]
        System.out.println("  last element: " + arr[arr.length - 1]);

        // Looping backwards: start at length - 1, condition i >= 0, step i--
        System.out.print("  backwards: ");
        for (int i = arr.length - 1; i >= 0; i--) {
            System.out.print(arr[i] + " ");
        }
        System.out.println();

        // Sub-range [start, end): end is EXCLUSIVE — Java convention everywhere
        // (subList, substring, Arrays.copyOfRange all work this way)
        int count = 0;
        for (int i = 1; i < 4; i++) {          // indices 1,2,3 -> 3 iterations
            count++;
        }
        System.out.println("  range [1,4) iterates " + count + " times");
    }

    // ------------------------------------------------------------------
    // 3. break / continue / LABELED break
    // ------------------------------------------------------------------
    static void breakAndContinue() {
        System.out.println("\n=== 3. break & continue ===");

        // break: exit the INNERMOST loop entirely
        for (int i = 0; i < 10; i++) {
            if (i == 3) break;
            System.out.print(i + " ");          // 0 1 2
        }
        System.out.println(" <- stopped at 3");

        // continue: skip to next iteration
        for (int i = 0; i < 6; i++) {
            if (i % 2 == 0) continue;
            System.out.print(i + " ");          // 1 3 5 (odds only)
        }
        System.out.println(" <- odds via continue");

        // LABELED break: exit OUTER loop from inner — interview favorite
        int[][] grid = {{1, 2}, {3, -1}, {5, 6}};
        outer:
        for (int r = 0; r < grid.length; r++) {
            for (int c = 0; c < grid[r].length; c++) {
                if (grid[r][c] < 0) {
                    System.out.println("  found negative at [" + r + "][" + c + "], exiting both loops");
                    break outer;
                }
            }
        }
    }

    // ------------------------------------------------------------------
    // 4. MODERN switch (Java 14+)
    // ------------------------------------------------------------------
    // Old switch: fall-through by default, easy to forget break.
    // New switch: arrow labels (no fall-through), can RETURN a value.
    static void modernSwitch() {
        System.out.println("\n=== 4. Modern switch ===");

        String day = "TUESDAY";

        // Old style (still valid, still error-prone):
        int oldLen;
        switch (day) {
            case "MONDAY":
                oldLen = 1;
                break;                          // forget this -> fall-through bug!
            default:
                oldLen = 0;
        }

        // New style: switch EXPRESSION — assigns directly, no break needed
        int len = switch (day) {
            case "MONDAY", "FRIDAY" -> 1;       // multiple labels, comma-separated
            case "TUESDAY" -> {
                System.out.println("  (block inside arrow case)");
                yield 2;                        // 'yield' returns from a block
            }
            default -> 0;                       // required when used as expression
        };
        System.out.println("  switch expression returned: " + len + " (old style: " + oldLen + ")");
    }

    // ------------------------------------------------------------------
    // 5. LOOP PATTERNS YOU MUST KNOW (memorize these idioms)
    // ------------------------------------------------------------------
    static void loopPatternsYouMustKnow() {
        System.out.println("\n=== 5. Essential Loop Idioms ===");

        // (a) Running total / accumulator
        int[] nums = {4, 8, 15, 16, 23, 42};
        int total = 0;
        for (int n : nums) total += n;
        System.out.println("  sum=" + total);

        // (b) Find max (initialize to first element or Integer.MIN_VALUE)
        int max = nums[0];
        for (int i = 1; i < nums.length; i++) {
            if (nums[i] > max) max = nums[i];
        }
        System.out.println("  max=" + max);

        // (c) Early-exit search
        int target = 16, foundAt = -1;         // -1 = "not found" convention
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] == target) { foundAt = i; break; }
        }
        System.out.println("  target " + target + " found at index " + foundAt);

        // (d) Count matches
        int evens = 0;
        for (int n : nums) {
            if (n % 2 == 0) evens++;
        }
        System.out.println("  even count=" + evens);

        // (e) Nested loop over pairs — O(n^2), know the cost!
        int pairCount = 0;
        for (int i = 0; i < nums.length; i++) {
            for (int j = i + 1; j < nums.length; j++) {  // j starts at i+1: each pair once
                pairCount++;
            }
        }
        System.out.println("  unique pairs=" + pairCount + " for n=" + nums.length);
    }

    // ------------------------------------------------------------------
    // INTERVIEW QUESTIONS — answer out loud before tomorrow
    // ------------------------------------------------------------------
    static void interviewQuestions() {
        System.out.println("\n=== Say these answers out loud ===");
        System.out.println("Q1: Why can't you mutate array elements with enhanced for?");
        System.out.println("Q2: What's the difference between break and labeled break?");
        System.out.println("Q3: Why does modern switch not need 'break'?");
        System.out.println("Q4: In a pairs loop, why does j start at i+1?");
        System.out.println("Q5: When must a 'default' branch exist in a switch expression?");
    }
}
