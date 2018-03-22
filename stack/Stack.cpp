
/*
* Author:tomvolek  
* Insert: O(1)
* Deletion: O(1)
* Search: O(n)
* Access: O (n) 
*/

#include <cstdlib>
#include <iostream>

using namespace std;
#define STACKSIZE 1000

 class Stack {
    int top ;  // top of stack 
    public:  int stackArray[];   
      
    // Stack Array constructor 
    Stack(){
        top = -1; 
    }
    
    // Add a new item to top of the stack 
    bool push(int newValue) {     
        if (top >= STACKSIZE ){
            cout << "Stack is full...Can not insert  " ;
            return false; 
        }
        else {
            this->stackArray[++top] = newValue; 
            return true;
        }
    }
    
    // Return top of the stack without removing the item
    int peek() {
        return this->stackArray[top];
    } 
    
    // Remove an item from top of the stack 
    int pop(){
        if (top < 0 ) { 
            cout << "Stack underflow: No items to remove. "; 
            return -1;
        }
        else { int x =  this->stackArray[top--];
          return x;
        }
    }
 };
   
    int main(int argc, char** argv) {
        Stack theStack;
             
        theStack.push(1);
        theStack.push(2);
        theStack.push(3);
       
        cout << " Top of stack is ==> " <<  theStack.peek() << "\n";
        cout << "Top element: = >  " <<  theStack.pop() <<  " was poped\n";
 
        theStack.push(4);
        theStack.push(5);
        
        cout << " Top of stack is ==> " << theStack.peek() << "\n";
        cout << "Top element: = >  " << theStack.pop() << " was poped\n";
        cout << " Top of stack is ==> " << theStack.peek() << "\n";
    return 0;
}
   

