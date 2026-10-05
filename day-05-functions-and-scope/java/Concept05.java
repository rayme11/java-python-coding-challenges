/**
 * ============================================================================
 * DAY 05 (Java) — Functions & Scope
 * ============================================================================
 *
 * READ ME FIRST:
 *   This file is a lesson. Read it top to bottom, then run it:
 *       javac Concept05.java && java Concept05
 *   Then RETYPE the key snippets from memory in Exercise05.java.
 *
 * TODAY'S BIG IDEAS:
 *   1. Java methods live on CLASSES; overloading = same name, different
 *      parameter TYPES/COUNT — return type alone doesn't overload.
 *   2. Varargs (int... nums) is Java's answer to *args — an array in disguise.
 *   3. Scope: block scope rules everything; loop/try/if bodies create scope.
 *   4. Lambdas are anonymous implementations of a SINGLE-method interface.
 * ============================================================================
 */
import java.util.Arrays;
import java.util.List;
import java.util.function.Function;
import java.util.function.Predicate;

public class Concept05 {

    public static void main(String[] args) {
        methodSignatures();
        overloading();
        varargsDemo();
        scopeRules();
        lambdasIntro();
        interviewQuestions();
    }

    // ------------------------------------------------------------------
    // 1. METHOD SIGNATURES
    // ------------------------------------------------------------------
    // A signature = method NAME + parameter TYPES (in order).
    // NOT included: return type, parameter names, exceptions.
    static void methodSignatures() {
        System.out.println("=== 1. Method signatures ===");

        // static vs instance: static belongs to the CLASS, no object needed.
        // main() is static, which is why all our helpers so far are static.
        System.out.println("  greet(\"Ada\"): " + greet("Ada"));

        // Access modifiers you'll be asked about:
        //   public            -> anywhere
        //   private           -> this class only
        //   (default/package) -> same package only
        //   protected         -> package + subclasses (Day 16!)
    }

    static String greet(String name) {
        return "Hello, " + name + "!";
    }

    // ------------------------------------------------------------------
    // 2. OVERLOADING — Java's "default arguments" alternative
    // ------------------------------------------------------------------
    static void overloading() {
        System.out.println("\n=== 2. Overloading ===");

        System.out.println("  area(5):        " + area(5));          // int version
        System.out.println("  area(5.0):      " + area(5.0));        // double version
        System.out.println("  area(3, 4):     " + area(3, 4));       // two-arg version
        System.out.println("  Compiler picks by ARGUMENT TYPES at compile time.");

        // ILLEGAL overload (won't compile):
        //   static int area(int side) { ... }
        //   static long area(int side) { ... }   // same params, different return — NO
        // Return type is NOT part of the signature.
    }

    static int area(int side) {              // square
        return side * side;
    }

    static double area(double radius) {      // circle
        return Math.PI * radius * radius;
    }

    static int area(int w, int h) {          // rectangle
        return w * h;
    }

    // ------------------------------------------------------------------
    // 3. VARARGS — int... is really int[]
    // ------------------------------------------------------------------
    static void varargsDemo() {
        System.out.println("\n=== 3. Varargs ===");

        System.out.println("  sum():           " + sum());             // 0 — empty is legal
        System.out.println("  sum(1, 2, 3):    " + sum(1, 2, 3));
        System.out.println("  sum(array):      " + sum(new int[]{4, 5, 6}));

        // Rules:
        //   - at most ONE varargs parameter per method
        //   - it must be the LAST parameter
        //   - inside the method, treat it as an array
    }

    static int sum(int... nums) {
        int total = 0;
        for (int n : nums) total += n;
        return total;
    }

    // ------------------------------------------------------------------
    // 4. SCOPE RULES
    // ------------------------------------------------------------------
    static void scopeRules() {
        System.out.println("\n=== 4. Scope ===");

        int x = 1;                              // method scope
        {
            int y = 2;                          // block scope
            System.out.println("  inside block: x=" + x + ", y=" + y);
        }
        // System.out.println(y);               // COMPILE ERROR — y is gone

        for (int i = 0; i < 2; i++) {
            String msg = "i=" + i;              // new scope PER ITERATION
        }
        // System.out.println(i);               // COMPILE ERROR — i scoped to loop

        // Shadowing: inner scope can RE-declare an outer name (bad style!)
        int value = 10;
        if (true) {
            // int value = 99;                  // actually ILLEGAL in Java
                                               // (unlike C) — no shadowing locals
        }
        System.out.println("  Java forbids local-variable shadowing — a feature, not a bug.");

        // Fields CAN be shadowed by locals; disambiguate with `this.field`.
    }

    // ------------------------------------------------------------------
    // 5. LAMBDAS — anonymous functions (Java 8+)
    // ------------------------------------------------------------------
    // A lambda implements a FUNCTIONAL INTERFACE: an interface with exactly
    // one abstract method. Key ones in java.util.function:
    //   Predicate<T>   T -> boolean
    //   Function<T,R>  T -> R
    //   Consumer<T>    T -> void
    //   Supplier<T>    () -> T
    static void lambdasIntro() {
        System.out.println("\n=== 5. Lambdas ===");

        // Before lambdas (anonymous class) vs after:
        Predicate<Integer> oldWay = new Predicate<Integer>() {
            @Override public boolean test(Integer n) { return n % 2 == 0; }
        };
        Predicate<Integer> isEven = n -> n % 2 == 0;

        System.out.println("  isEven.test(4): " + isEven.test(4));

        // Where lambdas shine: passing behavior INTO methods
        List<String> names = Arrays.asList("ada", "grace", "edsger", "barbara");

        long longNames = names.stream()
                .filter(n -> n.length() > 4)          // Predicate
                .map(String::toUpperCase)             // method reference — a lambda shorthand
                .count();
        System.out.println("  names >4 chars, uppercased, counted: " + longNames);

        // Effectively final rule: lambdas can capture local variables ONLY
        // if they're never reassigned ("effectively final"):
        int threshold = 4;
        names.stream().filter(n -> n.length() > threshold).forEach(System.out::println);
        // threshold++;                              // would BREAK the lambda — compile error

        // When NOT to use a lambda: body longer than ~3 lines, or needs a name
        // for stack traces/recursion. Write a named method instead.
    }

    // ------------------------------------------------------------------
    // SAY THESE OUT LOUD
    // ------------------------------------------------------------------
    static void interviewQuestions() {
        System.out.println("\n=== Interview quick-fire (answer aloud!) ===");
        System.out.println("  Q: Two methods, same name?            A: overload — different param types/count");
        System.out.println("  Q: Overload on return type only?      A: illegal — not part of the signature");
        System.out.println("  Q: int... inside the method?          A: just an int[] — iterate it");
        System.out.println("  Q: Loop variable visible after loop?  A: no — block scope");
        System.out.println("  Q: Lambda captures a mutated local?   A: no — must be effectively final");
    }
}
