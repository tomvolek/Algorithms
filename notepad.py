import calendar

cal = calendar.month(2018, 2)
print ("Here is the calendar:")
print (cal)

people =['bob','tom','jack']
people.append(6)
print ("length =",len(people))  # count



people.count(1)
people.pop()
people.count(1)
print (people)
for person in people :
    print(person)

for i in range(0,10):
    print (i)


def checkDivisibility(a, b):
    if a % b == 0:
        print ("a is bigger ")
    else:
        print ("b is better ")


checkDivisibility(2, 5)

d = dict()
d['xyz'] = 123
d['abc'] = 345

print (d.keys())
print (d.values())

for i in d :
    print ("%s %d" %(i, d[i]))

# Function to test map
def cube(x):
    return x ** 2

# Driver to test above function

# Program for working of map
print ("MAP EXAMPLES")
cubes = map(cube, range(10))
print (cubes)

list = ['phyhiscs','foo','bar']
print (list[:1])

print (list)
