/**
 * ============================================================================
 * DAY 04 EXERCISE (Java) — Sales Dashboard
 * ============================================================================
 * Apply today's concepts: arrays vs lists, in-place ops, two pointers.
 * Fill in every TODO, then run:  javac Exercise04.java && java Exercise04
 * Target time: 25 minutes.
 * ============================================================================
 */
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Exercise04 {

    public static void main(String[] args) {
        int[] dailySales = {120, 85, 0, 200, 95, 0, 150};

        // ---------------------------------------------------------------
        // TASK 1: Print the array, its length, the first element, and the
        // last element (no off-by-one — Day 02 callback).
        // ---------------------------------------------------------------
        // TODO 1


        // ---------------------------------------------------------------
        // TASK 2: Write findMax(int[] arr) returning the largest value,
        // using an enhanced for loop. Edge case in a comment: what should
        // happen for an EMPTY array? Pick a behavior and defend it.
        // Print findMax(dailySales).
        // ---------------------------------------------------------------
        // TODO 2


        // ---------------------------------------------------------------
        // TASK 3: Write reverseInPlace(int[] arr) using the two-pointer
        // template (swap until left >= right). Print the array before
        // and after on a COPY — so dailySales stays intact.
        // Hint: Arrays.copyOf(arr, arr.length).
        // ---------------------------------------------------------------
        // TODO 3


        // ---------------------------------------------------------------
        // TASK 4: Write removeZeroDays(int[] arr) that returns a NEW
        // List<Integer> containing only the non-zero sales, in order.
        // Question in a comment: why return a List instead of an int[]?
        // (What don't you know before you start?)
        // ---------------------------------------------------------------
        // TODO 4


        // ---------------------------------------------------------------
        // TASK 5: Write hasPairSummingTo(int[] sortedArr, int target)
        // using the OPPOSITE-DIRECTION two-pointer approach — NOT the
        // brute-force nested loop from Day 02. Sort a copy of dailySales
        // first. Test with target 285 (120+... find the real pair) and 999.
        // Comment: why does this only work on a SORTED array?
        // ---------------------------------------------------------------
        // TODO 5


        // ---------------------------------------------------------------
        // TASK 6: Write runningTotals(int[] arr) that returns a NEW int[]
        // where result[i] = sum of arr[0..i] (a prefix-sum array).
        //   {120, 85, 0, 200} -> {120, 205, 205, 405}
        // Comment: what pattern makes each element O(1) after the first?
        // ---------------------------------------------------------------
        // TODO 6


        // ---------------------------------------------------------------
        // STRETCH (optional): Write maxSubarraySum(int[] arr) — Kadane's
        // algorithm: the largest sum of any contiguous subarray.
        //   {-2, 1, -3, 4, -1, 2, 1, -5, 4} -> 6  (the subarray {4,-1,2,1})
        // One loop, two variables (current best, overall best). O(n).
        // This is a top-10 interview question — worth the extra 10 min.
        // ---------------------------------------------------------------
        // TODO STRETCH

    }

    // Write your helper methods below main():

}
