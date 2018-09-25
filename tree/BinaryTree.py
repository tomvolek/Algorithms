"""
Program: Binarry Tree with Post Order Traversal
Search:  O (log(n) 
 """

class Node: 
    def __init__(self,value):
        self.left = None 
        self.right = None 
        self.data = value 
        
    def insert(self,value):
        """ Insert new node with data 
        @param data node dat object to insert
        """
        if self.data: 
            if value <= self.data:
                if self.left is None: 
                   self.left = Node(value)
                else: 
                   self.left.insert(value)
            elif value > self.data: 
                 if self.right is None: 
                    self.right = Node(value)
                 else: 
                     self.right.insert(value)    
        else: 
            self.data = value



    def Print_Tree_Inorder(self): 
        """ Print tree content inorder """
        if self.left:
            self.left.Print_Tree_Inorder()
        print (self.data)
        if self.right: 
            self.right.Print_Tree_Inorder()

    def Print_Tree_Postorder(self): 
        """  Print the tree in Postorder """        
        if self.left: 
            self.left.Print_Tree_Postorder()
        if self.right: 
            self.right.Print_Tree_Postorder()
        print(self.data)

    def Print_Tree_Preorder(self): 
        """  Print the tree in Postorder """  
        if self.data: 
            print(self.data)      
        if self.left: 
            self.left.Print_Tree_Postorder()
        if self.right: 
            self.right.Print_Tree_Postorder()
        



    def search_tree(self,data,parent=None):
        """
        Look up node data in the tree 
        @param parent node's parent 
        @returns node and node's parent
        """
        if data < self.data: 
            if self.left is None: 
                return None, None
            return self.left.search_tree(data,self)
        elif data > self.data: 
            if self.right is None: 
                return None, None
            return self.right.search_tree(data,self) 
        else: return self, parent

    def delete(self,data): 
        """ Delete node from tree """
        #@param data nodes content to delete   
        node,parent = self.search_tree(data)

        if node is not None : 
            children_count = node.children_count()
        if children_count == 0 : 
            # node has no childredn just remove it 
            if parent: 
                if parent.left is node: 
                    parent.left = None
                else: 
                    parent.right = None
                del node       
            else : 
                self.data = None 
        elif children_count == 1 : 
            # if node has 1 child replace node with its child
            if node.left:
                n = node.left
            else: 
                n = node.right
            if parent: 
                if parent.left is node: 
                    parent.left = n 
                else: 
                    parent.right = n 
            else: 
                self.left = n.left 
                self.right = n.right 
                self.data = n.data

        else: 
            # if node has two children 
            parent = none 
            sucessor = node.right 
            while sucessor.left: 
                parent = sucessor
                sucessor = sucessor.left 
            #replace node  data by its successor data 
            node.data = sucessor.data
            #fix sucessors parent child 
            if (parent.left == sucessor): 
                parent.left = sucessor.right
            else: 
                parent.right = sucessor.right 
                    
    def children_count(self): 
        """ return number of cildresns """
        cnt = 0 
        if self.left: 
            cnt += 1
        if self.right: 
            cnt += 1
        return cnt   


root = Node(8)
root.insert(3)
root.insert(10)
root.insert(1)
#root.Print_Tree_Inorder()
root.insert(4)
root.insert(7)
root.insert(14)
root.insert(13)
root.insert(7)

print("Inorder print of the tree : " )
root.Print_Tree_Inorder()

print("Postorder print of the tree : " )
root.Print_Tree_Postorder()

print("Preorder  print of the tree : " )
root.Print_Tree_Preorder()

node, parent = root.search_tree(13)
print("Node data :",node.data)
