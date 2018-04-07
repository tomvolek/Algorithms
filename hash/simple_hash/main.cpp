
/* 
 * File:   main.cpp
 * Author: tomvolek
 * Search: O(1) 
 * Add: O(1) 
 * 
 * Created on April 6, 2018, 8:24 PM
 */

#include <cstdlib>
#include <iostream> 
#include <string>

#include "hash.h"

using namespace std;

int main(int argc, char** argv) {
    int index,count; 
    myhash hashObj;
    
   
    //index = hashObj.Hash("Paula") ;
    
    //cout << "index = " << index << endl;
    
    hashObj.AddItem("Tom","beer");
    hashObj.AddItem("John","wine");
    hashObj.AddItem("Tina","water");
    hashObj.AddItem("Paul","Foo");
    hashObj.AddItem("Kim","wine");
    hashObj.AddItem("Emma","k2");
    hashObj.AddItem("Hamid","wine");   
    hashObj.AddItem("Suzie","wine");
    hashObj.AddItem("Suzie","Water");
  
     
   count = hashObj.NumberOfItemsInIndex(1);
   cout << "count of items in bucket 1 ="<< count<< endl;
  
    
   hashObj.PrintTable();
   
   
   
   
   
}

