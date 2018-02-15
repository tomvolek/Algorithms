"""
Given a circular list of items, print each third member and
then remove them. The next counter starts immedietly after
the member is removed. print till all the members are exusted.
Array= ['1','2','3','4','5','6','7','8','9']
"""



def circular_array_counter(array_list,skip):
    array_len = len(Array)
    print(array_len)

# input a list of number ito a list
array = [int(x) for x in input().split()]


circular_array_counter(Array,3)

