
/* 
 * File:   hash.cpp
 * Author: tomvolek
 * Search: O(1) 
 * Add: O(1) 
 * 
 * Created on April 6, 2018, 8:24 PM
 */

#include <cstdlib>
#include <iostream> 
#include <string>
#include  "hash.h"

using namespace std;

myhash::myhash()
{
    for (int i = 0; i < tableSize; ++i){
        HashTable[i] = new item; 
        HashTable[i]->name = "empty";
        HashTable[i]->drink="empty";
        HashTable[i]->next = NULL;
    }
}

void myhash::AddItem(string name, string drink)
{
    int index = Hash (name) ;
    
    if (HashTable[index]->name == "empty")
    {
        HashTable[index]->name= name ;
        HashTable[index]->drink=drink;
    }
    else {
        item * Ptr = HashTable[index];
        item * n = new item;
        n->name= name;
        n-> drink = drink;
        n->next = NULL;
        while (Ptr -> next != NULL )
        {
            Ptr = Ptr-> next;
        }
        Ptr->next = n;
    }
}

// return number of of items in a hash bucket
int myhash::NumberOfItemsInIndex(int index)
{
    int count= 0 ; 
    if (HashTable[index]->name == "empty")
    {
        return count ; 
    }
    else { 
        count ++ ; 
        item * Ptr = HashTable[index];
        while (Ptr != NULL){
            count++ ; 
            Ptr = Ptr->next;
        }
    }
    return count;
}

void myhash::PrintTable()
{
    int number ; 
    for (int i=0; i < tableSize;++i){
        number = NumberOfItemsInIndex(i);
        cout << "---------\n";
        cout << "index =" << i << endl;
        cout << HashTable[i]-> name << endl;
        cout << HashTable[i]-> drink << endl;
        cout << " # of items =" << number << endl;
        cout << "----------------\n";
    }
}

//Hash function to create our hash value using a modulo 
 int myhash::Hash(string key)
 {
     int hash = 0 ;
     int index; 
     for (int i=0; i < key.length(); ++i)
     {
         hash = hash + (int)key[i];
         cout << "hash=" << hash << endl;
     }
     
     index = hash % tableSize; 
 
     return index; 
 }