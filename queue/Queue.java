/**
 *
 * Function: FIFO queue data structure 
 * Search : O (n) 
 * Access: O (n) 
 * Insertion: O (1)
 * Deletion: O(1) 
 * 
 */


package queue;
import java.util.NoSuchElementException;


public class Queue<Item> {
    
    public class Node {
        private Item item ;
        private Node nextNode;
    }
    
    private Node front; // head of queue / beginigng 
    private Node rear;  // end of queue 
    
    // constructor 
    public Queue() { 
        front = null; 
        rear = null ; 
    } 
      
 public void enqueue(Item item) {
    Node newNode = new Node(); 
    newNode.item = item; 
    newNode.nextNode = null;
    if (front == null ) {
        front = newNode;
        System.out.println("Item enqueded:" + newNode.item);
    }
    else {
        rear.nextNode = newNode;
        System.out.println("Item enqueded:" + newNode.item);
    }
    rear = newNode;
 }
 
 public void  dequeue() {
     
    if (front == null ){
        throw new NoSuchElementException("Queue underflow");
    }
    else {
        Node temp ; 
        temp = front ; 
        System.out.println("Item enqueded:" + temp.item);
        front = front.nextNode;
    }
 }
 
 public void display() {
     
    Node ptr ;
    ptr = front;
    if (front == null)
        System.out.println("Queue is empty");
    else
    {
        System.out.println("Queue elements : ");
        while (ptr != null)
        {
            System.out.println(ptr.item);
            ptr = ptr.nextNode;
        }
        System.out.println("\n");
    }
 }
 
 
 public static void main(String[] args ){

 Queue<Integer> queue = new Queue <>(); 
 
 queue.enqueue(5);
 queue.enqueue(6);
 queue.enqueue(7);
 queue.enqueue(8);
 
 queue.display();
 
 queue.dequeue();
 queue.dequeue();

 queue.display();
 
 }  // main 

} // end Queue class 
   


