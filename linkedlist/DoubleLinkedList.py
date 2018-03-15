"""  Create a link list and add items to the head or middle or end of the Linkedlist.

 * Double linked list in Java
 * Insertion:  O(1)
 * Search: O(1)
 * Deletion: O(1)
 * @author tajayebi
 """

class Node(object):
    #__slots__ = ['data','next_ptr','prev_ptr']  # Tell python not to use dictionary for instance variables
    def __init__(self, data: object, next_node: object = None, prev_node: object = None) -> object:
        self.data = data
        self.next_ptr = next_node
        self.prev_ptr = prev_node

    def getData(self):
        return self.data

    def setData(self, data):
        self.data = data

    def getNextNode(self):
        return self.next_ptr

    def setNextNode(self, Node):
        self.next_ptr = Node

    def getPrevNode(self):
        return self.prev_ptr

    def setPrevNod(self, Node):
        self.prev_ptr = Node


class LinkList:
    """ Lx$inkedList class constructor, vaiables with underscore are private class variables """

    def __init__(self, head=None, tail=None):
        self._size = 0
        self._data = 0
        self._head = head
        self._tail = tail

    def getSize(self):
        return self._size

    def incrementSize(self):
        self._size += 1

    def isEmpty(self):
        """ check to see if the list empty """
        return self._size <= 0

    def addNode(self, newValue):
        newNode = Node(newValue)

        currentNode = self._head
        # if LinkedList is empty
        if (self.getSize() <= 0):
            self._head = newNode
            self._tail = newNode
            self.incrementSize()
            print( newNode.data," Added first item")
            return True

        while currentNode is not None:
              if newNode.data <= currentNode.data:
                  if currentNode.prev_ptr is None:
                      newNode.next_ptr = self._head
                      self._head.previous_ptr = newNode
                      print (newNode.data," Added to Head")
                      self._head = newNode;
                      self.incrementSize()
                      return True

                  if  currentNode.prev_ptr is not None:

                      currentNode.prev_ptr = newNode // bug

                      newNode.next_ptr = currentNode
                      newNode.prev_ptr = currentNode.prev_ptr
                      self.incrementSize()
                      print(newNode.data , " Added to middle")
                      return True
              else:
                  if currentNode.next_ptr is None:
                      currentNode.next_ptr= newNode
                      newNode.previous_ptr = currentNode
                      self._tail = newNode
                      self.incrementSize()
                      print(newNode.data , " Added to tail")
                      return True

                  else:
                      currentNode = currentNode.next_ptr



    def removeNode(self, node_value):
        previousNode = None
        currentNode = self.head
        while currentNode is not None:
            if currentNode.getData() == node_value:
                if previousNode:
                    previousNode.setNextNode(currentNode.getNextNode())
                else:
                    self.head = currentNode.getNextNode()
                return True
            previouNode = currentNode
            currentNode = currentNode.getNextNode()
            return False

    def printList(self):
        currentNode = self._head
        print('Total number of items in the LinkedList:', self.getSize())
        print('Item on the list :')
        while currentNode is not None:
            print(currentNode.getData())
            currentNode = currentNode.next_ptr


def main():
    DLL = LinkList()
    DLL.addNode(6)
    DLL.addNode(2)
    DLL.addNode(3)
    DLL.addNode(8)
    DLL.addNode(4)

    DLL.printList()


if __name__ == "__main__":
    main()
