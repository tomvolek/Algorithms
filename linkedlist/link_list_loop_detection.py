# detect if a loop in a link list. 

class Node: 
    def __init__ (self,data):
        self.data = data
        self.next = None #init next pointer to next object as null

class LinkedList: 

    def __init__(self):
        self.head = None

    def push(self,new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def detect_loop(self):
        s = set()
        current_node = self.head
        while(current_node):
            # If we have already has 
             # this node in hashmap it 
             # means their is a cycle 
             # (Because you we encountering 
             # the node second time).  
            if (current_node in s):
                return current_node.data

            #add the new node if we are seeing it for the first time.
            s.add(current_node)
            current_node = current_node.next

        return False

linklist = LinkedList()
linklist.push(10)
linklist.push(5)
linklist.push(20)
linklist.push(15)

    # create a loop 
linklist.head.next.next.next.next = linklist.head

if(linklist.detect_loop() != 0 ):
    print ("Loop detected")
else: 
    print (" No loop detected ")    