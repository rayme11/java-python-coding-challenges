/**
 * ============================================================================
 * DAY 07 (Java) — Inheritance & Polymorphism
 * ============================================================================
 *
 * READ ME FIRST:
 *   This file is a lesson. Read it top to bottom, then run it:
 *       javac Concept07.java && java Concept07
 *   Then RETYPE the key snippets from memory in Exercise07.java.
 *
 * TODAY'S BIG IDEAS:
 *   1. Inheritance: `extends` for code reuse; subclasses inherit public/protected
 *      members, but NOT private ones (though they exist!).
 *   2. `super`: Calls a superclass constructor or method. `super()` must be
 *      first in a subclass constructor if explicit.
 *   3. Method Overriding: `@Override` annotation is good practice; same signature,
 *      different implementation in subclass.
 *   4. Polymorphism: "Many forms"; an object can take on types of its ancestors.
 *      Upcasting (implicit) and Downcasting (explicit, `instanceof` check).
 *   5. Abstract Classes: Classes that cannot be instantiated directly; can have
 *      abstract (no body) and concrete methods. Subclasses MUST implement
 *      abstract methods unless they are also abstract.
 *   6. Interfaces: Define a contract (what a class DOES). All methods implicitly
 *      public abstract (pre-Java 8); can have default and static methods (Java 8+).
 * ============================================================================
 */
import java.util.ArrayList;
import java.util.List;

public class Concept07 {

    public static void main(String[] args) {
        inheritanceBasics();
        superKeyword();
        methodOverriding();
        polymorphismDemo();
        abstractClassesDemo();
        interfacesDemo();
        interviewQuestions();
    }

    // ------------------------------------------------------------------
    // 1. INHERITANCE BASICS
    // ------------------------------------------------------------------
    // `extends` keyword establishes an "is-a" relationship.
    // Subclass inherits public/protected fields and methods from superclass.
    static void inheritanceBasics() {
        System.out.println("=== 1. Inheritance Basics ===");

        Car myCar = new Car("Toyota", "Camry", 2020);
        myCar.start();
        myCar.drive();
        myCar.stop();
        System.out.println("  Car brand: " + myCar.getBrand());

        ElectricCar myElectricCar = new ElectricCar("Tesla", "Model 3", 2023, 300);
        myElectricCar.start();
        myElectricCar.charge();
        myElectricCar.drive();
        System.out.println("  Electric Car range: " + myElectricCar.getRange() + " miles");
        myElectricCar.stop();
        System.out.println();
    }

    // ------------------------------------------------------------------
    // 2. `super` KEYWORD
    // ------------------------------------------------------------------
    // `super()` calls the superclass constructor. MUST be first statement.
    // `super.method()` calls a superclass method.
    static void superKeyword() {
        System.out.println("=== 2. `super` Keyword ===");

        SportsCar porsche = new SportsCar("Porsche", "911", 2024, 300);
        porsche.start(); // Uses overridden start()
        System.out.println("  Engine type: " + porsche.getEngineType()); // Inherited
        porsche.accelerate(); // Subclass specific
        porsche.stop();
        System.out.println();
    }

    // ------------------------------------------------------------------
    // 3. METHOD OVERRIDING
    // ------------------------------------------------------------------
    // Subclass provides a specific implementation for a method already
    // defined in its superclass. Same signature. `@Override` annotation
    // is a good safety check (compiler error if not actually overriding).
    static void methodOverriding() {
        System.out.println("=== 3. Method Overriding ===");

        Vehicle basicVehicle = new Vehicle("Generic", "Model", 0);
        basicVehicle.start(); // Vehicle's start
        basicVehicle.stop();

        Car specificCar = new Car("Ford", "Focus", 2018);
        specificCar.start(); // Car's start (overridden)
        specificCar.stop();

        ElectricCar tesla = new ElectricCar("Tesla", "Model S", 2022, 400);
        tesla.start(); // ElectricCar's start (overridden)
        tesla.stop();
        System.out.println();
    }

