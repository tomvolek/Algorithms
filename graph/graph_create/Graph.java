/*
 *   File : Graph.java 
 *   Search:  O(1) 
 *   Delete:  O(1) 
 *   Add :  O(V**2) 
 */


package graph;
import java.util.LinkedList;

public class Graph {
    
    int V ; 
    LinkedList<Integer> adjListArray[];
    
    //constructor 
    public Graph(int V){
        this.V = V; 
        
        // define the size of array as number of verticies 
        adjListArray = new  LinkedList[V];
        
        // Create a new list for each vertix 
        // such that adjacent nodes can be stored.
        for (int i=0; i <V; i++){
            adjListArray[i] = new LinkedList<>();
        }
    }
    
    static void addEdge(Graph graph, int src, int dest){
        // add an edge from src to dest. 
        graph.adjListArray[src].addFirst(dest);
        
        // Since graph is undirected , add and edge from destination to source.
        graph.adjListArray[dest].addFirst(src);
        
    }
    
    static void printGraph(Graph graph){
        for (int vertices = 0; vertices < graph.V; vertices++  ){
            
        System.out.println("Adjacent list of vertecies " + vertices);
        System.out.print("head"); 
            for (Integer pCrawl: graph.adjListArray[vertices]){
                System.out.print(" -> "+ pCrawl);
            }
        System.out.println("\n");
        }
    }  // printGraph
    
    public static void main(String[] args) {
     
        int V = 6 ; 
        
        Graph graph = new Graph(V) ;
        addEdge(graph, 0, 1);
        addEdge(graph, 0, 4);
        addEdge(graph, 1, 2);
        addEdge(graph, 1, 3);
        addEdge(graph, 1, 4);
        addEdge(graph, 2, 3);
        addEdge(graph, 3, 4);
        addEdge(graph, 1, 5);
        addEdge(graph, 5, 0);
        addEdge(graph, 5, 1);
        addEdge(graph, 5, 2);
        addEdge(graph, 5, 3);
        addEdge(graph, 5, 4);
       
        
       
        printGraph(graph);
    }
} // End Graph 