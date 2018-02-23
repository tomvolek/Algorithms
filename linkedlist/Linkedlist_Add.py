/*  Create a link list and add items to the head or middle or end of the Linkedlist. */ 

class Node: 
    def __init__(self, data, next_node=None, prev_node=None)):
	self.data = data 
	self.next_none = next_none
        self.prev_none = prev_none


class LinkList:
        /* LinkedList class constructor */ 
	def __init__(self): 
                self.length = 0 
		self.head = None
		self.tail = None 
	