    // ------------------------------------------------------------------
    // 4. POLYMORPHISM
    // ------------------------------------------------------------------
    // A reference variable of a supertype can refer to an object of any
    // of its subtypes.
    // Upcasting: implicit (Vehicle v = new Car();)
    // Downcasting: explicit, potentially dangerous (Car c = (Car)v;).
    // Always use `instanceof` before downcasting.
    static void polymorphismDemo() {
        System.out.println("=== 4. Polymorphism ===");

        List<Vehicle> vehicles = new ArrayList<>();
        vehicles.add(new Vehicle("Bike", "Mountain", 2021));
        vehicles.add(new Car("Honda", "Civic", 2020));
        vehicles.add(new ElectricCar("Nissan", "Leaf", 2019, 150));
        vehicles.add(new SportsCar("Ferrari", "488", 2025, 200));

        for (Vehicle v : vehicles) {
            v.start(); // Polymorphic method call
            v.drive(); // All vehicles can drive
            v.stop();
            if (v instanceof ElectricCar) {
                // Downcasting is needed to access ElectricCar specific methods
                ((ElectricCar) v).charge();
            }
            if (v instanceof SportsCar) {
                ((SportsCar) v).accelerate();
            }
            System.out.println("  Type: " + v.getClass().getSimpleName());
            System.out.println("---");
        }
        System.out.println();
    }

    // ------------------------------------------------------------------
    // 5. ABSTRACT CLASSES
    // ------------------------------------------------------------------
    // Cannot be instantiated. Can have abstract (no body) and concrete methods.
    // Subclasses must implement all abstract methods or be declared abstract themselves.
    static void abstractClassesDemo() {
        System.out.println("=== 5. Abstract Classes ===");

        // Cannot do: Animal a = new Animal(); // Compile error
        Dog myDog = new Dog("Buddy");
        myDog.makeSound();
        myDog.sleep();

        Cat myCat = new Cat("Whiskers");
        myCat.makeSound();
        myCat.sleep();
        System.out.println();
    }

    // ------------------------------------------------------------------
    // 6. INTERFACES
    // ------------------------------------------------------------------
    // A contract. A class `implements` an interface. All methods are implicitly
    // `public abstract` (pre-Java 8). Can have `default` and `static` methods (Java 8+).
    // A class can implement multiple interfaces.
    static void interfacesDemo() {
        System.out.println("=== 6. Interfaces ===");

        // Using a class that implements an interface
        Circle circle = new Circle(5.0);
        System.out.println("  Circle area: " + circle.calculateArea());
        circle.draw();

        Rectangle rectangle = new Rectangle(4.0, 6.0);
        System.out.println("  Rectangle area: " + rectangle.calculateArea());
        rectangle.draw();
        System.out.println();

        // Polymorphism with interfaces
        List<Drawable> drawables = new ArrayList<>();
        drawables.add(new Circle(2.5));
        drawables.add(new Rectangle(3.0, 5.0));

        System.out.println("  Drawing all shapes:");
        for (Drawable d : drawables) {
            d.draw();
        }
        System.out.println("  Interface default method: " + Drawable.getDefaultColor());
        Drawable.staticMethodExample();
        System.out.println();
    }

    // ------------------------------------------------------------------
    // 7. INTERVIEW-STYLE QUESTIONS
    // ------------------------------------------------------------------
    static void interviewQuestions() {
        System.out.println("=== 7. Interview quick-fire (answer aloud!) ===");
        System.out.println("  Q1: What's the key difference between `extends` and `implements`?");
        System.out.println("  Q2: When should you use an abstract class vs. an interface?");
        System.out.println("  Q3: Can you instantiate an abstract class? Why/why not?");
        System.out.println("  Q4: Explain upcasting and downcasting in polymorphism.");
        System.out.println("  Q5: What's the purpose of the `@Override` annotation?");
    }
}


// ======================================================================
// SUPPORTING CLASSES (package-private)
// ======================================================================

// Base class for demonstrating inheritance
class Vehicle {
    private String brand;
    private String model;
    private int year;

    public Vehicle(String brand, String model, int year) {
        this.brand = brand;
        this.model = model;
        this.year = year;
    }

    public void start() {
        System.out.println("  Vehicle " + brand + " " + model + " starting...");
    }

    public void stop() {
        System.out.println("  Vehicle " + brand + " " + model + " stopping.");
    }

