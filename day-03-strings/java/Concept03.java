/**
 * ============================================================================
 * DAY 03 (Java) — Strings & String Manipulation
 * ============================================================================
 *
 * READ ME FIRST:
 *   This file is a lesson. Read it top to bottom, then run it:
 *       javac Concept03.java && java Concept03
 *   Then RETYPE the key snippets from memory in Exercise03.java.
 *
 * TODAY'S BIG IDEAS:
 *   1. Strings are IMMUTABLE — every "modification" creates a new object.
 *   2. `+` in a loop is O(n^2); StringBuilder is the fix. Know it cold.
 *   3. substring(a, b): a inclusive, b EXCLUSIVE (same [start, end) rule as Day 02).
 *   4. The method toolkit: charAt, indexOf, split, trim, replace, equalsIgnoreCase.
 *   5. Palindrome check via two pointers — the #1 string warm-up.
 * ============================================================================
 */
public class Concept03 {

    public static void main(String[] args) {
        immutability();
        stringBuilderVsPlus();
        substringAndSlicing();
        methodToolkit();
        palindromeTwoPointers();
        interviewQuestions();
    }

    // ------------------------------------------------------------------
    // 1. IMMUTABILITY
    // ------------------------------------------------------------------
    // A String can never change after creation. Methods that look like
    // they modify (toUpperCase, replace, trim) all return NEW strings.
    static void immutability() {
        System.out.println("=== 1. Immutability ===");

        String s = "hello";
        s.toUpperCase();                       // result DISCARDED — s unchanged!
        System.out.println("  after toUpperCase(): " + s);   // still "hello"

        s = s.toUpperCase();                   // rebind to the NEW string
        System.out.println("  after rebinding:     " + s);   // "HELLO"

        // == vs equals (Day 01 callback):
        String a = "java";
        String b = new String("java");         // forces a NEW object, not pooled
        System.out.println("  a == b:        " + (a == b));        // false (identity)
        System.out.println("  a.equals(b):   " + a.equals(b));     // true  (value)
        System.out.println("  RULE: compare strings with .equals(), never ==");
    }

    // ------------------------------------------------------------------
    // 2. StringBuilder vs +
    // ------------------------------------------------------------------
    // Each `s += part` creates a whole new String (copies all chars).
    // In a loop over n parts that's O(n^2) total copying.
    // StringBuilder keeps ONE mutable buffer: O(n) total.
    static void stringBuilderVsPlus() {
        System.out.println("\n=== 2. StringBuilder vs + ===");

        // BAD in a loop (fine for one-shot joins):
        // String s = "";
        // for (int i = 0; i < n; i++) s += i;   // O(n^2) — interview red flag

        // GOOD:
        StringBuilder sb = new StringBuilder();
        for (int i = 1; i <= 5; i++) {
            sb.append(i);
            if (i < 5) sb.append("-");
        }
        System.out.println("  built: " + sb);                    // 1-2-3-4-5

        // StringBuilder is also the idiomatic way to REVERSE:
        String reversed = new StringBuilder("stressed").reverse().toString();
        System.out.println("  reversed: " + reversed);           // desserts

        // Other useful ops:
        StringBuilder sb2 = new StringBuilder("helo");
        sb2.insert(3, "l");                  // "hello"
        sb2.deleteCharAt(0);                 // "ello"
        System.out.println("  insert/delete demo: " + sb2);

        // Follow-up interviews love: StringBuilder vs StringBuffer
        //   StringBuffer = synchronized (thread-safe, slower) — almost never needed.
    }

