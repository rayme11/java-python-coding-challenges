/**
 * ============================================================================
 * DAY 04 (Java) — Arrays & Lists
 * ============================================================================
 *
 * READ ME FIRST:
 *   This file is a lesson. Read it top to bottom, then run it:
 *       javac Concept04.java && java Concept04
 *   Then RETYPE the key snippets from memory in Exercise04.java.
 *
 * TODAY'S BIG IDEAS:
 *   1. Java arrays are FIXED size — know Arrays.asList vs ArrayList.
 *   2. "In-place" means O(1) extra space — swap, don't copy.
 *   3. TWO POINTERS: the #1 array interview pattern. Memorize the template.
 *   4. Front insertion is O(n); appends are (amortized) O(1).
 * ============================================================================
 */
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Concept04 {

    public static void main(String[] args) {
        arraysVsArrayList();
        inPlaceReversal();
        twoPointerTemplate();
        costModel();
        interviewQuestions();
    }

    // ------------------------------------------------------------------
    // 1. ARRAYS vs ArrayList
    // ------------------------------------------------------------------
    static void arraysVsArrayList() {
        System.out.println("=== 1. Arrays vs ArrayList ===");

        // Fixed size, set at creation. Primitives allowed (int[]).
        int[] fixed = new int[3];              // {0, 0, 0} — zero-initialized!
        fixed[0] = 10;
        // fixed[3] = 99;                      // ArrayIndexOutOfBoundsException
        System.out.println("  fixed:    " + Arrays.toString(fixed) + " (length " + fixed.length + ")");

        // Dynamic, grows/shrinks. Objects only (Integer, not int — boxing!).
        List<Integer> dynamic = new ArrayList<>(List.of(10, 20, 30));
        dynamic.add(40);
        dynamic.remove(0);                     // shifts everything left — O(n)
        System.out.println("  dynamic:  " + dynamic + " (size " + dynamic.size() + ")");

        // GOTCHA interviews love: Arrays.asList returns a FIXED-SIZE list!
        List<Integer> trap = Arrays.asList(1, 2, 3);
        trap.set(0, 99);                       // OK — set works
        // trap.add(4);                        // UnsupportedOperationException!
        System.out.println("  Arrays.asList is fixed-size — add() throws. Wrap it:");
        System.out.println("  new ArrayList<>(Arrays.asList(1,2,3)) is the safe idiom");

        // Conversions (you'll type these a lot):
        int[] arr = {1, 2, 3};
        Integer[] boxed = Arrays.stream(arr).boxed().toArray(Integer[]::new);
        int[] back = Arrays.stream(boxed).mapToInt(Integer::intValue).toArray();
    }

    // ------------------------------------------------------------------
    // 2. IN-PLACE REVERSAL (the template everything builds on)
    // ------------------------------------------------------------------
    static void inPlaceReversal() {
        System.out.println("\n=== 2. In-place reversal (two pointers) ===");

        int[] a = {1, 2, 3, 4, 5};
        int left = 0, right = a.length - 1;
        while (left < right) {                 // stop when they MEET — not <=
            int tmp = a[left];
            a[left] = a[right];
            a[right] = tmp;
            left++;
            right--;
        }
        System.out.println("  reversed in place: " + Arrays.toString(a));

        // Why "in-place" matters: O(1) extra space vs O(n) for a copy.
        // Say the complexity out loud whenever you write one:
        //   time O(n) — each element swapped once
        //   space O(1) — only tmp + two indices
    }

    // ------------------------------------------------------------------
    // 3. THE TWO-POINTER TEMPLATE (and its two flavors)
    // ------------------------------------------------------------------
    static void twoPointerTemplate() {
        System.out.println("\n=== 3. Two-pointer flavors ===");

        // FLAVOR A: pointers move TOWARD each other (reverse, palindrome, pair-sum)
        //   left=0, right=n-1; while (left < right) { ...; left++; right--; }

        // FLAVOR B: slow/fast, same direction (dedupe in place, move zeroes)
        int[] nums = {0, 1, 0, 3, 12};
        moveZeroes(nums);
        System.out.println("  moveZeroes:  " + Arrays.toString(nums));   // [1,3,12,0,0]

        // Classic pair-sum on a SORTED array — O(n) instead of brute O(n^2):
        int[] sorted = {1, 2, 4, 7, 11, 15};
        System.out.println("  pair summing to 9: " + Arrays.toString(twoSumSorted(sorted, 9)));
    }

    // Slow/fast: `slow` marks where the next non-zero goes.
    static void moveZeroes(int[] nums) {
        int slow = 0;
        for (int fast = 0; fast < nums.length; fast++) {
            if (nums[fast] != 0) {
                int tmp = nums[slow];
                nums[slow] = nums[fast];
                nums[fast] = tmp;
                slow++;
            }
        }
    }

    // Opposite-direction: shrink the window by logic, not by scanning.
    static int[] twoSumSorted(int[] nums, int target) {
        int left = 0, right = nums.length - 1;
        while (left < right) {
            int sum = nums[left] + nums[right];
            if (sum == target) return new int[]{left, right};
            if (sum < target) left++;        // need a bigger sum
            else right--;                    // need a smaller sum
        }
        return new int[]{-1, -1};
    }

    // ------------------------------------------------------------------
    // 4. COST MODEL (say these out loud until automatic)
    // ------------------------------------------------------------------
    static void costModel() {
        System.out.println("\n=== 4. Cost model ===");
        System.out.println("  access by index        O(1)   — contiguous memory");
        System.out.println("  append at end          O(1)*  — *amortized for ArrayList");
        System.out.println("  insert/remove at front O(n)   — everything shifts");
        System.out.println("  search unsorted        O(n)   — linear scan");
        System.out.println("  search sorted          O(log n) — binary search (Day 25!)");
        System.out.println("  sort                   O(n log n) — Arrays.sort / Collections.sort");

        // Sorting both ways:
        int[] a = {5, 2, 8, 1};
        Arrays.sort(a);                                   // in place, ascending
        System.out.println("  sorted ascending:  " + Arrays.toString(a));

        Integer[] b = {5, 2, 8, 1};
        Arrays.sort(b, (x, y) -> y - x);                  // descending needs Comparator
        System.out.println("  sorted descending: " + Arrays.toString(b));
        // NOTE: primitives (int[]) can't take a Comparator — another boxing gotcha.
    }

    // ------------------------------------------------------------------
    // SAY THESE OUT LOUD
    // ------------------------------------------------------------------
    static void interviewQuestions() {
        System.out.println("\n=== Interview quick-fire (answer aloud!) ===");
        System.out.println("  Q: Array full — now what?            A: ArrayList (or allocate new + copy)");
        System.out.println("  Q: Reverse in place, extra space?    A: O(1) — two pointers + swap");
        System.out.println("  Q: When do two pointers stop?        A: when they meet: left < right");
        System.out.println("  Q: Insert at front cost?             A: O(n) — all elements shift");
        System.out.println("  Q: Pair-sum on sorted array?         A: two pointers O(n), not brute O(n^2)");
    }
}
