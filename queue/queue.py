"""
 * File:   queue.py
 * Author: tomvolek
 * Insert: O (1)
 * Delete: O (1)
 * Peek : O (1)
 * Search : O(n)
 * Created on March 22, 2018, 6:46 PM
 """

# Primary Node object
class Node:
    def __init__(self, item:None, nextNode= None):
        self.item = item
        self.nextNode = nextNode

    def get_data(self):
        return self.item

    def get_next(self):
        return  self.nextNode

    def set_next(self,new_node):
        self.nextNode = new_node

class Queue:
    def __init__(self, head=None):
        self.head = head

    def enqueue(self,newValue):
        newNode = Node(newValue)
        current = self.head
        if self.head is None:
            self.head = newNode
            print('Item enqueued:',newNode.item)
        else:
            while current.get_next():
                current = current.get_next()
            current.set_next(newNode)
            print('Item enqueued:' , newNode.item)

    def dequeue(self):
        current = self.head
        if current != None:
            self.head = current.get_next()
        else: print ("Queue is empty")

    def display(self):
        current = self.head

        self.temp = []
        while current:
            self.temp.append(current.get_data())
            current = current.get_next()
        print(self.temp)

def main():
    queue = Queue()

    queue.enqueue(5)
    queue.enqueue(6)
    queue.enqueue(7)
    queue.enqueue(8)

    queue.display()
    queue.dequeue()
    queue.display()
    queue.dequeue()
    queue.display()
    queue.dequeue()
    queue.display()
    queue.dequeue()
    queue.display()
    queue.dequeue()
    queue.display()

if __name__ == "__main__":
    main()

