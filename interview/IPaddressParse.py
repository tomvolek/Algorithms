""" Scan a file like access.log file and parse for repeated IPv and Ip6
"""

import re
from collections import Counter


#Note:  compile() is used to declare a pattern for matching, it can be used in subsequent calls to re.search()
patternIP4 = re.compile(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}")
patternIP6 = re.compile(r"(([0-9a-f]{1,4}:){7}[0-9a-f]{1,4}) | \d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}")

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

except IOError:
    print("File could not be opened")
    

