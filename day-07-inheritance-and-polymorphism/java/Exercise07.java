/**
 * ============================================================================
 * DAY 07 (Java) — Inheritance & Polymorphism: EXERCISES
 * ============================================================================
 *
 * GOAL:
 *   Retype the key snippets from memory from Concept07.java.
 *   Focus on understanding, not just copying.
 *
 * EXERCISES:
 *   1. Create a `Vehicle` class, `Car` subclass, and `ElectricCar` subclass
 *      demonstrating inheritance. Include constructors and overridden methods.
 *   2. Implement the `super` keyword in your `Car` and `ElectricCar` classes
 *      to call superclass constructors and (optionally) methods.
 *   3. Demonstrate method overriding with `@Override` annotation for a method
 *      like `start()` or `drive()` across your `Vehicle` hierarchy.
 *   4. Show polymorphism by creating a `List` of `Vehicle` objects that contains
 *      `Car` and `ElectricCar` instances. Iterate through the list and call
 *      polymorphic methods. Use `instanceof` for safe downcasting to access
 *      subclass-specific methods (e.g., `charge()` for `ElectricCar`).
 *   5. Design an `abstract Animal` class with an abstract method `makeSound()`
 *      and a concrete method `sleep()`. Create concrete subclasses `Dog` and `Cat`
 *      that implement `makeSound()`.
 *   6. Define an `interface Shape` with an abstract method `getArea()` and a default
 *      method `printDescription()`. Create classes `Circle` and `Rectangle` that
 *      implement `Shape`. Demonstrate polymorphism with an `ArrayList` of `Shape` objects.
 *
 * HINT: Refer back to Concept07.java if you get stuck, but try to
 *       solve these from memory first!
 * ============================================================================
 */

public class Exercise07 {

    public static void main(String[] args) {
        System.out.println("=== Day 07 Exercises: Inheritance & Polymorphism ===");

        // --- Exercise 1-3: Inheritance, `super`, Method Overriding ---
        // Your code for Vehicle, Car, ElectricCar classes and their usage here.
        // Make sure to include constructors and overridden methods.


        // --- Exercise 4: Polymorphism ---
        // Create a List<Vehicle> and add different types of vehicles.
        // Iterate and call methods polymorphically, demonstrating downcasting.


        // --- Exercise 5: Abstract Classes ---
        // Implement abstract Animal class and its concrete subclasses Dog and Cat.
        // Create instances and call their methods.


        // --- Exercise 6: Interfaces ---
        // Implement the Shape interface and its concrete classes Circle and Rectangle.
        // Use an ArrayList<Shape> to demonstrate interface polymorphism.

    }
}

// Define your supporting classes (Vehicle, Car, ElectricCar, Animal, Dog, Cat, Shape, Circle, Rectangle) here
// as package-private classes, similar to how they are structured in Concept07.java.
// e.g.,
// class Vehicle { ... }
// class Car extends Vehicle { ... }
// abstract class Animal { ... }
// class Dog extends Animal { ... }
// interface Shape { ... }
// class Circle implements Shape { ... }
