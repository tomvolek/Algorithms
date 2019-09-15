"""  Parse /var/log/messages and list date and time column in assending order base on number of messages per minute """
# ex: Jan 20 05:03:03 fakehost ntpd[3705]: synchronized to time.faux.biz, stratum 2
# ex: Jan 20 03:26:22 fakehost anacron[28969]: Normal exit (1 job run)
# ex: Jan 20 03:25:09 fakehost run-parts(/etc/cron.daily)[20447]: finished logrotate

try : 
    timestamp_list =[]
    message_dict= {} 
    
    # open file and add first 12 characters to a list 
    with open("var_log_messages.txt") as fd:
        for line in fd:
            timestamp_list.append( line[0:12] )  
        timestamp_list.sort()

    # add list items to a dictionary, key is a unique timestamp, value of key is number of times key is repeated in list        
    for i in range(len(timestamp_list)): 
        if timestamp_list[i] in message_dict: 
            message_dict[timestamp_list[i]] += 1
        else:
            message_dict[timestamp_list[i]] = 1
    # go over dictionary items and print each ley and value representin unique time stamps and number of occurances
    for key in message_dict.keys(): 
        print (str(key)+","+str(message_dict[key]))
        
except IOError:
    print("File could not be opened")

List = []
with open("/Users/tom/marks.txt") as fd: 
    for line in fd:
        List.append(line[0:12])
    List.sort()
    print(List)

print (open ("/Users/tom/marks.txt",'r').read().find("2") )


import re 
import requests

#  reading a URL 
link = "http://www.google.com"
f = requests.get(link)
print(f.text)
str = "google"
print (  re.findall("google",f.text))

########
import json
# some JSON:
x =  '{ "name":"John", "age":30, "city":"New York"}'
# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print("Age ==> ",y["age"])

#######
# Count recurrance of a text in a file 
def main():

    file  = open('/Users/tom/marks.txt', 'r').read()
    team  = "Amit"
    count = file.count(team)

    print(count)

main()


x = 5 
y = [ 1, 2, 3]
if x <5: 
    print("less than")

elif x > 5 and  x < 10 : 
    print("greater 5 ")
elif x == 5:
    print("exit") 
print ("count",y.count())




