"""
Given a circular list of items, print each third member and
then remove them. The next counter starts immedietly after
the member is removed. print till all the members are exusted.
Array= ['1','2','3','4','5','6','7','8','9']
"""

def circular_array_counter(array_list,skip):
    skip = skip -1 # we skip every three item, however list starts with index zero so , minus 1
    index = 0   # array index starts at 0
    list_len = (len(array_list))
    print('length of array',list_len)

    while list_len > 0:
        index = (skip + index) % list_len
        print (array_list.pop(index))
        list_len -= 1

# input a list of number ito a list
print ('input a list of numbers: ')
Array = [int(x) for x in input().split()]
print ('Array inouted=>',  Array)


circular_array_counter(Array,3)

########
