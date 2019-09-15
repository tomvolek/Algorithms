"""
Q1 : Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
between 2000 and 3200 (both included).
The numbers obtained should be printed in a comma-separated sequence on a single line.
"""
l = []
for x in range(2000,3200):
    if (x%7 == 0 ) and (x%5 != 0):
        l.append(str(x))
print ("Question1:")
print (','.join(l))        


"""
Q2: Write a program which can compute the factorial of a given numbers.
The results should be printed in a comma-separated sequence on a single line.
Suppose the following input is supplied to the program:
8
Then, the output should be:
40320
"""
def fact(number):
    if number == 0: 
        return 1
    return number * fact(number-1)    
x = 8
print("factorial of x = ", fact(x))   


"""
Q3: With a given integral number n, write a program to generate a dictionary that contains (i, i*i) such that
is an integral number between 1 and n (both included). and then the program should print the dictionary.
Suppose the following input is supplied to the program:
8
Then, the output should be:
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}
"""

integral_dict = {}
integral_number = 8 
for i in range(1,integral_number): 
    integral_dict[i] = i*i
print (integral_dict)   


"""
Q5: Define a class which has at least two methods:
getString: to get a string from console input
printString: to print the string in upper case.
Also please include simple test function to test the class methods.

"""
class inputclass: 
        def __init__(self): 
                self.string=''
        def getString(self):
                print ("Input value for method getString : ")
                self.string = input()
                
        def printString(self): 
                print ("inputed value using printString methond: ",self.string)

myobj = inputclass()
myobj.getString()
myobj.printString()


"""
Question 6  Level 2
Question: Write a program that calculates and prints the value according to the given formula:
Q = Square root of [(2 * C * D)/H]
Following are the fixed values of C and H:
C is 50. H is 30.
D is the variable whose values should be input to your program in a comma-separated sequence.
Example:
Let us assume the following comma separated input sequence is given to the program: 100,150,180
The output of the program should be: 18,22,24

Hints:
If the output received is in decimal form, it should be rounded off to its nearest value (for example, if the output received is 26.0, it should be printed as 26)
In case of input data being supplied to the question, it should be assumed to be a console input. 
"""

import math
C = 50 
H = 30
value = []
print ("Input values ")
items = [x for x in input().split(' ')]
for d in items: 
        value.append( str(int(round(math.sqrt(2*C*float(d)/H )))))

print (','.join(value))