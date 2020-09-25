import java.util.*;

public class LinkListLoopDetect {
	
	static class Node { 
		int data; 
		Node next; 
		Node (int d ){
			data = d; 
			next = null; 
		}
	}
	
	static Node head; 
	
	
	static public void push(int new_data) {
		Node new_node = new Node(new_data );
		new_node.next = head;
		head = new_node; 
	}
	
	static boolean detect_loop(Node h) {
		HashSet<Node> s = new HashSet<Node>(); 
		while (h != null) { 
			if (s.contains(h)) {
				return true ; 
			}
			s.add(h);
			h = h.next;
		
		}
		return false ;
	}
	
	public static void main(String [] args) {
		
		LinkListLoopDetect LinkList = new LinkListLoopDetect(); 
		
		LinkList.push(20);
		LinkList.push(4);
		LinkList.push(15);
		LinkList.push(10);
		
		/*Create loop for testing */
		LinkList.head.next.next.next.next = LinkList.head; 
   
        if (detect_loop(head) ) 
            System.out.println("Loop found"); 
        else
            System.out.println("No Loop"); 
		
		
	}
	
	
	
	
	
}
