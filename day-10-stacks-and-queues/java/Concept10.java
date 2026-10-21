import java.util.ArrayDeque;
import java.util.Deque;
import java.util.Queue;

public class Concept10 {

    public static void main(String[] args) {
        System.out.println("--- Day 10: Stacks & Queues ---");

        // --- STACK (LIFO - Last-In, First-Out) ---
        System.out.println("\n--- Stack Example (LIFO) ---");
        // In Java, Deque is preferred over the legacy Stack class
        Deque<String> stack = new ArrayDeque<>();

        // Push elements onto the stack
        stack.push("Book 1"); // Add to the top
        stack.push("Book 2");
        stack.push("Book 3");
        System.out.println("Stack after pushes: " + stack);

        // Peek at the top element without removing it
        System.out.println("Peek (top element): " + stack.peek());
        System.out.println("Stack after peek: " + stack);

        // Pop elements from the stack
        System.out.println("Popped: " + stack.pop()); // Removes Book 3
        System.out.println("Stack after first pop: " + stack);

        System.out.println("Popped: " + stack.pop()); // Removes Book 2
        System.out.println("Stack after second pop: " + stack);

        System.out.println("Is stack empty? " + stack.isEmpty());

        // --- QUEUE (FIFO - First-In, First-Out) ---
        System.out.println("\n--- Queue Example (FIFO) ---");
        // Queue is an interface, ArrayDeque is a common implementation
        Queue<String> queue = new ArrayDeque<>();

        // Offer (add) elements to the queue
        queue.offer("Person A"); // Add to the rear
        queue.offer("Person B");
        queue.offer("Person C");
        System.out.println("Queue after offers: " + queue);

        // Peek at the front element without removing it
        System.out.println("Peek (front element): " + queue.peek());
        System.out.println("Queue after peek: " + queue);

        // Poll (remove) elements from the queue
        System.out.println("Polled: " + queue.poll()); // Removes Person A
        System.out.println("Queue after first poll: " + queue);

        System.out.println("Polled: " + queue.poll()); // Removes Person B
        System.out.println("Queue after second poll: " + queue);

        System.out.println("Is queue empty? " + queue.isEmpty());

        // --- DEQUE (Double-Ended Queue) ---
        System.out.println("\n--- Deque Example ---");
        // ArrayDeque can be used as both a Stack and a Queue, or a true Deque
        Deque<Character> deque = new ArrayDeque<>();

        // Add to front
        deque.addFirst('C');
        deque.addFirst('B');
        deque.addFirst('A');
        System.out.println("Deque after addFirst: " + deque);

        // Add to rear
        deque.addLast('D');
        deque.addLast('E');
        System.out.println("Deque after addLast: " + deque);

        // Remove from front
        System.out.println("Removed from front: " + deque.removeFirst());
        // Remove from rear
        System.out.println("Removed from rear: " + deque.removeLast());
        System.out.println("Deque after removals: " + deque);
    }
}
