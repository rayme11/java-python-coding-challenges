/**
 * ============================================================================
 * DAY 05 EXERCISE (Java) — Text Formatter Toolkit
 * ============================================================================
 * Apply today's concepts: signatures, overloading, varargs, scope, lambdas.
 * Fill in every TODO, then run:  javac Exercise05.java && java Exercise05
 * Target time: 25 minutes.
 * ============================================================================
 */
import java.util.Arrays;
import java.util.List;
import java.util.function.Function;
import java.util.function.Predicate;

public class Exercise05 {

    public static void main(String[] args) {

        // ---------------------------------------------------------------
        // TASK 1: Write shout(String text) that returns the text uppercased
        // with "!" appended: shout("hello") -> "HELLO!"
        // Print shout("functions are fun").
        // ---------------------------------------------------------------
        // TODO 1


        // ---------------------------------------------------------------
        // TASK 2: OVERLOAD shout: add shout(String text, int times) that
        // repeats the shouted text `times` times, space-separated:
        //   shout("hey", 3) -> "HEY! HEY! HEY!"
        // Print both versions. Comment: why does Java pick the right one?
        // ---------------------------------------------------------------
        // TODO 2


        // ---------------------------------------------------------------
        // TASK 3: Write joinAll(String separator, String... parts) using
        // varargs: joinAll("-", "a", "b", "c") -> "a-b-c"
        // Edge case: what should joinAll("-") return? (Hint: empty varargs
        // is a valid call.) Print joinAll(" | ", "red", "green", "blue").
        // ---------------------------------------------------------------
        // TODO 3


        // ---------------------------------------------------------------
        // TASK 4: Scope puzzle — predict BEFORE running, then uncomment
        // and check. Which lines compile? Fix or delete the broken ones
        // and explain in a comment what scope rule each demonstrates.
        // ---------------------------------------------------------------
        int outer = 10;
        for (int i = 0; i < 1; i++) {
            int inner = outer + 1;
            // TODO 4a: can you print `inner` here? try it.
        }
        // TODO 4b: can you print `inner` here? try it (then fix).


        // ---------------------------------------------------------------
        // TASK 5: Given the list of words below, use a lambda with
        // stream().filter(...) to keep only words starting with "p",
        // then map them through shout(String) from Task 1 using a
        // METHOD REFERENCE. Print the result as a List.
        // Expected: [PYTHON!, JAVA! no wait — only p-words] -> [PYTHON!]
        // ---------------------------------------------------------------
        List<String> words = Arrays.asList("python", "java", "perl", "ruby", "php");
        // TODO 5
        // Hint: List<String> result = words.stream()
        //          .filter(<lambda: Predicate>)
        //          .map(<method ref>)
        //          .toList();


        // ---------------------------------------------------------------
        // TASK 6: Write applyToEach(List<String> items, Function<String,String> f)
        // that returns a new List with f applied to every element.
        // Then call it twice on `words`:
        //   a) with a lambda that reverses each word
        //   b) with a method reference to String::toUpperCase
        // ---------------------------------------------------------------
        // TODO 6


        // ---------------------------------------------------------------
        // STRETCH (optional): Write compose(Function<String,String> f,
        // Function<String,String> g) returning a Function that applies
        // g FIRST then f. Use it to build shoutThenReverse and print
        // compose(shout, reverse) applied to "hello".
        // (This is how functional pipelines get built — Day 19 preview.)
        // ---------------------------------------------------------------
        // TODO STRETCH

    }

    // Write your helper methods below main():

}
