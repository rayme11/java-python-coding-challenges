/**
 * ============================================================================
 * DAY 06 (Java) — OOP: Classes & Objects
 * ============================================================================
 *
 * READ ME FIRST:
 *   This file is a lesson. Read it top to bottom, then run it:
 *       javac Concept06.java && java Concept06
 *   Then RETYPE the key snippets from memory in Exercise06.java.
 *
 * TODAY'S BIG IDEAS:
 *   1. A class is a blueprint; an object is an instance built from it.
 *      Fields hold STATE, methods hold BEHAVIOR.
 *   2. Constructors run at `new`. No constructor written? Java gives you a
 *      free no-arg one — but ONLY until you write any constructor yourself.
 *   3. `static` = one copy per CLASS; instance fields = one copy per OBJECT.
 *   4. Encapsulation: keep fields private, expose behavior via methods.
 *   5. toString() makes objects printable; equals() defines "sameness".
 * ============================================================================
 */
public class Concept06 {

    public static void main(String[] args) {
        basics();
        constructorsAndThis();
        staticVsInstance();
        encapsulation();
        printingAndEquality();
        interviewQuestions();
    }

    // ------------------------------------------------------------------
    // 1. CLASSES AND OBJECTS — the mental model
    // ------------------------------------------------------------------
    // A class defines fields (data) + methods (behavior).
    // `new Dog("Rex")` allocates an object on the HEAP and returns a
    // REFERENCE to it (Day 01: Java is pass-by-value, of references!).
    static void basics() {
        System.out.println("=== 1. Classes & objects ===");

        Dog rex = new Dog("Rex", 3);
        Dog fido = new Dog("Fido", 5);

        rex.bark();                       // Rex says woof
        fido.bark();                      // Fido says woof

        System.out.println("  rex == fido: " + (rex == fido));
        System.out.println("  == compares REFERENCES, not content!");

        Dog alsoRex = rex;                // same object, second name for it
        alsoRex.age = 4;                  // mutates the ONE shared object
        System.out.println("  rex.age after alsoRex.age = 4 -> " + rex.age);
    }

    // ------------------------------------------------------------------
    // 2. CONSTRUCTORS AND `this`
    // ------------------------------------------------------------------
    // Constructor rules:
    //   - Name MUST match the class name; no return type (not even void).
    //   - If you write NO constructor, Java gives a free no-arg one.
    //   - If you write ANY constructor, the free one DISAPPEARS.
    //   - Constructors can be overloaded (Day 05!) and can chain: this(...).
    static void constructorsAndThis() {
        System.out.println("\n=== 2. Constructors & this ===");

        Point a = new Point(3, 4);          // full constructor
        Point origin = new Point();         // chained no-arg constructor
        System.out.println("  a:      " + a);
        System.out.println("  origin: " + origin);

        // `this` disambiguates fields from parameters:
        //   Point(int x, int y) { this.x = x; }  // field = parameter
        // `this(...)` calls another constructor in the SAME class.
        // It must be the FIRST statement of the constructor.

        // Won't compile — Point has no free no-arg anymore? It DOES,
        // because we wrote one. But remove it and `new Point()` fails:
        //   "constructor Point in class Point cannot be applied"
    }

    // ------------------------------------------------------------------
    // 3. STATIC VS INSTANCE — one per class vs one per object
    // ------------------------------------------------------------------
    static void staticVsInstance() {
        System.out.println("\n=== 3. static vs instance ===");

        Counter c1 = new Counter();
        Counter c2 = new Counter();
        c1.increment();
        c1.increment();
        c2.increment();

        System.out.println("  c1.count (instance): " + c1.count);   // 2
        System.out.println("  c2.count (instance): " + c2.count);   // 1
        System.out.println("  Counter.total (static): " + Counter.total); // 3
        System.out.println("  static belongs to the CLASS — shared by ALL objects.");

        // Access statics via the CLASS name: Counter.total, not c1.total
        // (c1.total compiles but is misleading style — interviewers notice).

        // A static method CANNOT touch instance fields — no `this` exists.
        // That's why all our Day 01–05 helpers were static: main is static.
    }

