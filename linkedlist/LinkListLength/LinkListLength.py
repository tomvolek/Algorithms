# count number of elements in a link List

class Node: 
    def __init__ (self,data):
        self.data = data
        self.next = None #init next pointer to next object as null

class LinkListLength:
    # Function to init head 
    def __init__(self):
        self.head = None 

    def push(self,new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def getCount(self): 
        temp = self.head #init temp 
        count = 0 
        while (temp):
            count += 1
            temp = temp.next
        return count

if __name__ == '__main__':
    linklist = LinkListLength()
    linklist.push(1)
    linklist.push(3)
    linklist.push(1)
    linklist.push(2)
    linklist.push(1)
    print ("Count of nodes is :",linklist.getCount()) 

