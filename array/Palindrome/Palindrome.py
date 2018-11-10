import sys 
import re
import os 

def recursive_function(x,y): 
    if (x%2== 0):
        print (x) 
    else: 
        y = y+3
        return recursive_function(x-y,y)    

print (recursive_function(10,3))

def op(arg1,arg2): 
    return arg1+arg2

args= []
args.append(3)
args.append(5)
print(op(*args))

# Matrix 
M=[[1,2,3,10],[4,5,6],[7,8,9]]
print (len(M[0]))

#Tower of Hanoi 
def TOH( n, A,  B, C):
    if (n > 0 ): 
        TOH(n-1, A ,C,B)
        print ("Moved a Disc from %d to %d", A, C)
        TOH(n-1,B,A,C)

TOH(3,1,2,3)

text_to_search = '''
abcdefghijklmnopqrstuvwxz
ABCDEFGHIJKLMNOPQRSTUVWXZ
1234567890

Ha  HaHa 
Metacharacters (need to be escaped): 
.^$*+?{}[]\|()
coreyms.com
321-555-4321
123.555.1234

Mr. Schafer 
Mr. Smith
Ms. David
Mrs. Robinon
Mr. T 
'''
sentence = 'start a  senence and then bring it to an end'

pattern = re.compile(r'[1][1][1].\d\d\d')
matches = pattern.finditer(text_to_search)

#for match in matches:
#    print(match)
#
#print (text_to_search[1:4])

print(os.getcwd())




try:
    with open('data.txt' ) as fd: 
        contents = fd.read()
        matches = pattern.finditer(contents)
        for match in matches: 
            print(match)
except IOError:
    print("inout file doeesnt exit......")


