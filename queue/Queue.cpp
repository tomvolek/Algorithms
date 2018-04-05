
/* 
 * File:   queue.cpp
 * Author: tomvolek
 * Insert: O (1) 
 * Delete: O (1) 
 * Peek : O (1) 
 * Search : O(n) 
 * Created on March 22, 2018, 6:46 PM
 */

#include <iostream>
using namespace std;

//Primary queue object 
template <class T> 
class Queue 
{
    private : 
        struct Node { 
            T *item ;
            Node *nextNode;  
        } *front,*rear;
       
    public: 
        Queue();
        ~Queue();
        void enqueue(T *item);
        void display();
        T* dequeue();
        
};
    
// constructor
template <class T>
Queue <T>:: Queue() { 
        front = NULL; 
        rear = NULL ; 
} 
    
    // destructor  
template <class T>
Queue <T>::~Queue(){
        Node *p,*q;
        p = rear;
        if (p == NULL ) return; 
        while (p) {
            q = p->nextNode;
            delete p;
            p = q;
        } 
        delete front;
        delete rear;
}
        
template <class T > 
void Queue <T>:: enqueue(T *item) 
{
   
            Node *newNode = new Node();
            cout << "in enqueue: " << *item;
            newNode->item = item; 
            newNode->nextNode = NULL ;

            if (front == NULL ) {
                front = newNode; 
            } else {
                rear->nextNode = newNode;
            }
            rear = newNode; 
            display();
} 

template <class T> 
T* Queue <T>:: dequeue() {
        Node *temp;
        T *item;
        if (front == 0 ){
            cout << "Queue underflow" << endl ;
            return 0;
        }
        else {
            temp = front;
            cout << "Element deleted: "<< *temp->item << endl ;
            front = front->nextNode;
            item = temp->item;
            }
        free (temp);
        return item;
        
} // end dequeue()


//  Traversing the queue
 
template <class T>
void Queue <T>:: display()
{       
    Node *ptr; 
    ptr = front;
    if (front == NULL)
        cout<<"Queue is empty"<<endl;
    else
    {
        cout<<"Queue elements :"<<endl;
        while (ptr != NULL)
        {
            cout<<*ptr->item<<" ";
            ptr = ptr->nextNode;
        }
        cout<<endl;
    }
}
 

  int main(int argc, char** argv) {

    Queue <int> queue;
  
    int choice, item;
    
    int input [] = {};
   
    while (1)
    {
        cout<<"\n-------------"<<endl;
        cout<<"Operations on Queue"<<endl;
        cout<<"\n-------------"<<endl;
        cout<<"1.Insert Element into the Queue"<<endl;
        cout<<"2.Delete Element from the Queue"<<endl;
        cout<<"3.Traverse the Queue"<<endl;
        cout<<"4.Quit"<<endl;
        cout<<"Enter your Choice: ";
        cin>>choice;
        switch(choice)
        {
        case 1: {
            cout<<"Enter value to be inserted into the queue: ";
            cin>>item;
            // client owns the supplied data
            int *item_m = (int*) malloc(1 * sizeof(int));
            *item_m = item;
            queue.enqueue(item_m);
            
            break;
        }
        case 2:
            queue.dequeue ();
            break;
        case 3:
            queue.display();
            break;
        case 4:
            exit(1);
            break;
        default:
            cout<<"Wrong Choice"<<endl;
        }
    }
 

    return 0 ;
    
 }  // End main 
 
