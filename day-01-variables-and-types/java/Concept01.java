/**
 * ============================================================================
 * DAY 01 (Java) — Variables, Types & Mutability
 * ============================================================================
 *
 * READ ME FIRST:
 *   This file is a lesson. Read it top to bottom, then run it:
 *       javac Concept01.java && java Concept01
 *   Then RETYPE the key snippets from memory in Exercise01.java.
 *
 * TODAY'S BIG IDEAS:
 *   1. Java is STATICALLY TYPED — every variable's type is fixed at compile time.
 *   2. There are exactly two kinds of types: PRIMITIVES and REFERENCES.
 *   3. Java is PASS-BY-VALUE. Always. (The *value* of a reference variable
 *      is a memory address — that address is what gets copied.)
 *   4. Strings are IMMUTABLE — you never change a String, only make new ones.
 * ============================================================================
 */
public class Concept01 {

    public static void main(String[] args) {
        primitivesVsReferences();
        equalityPitfall();
        stringImmutability();
        passByValueDemo();
        interviewQuestions();
    }

    // ------------------------------------------------------------------
    // 1. PRIMITIVES vs REFERENCES
    // ------------------------------------------------------------------
    // Primitives (8 total): byte, short, int, long, float, double, char, boolean
    //   - store the actual value
    //   - live on the stack (for local variables)
    //   - CANNOT be null
    //
    // Reference types: String, arrays, every class/interface you write
    //   - the variable stores a REFERENCE (address) to an object on the heap
    //   - CAN be null
    //   - every primitive has a "wrapper" class: Integer, Double, Boolean...
    static void primitivesVsReferences() {
        System.out.println("=== 1. Primitives vs References ===");

        int a = 42;                 // primitive: 'a' IS the value 42
        int b = a;                  // copy of the VALUE
        b = 99;
        System.out.println("a after changing b: " + a);   // 42 — untouched

        int[] arr1 = {1, 2, 3};     // reference: arr1 points to an array object
        int[] arr2 = arr1;          // copy of the REFERENCE — same object!
        arr2[0] = 99;
        System.out.println("arr1[0] after changing arr2: " + arr1[0]); // 99 (!)

        // Wrapper types + autoboxing
        Integer boxed = a;          // autoboxing: int -> Integer
        int unboxed = boxed;        // unboxing: Integer -> int
        Integer n = null;           // legal for references...
        // int crash = n;           // ...but unboxing null throws NullPointerException!
        System.out.println("boxed=" + boxed + ", unboxed=" + unboxed + ", n=" + n);

        // var (Java 10+): type is INFERRED, still static. Not dynamic typing!
        var message = "hello";      // compiler treats this as String
        var count = 10;             // int
        System.out.println("var message=" + message + ", count=" + count);
    }

    // ------------------------------------------------------------------
    // 2. EQUALITY: == vs .equals()
    // ------------------------------------------------------------------
    // ==       compares PRIMITIVE VALUES, or for references: SAME OBJECT?
    // .equals() compares CONTENT (for classes that override it, like String)
    static void equalityPitfall() {
        System.out.println("\n=== 2. == vs .equals() ===");

        String s1 = "hello";                  // string literal -> interned pool
        String s2 = "hello";                  // same pool entry
        String s3 = new String("hello");      // explicitly NEW object on heap

        System.out.println("s1 == s2:      " + (s1 == s2));        // true  (pool)
        System.out.println("s1 == s3:      " + (s1 == s3));        // false (!)
        System.out.println("s1.equals(s3): " + s1.equals(s3));     // true  (content)

        // INTERVIEW RULE: NEVER use == for Strings. Always .equals().
        // Bonus trap: Integer cache works for -128..127
        Integer x = 127, y = 127;
        Integer p = 128, q = 128;
        System.out.println("127 == 127 (Integer): " + (x == y));   // true  (cached)
        System.out.println("128 == 128 (Integer): " + (p == q));   // false (!)
    }

    // ------------------------------------------------------------------
    // 3. STRING IMMUTABILITY
    // ------------------------------------------------------------------
    // String methods NEVER modify the original — they return new objects.
    // In loops, use StringBuilder (mutable) to avoid O(n^2) copying.
    static void stringImmutability() {
        System.out.println("\n=== 3. String Immutability ===");

        String s = "hello";
        s.toUpperCase();                       // return value DISCARDED — s unchanged!
        System.out.println("after toUpperCase() ignored: " + s);   // hello
        s = s.toUpperCase();                   // reassign to the NEW string
        System.out.println("after reassignment:          " + s);   // HELLO

        // Efficient building
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < 5; i++) {
            sb.append(i);                      // mutates in place — no new objects
        }
        System.out.println("StringBuilder result: " + sb);         // 01234
    }

    // ------------------------------------------------------------------
    // 4. PASS-BY-VALUE (the classic interview trap)
    // ------------------------------------------------------------------
    // Java copies the variable's VALUE into the parameter.
    //   - primitive  -> copy of the number: callee can't change caller's var
    //   - reference  -> copy of the address: callee CAN mutate the shared
    //                   object, but CANNOT make caller's variable point elsewhere
    static void passByValueDemo() {
        System.out.println("\n=== 4. Pass-by-Value ===");

        int num = 5;
        tryToChangePrimitive(num);
        System.out.println("num after method: " + num);            // 5

        int[] data = {1, 2, 3};
        mutateArray(data);
        System.out.println("data[0] after mutate: " + data[0]);    // 99 (shared object)

        reassignArray(data);
        System.out.println("data[0] after reassign: " + data[0]);  // still 99
    }

    static void tryToChangePrimitive(int n) { n = 999; }           // local copy only
    static void mutateArray(int[] arr)      { arr[0] = 99; }       // same object!
    static void reassignArray(int[] arr)    { arr = new int[]{7}; }// caller unaffected

    // ------------------------------------------------------------------
    // INTERVIEW QUESTIONS — answer out loud before tomorrow
    // ------------------------------------------------------------------
    static void interviewQuestions() {
        System.out.println("\n=== Say these answers out loud ===");
        System.out.println("Q1: Why is 'new String(\"a\") == \"a\"' false?");
        System.out.println("Q2: Why did arr1[0] change when we modified arr2?");
        System.out.println("Q3: Java: pass-by-value or pass-by-reference? Explain.");
        System.out.println("Q4: Why use StringBuilder in a loop?");
        System.out.println("Q5: What happens when you unbox a null Integer?");
    }
}
