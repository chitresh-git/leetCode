def uniqueOccurrences(arr):
        """
        :type arr: List[int]
        :rtype: bool
        """

        uni=set(arr)
        flag=True

        a=[ arr.count(x) for x in uni ]
        print(a)
        
        a=[a.count(x) for x in a]
        print(a)

        for i in a :
                if i>1: return False
        
        return flag
                



ans=uniqueOccurrences([1,1,2,2,2,2,3,3,3,4])
print(ans)

"""
Given an array of integers arr, return true if the number of occurrences of each value in the array is unique or false otherwise.

 

Example 1:

Input: arr = [1,2,2,1,1,3]
Output: true
Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two values have the same number of occurrences.
Example 2:

Input: arr = [1,2]
Output: false
Example 3:

Input: arr = [-3,0,1,-3,1,1,1,-3,10,0]
Output: true
"""