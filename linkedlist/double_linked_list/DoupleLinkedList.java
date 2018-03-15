/*
 * Double linked list in Java 
 * Insertion:  O(1) 
 * Search: O(1)
 * Deletion: O(1)
 * @author tajayebi
 */
package douplelinkedlist;
    
    // class identifying a single Node or Link 
    class Node {
          public int data ;
          public Node next_ptr;
          public Node previous_ptr; 
          
          public Node(int d) //constructor 
            { this.data = d; }
          
          public void printNode()  // Print Node 
            { System.out.print(data + " ");  }   
          
          public int getNode(){ return this.data;}
          
          public void setNode(int newdata) { this.data = newdata;}
          
    }
  
   // main class defining          
   public class DoupleLinkedList {
    
       private Node head; 
       private Node tail;
       
       public DoupleLinkedList()
            {
               head = null ; 
               tail = null; 
            } 
       
       public boolean isEmpty()
            {return head==null;}
       
       
       public void insertFirst(int newdata){
           Node newNode = new Node(newdata);
           if (isEmpty())
              {  head = newNode;
              System.out.println(head.data + "is added to the Head ");
              }
           else {
               head.previous_ptr = newNode;  //point current Heads previous ptr to point to the newNode
               newNode.next_ptr = head;   // point the new node next pointer to 
               head = newNode;   // make head of the list to be the newNode
               tail = newNode;
           
           } 
       }
       
       public boolean insert(int newdata) {
           Node newNode = new Node(newdata);
           Node currentNode =  head;
         
           // System.out.println("outside while loop insert 1");
           while ( currentNode != null ) {
                   if (newNode.data <= currentNode.data){
                       // if (newNode.data < head.data){
                       if (currentNode.previous_ptr == null){
                           newNode.next_ptr = head;
                           head.previous_ptr = newNode;
                           System.out.println(newNode.data + " Added to Head");
                           head = newNode;
                           return true;
                       }
                       
                       //currentNode.previous_ptr = newNode; 
                       if (null != currentNode.previous_ptr)
                       {
                           currentNode.previous_ptr.next_ptr = newNode; 
                            newNode.next_ptr = currentNode;
                            newNode.previous_ptr = currentNode.previous_ptr; // needed ? 
                            System.out.println(newNode.data +" Added to middle");
                            return true; 
                       }

                   }
                   else { 
                       if (currentNode.next_ptr == null ) { //we haev reached end of list, add to the end
                           currentNode.next_ptr = newNode; 
                           newNode.previous_ptr = currentNode;
                           tail = newNode;
                           System.out.println(newNode.data + " Added to tail");
                           return true; 
                       }
                       else {
                           currentNode = currentNode.next_ptr ;
                         
                       }
                   }
           }  // End while newNode.data > 0 
           return true;
          
       } // End insert()
       
       public void printList()
       {
           Node currentNode = head; 
           while (currentNode != null){
                System.out.print(currentNode.data + " ");
                currentNode = currentNode.next_ptr;
           }
           System.out.println();
        }     
   }   
       
    class DoubleLinkedListApp
    {
        public static void main(String[] args) 
        {
            DoupleLinkedList DLL = new DoupleLinkedList();  // instantiate an empty  new Double linked list
            
            DLL.insertFirst(6);
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
           
            
          
            
     }
    }
