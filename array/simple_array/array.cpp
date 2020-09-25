#include <iostream>
#include <vector>
#include <string>
#include <sstream>

using namespace std;
using std::cout;
using std::cin;
using std::endl;


int main()
{
int num1,num2,sum;
string mystr;

cout << "inout string" << endl;
getline(cin,mystr);
cout << " inoutted string is = " << mystr << endl;


num1= 3; num2=2;
sum= num1+num2;

cout << " Sum of nume1,num2=" << sum << endl ;


   vector<string> msg {"Hello", "C++", "World", "from", "VS Code", "and the C++ extension!"};
   vector<string> msg2; 

   for (const string& word : msg)
   {
      cout << word << " ";
      
   }
   msg2  = msg;
   for (int i; i < msg2.size(); i++){
       cout << msg2[i] << "        " ; 
   }
   
   cout << endl;

   cout << "input new sum " << endl; 
    cin.get() >> sum;
   cout << " new sum is = " << sum << endl;

}