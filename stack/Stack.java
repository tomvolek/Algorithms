/*
* Author:tomvolek  
* Insert: O(1)
* Deleton: O(1)
* Search: O(n)
* Acess: O (n) 
*/
  
package stack;

public class Stack {
    private final  int STACKSIZE ;
    private final  int stackArray[];   
    private  int top ;  // top of stack 
    
    // Stack Array constructor 
    public Stack(int s){
        STACKSIZE = s; 
         this.stackArray = new int [STACKSIZE];
         top = -1; 
    }
    
    // Add a new item to top of the stack 
    public boolean push(int newValue) {
        
        if (top >= this.STACKSIZE ){
            System.out.printf("Stack is full...Can not insert  ");
            return false; 
        }
        else {
            this.stackArray[++top] = newValue; 
            return true;
        }
    }
    
    // Return top of the stack without removing the item
    public int peek() {
        return this.stackArray[top];
    } 
    
    // Remove an item from top of the stack 
    public int pop(){
        if (top < 0 ) { 
            System.out.printf("Stack underflow: No items to remove. "); 
            return -1;
        }
        else { int x =  this.stackArray[top--];
          return x;
        }
    }
    
   
    public static void main(String[] args) {
        // TODO code application logic here
        Stack theStack = new Stack(1000);
        theStack.push(1);
        theStack.push(2);
        theStack.push(3);
       
        System.out.println(" Top of stack is ==> " + theStack.peek() );
        System.out.println("Top element: = >  " + theStack.pop() + " was poped");
        
        
        theStack.push(4);
        theStack.push(5);
        
        System.out.println(" Top of stack is ==> " + theStack.peek());
        System.out.println("Top element: = >  " + theStack.pop() + " was poped");
    }
}
