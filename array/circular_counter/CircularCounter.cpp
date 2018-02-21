/*
* Given a circular list of items, print each third member and
* then remove them from the list. The next counter starts imedietly after
* the member is removed. print till all the members are exusted.
* ex: Array= ['1','2','3','4','5','6','7','8','9']
* print => 3 6 9 4 8 5 2 7 1
* File:   CircularCounter.cpp
* Author: tajayebi
*/

#include <cstdlib>
#include <iostream>
#include <vector>
using namespace std;

void circular_array_counter(vector <int>& array_list, int skip)
    {   
     // we skip every three item, however list starts with index zero so , minus 1
    int index = 0 ;  // array index starts at 0
    skip = skip -1 ; 
    int list_len = array_list.size();

    while (list_len >  0 )
        {
        index = (skip +index)  % list_len ; 
        cout << "index = " << index << endl;
        cout << array_list[index] << " " << endl;      
        array_list.erase (array_list.begin()+index);
        list_len -= 1 ; 
    }
} 


int main(int argc, char** argv) {
    static const int arr[] = {1,2,3,4,5,6,7,8,9};
    vector<int> array (arr,arr+sizeof(arr)/sizeof(arr[0]));
   
    circular_array_counter(array,3);
   
    return 0;
}

