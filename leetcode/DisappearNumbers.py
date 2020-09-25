# https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/
""" Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.
Find all the elements of [1, n] inclusive that do not appear in this array.
Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.
"""

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        max = 1
        min = 1
        for i in range (len(nums)-1): 
            if (nums[i] >= max): 
                max= nums[i]
            elif (nums[i]) <= min:
                min = nums[i]

            

def main(): 
    if if __name__ == "__main__":
        myArray = [4,3,2,7,8,2,3,1]
        mySolution = Solution()
        mySolution.findDisappearedNumbers(myArray)

