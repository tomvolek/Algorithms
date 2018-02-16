/*
 * Given a circular list of items, print each third member and
 * then remove them from the list. The next counter starts imedietly after
 * the member is removed. print till all the members are exusted.
 * ex: Array= ['1','2','3','4','5','6','7','8','9']
 * print => 3 6 9 4 8 5 2 7 1
 */
package circularcounter;

import java.util.*;

public class CircularCounter {

    public static void printArray(ArrayList<Integer> array_list, int skip){
    skip = skip -1; // we skip every three item, however list starts with index zero so , minus 1
    int index = 0;   // array index starts at 0
    int list_len = array_list.size();
    
    System.out.println("Array length: " +  Integer.toString(list_len));

    while (list_len > 0) {
        index = (skip + index) % list_len;
        System.out.println(array_list.get(index));
        array_list.remove(index);
        list_len -= 1;
                }
    } // printArray
    
    public static void main(String[] args) {
          int skip = 3; 
          ArrayList<Integer> arr = new ArrayList ();
          
          arr.add(1);
          arr.add(2);
          arr.add(3);
          arr.add(4);
          arr.add(5);
          arr.add(6);
          arr.add(7);
          arr.add(8);
          arr.add(9);
          arr.add(10);
          printArray(arr,skip);
    }
    
}
