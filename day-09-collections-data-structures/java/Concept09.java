/**
 * ============================================================================
 * DAY 09 (Java) — Collections & Data Structures
 * ============================================================================
 *
 * READ ME FIRST:
 *   This file is a lesson. Read it top to bottom, then run it:
 *       javac Concept09.java && java Concept09
 *   Then RETYPE the key snippets from memory in Exercise09.java.
 *
 * TODAY'S BIG IDEAS:
 *   1. Overview of Java Collections Framework: Interfaces (List, Set, Map) and Classes (ArrayList, HashSet, HashMap).
 *   2. `List` Interface: Ordered, allows duplicates (e.g., `ArrayList`, `LinkedList`).
 *   3. `Set` Interface: Unordered, no duplicates (e.g., `HashSet`, `LinkedHashSet`, `TreeSet`).
 *   4. `Map` Interface: Key-value pairs, unique keys (e.g., `HashMap`, `LinkedHashMap`, `TreeMap`).
 *   5. Generics: Type safety and compile-time checks with collections.
 *   6. Iterators: Traversing collections.
 * ============================================================================
 */

import java.util.ArrayList;
import java.util.HashSet;
import java.util.HashMap;
import java.util.List;
import java.util.Set;
import java.util.Map;
import java.util.Iterator;

public class Concept09 {

    public static void main(String[] args) {
        System.out.println("=== DAY 09: Collections & Data Structures ===");

        overviewDemo();
        listDemo();
        setDemo();
        mapDemo();
        genericsDemo();
        iteratorDemo();

        System.out.println("\nEnd of Day 09 Concepts.");
    }

    static void overviewDemo() {
        System.out.println("\n--- 1. Overview of Java Collections Framework ---");
        System.out.println("The Collections Framework provides a unified architecture for representing and manipulating collections.");
        System.out.println("Key Interfaces: List, Set, Map.");
        System.out.println("Key Implementations: ArrayList, LinkedList, HashSet, TreeSet, HashMap, TreeMap.");
    }

    static void listDemo() {
        System.out.println("\n--- 2. List Interface (ArrayList) ---");
        List<String> fruits = new ArrayList<>();
        fruits.add("Apple");
        fruits.add("Banana");
        fruits.add("Apple"); // Allows duplicates
        System.out.println("Fruits list: " + fruits);
        System.out.println("Size: " + fruits.size());
        System.out.println("Element at index 1: " + fruits.get(1));
        fruits.remove("Banana");
        System.out.println("Fruits after removing Banana: " + fruits);
    }

    static void setDemo() {
        System.out.println("\n--- 3. Set Interface (HashSet) ---");
        Set<String> uniqueColors = new HashSet<>();
        uniqueColors.add("Red");
        uniqueColors.add("Green");
        uniqueColors.add("Red"); // Duplicates are not added
        System.out.println("Unique Colors set: " + uniqueColors);
        System.out.println("Size: " + uniqueColors.size());
        System.out.println("Contains Red? " + uniqueColors.contains("Red"));
        uniqueColors.remove("Green");
        System.out.println("Colors after removing Green: " + uniqueColors);
    }

    static void mapDemo() {
        System.out.println("\n--- 4. Map Interface (HashMap) ---");
        Map<String, Integer> studentScores = new HashMap<>();
        studentScores.put("Alice", 95);
        studentScores.put("Bob", 88);
        studentScores.put("Alice", 97); // Updates value for existing key
        System.out.println("Student Scores map: " + studentScores);
        System.out.println("Bob's score: " + studentScores.get("Bob"));
        System.out.println("Contains key 'Alice'? " + studentScores.containsKey("Alice"));
        System.out.println("All keys: " + studentScores.keySet());
        System.out.println("All values: " + studentScores.values());
        studentScores.remove("Bob");
        System.out.println("Scores after removing Bob: " + studentScores);
    }

    static void genericsDemo() {
        System.out.println("\n--- 5. Generics ---");
        // Without generics, you could add any object, leading to runtime errors.
        // List rawList = new ArrayList();
        // rawList.add("String");
        // rawList.add(123); // No compile-time error
        // String s = (String) rawList.get(1); // ClassCastException at runtime

        List<Integer> numbers = new ArrayList<>();
        numbers.add(10);
        numbers.add(20);
        // numbers.add("thirty"); // Compile-time error due to generics
        int firstNum = numbers.get(0);
        System.out.println("Integer list with generics: " + numbers);
    }

    static void iteratorDemo() {
        System.out.println("\n--- 6. Iterators ---");
        List<String> cars = new ArrayList<>();
        cars.add("Ford");
        cars.add("BMW");
        cars.add("Mercedes");

        Iterator<String> it = cars.iterator();
        while (it.hasNext()) {
            String car = it.next();
            System.out.println("  Iterating: " + car);
            if (car.equals("BMW")) {
                it.remove(); // Safe removal during iteration
            }
        }
        System.out.println("Cars after iteration and removal: " + cars);
    }
}