    // ------------------------------------------------------------------
    // 4. ENCAPSULATION — private fields, public behavior
    // ------------------------------------------------------------------
    // Rule: fields private, access through methods that enforce invariants.
    // "Invariant" = a rule that must always hold (balance >= 0, age <= 150).
    static void encapsulation() {
        System.out.println("\n=== 4. Encapsulation ===");

        BankAccount acct = new BankAccount("Ada", 100.0);
        acct.deposit(50);
        boolean ok = acct.withdraw(30);
        System.out.println("  withdraw(30) ok? " + ok);
        System.out.println("  balance: " + acct.getBalance());       // 120.0

        boolean bad = acct.withdraw(1000);
        System.out.println("  withdraw(1000) ok? " + bad);           // false!
        // acct.balance = -500;   // WON'T COMPILE — balance is private.
        // The class PROTECTS its own invariant. That is encapsulation.

        // Getters/setters: expose only what's needed.
        // No setter for balance — you must use deposit/withdraw.
    }

    // ------------------------------------------------------------------
    // 5. toString() AND equals()
    // ------------------------------------------------------------------
    static void printingAndEquality() {
        System.out.println("\n=== 5. toString() & equals() ===");

        Point p = new Point(3, 4);
        System.out.println("  with toString:    " + p);              // Point(3, 4)

        Object raw = new Object();
        System.out.println("  without toString: " + raw);            // Object@6d06d69c
        // Default toString = ClassName@hashCode — useless. Override it.

        Point p2 = new Point(3, 4);
        System.out.println("  p == p2:      " + (p == p2));          // false
        System.out.println("  p.equals(p2): " + p.equals(p2));       // true
        // Default equals() IS ==. Override it to compare CONTENT.
        // (Full equals/hashCode contracts come later — today: know why.)
    }

    // ------------------------------------------------------------------
    // 6. INTERVIEW-STYLE QUESTIONS
    // ------------------------------------------------------------------
    static void interviewQuestions() {
        System.out.println("\n=== 6. Quick-fire (answer out loud) ===");
        System.out.println("  Q1: Can a static method call an instance method directly? Why not?");
        System.out.println("  Q2: What constructor does Java give you for free — and when do you lose it?");
        System.out.println("  Q3: new Dog(\"A\") == new Dog(\"A\") — true or false?");
        System.out.println("  Q4: Why is `public int balance;` on a bank account a bug factory?");
        System.out.println("  Q5: What must be the first line when chaining constructors with this(...)?");
    }
}

// ======================================================================
// SUPPORTING CLASSES — one public class per FILE, so these are
// package-private (no modifier). Fine for learning files.
// ======================================================================

class Dog {
    String name;      // instance fields — every Dog gets its own copy
    int age;

    Dog(String name, int age) {
        this.name = name;   // this.field = parameter
        this.age = age;
    }

    void bark() {           // instance method — has access to `this`
        System.out.println("  " + name + " says woof");
    }
}

class Point {
    int x, y;

    Point(int x, int y) {   // full constructor
        this.x = x;
        this.y = y;
    }

    Point() {               // no-arg constructor — chains to the full one
        this(0, 0);         // MUST be first statement
    }

    @Override
    public String toString() {
        return "Point(" + x + ", " + y + ")";
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;                 // same reference
        if (!(o instanceof Point other)) return false;
        return this.x == other.x && this.y == other.y;
    }
}

class Counter {
    int count;              // instance: one per object
    static int total;       // static: one per class, shared

    void increment() {
        count++;
        total++;
    }
}

class BankAccount {
    private String owner;       // private = only this class can touch it
    private double balance;

    BankAccount(String owner, double openingBalance) {
        this.owner = owner;
        if (openingBalance < 0) {
            throw new IllegalArgumentException("opening balance must be >= 0");
        }
        this.balance = openingBalance;
    }

    public void deposit(double amount) {
        if (amount <= 0) return;
        balance += amount;
    }

    public boolean withdraw(double amount) {
        if (amount <= 0 || amount > balance) return false;  // guard the invariant
        balance -= amount;
        return true;
    }

    public double getBalance() {     // getter — read-only access
        return balance;
    }

    public String getOwner() {
        return owner;
    }
}
