/**
 * ============================================================================
 * DAY 02 EXERCISE (Java) — Grade Analyzer
 * ============================================================================
 * Apply today's concepts: loop choice, bounds, break/continue, switch.
 * Fill in every TODO, then run:  javac Exercise02.java && java Exercise02
 * Target time: 25 minutes.
 * ============================================================================
 */
public class Exercise02 {

    public static void main(String[] args) {
        int[] scores = {88, 92, 45, 76, 100, 61, 39, 84};

        // ---------------------------------------------------------------
        // TASK 1: Print every score with its index, using an INDEXED for:
        //   "Student 0: 88"
        // Then print just the scores (no index) using an ENHANCED for.
        // Question in a comment: why did the second version need the
        // different loop?
        // ---------------------------------------------------------------
        // TODO 
        


        // ---------------------------------------------------------------
        // TASK 2: Compute the class average as a double. Watch out:
        // int / int does INTEGER division. Fix it with a cast.
        // Print: "Average: 73.125" (verify your math!)
        // ---------------------------------------------------------------
        // TODO 2


        // ---------------------------------------------------------------
        // TASK 3: Count how many scores are passing (>= 60) and how many
        // are failing. Use continue to skip failing scores in your count
        // loop (yes, there are other ways — practice continue here).
        // Print both counts.
        // ---------------------------------------------------------------
        int passing = 0;
        for (int s : scores) {
            if (s < 60) continue; // skip failing scores
            passing++;
        }
        int failing = scores.length - passing;
        System.out.println("Passing: " + passing + ", Failing: " + failing);

        // ---------------------------------------------------------------
        // TASK 4: Find the index of the FIRST perfect score (100) using
        // an early-exit search with break.
        // If none exist, report index -1. Print the result.
        // ---------------------------------------------------------------
        int firstPerfect = -1; // -1 = "not found" convention
        for (int i = 0; i < scores.length; i++) {
            if (scores[i] == 100) {
                firstPerfect = i;
                break; // stop at first match
            }
        }
        System.out.println("First perfect score at index: " + firstPerfect);

        // ---------------------------------------------------------------
        // TASK 5: Write a method letterGrade(int score) that returns a
        // String using a MODERN switch EXPRESSION on score / 10:
        //   90+ -> "A", 80s -> "B", 70s -> "C", 60s -> "D", else "F"
        // Then loop over scores and print "88 -> B" style lines.
        // ---------------------------------------------------------------
        for (int s : scores) {
            System.out.println(s + " -> " + letterGrade(s));
        }

        // ---------------------------------------------------------------
        // TASK 6: Reverse-print the scores array (last element first)
        // using a backwards indexed for loop. One line, space-separated.
        // ---------------------------------------------------------------
        for (int i = scores.length - 1; i >= 0; i--) {
            System.out.print(scores[i] + " ");
        }
        System.out.println();

        // ---------------------------------------------------------------
        // STRETCH (optional): Write a method hasPairSummingTo(int[] arr,
        // int target) using the nested-pairs idiom (j starts at i+1).
        // Return as soon as a pair is found. Test with target 184 (88+96?
        // no — find the real pair) and target 999.
        // Question in a comment: what is the Big-O of this approach?
        // ---------------------------------------------------------------
        System.out.println("hasPairSummingTo(scores, 184): " + hasPairSummingTo(scores, 184)); // true (100+84)
        System.out.println("hasPairSummingTo(scores, 999): " + hasPairSummingTo(scores, 999)); // false
        // Big-O: O(n^2) time — nested loop checks up to n(n-1)/2 pairs; O(1) extra space.
    }

    static String letterGrade(int score) {
        return switch (score / 10) {
            case 10, 9 -> "A";
            case 8 -> "B";
            case 7 -> "C";
            case 6 -> "D";
            default -> "F"; // required: switch expression must be exhaustive
        };
    }

    static boolean hasPairSummingTo(int[] arr, int target) {
        for (int i = 0; i < arr.length; i++) {
            for (int j = i + 1; j < arr.length; j++) { // j = i+1: each unique pair once
                if (arr[i] + arr[j] == target) return true; // early exit
            }
        }
        return false;
    }
}
