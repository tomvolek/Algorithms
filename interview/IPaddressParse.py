""" Scan a file like access.log file and parse for repeated IPv and Ip6
"""
import sys
import os.path
import re
import urllib.request
from collections import Counter
from itertools import permutations
import faulthandler

faulthandler.enable()

#import files base on python version 
if ((3, 0) <= sys.version_info <= (3, 9)):
    print(sys.version)
    from urllib.parse import urlparse
elif ((2, 0) <= sys.version_info <= (2, 9)):
    print(sys.version)
    from urlparse import urlparse


query = {"lat": 40.71, "lon": -74}
url = "http://api.open-notify.org/iss-pass.json"

query_string = urllib.parse.urlencode (query) 
url = url + "?" + query_string
with urllib.request.urlopen( url ) as response:
    response_text = response.read()        
    print( response_text )  

#Note:  compile() is used to declare a pattern for matching, it can be used in subsequent calls to re.search()
patternIP4 = re.compile(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}")
patternIP6 = re.compile(r"(([0-9a-f]{1,4}:){7}[0-9a-f]{1,4}) | \d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}")
patternHTTP = re.compile(r"http://\w+\.com" )
try: 
    with open('/Users/tom/Development/Algorithms/interview/access.log') as fd: 
        log = fd.read()  # read entire file into log structure
        
        my_iplist4 = re.findall(patternIP4,log)  # use re.findall to find all patterns in log file 
        ipcount = Counter (my_iplist4) 
        for k,v in ipcount.items():
            print("Unique IP 4 Address " + "=> " + str(k) + " " + "Count "  + "=> " + str(v))                    

        my_iplist6 = re.findall(patternIP6,log)  # use re.findall to find all patterns in log file 
        ipcount = Counter (my_iplist6)  #
        #print (ipcount) 
        
        for k,v in ipcount.items():
            print("Unique IP 6 Address " + "=> " + str(k) + " " + "Count "  + "=> " + str(v)) 
        
        print ("Http found:", re.findall(patternHTTP,log))
        
except IOError:
    print("File could not be opened")
    

# try , catch exception 
try: 
    print("try somethign here")
except: 
    print ("if we have a failure ")
else: 
    print ("only if we succed ")
finally: 
    print ("finally we play here")

I = iter([2,4,6,7,8,9])
print(next(I))

'''map iterator : map values of range to each square function '''
square = lambda x: x**2 
for val in map (square,range(10)):
    print (val,end=' ')

'''filter iterator : filters the values which only the result of lamba evalutes to true'''
myvalue = lambda x: x %2 == 0 
for val in filter(myvalue,range(10)):
    print (val) 


'''permutations ''' 
p = permutations(range(3))
print (*p)

print ([i for i in range(20) if i % 3 > 0])
type (p)

print( [i for i in range (10) if not (i % 3) ])


''' write a string to a file  '''
with open("/tmp/outfile", "w") as outfile:
    for foo in range(10):
         outfile.write('%s Writting to a file\n '%(foo) )
    outfile.close()

with open("/tmp/outfile","r") as infd: 
    for line in infd:
        print(infd.readline())
i = 0
while i < 10: 
    print (hex(i), end=',' )
    i +=1

def myfunction (*args, **kwargs):
    print("args =", args)
    print("kwargs = ", kwargs)

myfunction("foo","bar",a=4,b=5)    

num = 140
if num in range(1,100): 
    print("Our Number %s is in range"%str(num))
else: 
     print("Our Number %s is not range"%str(num))   



shape =  ['circle','square','rect']
        
print (list(enumerate(shape)))

with open ("/Users/tom/Development/Algorithms/interview/access.log") as fp: 
    for line in iter(fp.readline,''):
        print(line)

numbers_divisible_by_three = [3, 6, 9, 12, 15]

for num in numbers_divisible_by_three:
    quotient = num / 3
    print(f"{num} divided by 3 is {int(quotient)}.")


# for loop over ditionary items   with format print statement 
table = {'Color': 23,'hight': 45 } 
for color,hight in table.items(): 
    print (f'{color:10} => {hight:4d}')       


with open ('/Users/tom/Development/Algorithms/interview/access.log',"r") as fd: 
    for line in iter(fd.readline,''): 
        print ("line is ",line)



#  create custom iterator class myNumbers 
class MyNumbers: 
    def __iter__(self):
        self.a = 1
        return self
    
    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration

myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
  print(x)


a = '1110101011011011'
print (max(map(len,a.split('0'))))
