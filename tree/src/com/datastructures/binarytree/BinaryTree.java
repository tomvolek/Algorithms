package com.datastructures.binarytree;

/*
BinaryTree :
* Search : O (logn)

*/

class Node {
    int data;
    Node left, right;

    public Node(int item) {
        data = item;
        left = right = null ;
    }
}

public class BinaryTree {
    Node root;

    public BinaryTree() {
        root = null;
    }

    private void insert (int value ){
        Node newNode = new Node (value) ;

        if (root == null) {
            root = newNode ;
        }
        else {
            Node current = root;
            Node parent;
            while (true){
                parent = current ;
                if (value < current.data) {
                    current = current.left;
                    if (current == null) {
                        parent.left = newNode;
                        return;
                    }
                }
                else if (value > current.data) {
                    current = current.right;
                    if (current == null){
                        parent.right = newNode;
                        return;
                    }
                } // else if
            }
        }  // else
    }  //end insert


    private void print_tree_inorder(Node local_root){
        Node current = local_root;
        if (current.left != null) {
            print_tree_inorder(current.left);
        }
        System.out.println(local_root.data);
        if (current.right != null){
            print_tree_inorder(current.right);
        }
    }
    private void print_tree_preorder(Node local_root){
        Node current = local_root;
        if (current == null)
            return;
        System.out.println(local_root.data);
        if(current.left != null){
            print_tree_preorder(current.left);
        }
        if(current.right!= null){
            print_tree_preorder(current.right);
        }
    }

    private void print_tree_postorder(Node local_root){
        Node current = local_root;
        if (current.right != null){
            print_tree_postorder(current.right);
        }
        System.out.println(local_root.data);
        if (current.left != null) {
            print_tree_postorder(current.left);
        }

    }




    public static void main(String[] args) {
        BinaryTree tree = new BinaryTree();
        tree.root = new Node(1);
        tree.insert(5);
        tree.insert(4);
        tree.insert(2);
        tree.insert(7);
        System.out.println("Inorder output:");
        tree.print_tree_inorder(tree.root);
        System.out.println("Preorder output: ");
        tree.print_tree_preorder(tree.root);
        System.out.println("Post order output:");
        tree.print_tree_postorder(tree.root);



    }

    }
