"""" interview question""" 
#  given a list of numbers [14 ,13,16,7,8,10,1,2] with target number, 
# determine if there is a sum of numbers which is equal to target 
# example if target is 3 , then we have 1,2 which are candidates 


def find_pair(list_num,target):
    if len(list_num) == 0:  
        print ("no item in our array list") 
        return 
    if target == 0: 
        print ("Target value needs to be more than 0 ")  
        return 
    list_dict = {}
    
    found = None
    for value in list_num:
        if value in list_dict:
            list_dict[value] += 1 
        else:
            list_dict[value ] = 1   

    for value in list_num: 
            subnumber_target = target - value
            if subnumber_target in list_dict and list_dict[subnumber_target] != 0:
                    print ("keys => ",str(subnumber_target) + " and  " + str(value))
                    found = True
                    
    if not found: 
        print(" no pairs to sum up to target value ")
    return 
find_pair([], 2)  #test for emtpy list 
find_pair([1,2],0) # test for target value 0 

find_pair([1,2,2,3,13,4,5,16,8,8,9,10],4) 
#find_pair([1,2,3],2)