// Count number of elements in a link list 


class Node { 
	int data; 
	Node next; 
	Node (int d){
		data = d ; 
		next = null; 
	}
}

public class LinkListLength {

	Node head;  // dead of list 
	
	public void push(int new_data ) {
		Node new_node = new Node(new_data);
		new_node.next = head; 
		head = new_node; 
	}
	
	public int getCount() { 
		Node temp = head; 
		int count = 0; 
		while (temp != null ) {
			count++; 
			temp = temp.next; 
		}
		return count; 
	}
	
	public static void main(String [] args) {
		LinkListLength linklist = new LinkListLength();
		linklist.push(1);
		linklist.push(3);
		linklist.push(1);
		linklist.push(2);
		linklist.push(1);
		System.out.println("count of nodes is: " + linklist.getCount());
		
		
	}
	
	
	
}
