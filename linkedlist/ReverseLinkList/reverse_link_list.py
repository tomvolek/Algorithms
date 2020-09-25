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

    def printLinkList(self):
        print ("Current list of items in link list: ")
        temp = self.head 
        while (temp):
            print (temp.data)
            temp = temp.next

    def reverse_list(self):
       prev = Node
       current = self.head
       next = None
       while (current is not None):
           next = current.next
           current.next = prev 
           prev = current 
           current = next
       self.head = prev

llist = LinkedList()
llist.push(10)
llist.push(20)
llist.push(30)
llist.push(40)

llist.printLinkList()
llist.reverse_list()

print ("List after being reversed ")
llist.printLinkList()