    public void drive() {
        System.out.println("  Vehicle " + brand + " " + model + " is driving.");
    }

    public String getBrand() {
        return brand;
    }

    public String getModel() {
        return model;
    }

    public int getYear() {
        return year;
    }
}

// Subclass Car inheriting from Vehicle
class Car extends Vehicle {
    private String engineType; // Added field

    public Car(String brand, String model, int year) {
        super(brand, model, year); // Call superclass constructor
        this.engineType = "Internal Combustion";
    }

    // Overriding the start method
    @Override
    public void start() {
        System.out.println("  Car " + getBrand() + " " + getModel() + " (engine: " + engineType + ") ignition engaged.");
    }

    @Override
    public void drive() {
        System.out.println("  Car " + getBrand() + " " + getModel() + " is driving on four wheels.");
    }

    public String getEngineType() {
        return engineType;
    }
}

// Subclass ElectricCar inheriting from Car
class ElectricCar extends Car {
    private int range; // Added field

    public ElectricCar(String brand, String model, int year, int range) {
        super(brand, model, year); // Call superclass constructor
        this.range = range;
    }

    public void charge() {
        System.out.println("  Electric Car " + getBrand() + " " + getModel() + " is charging.");
    }

    @Override
    public void start() {
        System.out.println("  Electric Car " + getBrand() + " " + getModel() + " silently powering on.");
    }

    @Override
    public void drive() {
        System.out.println("  Electric Car " + getBrand() + " " + getModel() + " is driving emission-free.");
    }

    public int getRange() {
        return range;
    }
}

// Subclass SportsCar demonstrating super.method()
class SportsCar extends Car {
    private int horsepower;

    public SportsCar(String brand, String model, int year, int horsepower) {
        super(brand, model, year);
        this.horsepower = horsepower;
    }

    @Override
    public void start() {
        super.start(); // Call Car's start method
        System.out.println("  Sports Car engine roars to life with " + horsepower + " HP!");
    }

    public void accelerate() {
        System.out.println("  Sports Car " + getBrand() + " " + getModel() + " accelerating rapidly!");
    }
}


// Abstract Class Example
abstract class Animal {
    private String name;

    public Animal(String name) {
        this.name = name;
    }

    // Abstract method (no body) - subclasses must implement
    public abstract void makeSound();

    // Concrete method
    public void sleep() {
        System.out.println("  " + name + " is sleeping.");
    }

    public String getName() {
        return name;
    }
}

// Concrete subclass of Animal
class Dog extends Animal {
    public Dog(String name) {
        super(name);
    }

    @Override
    public void makeSound() {
        System.out.println("  " + getName() + " barks: Woof! Woof!");
    }
}

// Another concrete subclass of Animal
class Cat extends Animal {
    public Cat(String name) {
        super(name);
    }

    @Override
    public void makeSound() {
        System.out.println("  " + getName() + " meows: Meow!");
    }
}

// Interface Example
interface Drawable {
    // All interface methods are implicitly public abstract before Java 8
    // Since Java 8, methods can have default implementations
    double calculateArea(); // Implicitly public abstract

    // Default method (Java 8+)
    default void draw() {
        System.out.println("  Drawing a generic shape.");
    }

    // Static method (Java 8+)
    static String getDefaultColor() {
        return "Blue";
    }

    static void staticMethodExample() {
        System.out.println("  This is a static method in an interface.");
    }
}

// Class implementing the Drawable interface
class Circle implements Drawable {
    private double radius;

    public Circle(double radius) {
        this.radius = radius;
    }

    @Override
    public double calculateArea() {
        return Math.PI * radius * radius;
    }

    @Override
    public void draw() {
        System.out.println("  Drawing a circle with radius " + radius + ".");
    }
}

// Another class implementing the Drawable interface
class Rectangle implements Drawable {
    private double width;
    private double height;

    public Rectangle(double width, double height) {
        this.width = width;
        this.height = height;
    }

    @Override
    public double calculateArea() {
        return width * height;
    }

    @Override
    public void draw() {
        System.out.println("  Drawing a rectangle with width " + width + " and height " + height + ".");
    }
}