    // ------------------------------------------------------------------
    // 3. substring & slicing — [start, end), end EXCLUSIVE
    // ------------------------------------------------------------------
    static void substringAndSlicing() {
        System.out.println("\n=== 3. substring ===");

        String s = "interview";
        //            012345678

        System.out.println("  substring(0, 5): " + s.substring(0, 5));  // "inter"
        System.out.println("  substring(5):    " + s.substring(5));     // "view" (to end)
        System.out.println("  length:          " + s.length());          // 9

        // GOTCHA: substring(0, 5) gives chars at 0,1,2,3,4 — length is (end - start)
        System.out.println("  substring(i, i) is always: '" + s.substring(3, 3) + "' (empty)");

        // Off-by-one: last char is charAt(length() - 1)
        System.out.println("  last char: " + s.charAt(s.length() - 1));  // 'w'

        // Common idiom: first half / second half
        int mid = s.length() / 2;
        System.out.println("  halves: [" + s.substring(0, mid) + "] [" + s.substring(mid) + "]");
    }

    // ------------------------------------------------------------------
    // 4. THE METHOD TOOLKIT
    // ------------------------------------------------------------------
    static void methodToolkit() {
        System.out.println("\n=== 4. Method toolkit ===");

        String raw = "  Hello, World  ";

        System.out.println("  trim():           '" + raw.trim() + "'");
        System.out.println("  toLowerCase():    " + raw.trim().toLowerCase());
        System.out.println("  contains:         " + raw.contains("World"));
        System.out.println("  startsWith:       " + raw.trim().startsWith("Hello"));
        System.out.println("  indexOf('o'):     " + raw.indexOf('o'));          // first occurrence
        System.out.println("  lastIndexOf('o'): " + raw.lastIndexOf('o'));
        System.out.println("  replace:          " + raw.trim().replace("World", "Java"));

        // split — returns String[], takes a REGEX
        String csv = "ana,bruno,carla";
        String[] names = csv.split(",");
        System.out.println("  split:            " + String.join(" | ", names));

        // join (static) — the reverse of split
        System.out.println("  join:             " + String.join(", ", names));

        // equalsIgnoreCase — case-insensitive compare without allocating
        System.out.println("  equalsIgnoreCase: " + "JAVA".equalsIgnoreCase("java"));

        // char iteration — two ways:
        String word = "abc";
        for (int i = 0; i < word.length(); i++) {
            char c = word.charAt(i);         // indexed access
        }
        for (char c : word.toCharArray()) {
            // enhanced for needs a char[] copy — fine for small strings
        }

        // Char helpers you'll use constantly:
        System.out.println("  isLetter('a'):    " + Character.isLetter('a'));
        System.out.println("  isDigit('7'):     " + Character.isDigit('7'));
        System.out.println("  toLowerCase('A'): " + Character.toLowerCase('A'));

        // String formatting (like printf):
        System.out.println(String.format("  formatted: %s=%.2f", "pi", Math.PI));
    }

    // ------------------------------------------------------------------
    // 5. PALINDROME — two pointers (memorize this pattern)
    // ------------------------------------------------------------------
    static void palindromeTwoPointers() {
        System.out.println("\n=== 5. Palindrome (two pointers) ===");

        System.out.println("  isPalindrome(\"racecar\"): " + isPalindrome("racecar"));  // true
        System.out.println("  isPalindrome(\"java\"):    " + isPalindrome("java"));     // false

        // Why two pointers instead of reverse-and-compare?
        //   - O(1) extra space (reverse builds a whole new string)
        //   - early exit on first mismatch
    }

    static boolean isPalindrome(String s) {
        int left = 0;
        int right = s.length() - 1;
        while (left < right) {
            if (s.charAt(left) != s.charAt(right)) return false;
            left++;
            right--;
        }
        return true;
    }

    // ------------------------------------------------------------------
    // SAY THESE OUT LOUD
    // ------------------------------------------------------------------
    static void interviewQuestions() {
        System.out.println("\n=== Interview quick-fire (answer aloud!) ===");
        System.out.println("  Q: Why is += in a loop bad?               A: O(n^2) copying — use StringBuilder");
        System.out.println("  Q: substring(2, 5) includes index 5?      A: NO — end is exclusive");
        System.out.println("  Q: Compare strings with == ?              A: NEVER — use .equals()");
        System.out.println("  Q: Reverse a string idiomatically?        A: new StringBuilder(s).reverse()");
        System.out.println("  Q: split() takes what kind of argument?   A: a regex");
    }
}
