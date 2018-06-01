/*
 *  Rotate an array to the right for K number of spots 
 * Space O(1), Time O(n) 
 */

package rotatearray;
import java.util.Arrays;
import java.util.Scanner;

public class RotateArray {

    public static void main(String[] args) {
        Scanner reader = new Scanner(System.in);  // Reading from System.in        
        System.out.println("Input Array Length:");
        
        int order ;  // order of rotation
        int array_length = reader.nextInt(); // length of our array 
        int [] array_num = new int[array_length];  // array of numbers
        int[] results = new int[array_length];
        
        
        System.out.println("Input array element:  ");
        for (int i=0; i < array_length; i++){
          array_num[i] = reader.nextInt();
        }
       
        System.out.println("Input how many positions to rotate:  ");
        order = reader.nextInt(); 
        reader.close();
                
                int k = 0; 
		for (int i = array_length , j = 0; j < array_length;  j++, i--) {
			if (j < order ) {
                            results[order-j-1] = array_num[i -1];
                            }
			if ( j >= order ) {
                            results[j] = array_num[k];
                            k++;
			}
		}                
		System.out.println(Arrays.toString(results));
    }
}

