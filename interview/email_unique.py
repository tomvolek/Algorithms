""" find how many unique emails are a given list:  Pattern foo@google.com """ 
import os 
import sys
import re
from collections import Counter

pattern = re.compile (r"\w+@\w+\.[a-z]{3}")

try:
    os.chdir(sys.path[0])   # change the directory to the place which this script runs from
    with open('access.log') as fd: 
        log = fd.read()  # read entire file into log structure
        email_list = re.findall(pattern,log)  # use re.findall to find all email patterns in log file 
        emailcount = Counter(email_list)
        for k,v in emailcount.items(): 
            print ("Email address : " + k ,  v ," Times " ) 

except IOError:
    print("File could not be opened")
    

