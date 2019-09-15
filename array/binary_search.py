""" Binary search """
def binary_search(array,num):
    left = 0 
    right= len(array) -1
    #print (right)
    while (array[left] <= array[right]):
        mid = left + ((right -1)//2)
        if array[mid] == num: 
            return mid
        elif num > array[mid]:   # num greater than mid look on right  
            left = mid+1   
        else:                    # num less than mid look on left 
            right = mid -1     
    return -1

if __name__ == "__main__":   
    myarray = [2,4,6,8,15,30,55,70,100]
    x = 30 
    result = binary_search(myarray,x)

    if result != -1: 
        print ("index of number is: ",result)
    else: 
        print("number is not present in array")