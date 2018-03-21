/* 
 * File:   DoubleLinedList.cpp
 * Author: tomvolek  
 * Insertion: O(1)
 * Search: O(n)
 * Deletion: O(n)
 * Fcuntion: Sorted Double Linked List, insertion() and printlist() 
 * Created on March 20, 2018, 11:59 PM
 */

#include <cstdlib>
#include <iostream>
#include <cstdlib>

using namespace std;

struct Node{
        int data;
         Node *next_ptr;
         Node *previous_ptr;
    } ;
    
class DoubleLinkedList {
      private: Node *head, *tail;
  
      // Constructor  
    public: DoubleLinkedList() {
        int value;
        head = NULL;
        tail = NULL;
    }
    
     void insert(int newdata){
     Node *newNode = new Node;
     newNode->data  = newdata ;
     newNode->next_ptr = NULL;
     newNode->previous_ptr = NULL; 
     
    if (head == NULL){
        head = newNode; 
        tail = newNode; 
        newNode = NULL; //free up the created newNode space 
        return;
        } 
    else {
        
        Node *currentNode = new Node;
        currentNode = head;
        while (currentNode != NULL  ){
            if (newNode->data <= currentNode->data){
                       // if (newNode->data < head->data){
                       if (currentNode->previous_ptr == NULL){
                           newNode->next_ptr = head;
                           head->previous_ptr = newNode;
                           cout << newNode->data << " Added to Head\n" ;
                           head = newNode;
                           return;
                       }
                       
                       //currentNode->previous_ptr = newNode; 
                       if (NULL != currentNode->previous_ptr)
                       {
                           currentNode->previous_ptr->next_ptr = newNode; 
                            newNode->next_ptr = currentNode;
                            newNode->previous_ptr = currentNode->previous_ptr; // needed ? 
                            cout << newNode->data << " Added to middle\n" ;
                            return; 
                       }

                   }
                   else { 
                       if (currentNode->next_ptr == NULL ) { //we have reached end of list, add to the end
                           currentNode->next_ptr = newNode; 
                           newNode->previous_ptr = currentNode;
                           tail = newNode;
                           cout << newNode->data << " Added to tail";
                           return ; 
                       }
                       else {
                           currentNode = currentNode->next_ptr ;
                         
                       }
                   }
            
        }
    
    
    }
            

    }  // End insert() 

    void printList(){
        Node *currentNode = head; 
           while (currentNode != NULL){
                cout << currentNode->data << " " ;
                currentNode = currentNode->next_ptr;
           }
           cout << "\n";
           
    } // End printList()

};  // End DoubleLinkedList 
    
 

int main(int argc, char** argv) {
    
           DoubleLinkedList DLL ;  //instantiate an empty  new Double linked list
           
            DLL.insert(6);
            DLL.printList();
            
            DLL.insert(3);
            DLL.printList();
            
            DLL.insert(5);
            DLL.printList();
            
            DLL.insert(2);
            DLL.printList();
            
            DLL.insert(7);
            DLL.printList();
            
            
            DLL.insert(8);
            DLL.printList();
            
            DLL.insert(10);
            DLL.printList();
            
            DLL.insert(7);
            DLL.printList();
            
            DLL.insert(7);
            DLL.printList();
            
            DLL.insert(5);
            DLL.printList();
    return 0;
}
