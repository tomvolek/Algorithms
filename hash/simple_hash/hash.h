/* 
 * File:   hash.h
 * Author: tomvolek
 * Search: O(1) 
 * Add: O(1) 
 * 
 * Created on April 6, 2018, 8:24 PM
 */ 


#include <cstdlib>
#include <iostream>
#include <string>

using namespace std;

#ifndef HASH_H
#define HASH_H


class myhash {
    private : 
        static const int tableSize= 40;
        
        struct item {
            string name; 
            string drink;
            item *next; 
        };
        
        item * HashTable[tableSize];
        
    public: 
        myhash();
        int Hash(string key);
        void AddItem(string name, string drink);
        int NumberOfItemsInIndex(int item);
        void PrintTable(); 
};



#endif /* HASH_H */

