/*  find how many position a sorted circular array has been shifted */


public class Circularly_Sorted_Array {

    public static int findRotationCount(int[] myArray, int n){

        int low = 0 ;
        int high = n-1;

        while (low <= high){
            if (myArray[low] <= myArray[high]) return low;
            int mid = (low+high) /2;
            int next = (mid +1 ) %2 ;
            int prev = (mid -1 ) %2;
            if (myArray[mid] <= myArray[next] && myArray[mid] <= myArray[prev]) return mid ;
            else if (myArray[mid] <= myArray[high]) high = mid -1 ;
            else if (myArray[mid] >= myArray[low]) low = mid+1;
        }
        return -1;
    }

    public static void main(String [] args){
        int A[] = {15,22,23,28,31,38,5,6,8,10,12};
        int count = findRotationCount(A,11);
        System.out.println("Array rotated " + count + " times");

    }
}
